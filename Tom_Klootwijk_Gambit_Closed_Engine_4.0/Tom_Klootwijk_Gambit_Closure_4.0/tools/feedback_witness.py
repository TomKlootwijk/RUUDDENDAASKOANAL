#!/usr/bin/env python3
from pathlib import Path
import argparse,json,csv
from reference import Reference,decode_asset
ROOT=Path(__file__).resolve().parents[1]
def witness(asset:Path,out:Path):
    p,lut=decode_asset(asset.read_bytes());a=Reference(p,lut);b=Reference(p,lut);records=[]
    first_state=first_pulse=None
    for t in range(40):
        a.tick();b.tick(7 if t==3 else -1)
        nd=sum(x!=y for x,y in zip(a.cells,b.cells))
        hd=sum((x^y).bit_count() for x,y in zip(a.words[:a.n//32],b.words[:b.n//32]))
        if nd and first_state is None:first_state=t
        if hd and first_pulse is None:first_pulse=t
        records.append([t,a.cells[7].z,b.cells[7].z,(a.cells[7].flags>>1)&1,(b.cells[7].flags>>1)&1,nd,hd])
    if first_state!=3 or first_pulse is None:raise RuntimeError('No causal witness')
    out.mkdir(parents=True,exist_ok=False)
    with (out/'trace.csv').open('w',newline='') as f:
        w=csv.writer(f,lineterminator='\n');w.writerow('tick baseline_z7 intervention_z7 baseline_q7 intervention_q7 differing_cells differing_pulse_bits'.split());w.writerows(records)
    result={'asset':asset.name,'intervention':'One prior-pulse read XOR 1 at cell 7, zero-based tick 3; not ordinary autonomous operation',
            'identical_before_tick':3,'first_state_difference_tick':first_state,'first_pulse_difference_tick':first_pulse,
            'baseline_q7':''.join(str(row[3]) for row in records),'intervention_q7':''.join(str(row[4]) for row in records),
            'claim':'Causal self-feedback in this finite machine, not subjective experience'}
    (out/'witness.json').write_text(json.dumps(result,indent=2)+'\n');return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--asset',type=Path,default=ROOT/'assets/verify_xy.gblut');p.add_argument('--out',type=Path,required=True);a=p.parse_args();print(json.dumps(witness(a.asset,a.out),indent=2))
