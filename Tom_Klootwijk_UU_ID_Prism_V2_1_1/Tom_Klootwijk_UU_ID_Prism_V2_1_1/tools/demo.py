#!/usr/bin/env python3
"""Replay a synthetic holder's authorized metadata, never a real personal history."""
from pathlib import Path
import sys,json,hashlib,argparse
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from uu_prism.core import Prism,load_registry,digest
ROOT=Path(__file__).resolve().parents[1]
AS_OF='2026-09-11T12:00:00Z'
HOLDER='holder:synthetic-001'

def make_inputs() -> list[dict]:
    selected=['F01','F02','F03','F06','F08','F11','F13','F16','F19','F21','F24','F26','F27','F30','F31','F35']
    result=[]
    for i,f in enumerate(selected):
        payload=f'SYNTHETIC OBJECT {max(0,i-1) if i==1 else i}: no real human measurements.\n'.encode()
        observed='2024-06-01T08:00:00Z' if f in ('F01','F02','F26') else '2026-09-11T11:59:45Z'
        if f=='F30':observed=None
        if f=='F08':observed='2026-09-11T12:00:15Z'
        result.append({'record_id':f'demo:{f}','holder_ref':HOLDER,'facet_id':f,
          'source_ref':f'synthetic:object:{0 if i==1 else i}','source_kind':'synthetic',
          'permission':'granted','permission_ref':'synthetic:grant:001','link_status':'holder_confirmed',
          'observed_at':observed,'received_at':f'2026-09-11T11:59:{i:02d}Z',
          'payload_sha256':hashlib.sha256(payload).hexdigest(),'byte_size':len(payload),
          'assertion_kind':'synthetic'})
    return result

def run(out: Path) -> dict:
    out.mkdir(parents=True,exist_ok=True)
    registry=load_registry(ROOT/'spec/facets.json')
    plan=json.loads((ROOT/'data/synthetic_plan.json').read_text())
    plan['targets']['F01']=2;plan['targets']['F05']=0
    p=Prism(HOLDER,registry,plan['targets'])
    inputs=make_inputs();statuses=[p.add(r) for r in inputs]
    before=p.snapshot(AS_OF)
    statuses.append(p.add(inputs[0]))
    for changes in ({'holder_ref':'holder:someone-else'},{'assertion_kind':'inferred'},
                    {'permission':'withheld'},{'facet_id':'F99'}):
        candidate=dict(inputs[0],**changes);statuses.append(p.add(candidate))
    changed=dict(inputs[10],received_at='2026-09-11T11:59:50Z',observed_at='2026-09-11T11:59:49Z',
                 supersedes=digest(inputs[10]),payload_sha256=hashlib.sha256(b'SYNTHETIC CORRECTED SCREEN-TIME EXPORT').hexdigest(),byte_size=38)
    statuses.append(p.add(changed))
    p.revoke('demo:F03','2026-09-11T11:59:55Z')
    exported=p.export(AS_OF);restored=Prism.restore(exported)
    if restored.snapshot(AS_OF)!=p.snapshot(AS_OF):raise ArithmeticError('Replay mismatch')
    for name,value in [('input_records.json',inputs),('snapshot_before.json',before),('passport.json',exported),('snapshot.json',p.snapshot(AS_OF))]:
        (out/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    summary={'version':'2.1.1','fixture':'synthetic-single-holder-16','input_records':len(inputs),
      'statuses':statuses,'active_links':exported['snapshot']['active_links'],
      'active_objects':exported['snapshot']['active_objects'],'active_unique_bytes':exported['snapshot']['active_unique_bytes'],
      'withdrawn_links':len(p.withdrawn),'quarantined_attempts':len(p.rejections),'duplicate_attempts':p.duplicates,
      'events':len(p.events),'fresh_facets':sum(f['data_status']=='fresh' for f in exported['snapshot']['facets']),
      'stale_facets':sum(f['data_status']=='stale' for f in exported['snapshot']['facets']),
      'unknown_time_facets':sum(f['data_status']=='time_unknown' for f in exported['snapshot']['facets']),
      'clock_conflict_facets':sum(f['data_status']=='clock_conflict' for f in exported['snapshot']['facets']),
      'uu_minimum':exported['snapshot']['uu_minimum'],'declared_plan_complete':False,
      'chain_verified':p.check_chain(),'restore_equal':True,'snapshot_sha256':exported['snapshot']['snapshot_hash']}
    (out/'results.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--out',type=Path,default=Path('demo_run'))
    args=parser.parse_args();print(json.dumps(run(args.out),indent=2))
