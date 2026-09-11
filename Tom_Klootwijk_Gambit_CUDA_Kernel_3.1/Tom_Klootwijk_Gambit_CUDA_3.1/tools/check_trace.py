#!/usr/bin/env python3
"""Read-only independent frame, latch, count and final accumulator audit."""
from __future__ import annotations
import argparse,csv,json,struct
from pathlib import Path
D=65536
def check(path:Path)->dict:
    raw=(path/'state.bin').read_bytes()
    if raw[:8]!=b'GBSTAT31' or len(raw)<24:raise ValueError('Bad state file')
    n,=struct.unpack_from('<I',raw,8)
    if n<1 or n>2048**2 or len(raw)!=24+40*n:raise ValueError('State size mismatch')
    cells=list(struct.iter_unpack('<6I2Q',raw[12:12+40*n]))
    final_step,level,last_growth=struct.unpack_from('<3I',raw,12+40*n)
    rows=list(csv.DictReader((path/'summary.csv').open(newline='')))
    counts=[0]*n;initial_latches=[0]*(n//32);ones=0;first_mass=None
    with (path/'words.bin').open('rb') as f:
        if f.read(8)!=b'GBWORD31':raise ValueError('Bad words magic')
        w,h,steps,planes,nw=struct.unpack('<5I',f.read(20))
        if w*h!=n or n%32 or planes!=5 or nw!=n//32 or len(rows)!=steps or final_step!=steps:raise ValueError('Frame dimensions mismatch')
        last=None
        for t in range(steps):
            payload=f.read(20*nw)
            if len(payload)!=20*nw:raise ValueError('Truncated bit frame')
            words=struct.unpack(f'<{5*nw}I',payload)
            for j in range(nw):
                if words[4*nw+j]!=words[j].bit_count()%2:raise ValueError(f'Parity failure step {t}, word {j}')
                if (initial_latches[j]^words[nw+j])!=words[2*nw+j]:raise ValueError('Latch event does not telescope')
                initial_latches[j]=words[nw+j]
                x=words[j]
                while x:
                    low=x&-x;b=low.bit_length()-1;counts[32*j+b]+=1;x-=low
            count=sum(x.bit_count() for x in words[:nw]);ones+=count
            r={k:int(v) for k,v in rows[t].items()}
            if r['step']!=t or r['errors'] or r['pulses']!=count or r['total_output']!=ones:raise ValueError('Summary/frame mismatch')
            if sum(x.bit_count() for x in words[nw:2*nw])!=r['latches']:raise ValueError('Latch count mismatch')
            mass=r['mass_u']+r['mass_v'];first_mass=mass if first_mass is None else first_mass
            if mass!=first_mass:raise ValueError('Non-conserved total mass')
            last=words
        if f.read(1):raise ValueError('Trailing word data')
    for i,(u,v,z,m,res,flags,ki,qo) in enumerate(cells):
        if not (0<=z<=D and 0<=m<=D and 0<=res<D and flags<=15 and D*qo+res==ki and counts[i]==qo):raise ValueError(f'Final per-cell certificate failed: {i}')
        for plane,shift in enumerate([1,0,3,2]):
            if ((last[plane*nw+i//32]>>(i%32))&1)!=((flags>>shift)&1):raise ValueError('Final packed flags mismatch')
    if sum(x[0]+x[1] for x in cells)!=first_mass or sum(x[6] for x in cells)!=int(rows[-1]['total_input']):raise ValueError('Final state/summary mismatch')
    return {'status':'TRACE_AUDIT_PASS','cells':n,'steps':steps,'pulse_bits':n*steps,'ones':ones,'total_mass':first_mass,
            'final_level':level,'last_growth_step':last_growth,'per_cell_final_certificates':n,
            'scope':'Checks delivered discrete trace; not an independent reconstruction of every prior drive or a GPU claim.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('run',type=Path);a=ap.parse_args();print(json.dumps(check(a.run),indent=2))
