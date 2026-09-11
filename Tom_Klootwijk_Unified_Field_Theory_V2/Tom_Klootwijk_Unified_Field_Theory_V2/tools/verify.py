#!/usr/bin/env python3
"""Verify V2 file integrity, literal records, tests and fresh deterministic replay."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from tkuft.core import Registry,dutch_number,AUTHOR
from tkuft.identity import Lineage

def manifest_check()->int:
    count=0
    for line in (ROOT/'checksums/SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        if not line:continue
        digest,name=line.split('  ',1);p=(ROOT/name).resolve()
        if ROOT not in p.parents:raise ValueError('Manifest path outside project')
        if hashlib.sha256(p.read_bytes()).hexdigest()!=digest:raise ValueError(f'Manifest mismatch: {name}')
        count+=1
    return count

def compare(a,b,path='result')->None:
    if isinstance(a,dict) and isinstance(b,dict):
        if a.keys()!=b.keys():raise ValueError(f'Different keys at {path}')
        for k in a:compare(a[k],b[k],path+'.'+k)
    elif isinstance(a,list) and isinstance(b,list):
        if len(a)!=len(b):raise ValueError(f'Different list length at {path}')
        for i,(x,y) in enumerate(zip(a,b)):compare(x,y,f'{path}[{i}]')
    elif isinstance(a,float) and isinstance(b,float):
        if not math.isclose(a,b,rel_tol=1e-12,abs_tol=1e-12):raise ValueError(f'Floating comparison mismatch at {path}')
    elif a!=b:raise ValueError(f'Comparison mismatch at {path}')

def main()->int:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--skip-manifest',action='store_true');p.add_argument('--schema',action='store_true',help='Also validate the JSON Schemas using jsonschema');args=p.parse_args()
    try:
        if not args.skip_manifest:print(f'Manifest: {manifest_check()} matching files',flush=True)
        world=json.loads((ROOT/'examples/literal_substrate.json').read_text(encoding='utf-8'));r=Registry(world['definitions'])
        if world['author']!=AUTHOR:raise ValueError('Author record mismatch')
        for instance in world['instances']:r.definition_at(instance['definition_ref'])
        profile=json.loads((ROOT/'data/dutch_profile_0_99.json').read_text(encoding='utf-8'))
        if profile!=[dutch_number(n) for n in range(100)]:raise ValueError('Profile regeneration mismatch')
        Lineage(json.loads((ROOT/'verification/demo/lineage.json').read_text(encoding='utf-8')))
        print(f'Registry: {len(r.definition_order())} sealed definitions; author, profile and lineage verified',flush=True)
        if args.schema:
            try:import jsonschema
            except ImportError as exc:raise ValueError('--schema requires jsonschema; see requirements-dev.txt') from exc
            for name in ('definition','corpus'):
                schema=json.loads((ROOT/f'spec/{name}.schema.json').read_text(encoding='utf-8'));jsonschema.Draft202012Validator.check_schema(schema)
            jsonschema.validate(world,json.loads((ROOT/'spec/corpus.schema.json').read_text(encoding='utf-8')))
            print('JSON Schema: both schemas checked; literal substrate validated',flush=True)
        env=dict(os.environ,PYTHONPATH=str(ROOT/'src'),PYTHONDONTWRITEBYTECODE='1')
        subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-v'],cwd=ROOT,env=env,check=True)
        spec=importlib.util.spec_from_file_location('v2_demo',ROOT/'examples/run_demo.py')
        if spec is None or spec.loader is None:raise ValueError('Cannot load demo')
        demo=importlib.util.module_from_spec(spec);spec.loader.exec_module(demo)
        with tempfile.TemporaryDirectory(prefix='tkuft_v2_verify_') as temp:
            tmp=Path(temp);actual=demo.run(tmp,64)
            expected=json.loads((ROOT/'verification/demo/demo_output.json').read_text(encoding='utf-8'));compare(actual,expected)
            exact=('initial.tku','final.tku','final_state.bin','words.json','summary.csv','feedback.csv','certificates.csv','state_horizon.json','historical_state_envelope.json','lineage.json','eight_bit_queries.csv')
            for name in exact:
                if (tmp/name).read_bytes()!=(ROOT/'verification/demo'/name).read_bytes():raise ValueError(f'Exact replay differs: {name}')
        print('PASS: tests, registry, profile, lineage, direct/UU ID replay, capsules and certificates',flush=True)
        return 0
    except (ValueError,OSError,subprocess.CalledProcessError) as exc:
        print('FAIL:',exc,file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
