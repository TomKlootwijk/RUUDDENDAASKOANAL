#!/usr/bin/env python3
"""Negative-path contract tests against a built native CPU executable."""
import argparse,subprocess,tempfile,struct,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--exe',type=Path,required=True);a=ap.parse_args();exe=a.exe.resolve()
    asset=ROOT/'assets/verify_xy.gblut';results=[]
    def reject(name,args):
        p=subprocess.run([str(exe)]+[str(x) for x in args],capture_output=True,text=True)
        if p.returncode==0:raise AssertionError(name+' was accepted')
        results.append({'test':name,'returncode':p.returncode,'diagnostic':p.stderr.strip()})
    with tempfile.TemporaryDirectory() as d:
        tmp=Path(d)
        for k,v in [('--steps','0'),('--steps','4097'),('--steps','-1'),('--block','48'),('--feedback','2'),('--fetch','bogus'),('--inject-cell','99999999')]:
            reject(k+'='+v,['--asset',asset,'--out',tmp/'no_output',k,v])
        reject('unpaired injection',['--asset',asset,'--inject-step','1'])
        reject('unknown flag',['--asset',asset,'--alien','1'])
        raw=asset.read_bytes()
        corruptions={'bad_magic':b'BADMAGIC'+raw[8:],'truncated':raw[:-4],'extra':raw+b'1234'}
        for index,value,name in [(0,31,'invalid_width'),(10,1,'unsafe_outflow'),(7,0,'division_zero')]:
            b=bytearray(raw);struct.pack_into('<I',b,16+index*4,value);corruptions[name]=b
        for name,b in corruptions.items():
            f=tmp/(name+'.gblut');f.write_bytes(b);reject(name,['--asset',f,'--out',tmp/name])
        out=tmp/'one_run';p=subprocess.run([str(exe),'--asset',str(asset),'--steps','1','--out',str(out)],capture_output=True)
        if p.returncode:raise AssertionError('Valid one-step run failed')
        reject('stale output refusal',['--asset',asset,'--steps','1','--out',out])
    print(json.dumps({'status':'NEGATIVE_PATH_PASS','tests':len(results),'results':results},indent=2))
if __name__=='__main__':main()
