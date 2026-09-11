#!/usr/bin/env python3
"""Run frozen SMT-LIB obligations via z3 executable or installed libz3 C API.
Uses only Python's standard library. Never downloads a solver. Exit 2 = BLOCKED.
The Z3 proof logs are solver evidence, not independently rechecked proof objects.
"""
from __future__ import annotations
from pathlib import Path
import argparse,ctypes,ctypes.util,json,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
def runner():
    exe=shutil.which('z3')
    if exe:
        version=subprocess.check_output([exe,'--version'],text=True).strip()
        def run(text):
            p=subprocess.run([exe,'-in'],input=text,text=True,capture_output=True,timeout=60)
            if p.returncode:raise RuntimeError(p.stdout+p.stderr)
            return p.stdout
        return version,run
    name=ctypes.util.find_library('z3')
    if not name:raise FileNotFoundError('Neither z3 executable nor libz3 is installed')
    lib=ctypes.CDLL(name)
    lib.Z3_mk_config.restype=ctypes.c_void_p
    lib.Z3_set_param_value.argtypes=[ctypes.c_void_p,ctypes.c_char_p,ctypes.c_char_p]
    lib.Z3_mk_context.argtypes=[ctypes.c_void_p];lib.Z3_mk_context.restype=ctypes.c_void_p
    lib.Z3_del_config.argtypes=[ctypes.c_void_p];lib.Z3_del_context.argtypes=[ctypes.c_void_p]
    lib.Z3_eval_smtlib2_string.argtypes=[ctypes.c_void_p,ctypes.c_char_p];lib.Z3_eval_smtlib2_string.restype=ctypes.c_char_p
    lib.Z3_get_full_version.restype=ctypes.c_char_p;version=lib.Z3_get_full_version().decode()
    def run(text):
        cfg=lib.Z3_mk_config();lib.Z3_set_param_value(cfg,b'proof',b'true');ctx=lib.Z3_mk_context(cfg);lib.Z3_del_config(cfg)
        try:return lib.Z3_eval_smtlib2_string(ctx,text.encode()).decode()
        finally:lib.Z3_del_context(ctx)
    return version,run

def check(out:Path):
    out.mkdir(parents=True,exist_ok=False);report={'status':'RUNNING','targets':[]}
    try:
        version,solve=runner();report['solver_version']=version
        for target in json.loads((ROOT/'formal/obligations.json').read_text())['targets']:
            answer=solve((ROOT/'formal'/target['file']).read_text());(out/(target['name']+'.log')).write_text(answer)
            actual=answer.strip().splitlines()[0].strip();ok=actual==target['expected'] and '(error' not in answer
            report['targets'].append(dict(target,actual=actual,passed=ok));print(target['name'],actual,flush=True)
            if not ok:raise RuntimeError('SMT target did not meet expected result')
        report['status']='PASS'
    except FileNotFoundError as e:report.update(status='BLOCKED',reason=str(e))
    except Exception as e:report.update(status='FAIL',reason=str(e))
    (out/'report.json').write_text(json.dumps(report,indent=2)+'\n')
    return 0 if report['status']=='PASS' else 2 if report['status']=='BLOCKED' else 1
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();sys.exit(check(a.out))
