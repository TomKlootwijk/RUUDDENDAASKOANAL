#!/usr/bin/env python3
"""Independent, standard-library scalar specification. No imports from native code.

Uses Python unbounded integers and explicit modulo 2^32 only for initial mixing.
Its traces are directly comparable with the C++ and CUDA canonical byte streams.
"""
from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass
import argparse, csv, hashlib, json, struct
D=65536
FIELDS=('width height levels start_level steps threshold feedback_gain memory_divisor '
        'phase_stride feedback_angle open_shift closed_shift reaction_uv_shift '
        'reaction_vu_shift growth_dwell growth_divisor seed pair device_budget_mib').split()
@dataclass(frozen=True)
class Cell:
    u:int;v:int;z:int;m:int;r:int;flags:int;ki:int;qo:int
    def serialize(self)->bytes: return struct.pack('<6I2Q',self.u,self.v,self.z,self.m,self.r,self.flags,self.ki,self.qo)
def trunc_div(x:int,y:int)->int: return x//y if x>=0 else -((-x)//y)
def mix32(x:int)->int:
    x^=x>>16;x=(x*0x7feb352d)&0xffffffff;x^=x>>15;x=(x*0x846ca68b)&0xffffffff;return x^(x>>16)
def load_asset(path:Path):
    raw=path.read_bytes()
    if len(raw)<92:raise ValueError('Truncated header')
    magic,ver,num,*data=struct.unpack_from('<8sII19I',raw)
    if (magic,ver,num)!=(b'GBLUT31\0',1,19):raise ValueError('Bad format')
    p=dict(zip(FIELDS,data));count=p['width']*p['height']*p['levels']
    if count>5*2048**2 or len(raw)!=92+4*count:raise ValueError('Invalid payload size')
    return p,list(struct.unpack_from(f'<{count}I',raw,92))
