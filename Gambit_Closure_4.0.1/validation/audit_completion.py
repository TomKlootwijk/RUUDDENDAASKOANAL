"""Independently inspect saved post-fix evidence and exact protected bytes."""
from pathlib import Path
import datetime, hashlib, json, re, subprocess

ROOT=Path(__file__).resolve().parents[1]
FULL=ROOT/'validation/full'
CPU=ROOT/'validation/cpu'
EDGE=ROOT/'validation/gpu_edges'
FILES=('initial.gbc','final.gbc','words.bin','summary.csv','counts.bin')
checks=[]

def sha(path):
    with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def read(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def require(name,condition,evidence,details):
    if not condition:raise RuntimeError(name+': '+str(details))
    checks.append({'name':name,'status':'PASS','evidence':evidence,'details':details})
def same(a,b):return all(sha(a/f)==sha(b/f) for f in FILES)
def manifest(root,filename):
    records=[line.split('  ',1) for line in (root/filename).read_text().splitlines()]
    for expected,name in records:
        p=(root/name).resolve()
        assert p.is_relative_to(root) and sha(p)==expected,name
    return records

revision=read(ROOT/'REVISION.json')
original=Path(revision['original_root'])
base=manifest(original,'SHA256SUMS.txt')
current=manifest(ROOT,'SHA256SUMS.txt')
require('original_release_integrity',len(base)==196 and sha(original/'SHA256SUMS.txt')==revision['original_manifest_sha256'],str(original/'SHA256SUMS.txt'),{'matched_files':len(base)})
require('revised_release_integrity',len(current)==203,'SHA256SUMS.txt',{'matched_files':len(current)})
changed={item['path']:item for item in revision['changed_files']}
for old,name in base:
    if name in changed:
        assert old==changed[name]['original_sha256'] and sha(ROOT/name)==changed[name]['revised_sha256']
    else:assert sha(ROOT/name)==old,name
require('protected_model_and_goldens_unchanged',len(changed)==5,'REVISION.json',{'changed_original_files':sorted(changed),'unchanged_original_files':len(base)-len(changed),'assets_and_formal_and_core_unchanged':True})
verified_snapshot=FULL/'verified_source_manifest.txt'
assert sha(verified_snapshot)=='1e190e3fed02812c7f054d3991d1935c15380461c47d97a47f33fa4152abf09c'
snapshot_entries=[line.split('  ',1) for line in verified_snapshot.read_text(encoding='utf-8').splitlines()]
post_run_changes=[name for expected,name in snapshot_entries if sha(ROOT/name)!=expected]
require('tested_runtime_matches_delivered_revision',set(post_run_changes)=={'README.md','REVISION.json','REVISION.patch'},'validation/full/verified_source_manifest.txt',{'post_run_changes':post_run_changes,'reason':'UTF-8 patch repair and README accuracy corrections only; compiled sources, tests, verification tools, model and inputs unchanged'})
patch_check=subprocess.run(['git','-C',str(original),'apply','--check',str(ROOT/'REVISION.patch')],capture_output=True,text=True)
(ROOT/'validation/patch_apply_check.txt').write_text('git apply --check exit='+str(patch_check.returncode)+'\n'+patch_check.stdout+patch_check.stderr,encoding='utf-8')
require('revision_diff_applies_to_original',patch_check.returncode==0,'validation/patch_apply_check.txt',{'utf8_diff':True,'original_not_modified':True})

full,cpu,edge=read(FULL/'verification.json'),read(CPU/'verification.json'),read(EDGE/'verification.json')
require('full_requested_coordinator',full['status']=='GPU_CPU_EXACT_PASS' and full['scope']=='full' and all(full[k]=='PASS' for k in ('cpu','gpu','formal','sanitizers')) and full['profile']=='CAPTURED_FOR_REVIEW_NOT_A_SPEED_CLAIM' and all(full['requested'].values()),'validation/full/verification.json',{'status':full['status'],'commands':len(full['commands'])})
require('cpu_formal_coordinator',cpu['status']=='CPU_PASS_GPU_NOT_RUN' and cpu['cpu']=='PASS' and cpu['formal']=='PASS' and cpu['scope']=='full','validation/cpu/verification.json',{'status':cpu['status']})
for label,report,root in [('full',full,FULL),('cpu',cpu,CPU)]:
    require(label+'_commands_succeeded',all(c['returncode']==0 and (root/'logs'/c['log']).is_file() for c in report['commands']),str(root/'verification.json'),{'commands':len(report['commands'])})
native_log=(FULL/'logs/native_tests.txt').read_text()
python_log=(FULL/'logs/python_tests.txt').read_text()
require('native_suite', 'PASS checks=338184' in native_log and '0 tests failed' in native_log,'validation/full/logs/native_tests.txt',{'native_checks':338184})
require('python_suites','Ran 28 tests' in python_log and re.search(r'\nOK\s*$',python_log) is not None,'validation/full/logs/python_tests.txt',{'model_methods':24,'coordinator_methods':4,'total_methods':28})
cuda_tests=(FULL/'logs/cuda_tests.txt').read_text()
require('production_cuda_helper_regression','PASS CUDA wrapper:' in cuda_tests and '0 tests failed out of 2' in cuda_tests,'validation/full/logs/cuda_tests.txt',{'uses_production_source':True,'single_evaluation_success_error_and_message':True})
require('clean_cuda_compile',not re.search(r'(?im)^.*\b(?:warning|error)\s+(?:[A-Z]+\d+|:)',(FULL/'logs/cuda_build.txt').read_text()),'validation/full/logs/cuda_build.txt',{'link_runtime_conflict_absent':True})

gold=read(ROOT/'assets/closure_goldens.json')['cases']
for name,g in gold.items():
    for f,h in g['files'].items():assert sha(FULL/'native'/name/f)==h,(name,f)
    assert same(FULL/'native'/name,CPU/'native'/name),name
    if not name.startswith('laptop'):
        assert same(FULL/'native'/name,FULL/'python'/name) and same(FULL/'native'/name,FULL/'gates'/name)
require('native_golden_and_independent_conformance',len(gold)==6,'validation/full/native; validation/full/python; validation/full/gates',{'native_profiles':6,'independent_python_boolean_profiles':4,'consensus_files_per_profile':5,'golden_files_matched':30})
gpu_runs=[]
for name,g in gold.items():
    variants=[('texture',32),('texture',128),('texture',256),('texture',512),('global',256)] if name=='verify_xy' else [('texture',256)]
    for fetch,block in variants:
        target=FULL/'cuda'/f'{name}_{fetch}_{block}'
        assert same(target,FULL/'native'/name)
        meta=read(target/'run.json')
        assert meta['status']=='PASS' and all(meta[k] for k in ('gpu_verified','every_step_cpu_comparison','full_lut_readback'))
        gpu_runs.append({'profile':name,'fetch':fetch,'block':block,'steps':g['steps'],'cells':full['cases'][name]['cells']})
require('gpu_frozen_conformance',len(gpu_runs)==10,'validation/full/cuda',{'runs':gpu_runs,'five_file_exact_comparison':True})
require('checkpoint_restart',same(FULL/'cuda_resume',FULL/'split_second') and sha(FULL/'split_second/final.gbc')==sha(FULL/'native/micro_xy/final.gbc'),'validation/full/cuda_resume',{'segment_split':[17,47]})
ptx_cmd=next(c for c in full['commands'] if c['log']=='cuda_forced_ptx.txt')
require('repeat_and_forced_ptx',same(FULL/'cuda_repeat',FULL/'native/micro_xy') and same(FULL/'cuda_forced_ptx',FULL/'native/micro_xy') and ptx_cmd['environment_overrides']['CUDA_FORCE_PTX_JIT']=='1','validation/full/logs/cuda_forced_ptx.txt',{'forced_ptx_jit':True,'fresh_process_repeat':True})
dump=(FULL/'logs/ptx_sass.txt').read_text()
require('ptx_and_sass_saved','sm_120' in dump and '.entry' in dump and 'Function :' in dump,'validation/full/logs/ptx_sass.txt',{'bytes':len(dump)})

formal_results=[]
obligations=read(ROOT/'formal/obligations.json')['targets']
for formal_root in (CPU/'formal',FULL/'formal'):
    formal=read(formal_root/'report.json')
    assert formal['status']=='PASS' and len(formal['targets'])==len(obligations)==24
    for target,expected in zip(formal['targets'],obligations):
        log=(formal_root/(target['name']+'.log')).read_text()
        assert target['name']==expected['name'] and target['actual']==expected['expected'] and target['passed']
        assert log.strip().splitlines()[0]==expected['expected'] and '(error' not in log
    formal_results.append({'path':str(formal_root.relative_to(ROOT)),'solver':formal['solver_version']})
require('all_formal_obligations',True,'validation/full/formal/report.json',{'unsat':22,'intentional_sat':2,'runs':formal_results,'scope':'Submitted algebraic targets, not whole-program proof'})
for mode in ('memcheck','racecheck','initcheck','synccheck'):
    logfile=FULL/'logs'/('sanitize_'+mode+'.txt')
    log=logfile.read_text()
    zero='ERROR SUMMARY: 0 errors' in log or (mode=='racecheck' and 'RACECHECK SUMMARY: 0 hazards' in log)
    require('sanitizer_'+mode,zero and 'PASS backend=cuda_checked' in log,str(logfile.relative_to(ROOT)),{'steps':8,'profile':'verify_xy','zero_errors_or_hazards':True})
for fetch in ('texture','global'):
    profile=FULL/('ncu_'+fetch+'.ncu-rep');log=(FULL/'logs'/('profile_'+fetch+'.txt')).read_text()
    require('profile_'+fetch,profile.is_file() and profile.stat().st_size>0 and '==PROF== Report:' in log and 'PASS backend=cuda_checked' in log,str(profile.relative_to(ROOT)),{'bytes':profile.stat().st_size,'scope':'Captured profiling data; no throughput comparison claim'})

require('gpu_edges',edge['status']=='PASS_REQUESTED_SCOPE' and all(c['status']=='PASS' for c in edge['cases'].values()) and edge['wrapper_contract']['status']=='PASS','validation/gpu_edges/verification.json',{'cases':list(edge['cases'])})
require('gpu_edge_commands',all(c['returncode']==c['expected_returncode'] for c in edge['commands']),'validation/gpu_edges/verification.json',{'commands':len(edge['commands']),'negative_tests_expect_failure':True})
for kind in ('cell','clock'):
    d=edge['diagnostics'][kind]
    require('step3_diagnostic_'+kind,d['status']=='PASS' and d['successful_updates_before_failure']==3 and 'step 3' in d['diagnostic'],'validation/gpu_edges/verification.json',{'test_only_fault_injection':True,'production_source_unchanged':True})

binaries={name:{'path':str(path.relative_to(ROOT)),'sha256':sha(path)} for name,path in {
    'gambit':FULL/'build/Release/gambit.exe','gambit_cuda':FULL/'cuda_build/Release/gambit_cuda.exe',
    'gambit_cuda_contract':FULL/'cuda_build/Release/gambit_cuda_contract.exe'}.items()}
assert binaries['gambit_cuda']['sha256']==edge['gpu_executable']['sha256']
audit={'status':'PASS','scope':'Post-fix code verification; PDF rendering and delivery audited separately',
       'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,
       'source_manifest_sha256':sha(ROOT/'SHA256SUMS.txt'),'original_manifest_sha256':revision['original_manifest_sha256'],
       'protected_model_files_unchanged':True,'asset_golden_sha256':sha(ROOT/'assets/closure_goldens.json'),
       'binaries':binaries,'device':full['device']}
(ROOT/'validation/completion_audit.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':audit['status'],'checks':len(checks),'binaries':binaries},indent=2))
