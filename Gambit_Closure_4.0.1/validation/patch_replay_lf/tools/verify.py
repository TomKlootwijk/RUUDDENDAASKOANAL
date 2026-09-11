#!/usr/bin/env python3
"""Fail-closed local verification. No network, installations or golden regeneration.
Default CPU mode verifies closure, not GPU execution. --hardware requires native
GPU equality and never substitutes CPU evidence. --formal requires Z3.
"""
from __future__ import annotations
from pathlib import Path
import argparse,datetime,hashlib,json,os,platform,re,shutil,subprocess,sys
from reference import Reference,decode_asset,run as python_run
from audit_trace import audit
ROOT=Path(__file__).resolve().parents[1]
FILES=['initial.gbc','final.gbc','words.bin','summary.csv','counts.bin']
class Blocked(RuntimeError):pass

def tool_path(name):
    """Use a direct executable, including NVIDIA's simple Windows launchers."""
    found=shutil.which(name)
    if not found:raise Blocked(name+' absent')
    path=Path(found).resolve()
    if os.name=='nt' and path.suffix.lower() in ('.bat','.cmd'):
        # Only unwrap a plain forwarding launcher. Do not discard setup commands
        # or run batch contents through a shell with differently quoted arguments.
        lines=[line.strip() for line in path.read_text().splitlines() if line.strip()]
        target=re.fullmatch(r'"%~dp0([^"\r\n]+\.exe)"\s+%\*',lines[1],re.IGNORECASE) if len(lines)==2 and lines[0].lower()=='@echo off' else None
        if target:
            direct=(path.parent/target.group(1).lstrip('\\/')).resolve()
            if direct.is_file():return direct
        raise Blocked('Cannot resolve batch launcher to a direct executable: '+str(path)+'; put the executable directory on PATH')
    return path

