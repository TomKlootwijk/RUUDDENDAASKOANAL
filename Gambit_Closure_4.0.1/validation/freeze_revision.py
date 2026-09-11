"""Disclose a separate source revision without changing any numerical goldens."""
from pathlib import Path
import datetime, difflib, hashlib, json

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = Path(r'C:\RUUDDENDAASKOANAL\Tom_Klootwijk_Gambit_Closed_Engine_4.0\Tom_Klootwijk_Gambit_Closure_4.0')
BASELINE_HASH = '7e1a34bf61de6c650b8035ab292d44b0f7a1822dc0b0eb6d4435c50a0c33dc81'
ALLOWED_CHANGES = {'CMakeLists.txt', 'README.md', 'docs/VERIFICATION.md', 'src/cuda.cu', 'tools/verify.py'}
ADDITIONS = ['tests/test_verify.py', 'tests/cuda_contract.cu', 'tools/verify_gpu_edges.py',
             'REVISION.md', 'provenance/release_4.0_SHA256SUMS.txt']

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

baseline = ROOT/'provenance/release_4.0_SHA256SUMS.txt'
assert digest(baseline) == BASELINE_HASH == digest(ORIGINAL/'SHA256SUMS.txt')
entries = [line.split('  ', 1) for line in baseline.read_text(encoding='utf-8').splitlines()]
changed, unchanged, patch = [], [], []
for old_hash, name in entries:
    original, revised = ORIGINAL/name, ROOT/name
    assert original.resolve().is_relative_to(ORIGINAL) and revised.resolve().is_relative_to(ROOT)
    assert digest(original) == old_hash, 'Original release changed: '+name
    new_hash = digest(revised)
    if old_hash != new_hash:
        assert name in ALLOWED_CHANGES, 'Undisclosed change to protected file: '+name
        changed.append({'path':name,'original_sha256':old_hash,'revised_sha256':new_hash})
        patch.extend(difflib.unified_diff(original.read_text(encoding='utf-8').splitlines(True), revised.read_text(encoding='utf-8').splitlines(True), fromfile='a/'+name, tofile='b/'+name))
    else:
        unchanged.append(name)
assert {item['path'] for item in changed} == ALLOWED_CHANGES
for name in ADDITIONS:
    assert (ROOT/name).is_file(), name
    if name != 'provenance/release_4.0_SHA256SUMS.txt':
        patch.extend(difflib.unified_diff([], (ROOT/name).read_text(encoding='utf-8').splitlines(True), fromfile='/dev/null', tofile='b/'+name))
(ROOT/'REVISION.patch').write_text(''.join(patch), encoding='utf-8', newline='\n')
revision = {'revision':'4.0.1','parent_release':'4.0','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'original_root':str(ORIGINAL),'original_manifest_sha256':BASELINE_HASH,
            'original_integrity_files':len(entries),'changed_files':changed,
            'added_files':[{'path':name,'sha256':digest(ROOT/name)} for name in ADDITIONS],
            'unchanged_original_files':unchanged,'unchanged_original_file_count':len(unchanged),
            'numerical_goldens_modified':False,
            'golden_manifest_sha256':digest(ROOT/'assets/closure_goldens.json'),
            'diff_sha256':digest(ROOT/'REVISION.patch')}
(ROOT/'REVISION.json').write_text(json.dumps(revision,indent=2)+'\n', encoding='utf-8', newline='\n')
names = sorted({name for _,name in entries} | set(ADDITIONS) | {'REVISION.patch','REVISION.json'})
(ROOT/'SHA256SUMS.txt').write_text(''.join(digest(ROOT/name)+'  '+name+'\n' for name in names), encoding='utf-8', newline='\n')
print(json.dumps({'original_files':len(entries),'changed_files':[x['path'] for x in changed],
                  'unchanged_original_files':len(unchanged),'revision_manifest_files':len(names),
                  'revision_manifest_sha256':digest(ROOT/'SHA256SUMS.txt'),'goldens_unchanged':True},indent=2))
