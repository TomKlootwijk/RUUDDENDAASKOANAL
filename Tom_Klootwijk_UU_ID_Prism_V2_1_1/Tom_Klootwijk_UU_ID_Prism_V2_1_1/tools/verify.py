#!/usr/bin/env python3
"""Verify the release manifest, Prism tests, synthetic replay and optional baseline.

No install or download is performed. Fresh replay and baseline extraction use
private temporary directories and never replace the shipped expected records.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from uu_prism.core import Prism, FACET_IDS, load_registry


def check_manifest() -> int:
    manifest = ROOT / 'checksums' / 'SHA256SUMS.txt'
    count = 0
    seen: set[str] = set()
    for line in manifest.read_text(encoding='utf-8').splitlines():
        if not line:
            continue
        expected, relative = line.split('  ', 1)
        target = (ROOT / relative).resolve()
        if ROOT not in target.parents or relative in seen:
            raise ValueError(f'Invalid or repeated manifest path: {relative}')
        if hashlib.sha256(target.read_bytes()).hexdigest() != expected:
            raise ValueError(f'Manifest mismatch: {relative}')
        seen.add(relative)
        count += 1
    if count == 0:
        raise ValueError('Empty manifest')
    return count


def check_registry() -> None:
    registry = load_registry(ROOT / 'spec/facets.json')
    if registry.get('version') != '2.1.1' or registry.get('profile') != 'UU-PRISM-35-1':
        raise ValueError('Registry version or profile mismatch')
    if [b['code'] for b in registry['bands']] != list('ROYGBIV'):
        raise ValueError('Band order mismatch')
    if tuple(f['id'] for f in registry['facets']) != FACET_IDS:
        raise ValueError('Facet sequence mismatch')
    if Counter(f['band'] for f in registry['facets']) != Counter({b: 5 for b in 'ROYGBIV'}):
        raise ValueError('Facet/band count mismatch')
    if not all(f['default_enabled'] is False for f in registry['facets']):
        raise ValueError('Acquisition must default to disabled')


def check_replay() -> None:
    spec = importlib.util.spec_from_file_location('prism_release_demo', ROOT / 'tools/demo.py')
    if spec is None or spec.loader is None:
        raise ValueError('Cannot load the demonstration module')
    demo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(demo)
    expected = ROOT / 'verification/demo'
    with tempfile.TemporaryDirectory(prefix='uu_prism_replay_') as directory:
        out = Path(directory)
        demo.run(out)
        for name in ('input_records.json', 'snapshot_before.json', 'passport.json', 'snapshot.json', 'results.json'):
            if (out / name).read_bytes() != (expected / name).read_bytes():
                raise ValueError(f'Differential replay mismatch: {name}')
        document = json.loads((out / 'passport.json').read_text(encoding='utf-8'))
        restored = Prism.restore(document)
        if restored.snapshot(document['snapshot']['as_of']) != document['snapshot']:
            raise ValueError('Passport restoration mismatch')


def check_migration() -> None:
    """Exercise the inventory -> manual classification -> private manifest CLI."""
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    with tempfile.TemporaryDirectory(prefix='uu_prism_migration_') as directory:
        workspace = Path(directory)
        source = workspace / 'selected_export'
        source.mkdir()
        samples = {'still.txt': b'SYNTHETIC STILL-IMAGE REFERENCE\n',
                   'authored.txt': b'SYNTHETIC AUTHORED-WORK REFERENCE\n',
                   'unmapped.txt': b'SYNTHETIC UNASSIGNED OBJECT\n'}
        for name, payload in samples.items():
            (source / name).write_bytes(payload)
        inventory_file = workspace / 'inventory.json'
        subprocess.run([sys.executable, str(ROOT / 'tools/inventory.py'), '--root', str(source),
                        '--out', str(inventory_file)], env=env, check=True, capture_output=True, text=True)
        inventory = json.loads(inventory_file.read_text(encoding='utf-8'))
        if inventory['file_count'] != 3 or inventory['skipped']:
            raise ValueError('Inventory smoke check failed')
        mapping = {'still.txt': 'F01', 'authored.txt': 'F26'}
        for row in inventory['files']:
            row['facet_id'] = mapping.get(row['relative_path'])
        inventory_file.write_text(json.dumps(inventory), encoding='utf-8')
        destination = workspace / 'passport'
        command = [sys.executable, str(ROOT / 'tools/migrate.py'), '--inventory', str(inventory_file),
                   '--holder', 'holder:synthetic-cli-test', '--out', str(destination)]
        rejected = subprocess.run(command, env=env, capture_output=True, text=True)
        if rejected.returncode == 0 or destination.exists():
            raise ValueError('Migration confirmation guard failed')
        subprocess.run(command + ['--confirm-authorized', '--confirm-holder-links'],
                       env=env, check=True, capture_output=True, text=True)
        document = json.loads((destination / 'passport.json').read_text(encoding='utf-8'))
        restored = Prism.restore(document)
        snapshot = restored.snapshot(document['snapshot']['as_of'])
        if snapshot['active_links'] != 2 or snapshot['active_objects'] != 2:
            raise ValueError('Migration record count mismatch')
        if any(name in json.dumps(snapshot) for name in samples):
            raise ValueError('Source filenames unexpectedly appear in the snapshot')
        receipt = json.loads((destination / 'migration_receipt.json').read_text(encoding='utf-8'))
        if receipt['assigned'] != 2 or receipt['unmapped'] != 1 or receipt['quarantined'] != 0:
            raise ValueError('Migration receipt mismatch')
        if any((source / name).read_bytes() != payload for name, payload in samples.items()):
            raise ValueError('A source file was changed')


def check_schemas() -> int:
    try:
        import jsonschema
    except ImportError as exc:
        raise ValueError('--schema requires the separately installed jsonschema package') from exc
    schemas = {}
    for name in ('record', 'snapshot'):
        schema = json.loads((ROOT / f'spec/{name}.schema.json').read_text(encoding='utf-8'))
        jsonschema.Draft202012Validator.check_schema(schema)
        schemas[name] = jsonschema.Draft202012Validator(schema)
    records = json.loads((ROOT / 'verification/demo/input_records.json').read_text(encoding='utf-8'))
    for record in records:
        schemas['record'].validate(record)
    for name in ('snapshot_before.json', 'snapshot.json'):
        schemas['snapshot'].validate(json.loads((ROOT / 'verification/demo' / name).read_text(encoding='utf-8')))
    return len(schemas)


def check_baseline(with_schema: bool) -> None:
    archive = ROOT / 'baseline/Unified_Field_Theory_V2_0_0.zip'
    with tempfile.TemporaryDirectory(prefix='uu_prism_baseline_') as directory:
        parent = Path(directory).resolve()
        with zipfile.ZipFile(archive) as zipped:
            if sum(i.file_size for i in zipped.infolist()) > 256 * 1024 * 1024:
                raise ValueError('Baseline archive exceeds the extraction budget')
            for info in zipped.infolist():
                target = (parent / info.filename).resolve()
                if parent not in target.parents or ((info.external_attr >> 16) & 0o170000) == 0o120000:
                    raise ValueError('Unsafe baseline archive entry')
            if zipped.testzip() is not None:
                raise ValueError('Baseline ZIP CRC check failed')
            zipped.extractall(parent)
        candidates = list(parent.glob('*/tools/verify.py'))
        if len(candidates) != 1:
            raise ValueError('Baseline verifier is not uniquely located')
        script = candidates[0]
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONPATH=str(script.parents[1] / 'src'))
        command = [sys.executable, str(script)] + (['--schema'] if with_schema else [])
        subprocess.run(command, cwd=script.parents[1], env=env, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skip-manifest', action='store_true', help='Test an edited working copy without original-file checks')
    parser.add_argument('--schema', action='store_true', help='Validate the two JSON Schemas and demonstration records')
    parser.add_argument('--baseline', action='store_true', help='Extract and invoke the unchanged V2 baseline verifier')
    args = parser.parse_args()
    try:
        if not args.skip_manifest:
            print(f'Manifest: {check_manifest()} matching files', flush=True)
        check_registry()
        print('Registry: 7 bands, 35 ordered facets, all acquisition defaults disabled', flush=True)
        env = dict(os.environ, PYTHONPATH=str(ROOT / 'src'), PYTHONDONTWRITEBYTECODE='1')
        subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'],
                       cwd=ROOT, env=env, check=True)
        check_replay()
        check_migration()
        print('Local migration CLI: confirmation guard, two admitted links, one unmapped row, unchanged sources', flush=True)
        print('Synthetic replay: five files match byte-for-byte; exact restoration passed', flush=True)
        if args.schema:
            print(f'JSON Schema: {check_schemas()} schema documents and all example records passed', flush=True)
        if args.baseline:
            check_baseline(args.schema)
            print('Retained V2 baseline: verifier passed in a fresh temporary extraction', flush=True)
        print('PASS: UU ID Prism release verification', flush=True)
        return 0
    except (ValueError, OSError, KeyError, TypeError, zipfile.BadZipFile, subprocess.CalledProcessError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