def digest(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def exe(build,name):
    for p in [build/(name+('.exe' if os.name=='nt' else '')),build/'Release'/(name+('.exe' if os.name=='nt' else ''))]:
        if p.exists():return p
    raise RuntimeError('Built executable missing: '+name)
def main():
    ap=argparse.ArgumentParser();m=ap.add_mutually_exclusive_group();m.add_argument('--cpu-only',action='store_true');m.add_argument('--hardware',action='store_true')
    ap.add_argument('--formal',action='store_true');ap.add_argument('--sanitizers',action='store_true');ap.add_argument('--profile',action='store_true')
    ap.add_argument('--cmake-cuda-toolset',help='Explicit CMake -T value for the CUDA build only (for example cuda=12.8 with Visual Studio)')
    ap.add_argument('--quick',action='store_true');ap.add_argument('--out',type=Path)
    a=ap.parse_args()
    if (a.profile or a.sanitizers) and not a.hardware:ap.error('CUDA instrumentation requires --hardware')
    if a.cmake_cuda_toolset and not a.hardware:ap.error('--cmake-cuda-toolset requires --hardware')
    out=(a.out or ROOT/'local_verification'/datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S_%fZ')).resolve()
    if out.exists():ap.error('--out must be an unused path')
    out.mkdir(parents=True);logs=out/'logs';logs.mkdir();report={'schema':'gambit-closure-verification-4.0','status':'RUNNING','scope':'quick' if a.quick else 'full',
        'cpu':'RUNNING','gpu':'NOT_RUN','formal':'NOT_RUN','sanitizers':'NOT_RUN','profile':'NOT_RUN',
        'requested':{'cpu':True,'gpu':a.hardware,'formal':a.formal,'sanitizers':a.sanitizers,'profile':a.profile},
        'cmake_cuda_toolset':a.cmake_cuda_toolset,'tools':{},'goldens_modified':False,'platform':platform.platform(),'python':platform.python_version(),'commands':[],'cases':{}}
    active_gate='cpu'
    def save():(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    def require_tool(name):
        path=tool_path(name);report['tools'][name]=str(path);save();return path
    def invoke(cmd,tag,env=None):
        cmd=[str(c) for c in cmd];print('+',subprocess.list2cmdline(cmd),flush=True)
        record={'argv':cmd,'returncode':None,'log':tag+'.txt','gate':active_gate}
        if env is not None:record['environment_overrides']={k:v for k,v in env.items() if os.environ.get(k)!=v}
        report['commands'].append(record);save()
        with (logs/(tag+'.txt')).open('w') as f:
            try:p=subprocess.run(cmd,cwd=ROOT,stdout=f,stderr=subprocess.STDOUT,env=env)
            except OSError as e:
                record['launch_error']=str(e);f.write(str(e)+'\n');save()
                raise Blocked(f'{tag} could not start: {e}; see logs/{tag}.txt') from e
        record['returncode']=p.returncode;save()
        if p.returncode==2 and tag=='formal':raise Blocked('Formal solver prerequisite unavailable; see formal/report.json')
        if p.returncode:raise RuntimeError(f'{tag} failed with exit code {p.returncode}; see logs/{tag}.txt')
    def same(x,y):
        for file in FILES:
            if digest(x/file)!=digest(y/file):raise RuntimeError(f'Conformance mismatch: {file}')
    try:
        manifest=ROOT/'SHA256SUMS.txt'
        if not manifest.exists():raise Blocked('Release integrity manifest is absent')
        count=0
        for line in manifest.read_text().splitlines():
            expected,name=line.split('  ',1);p=(ROOT/name).resolve()
            if not p.is_relative_to(ROOT) or digest(p)!=expected:raise RuntimeError('Release integrity mismatch: '+name)
            count+=1
        report['integrity_files']=count
        cmake=require_tool('cmake');ctest=require_tool('ctest')
        build=out/'build'
        invoke([cmake,'-S',ROOT,'-B',build,'-DGAMBIT_ENABLE_CUDA=OFF','-DCMAKE_BUILD_TYPE=Release'],'configure')
        invoke([cmake,'--build',build,'--config','Release','--parallel','2'],'build')
        invoke([ctest,'--test-dir',build,'-C','Release','-V','--output-on-failure'],'native_tests')
        invoke([sys.executable,'-m','unittest','discover','-s','tests','-p','test_*.py','-v'],'python_tests')
        cpu=exe(build,'gambit');gold=json.loads((ROOT/'assets/closure_goldens.json').read_text())['cases']
        selected={k:g for k,g in gold.items() if not(a.quick and k.startswith('laptop'))}
        for name,g in selected.items():
            dest=out/'native'/name
            invoke([cpu,'--asset',ROOT/'assets'/g['asset'],'--out',dest,'--steps',g['steps']],'native_'+name)
            for f,h in g['files'].items():
                if digest(dest/f)!=h:raise RuntimeError('Golden mismatch: '+name+'/'+f)
            evidence=audit(dest);evidence['golden_match']=True
            if not name.startswith('laptop'):
                py=out/'python'/name;python_run(Reference(*decode_asset((ROOT/'assets'/g['asset']).read_bytes())),py,g['steps']);same(dest,py);evidence['independent_python']=True
                gate=out/'gates'/name;invoke([cpu,'--asset',ROOT/'assets'/g['asset'],'--backend','gates','--out',gate,'--steps',g['steps']],'gates_'+name);same(dest,gate);evidence['boolean_ALU']=True
            report['cases'][name]=evidence;save()
        # Standalone resume: no --asset path and no missing sidecar lookup is allowed.
        asset=ROOT/'assets/micro_xy.gblut';first=out/'split_first';second=out/'split_second'
        invoke([cpu,'--asset',asset,'--out',first,'--steps',17],'split_first')
        invoke([cpu,'--resume',first/'final.gbc','--out',second,'--steps',47],'split_second')
        full=out/'native/micro_xy'
        if digest(full/'final.gbc')!=digest(second/'final.gbc') or (first/'words.bin').read_bytes()[28:]+(second/'words.bin').read_bytes()[28:]!=(full/'words.bin').read_bytes()[28:]:raise RuntimeError('Checkpoint semigroup failure')
        report['checkpoint_split_17_47']='PASS'
        # Negative paths must fail, not silently select defaults.
        negatives=[['--steps','0'],['--backend','nonsense'],['--feedback','2'],['--block','31']]
        for i,extra in enumerate(negatives):
            p=subprocess.run([str(cpu),'--asset',str(asset),'--out',str(out/f'negative_{i}')]+extra,capture_output=True,text=True)
            if p.returncode==0:raise RuntimeError('Invalid option was accepted')
        report['negative_cli_cases']=len(negatives)
        report['cpu']='PASS';save()
        if a.formal:
            active_gate='formal';report['formal']='RUNNING';save()
            try:invoke([sys.executable,'tools/check_formal.py','--out',out/'formal'],'formal')
            finally:
                formal_report=out/'formal/report.json'
                if formal_report.exists():
                    fr=json.loads(formal_report.read_text());report['formal']=fr['status'];save()
            if report['formal']!='PASS':raise RuntimeError('Formal solver did not report PASS; see formal/report.json')
        if not a.hardware:report['status']='CPU_PASS_GPU_NOT_RUN';save();return 0
        active_gate='gpu';report['gpu']='RUNNING';save()
        nvcc=require_tool('nvcc');smi=require_tool('nvidia-smi');cuobjdump=require_tool('cuobjdump')
        invoke([nvcc,'--version'],'nvcc_version');invoke([smi],'nvidia_smi')
        gb=out/'cuda_build';cuda_configure=[cmake,'-S',ROOT,'-B',gb,'-DGAMBIT_ENABLE_CUDA=ON','-DCMAKE_BUILD_TYPE=Release']
        if a.cmake_cuda_toolset:cuda_configure+=['-T',a.cmake_cuda_toolset]
        invoke(cuda_configure,'cuda_configure')
        invoke([cmake,'--build',gb,'--config','Release','--parallel','2'],'cuda_build');gpu=exe(gb,'gambit_cuda')
        invoke([ctest,'--test-dir',gb,'-C','Release','-V','--output-on-failure'],'cuda_tests')
        invoke([gpu,'--inspect'],'device');dev=json.loads((logs/'device.txt').read_text());report['device']=dev
        name=dev['device'].lower()
        if '5070 ti' not in name or 'laptop' not in name:raise Blocked('Detected device is not the requested RTX 5070 Ti Laptop GPU')
        for name,g in selected.items():
            for fetch,block in ([('texture',32),('texture',128),('texture',256),('texture',512),('global',256)] if name=='verify_xy' else [('texture',256)]):
                target=out/'cuda'/f'{name}_{fetch}_{block}';tag=f'cuda_{name}_{fetch}_{block}'
                invoke([gpu,'--asset',ROOT/'assets'/g['asset'],'--out',target,'--steps',g['steps'],'--fetch',fetch,'--block',block],tag)
                same(target,out/'native'/name);report['cases'][tag]=audit(target)
        # Native resume and a fresh process with forced PTX JIT.
        for tag,env in [('cuda_repeat',None),('cuda_forced_ptx',dict(os.environ,CUDA_FORCE_PTX_JIT='1'))]:
            target=out/tag;invoke([gpu,'--asset',ROOT/'assets/micro_xy.gblut','--out',target,'--steps',64],tag,env);same(target,out/'native/micro_xy')
        gpu_resume=out/'cuda_resume';invoke([gpu,'--resume',first/'final.gbc','--out',gpu_resume,'--steps',47],'cuda_resume');same(gpu_resume,second)
        invoke([cuobjdump,'--dump-ptx','--dump-sass',gpu],'ptx_sass')
        report['gpu']='PASS';save()
        if a.sanitizers:
            active_gate='sanitizers';report['sanitizers']='RUNNING';save()
            sanitizer=require_tool('compute-sanitizer')
            for tool in ['memcheck','racecheck','initcheck','synccheck']:
                invoke([sanitizer,'--tool',tool,'--error-exitcode','1',gpu,'--asset',ROOT/'assets/verify_xy.gblut','--steps',8,'--out',out/('sanitize_'+tool)],'sanitize_'+tool)
            report['sanitizers']='PASS';save()
        if a.profile:
            active_gate='profile';report['profile']='RUNNING';save()
            ncu=require_tool('ncu')
            for fetch in ['texture','global']:
                invoke([ncu,'--set','basic','--export',out/('ncu_'+fetch),gpu,'--asset',ROOT/'assets/verify_xy.gblut','--fetch',fetch,'--steps',8,'--out',out/('profile_'+fetch)],'profile_'+fetch)
            report['profile']='CAPTURED_FOR_REVIEW_NOT_A_SPEED_CLAIM'
        report['gpu']='PASS';report['status']='GPU_CPU_EXACT_PASS';save();return 0
    except Blocked as e:report[active_gate]='BLOCKED';report.update(status='BLOCKED',failed_gate=active_gate,reason=str(e));save();print('BLOCKED:',e);return 2
    except Exception as e:report[active_gate]='FAIL';report.update(status='FAIL',failed_gate=active_gate,reason=str(e));save();print('FAIL:',e);return 1
if __name__=='__main__':sys.exit(main())