class Reference:
    def __init__(self,p:dict,lut:list[int],feedback:int=1,inject_step:int=-1,inject_cell:int=-1):
        self.p=p.copy();self.lut=lut;self.feedback=feedback;self.inject_step=inject_step;self.inject_cell=inject_cell
        self.n=p['width']*p['height'];self.level=p['start_level'];self.step_number=0;self.last_growth=0
        self.words=[0]*(5*self.n//32);self.cells=[]
        for i in range(self.n):
            active=(lut[self.level*self.n+i]&65535)<=32768
            h=mix32(i^p['seed']^((p['pair']*0x9e3779b9)&0xffffffff))
            self.cells.append(Cell((64+(h&63))*active,(32+((h>>6)&31))*active,D//2,D//2,0,0,0,0))
        self.initial_mass=sum(c.u+c.v for c in self.cells)
        self.samples=[]
    def step(self):
        p=self.p;w=p['width'];h=p['height'];n=self.n;nw=n//32;t=self.step_number;old=self.cells;s=[]
        for i,c in enumerate(old):
            q=(self.words[i//32]>>(i%32))&1
            if t==self.inject_step and i==self.inject_cell:q^=1
            angle=(i%w+t*p['phase_stride']+(q*p['feedback_angle'] if self.feedback else 0))%w
            tex=self.lut[(self.level*h+i//w)*w+angle];d=(tex&65535)-32768
            m=trunc_div(c.m-D//2,p['memory_divisor']) if self.feedback else 0
            drive=(tex>>16)+16*m+(p['feedback_gain']*(2*q-1) if self.feedback else 0)
            s.append((d-m,max(0,min(D,drive))))
        words=[0]*(5*nw);next_cells=[]
        for i,c in enumerate(old):
            x=i%w;y=i//w;neighbors=[y*w+(x-1)%w,y*w+(x+1)%w]
            if y>0:neighbors.append(i-w)
            if y+1<h:neighbors.append(i+w)
            ou=iu=ov=iv=0
            for j in neighbors:
                if s[i][0]>0 or s[j][0]>0:continue
                shift=p['open_shift'] if (c.flags|old[j].flags)&1 else p['closed_shift']
                ou+=c.u//(1<<shift);iu+=old[j].u//(1<<shift)
                ov+=c.v//(1<<shift);iv+=old[j].v//(1<<shift)
            u=c.u-ou+iu;v=c.v-ov+iv;uv=u//(1<<p['reaction_uv_shift']);vu=v//(1<<p['reaction_vu_shift'])
            un=u-uv+vu;vn=v-vu+uv
            material=(D*un)//(un+vn) if un+vn else D//2
            drive=(3*s[i][1]+material)//4
            z=(3*c.z+drive)//4;m=(15*c.m+z)//16;a=c.r+z;q=int(a>=D);r=a-D*q
            b=1 if s[i][0]<=-p['threshold'] else 0 if s[i][0]>=p['threshold'] else c.flags&1
            event=(c.flags&1)^b;inside=int(s[i][0]<=0)
            cell=Cell(u-uv+vu,v-vu+uv,z,m,r,b|(q<<1)|(inside<<2)|(event<<3),c.ki+z,c.qo+q)
            assert 0<=cell.u<=0xffffffff and 0<=cell.v<=0xffffffff
            assert 0<=m<=D and 0<=z<=D and 0<=r<D and D*cell.qo+r==cell.ki
            next_cells.append(cell)
            for plane,bit in enumerate([q,b,event,inside]):words[plane*nw+i//32]|=bit<<(i%32)
        for i in range(nw):words[4*nw+i]=words[i].bit_count()%2
        self.cells=next_cells;self.samples=s;self.words=words
        used=self.level;pulses=sum((c.flags>>1)&1 for c in next_cells)
        self.step_number+=1;growth=0
        if self.level+1<p['levels'] and self.step_number-self.last_growth>=p['growth_dwell'] and pulses*p['growth_divisor']>=n:
            self.level+=1;self.last_growth=self.step_number;growth=1
        mu=sum(c.u for c in next_cells);mv=sum(c.v for c in next_cells)
        assert mu+mv==self.initial_mass
        return [t,used,self.level,growth,pulses,sum(c.flags&1 for c in next_cells),mu,mv,
                sum(c.ki for c in next_cells),sum(c.qo for c in next_cells),0]
    def serialize_state(self):
        return b'GBSTAT31'+struct.pack('<I',self.n)+b''.join(c.serialize() for c in self.cells)+struct.pack('<3I',self.step_number,self.level,self.last_growth)
def run(asset:Path,out:Path,steps:int|None=None,feedback:int=1,inject_step:int=-1,inject_cell:int=-1):
    p,lut=load_asset(asset);steps=steps or p['steps']
    if not 1<=steps<=4096:raise ValueError('Invalid step count')
    p['steps']=steps;e=Reference(p,lut,feedback,inject_step,inject_cell)
    out.mkdir(parents=True,exist_ok=True)
    for name in ['words.bin','summary.csv','state.bin','run.json']:
        if (out/name).exists():raise FileExistsError('Select an unused output directory')
    with (out/'words.bin').open('wb') as wf,(out/'summary.csv').open('w',newline='') as sf:
        wf.write(b'GBWORD31'+struct.pack('<5I',p['width'],p['height'],steps,5,e.n//32))
        writer=csv.writer(sf,lineterminator='\n');writer.writerow('step level_used level_next growth pulses latches mass_u mass_v total_input total_output errors'.split())
        for _ in range(steps):writer.writerow(e.step());wf.write(struct.pack(f'<{len(e.words)}I',*e.words))
    (out/'state.bin').write_bytes(e.serialize_state())
    (out/'run.json').write_text(json.dumps({'backend':'python_independent','gpu_verified':False,'steps':steps,'feedback':feedback,'inject_step':inject_step,'inject_cell':inject_cell},indent=2)+'\n')
    return e
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--asset',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--steps',type=int);ap.add_argument('--feedback',type=int,choices=[0,1],default=1)
    ap.add_argument('--inject-step',type=int,default=-1);ap.add_argument('--inject-cell',type=int,default=-1)
    a=ap.parse_args();run(a.asset,a.out,a.steps,a.feedback,a.inject_step,a.inject_cell);print('Independent reference completed')
