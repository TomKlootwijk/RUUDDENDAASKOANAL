#!/usr/bin/env python3
"""Local, fail-closed verification coordinator for Codex or a human operator.
No downloads, privilege changes, driver installs, or golden regeneration.
"""
from __future__ import annotations
import argparse,datetime,hashlib,json,os,platform,re,shutil,subprocess,sys
from pathlib import Path
from reference import run as python_reference
from check_trace import check as audit_trace
ROOT=Path(__file__).resolve().parents[1]
class Blocked(RuntimeError):pass
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def binary(build:Path,name:str)->Path:
    suffix='.exe' if os.name=='nt' else ''
    for p in [build/(name+suffix),build/'Release'/(name+suffix)]:
        if p.is_file():return p
    raise RuntimeError(f'Built executable not found: {name}')
def main()->int:
    ap=argparse.ArgumentParser();mode=ap.add_mutually_exclusive_group(required=True)
    mode.add_argument('--hardware',action='store_true');mode.add_argument('--cpu-only',action='store_true')
    ap.add_argument('--sanitizers',action='store_true');ap.add_argument('--profile',action='store_true')
    ap.add_argument('--quick',action='store_true',help='Skip laptop-sized cases; reports limited scope')
    ap.add_argument('--out',type=Path);ap.add_argument('--device',type=int,default=0)
    args=ap.parse_args()
    if (args.sanitizers or args.profile) and not args.hardware:ap.error('GPU instrumentation requires --hardware')
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S_%fZ')
    out=(args.out or ROOT/'local_verification'/stamp).resolve()
    if out.exists():ap.error('Verification output must be a NEW directory')
    out.mkdir(parents=True);logdir=out/'logs';logdir.mkdir()
    report={'schema':'gambit-local-verification-3.1','status':'RUNNING','gpu_status':'NOT_RUN','scope':'quick' if args.quick else 'full',
        'platform':platform.platform(),'python':platform.python_version(),'commands':[],'cases':{},'goldens_modified':False,
        'sanitizers':'NOT_RUN','profiling':'NOT_RUN'}
    def save(): (out/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    def invoke(cmd,tag,env=None):
        cmd=[str(c) for c in cmd];print('+',subprocess.list2cmdline(cmd),flush=True)
        with (logdir/(tag+'.txt')).open('w',encoding='utf-8') as log:
            p=subprocess.run(cmd,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,env=env,check=False)
        report['commands'].append({'argv':cmd,'returncode':p.returncode,'log':f'logs/{tag}.txt'});save()
        if p.returncode:raise RuntimeError(f'{tag} failed ({p.returncode}); inspect its log')
    try:
        # Freeze provenance before compiling. Extra local outputs are allowed; indexed files may not change.
        mf=ROOT/'SHA256SUMS.txt'
        if not mf.exists():raise RuntimeError('Package integrity manifest is missing')
        entries=[]
        for line in mf.read_text().splitlines():
            sha,name=line.split('  ',1);p=(ROOT/name).resolve()
            if not p.is_relative_to(ROOT) or digest(p)!=sha:raise RuntimeError(f'Package hash mismatch: {name}')
            entries.append(name)
        report['integrity_files']=len(entries)
        for f in (ROOT/'assets').glob('*.gblut'):
            if digest(f)!=json.loads(f.with_suffix('.json').read_text())['sha256']:raise RuntimeError('LUT hash mismatch')
        if not shutil.which('cmake'):raise Blocked('CMake 3.24+ must be installed')
        build=out/'build_cpu'
        invoke(['cmake','-S',ROOT,'-B',build,'-DGAMBIT_ENABLE_CUDA=OFF','-DCMAKE_BUILD_TYPE=Release'],'configure_cpu')
        invoke(['cmake','--build',build,'--config','Release','--parallel','2'],'build_cpu')
        invoke(['ctest','--test-dir',build,'-C','Release','--output-on-failure','-V'],'ctest')
        invoke([sys.executable,'-m','unittest','discover','-s','tests','-p','test_*.py','-v'],'python_tests')
        cpu=binary(build,'gambit_cpu')
        invoke([sys.executable,'tools/test_cli.py','--exe',cpu],'negative_paths')
        gold=json.loads((ROOT/'assets/golden_traces.json').read_text())['cases']
        selected={k:v for k,v in gold.items() if not(args.quick and k.startswith('laptop'))}
        for name,g in selected.items():
            run=out/'cpu'/name
            invoke([cpu,'--asset',ROOT/'assets'/g['asset'],'--out',run]+g['options'],f'cpu_{name}')
            for file,sha in g['files'].items():
                if digest(run/file)!=sha:raise RuntimeError(f'CPU golden mismatch: {name}/{file}')
            result=audit_trace(run);result['golden_match']=True
            if name.startswith('verify'):
                kwargs={}
                if '--feedback' in g['options']:kwargs['feedback']=int(g['options'][1])
                if '--inject-step' in g['options']:kwargs.update(inject_step=3,inject_cell=7)
                py=out/'independent_python'/name;python_reference(ROOT/'assets'/g['asset'],py,**kwargs)
                for file in g['files']:
                    if (py/file).read_bytes()!=(run/file).read_bytes():raise RuntimeError('Independent Python/native mismatch')
                result['independent_python_exact']=True
            report['cases'][name]=result;save()
        report['cpu_status']='CPU_PASS'
        if not args.hardware:
            report['status']='CPU_PASS_GPU_NOT_RUN';save();print(report['status']);return 0
        for name in ['nvcc','nvidia-smi','cuobjdump']:
            if not shutil.which(name):raise Blocked(f'{name} absent; GPU verification cannot be substituted by CPU success')
        invoke(['nvcc','--version'],'nvcc_version')
        invoke(['nvcc','--list-gpu-code'],'nvcc_architectures')
        if 'sm_120' not in (logdir/'nvcc_architectures.txt').read_text():raise Blocked('nvcc does not list sm_120')
        invoke(['nvidia-smi','--query-gpu=name,uuid,driver_version,memory.total','--format=csv'],'nvidia_smi')
        gb=out/'build_cuda'
        invoke(['cmake','-S',ROOT,'-B',gb,'-DGAMBIT_ENABLE_CUDA=ON','-DCMAKE_BUILD_TYPE=Release','-DCMAKE_CUDA_ARCHITECTURES=120-real;120-virtual'],'configure_cuda')
        invoke(['cmake','--build',gb,'--config','Release','--parallel','2'],'build_cuda')
        gpu=binary(gb,'gambit_cuda');invoke([gpu,'--inspect','--device',args.device],'device')
        hardware=json.loads((logdir/'device.txt').read_text());report['hardware']=hardware
        if '5070 ti' not in hardware['device'].lower() or 'laptop' not in hardware['device'].lower():
            raise Blocked('Detected device is not the requested RTX 5070 Ti Laptop GPU; recorded results must not be attributed to it')
        for name,g in selected.items():
            variants=[('texture',256)]
            if name in ['verify_xx','verify_xy']:variants=[('texture',b) for b in [32,128,256,512]]+[('global',256)]
            for fetch,block in variants:
                tag=f'{name}_{fetch}_{block}';run=out/'gpu'/tag
                invoke([gpu,'--asset',ROOT/'assets'/g['asset'],'--out',run,'--fetch',fetch,'--block',block,'--device',args.device,'--verify']+g['options'],'gpu_'+tag)
                for file,sha in g['files'].items():
                    if digest(run/file)!=sha:raise RuntimeError(f'GPU golden mismatch: {tag}/{file}')
                metadata=json.loads((run/'run.json').read_text())
                if metadata['status']!='GPU_CPU_EXACT_PASS' or not metadata['lut_readback_verified']:raise RuntimeError('Missing device equality evidence')
                report['cases']['gpu_'+tag]=dict(audit_trace(run),gpu_metadata=metadata,golden_match=True);save()
        # Repeat the same texture run in a fresh process, then exercise the embedded PTX path.
        g=gold['verify_xy']
        for tag,env in [('repeat',None),('forced_ptx',dict(os.environ,CUDA_FORCE_PTX_JIT='1'))]:
            run=out/'gpu'/tag
            invoke([gpu,'--asset',ROOT/'assets'/g['asset'],'--out',run,'--verify','--device',args.device],tag,env)
            for file,sha in g['files'].items():
                if digest(run/file)!=sha:raise RuntimeError(f'Replay mismatch: {tag}')
        invoke(['cuobjdump','--dump-sass',gpu],'sass')
        invoke(['cuobjdump','--dump-ptx',gpu],'ptx')
        report['disassembly']='CAPTURED_FOR_REVIEW_NOT_A_CACHE_HIT_CERTIFICATE'
        report['gpu_status']='GPU_FUNCTIONAL_PASS';save()
        if args.sanitizers:
            if not shutil.which('compute-sanitizer'):raise Blocked('Compute Sanitizer required for --sanitizers')
            for tool in ['memcheck','racecheck','initcheck','synccheck']:
                run=out/'instrumented'/tool
                invoke(['compute-sanitizer','--tool',tool,'--error-exitcode','3',gpu,'--asset',ROOT/'assets/verify_xy.gblut','--steps','8','--out',run,'--verify','--device',args.device],tool)
                text=(logdir/(tool+'.txt')).read_text()
                pattern=r'RACECHECK SUMMARY:\s+0\s+hazards' if tool=='racecheck' else r'ERROR SUMMARY:\s+0\s+errors'
                if not re.search(pattern,text):raise RuntimeError(f'{tool}: no explicit zero-error summary found; inspect log')
            report['sanitizers']='FOUR_TOOLS_PASS_ON_8_STEP_XY_CASE'
        if args.profile:
            if not shutil.which('ncu'):raise Blocked('Nsight Compute ncu required for --profile; do not disable security settings automatically')
            invoke(['ncu','--version'],'ncu_version');invoke(['ncu','--list-sections'],'ncu_sections')
            for fetch in ['texture','global']:
                run=out/'profile_run'/fetch;rep=out/('profile_'+fetch)
                invoke(['ncu','--section','MemoryWorkloadAnalysis','--section','LaunchStats','--kernel-name','regex:gambit_prepare',
                    '--launch-count','4','--export',rep,gpu,'--asset',ROOT/'assets/laptop_xy.gblut','--steps','4',
                    '--out',run,'--fetch',fetch,'--device',args.device],'profile_'+fetch)
            report['profiling']='CAPTURED_REQUIRES_COUNTER_INTERPRETATION; NOT A_SPEEDUP_CLAIM'
        report['gpu_status']='GPU_FUNCTIONAL_PASS';report['status']='GPU_FUNCTIONAL_PASS';save();print(report['status']);return 0
    except Blocked as e:
        report['status']='BLOCKED';report['reason']=str(e);save();print('BLOCKED:',e,file=sys.stderr);return 2
    except Exception as e:
        report['status']='FAIL';report['reason']=str(e);save();print('FAIL:',e,file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
