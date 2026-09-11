#!/usr/bin/env python3
"""Import manually classified inventory metadata into a single-holder Prism view.

Set facet_id in chosen inventory rows. Unassigned rows remain unmapped. The caller
must explicitly confirm authority for the folder and the subject links. Nothing in
this local prototype verifies that declaration cryptographically or issues an ID.
"""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,argparse
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from uu_prism.core import Prism,load_registry,digest
ROOT=Path(__file__).resolve().parents[1]
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inventory',type=Path,required=True);p.add_argument('--holder',required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--confirm-authorized',action='store_true');p.add_argument('--confirm-holder-links',action='store_true')
    a=p.parse_args()
    if not a.confirm_authorized or not a.confirm_holder_links:p.error('Both authorization and holder-link confirmation are required')
    try:
        data=json.loads(a.inventory.read_text(encoding='utf-8'))
        if data.get('format')!='UU-PRISM-INVENTORY':raise ValueError('Wrong inventory format')
        now=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
        assigned=[r for r in data['files'] if r.get('facet_id')]
        targets={f:sum(r['facet_id']==f for r in assigned) for f in {r['facet_id'] for r in assigned}}
        state=Prism(a.holder,load_registry(ROOT/'spec/facets.json'),targets)
        for r in assigned:
            # Paths stay in the caller's inventory; opaque links enter the view.
            source='inventory:'+digest({'path':r['relative_path'],'inventory_root':data['root_label']})
            record={'record_id':'record:'+digest({'holder':a.holder,'source':source,'facet':r['facet_id']}),
              'holder_ref':a.holder,'facet_id':r['facet_id'],'source_ref':source,
              'source_kind':'holder_export','permission':'granted','permission_ref':'local:explicit-import-confirmation',
              'link_status':'holder_confirmed','observed_at':None,'received_at':now,
              'payload_sha256':r['payload_sha256'],'byte_size':r['byte_size'],
              'assertion_kind':'self_report' if r['facet_id']=='F30' else 'source_record'}
            state.add(record)
        a.out.mkdir(parents=True,exist_ok=True)
        for name,value in [('passport.json',state.export(now)),('snapshot.json',state.snapshot(now)),
                           ('migration_receipt.json',{'assigned':len(assigned),'unmapped':len(data['files'])-len(assigned),
                            'quarantined':len(state.rejections),'mode':'metadata index-and-link; payloads not copied'})]:
            (a.out/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({'active_links':len(state.records),'unmapped':len(data['files'])-len(assigned),'quarantined':len(state.rejections)}))
    except (KeyError,ValueError,OSError) as exc:print(str(exc),file=sys.stderr);sys.exit(1)
