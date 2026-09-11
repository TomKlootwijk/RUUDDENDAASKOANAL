#!/usr/bin/env python3
"""Reproduce the V2 numerical, UU ID, chronotemporal and mapping examples."""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from tkuft.core import AUTHOR,dutch_number
from tkuft.engine import D,integer_chart_fixture,tick,pack_planes
from tkuft.codec import encode_state,encode_capsule,decode_capsule,state_bits
from tkuft.uuid import StateHorizon,encode_horizon,decode_horizon,tick_horizon,TaggedUnion,SphereHorizon
from tkuft.identity import Lineage,integrate_segments,history_envelope,continuity_path
from tkuft.wrap import AddressChart

def jsave(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def csvsave(path,rows):
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def run(out:Path,steps:int=64)->dict:
    if type(steps) is not int or not 1<=steps<=4096:raise ValueError('Choose 1 through 4096 updates')
    out.mkdir(parents=True,exist_ok=True)
    seed,s=integer_chart_fixture();initial=s;h=encode_horizon(seed,s);union_bits=list(h.bits)
    (out/'initial.tku').write_bytes(encode_capsule(seed,s))
    K=[0]*64;Q=[0]*64;rows=[];words=[];intervened=s;feedback=[];first_s=first_q=None;baseline_q=[];intervention_q=[];same=True;strict_envelope_changes=0
    for n in range(steps):
        s,summary=tick(seed,s);h,hs=tick_horizon(seed,h)
        if hs!=summary or decode_horizon(seed,h)!=s:raise ArithmeticError('UU ID conjugacy failed')
        next_union=[a|b for a,b in zip(union_bits,h.bits)]
        strict_envelope_changes+=int(next_union!=union_bits);union_bits=next_union
        for i,c in enumerate(s.cells):K[i]+=c.z;Q[i]+=c.pulse
        rows.append({'update':n,**summary});words.append({'update':n,**pack_planes(s)})
        intervened,_=tick(seed,intervened,7 if n==3 else None)
        changed=sum(a!=b for a,b in zip(s.cells,intervened.cells));changed_q=sum(a.pulse!=b.pulse for a,b in zip(s.cells,intervened.cells))
        if changed and first_s is None:first_s=n
        if changed_q and first_q is None:first_q=n
        feedback.append({'update':n,'baseline_z7':s.cells[7].z,'intervened_z7':intervened.cells[7].z,'changed_cells':changed,'changed_pulses':changed_q})
        baseline_q.append(str(s.cells[7].pulse));intervention_q.append(str(intervened.cells[7].pulse))
    final=encode_state(seed,s)
    (out/'final.tku').write_bytes(encode_capsule(seed,s));(out/'final_state.bin').write_bytes(final)
    certificates=[{'cell':i,'start_residual':initial.cells[i].r,'end_residual':c.r,'K':K[i],'Q':Q[i],'identity_holds':D*Q[i]+c.r==initial.cells[i].r+K[i]} for i,c in enumerate(s.cells)]
    if not all(r['identity_holds'] for r in certificates):raise ArithmeticError('Certificate failed')
    restart=initial
    for _ in range(steps//2):restart,_=tick(seed,restart)
    rs,restart=decode_capsule(encode_capsule(seed,restart))
    for _ in range(steps-steps//2):restart,_=tick(rs,restart)
    if restart!=s:raise ArithmeticError('Restart failed')
    csvsave(out/'summary.csv',rows);csvsave(out/'feedback.csv',feedback);csvsave(out/'certificates.csv',certificates);jsave(out/'words.json',words)
    jsave(out/'state_horizon.json',{'format':'TKUFT2-UU-state','bit_count':len(h.bits),'bits':list(h.bits),'spacing':3,'radius':.25,'permanent_anchor':0,'decoder_threshold':.25})
    jsave(out/'historical_state_envelope.json',{'format':'TKUFT2-UU-history-projection','included_states':steps+1,'bitwise_or':union_bits,'active_count':sum(union_bits),'strict_envelope_changes':strict_envelope_changes,'current_state_file':'state_horizon.json'})
    union=TaggedUnion((SphereHorizon('A',(0,),1),SphereHorizon('B',(3,),1)))
    samples=[]
    for k in range(141):
        x=-2+k*.05;r=union.evaluate((x,));samples.append({'x':x,'delta_A':r['layers'][0]['delta'],'delta_B':r['layers'][1]['delta'],'uu_id':r['value'],'witnesses':'|'.join(r['witnesses'])})
    csvsave(out/'uu_id_samples.csv',samples)
    little=StateHorizon((0,1,0,1,1,0,0,1));small=[{'j':j,'bit':b,'coordinate':3*j,'horizon_value':little.evaluate(3*j),'decoded':int(little.evaluate(3*j)<=.25)} for j,b in enumerate(little.bits,1)]
    csvsave(out/'eight_bit_queries.csv',small)
    events=[{'id':'experience:0','time':0,'centre':[0],'threshold':1},{'id':'experience:1','time':1,'centre':[.25],'threshold':1},{'id':'experience:2','time':2,'centre':[.5],'threshold':1}]
    jsave(out/'synthetic_experiences.json',{'origin':'explicit V2 synthetic example','events':events,'continuity':continuity_path([(0,),(.25,),(.5,)],.25)})
    chronology=[]
    for n in range(1,5):
        result=integrate_segments([(1,v) for v in (2,4,1,3)[:n]],.5)
        chronology.append({'time':n,**result,'historical_horizon_at_1_5':history_envelope(events,(1.5,),n)['value']})
    csvsave(out/'chronotemporal.csv',chronology)
    log=Lineage();log.append('root',0,[],{'origin':'synthetic example','label':'original structure'});log.append('branch:A',1,['root'],{'label':'material transition'});log.append('branch:B',1,['root'],{'label':'knowledge transition'});log.append('merge',2,['branch:A','branch:B'],{'label':'Theseus identity record'})
    jsave(out/'lineage.json',log.records())
    chart=AddressChart();mapping=[]
    for j,b in enumerate(h.bits,1):
        a=chart.address(j);x,y,z=a.pop('centre');mapping.append({**a,'x':x,'y':y,'z':z,'bit':b})
    csvsave(out/'bit_address_map.csv',mapping)
    nofb,ablate=integer_chart_fixture(False);ablate_count=0
    for _ in range(steps):ablate,ad=tick(nofb,ablate);ablate_count+=ad['pulses']
    result={'version':'2.0.0','author':AUTHOR,'fixture':seed.name,'cells':64,'levels':2,'updates':steps,'initial_mass':seed.initial_mass,'final_mass':summary['mass'],'total_pulses':sum(Q),'last_update_pulses':summary['pulses'],'state_bits':len(h.bits),'state_bytes':len(final),'local_certificates_passed':sum(r['identity_holds'] for r in certificates),'restart_equal':restart==s,'unsigned_conjugate_updates_verified':steps,'final_state_sha256':hashlib.sha256(final).hexdigest(),'final_capsule_sha256':hashlib.sha256((out/'final.tku').read_bytes()).hexdigest(),'history_envelope_active_bits':sum(union_bits),'history_envelope_strict_changes':strict_envelope_changes,'feedback_disabled_total_pulses':ablate_count,'feedback_witness':{'cell':7,'tick':3,'first_state_difference':first_s,'first_output_difference':first_q,'baseline_cell7_first40':''.join(baseline_q[:40]),'intervened_cell7_first40':''.join(intervention_q[:40])},'uu_id_example':union.evaluate((1.5,)),'chronotemporal_example':chronology[-1],'lineage_records':len(log.records()),'logpolar_address_count':chart.count,'logpolar_minimum_separation':chart.minimum_separation,'logpolar_horizon_radius':chart.horizon_radius,'dutch_count_matches':sum(dutch_number(n)['count_match'] for n in range(100))}
    jsave(out/'demo_output.json',result);return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--out',type=Path,default=Path('demo_run'));parser.add_argument('--steps',type=int,default=64);a=parser.parse_args();print(json.dumps(run(a.out,a.steps),ensure_ascii=False,indent=2))
