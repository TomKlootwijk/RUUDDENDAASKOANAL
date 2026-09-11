#!/usr/bin/env python3
"""Independent integer specification of the autonomous closure transition.
Standard library only. No imports of C++ or Boolean implementation.
Operational state has no absolute timestep or cumulative audit counters.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import argparse, csv, hashlib, json, struct
from reference31 import FIELDS, mix32, trunc_div
D=65536
@dataclass(frozen=True)
class Cell:
    u:int; v:int; z:int; m:int; r:int; flags:int

def validate_params(p:dict)->None:
    w=p['width'];h=p['height']
    if not (32<=w<=2048 and not w&(w-1) and 2<=h<=2048 and 1<=p['levels']<=5 and
            0<=p['start_level']<p['levels'] and 1<=p['steps']<=4096 and 1<=p['threshold']<=32767 and
            0<=p['feedback_gain']<=16384 and 1<=p['memory_divisor']<=65536 and
            0<=p['phase_stride']<w and 0<=p['feedback_angle']<w and 3<=p['open_shift']<=16 and
            p['open_shift']<=p['closed_shift']<=16 and 1<=p['reaction_uv_shift']<=16 and
            1<=p['reaction_vu_shift']<=16 and 1<=p['growth_dwell']<=4096 and
            1<=p['growth_divisor']<=65536 and p['pair'] in (0,1) and 16<=p['device_budget_mib']<=4096):
        raise ValueError('Parameters outside admitted contract')

def decode_asset(raw:bytes):
    if len(raw)<92:raise ValueError('Truncated asset')
    magic,ver,num,*data=struct.unpack_from('<8sII19I',raw)
    if (magic,ver,num)!=(b'GBLUT31\0',1,19):raise ValueError('Asset version')
    p=dict(zip(FIELDS,data));validate_params(p);n=p['width']*p['height']*p['levels']
    if len(raw)!=92+4*n:raise ValueError('Asset size')
    return p,list(struct.unpack_from(f'<{n}I',raw,92))

class Reference:
    def __init__(self,p:dict,lut:list[int],feedback:int=1):
        validate_params(p)
        if feedback not in (0,1) or len(lut)!=p['width']*p['height']*p['levels']:raise ValueError('Seed encoding')
        self.p=p.copy();self.lut=lut.copy();self.feedback=feedback;self.n=p['width']*p['height']
        self.phase=0;self.level=p['start_level'];self.cooldown=0;self.cells=[]
        for i in range(self.n):
            active=(lut[self.level*self.n+i]&65535)<=32768
            h=mix32(i^p['seed']^((p['pair']*0x9e3779b9)&0xffffffff))
            self.cells.append(Cell((64+(h&63))*active,(32+((h>>6)&31))*active,D//2,D//2,0,0))
        self.mass0=sum(c.u+c.v for c in self.cells);self.pack_words();self.validate()
    def validate(self):
        if not(0<self.mass0<=0xffffffff and self.feedback in (0,1) and len(self.cells)==self.n and
               0<=self.phase<self.p['width'] and self.p['start_level']<=self.level<self.p['levels'] and
               0<=self.cooldown<=self.p['growth_dwell']):raise ValueError('Invalid control')
        for c in self.cells:
            if not(0<=c.u<=0xffffffff and 0<=c.v<=0xffffffff and 0<=c.z<=D and 0<=c.m<=D and 0<=c.r<D and 0<=c.flags<16):raise ValueError('Invalid cell')
        if sum(c.u+c.v for c in self.cells)!=self.mass0:raise ValueError('Mass violation')
    def pack_words(self):
        nw=self.n//32;self.words=[0]*(5*nw)
        for i,c in enumerate(self.cells):
            for plane,bit in enumerate([(c.flags>>1)&1,c.flags&1,(c.flags>>3)&1,(c.flags>>2)&1]):
                self.words[plane*nw+i//32]|=bit<<(i%32)
        for k in range(nw):self.words[4*nw+k]=self.words[k].bit_count()%2
    def tick(self,inject_read:int=-1):
        if not -1<=inject_read<self.n:raise ValueError('Intervention index')
        p=self.p;w=p['width'];h=p['height'];old=self.cells;s=[]
        for i,c in enumerate(old):
            q=(self.words[i//32]>>(i%32))&1
            if i==inject_read:q^=1
            col=(i%w+self.phase+(q*p['feedback_angle'] if self.feedback else 0))%w
            tex=self.lut[(self.level*h+i//w)*w+col];d=(tex&65535)-32768
            m=trunc_div(c.m-D//2,p['memory_divisor']) if self.feedback else 0
            a=(tex>>16)+16*m+(p['feedback_gain']*(2*q-1) if self.feedback else 0)
            s.append((d-m,max(0,min(D,a))))
        nxt=[]
        for i,c in enumerate(old):
            x=i%w;y=i//w;neighbors=[y*w+(x-1)%w,y*w+(x+1)%w]
            if y:neighbors.append(i-w)
            if y+1<h:neighbors.append(i+w)
            ou=iu=ov=iv=0
            for j in neighbors:
                if s[i][0]>0 or s[j][0]>0:continue
                shift=p['open_shift'] if (c.flags|old[j].flags)&1 else p['closed_shift']
                ou+=c.u//(1<<shift);iu+=old[j].u//(1<<shift);ov+=c.v//(1<<shift);iv+=old[j].v//(1<<shift)
            u=c.u-ou+iu;v=c.v-ov+iv;uv=u//(1<<p['reaction_uv_shift']);vu=v//(1<<p['reaction_vu_shift'])
            un=u-uv+vu;vn=v-vu+uv;material=D*un//(un+vn) if un+vn else D//2
            drive=(3*s[i][1]+material)//4;z=(3*c.z+drive)//4;m=(15*c.m+z)//16
            q=int(c.r+z>=D);r=c.r+z-D*q
            b=1 if s[i][0]<=-p['threshold'] else 0 if s[i][0]>=p['threshold'] else c.flags&1
            ev=(c.flags&1)^b;o=int(s[i][0]<=0)
            if D*q+r!=c.r+z:raise ValueError('Local codec certificate')
            nxt.append(Cell(un,vn,z,m,r,b|(q<<1)|(o<<2)|(ev<<3)))
        self.cells=nxt;self.phase=(self.phase+p['phase_stride'])%w
        pulses=sum((c.flags>>1)&1 for c in nxt);self.cooldown=min(self.cooldown+1,p['growth_dwell'])
        if self.level+1<p['levels'] and self.cooldown==p['growth_dwell'] and pulses*p['growth_divisor']>=self.n:
            self.level+=1;self.cooldown=0
        self.validate();self.pack_words()
    def asset_bytes(self):
        return struct.pack('<8sII19I',b'GBLUT31\0',1,19,*[self.p[k] for k in FIELDS])+struct.pack(f'<{len(self.lut)}I',*self.lut)
    def capsule(self):
        self.validate();payload=bytearray();bitpos=0;buffer=0;filled=0
        def put(v,width):
            nonlocal bitpos,buffer,filled
            if not 0<=v<1<<width:raise ValueError('Bit range')
            buffer|=v<<filled;filled+=width;bitpos+=width
            while filled>=8:
                payload.append(buffer&255);buffer>>=8;filled-=8
        put(self.phase,11);put(self.level,3);put(self.cooldown,13)
        for c in self.cells:
            for v,width in zip((c.u,c.v,c.z,c.m,c.r,c.flags),(32,32,17,17,16,4)):put(v,width)
        if filled:payload.append(buffer)
        asset=self.asset_bytes();raw=struct.pack('<8s6I',b'GBCLOS40',1,len(asset),self.feedback,self.mass0,bitpos,0)+asset+payload
        return raw+hashlib.sha256(raw).digest()

def from_capsule(raw:bytes)->Reference:
    if len(raw)<160 or len(raw)>256*1024**2 or hashlib.sha256(raw[:-32]).digest()!=raw[-32:]:raise ValueError('Capsule size/digest')
    magic,v,asz,fb,mass,nbits,reserved=struct.unpack_from('<8s6I',raw)
    if magic!=b'GBCLOS40' or v!=1 or reserved or fb not in (0,1) or asz<92 or len(raw)!=32+asz+(nbits+7)//8+32:raise ValueError('Capsule header')
    p,lut=decode_asset(raw[32:32+asz]);e=Reference(p,lut,fb)
    if nbits!=27+118*e.n or mass!=e.mass0 or raw[-33]>>(nbits%8):raise ValueError('Capsule dimensions/padding')
    bitpos=0;payload=raw[32+asz:-32]
    def get(width):
        nonlocal bitpos
        byte,offset=divmod(bitpos,8);length=(offset+width+7)//8
        v=(int.from_bytes(payload[byte:byte+length],'little')>>offset)&((1<<width)-1)
        bitpos+=width
        return v
    e.phase=get(11);e.level=get(3);e.cooldown=get(13)
    e.cells=[Cell(*[get(w) for w in (32,32,17,17,16,4)]) for _ in range(e.n)]
    e.validate();e.pack_words();return e

def run(e:Reference,out:Path,steps:int):
    if not 1<=steps<=4096:raise ValueError('Segment bound')
    out.mkdir(parents=True,exist_ok=False);(out/'initial.gbc').write_bytes(e.capsule())
    r0=[c.r for c in e.cells];ks=[0]*e.n;qs=[0]*e.n
    with (out/'words.bin').open('wb') as wf,(out/'summary.csv').open('w',newline='') as sf:
        wf.write(struct.pack('<8s5I',b'GBWORD40',e.p['width'],e.p['height'],steps,5,e.n//32))
        writer=csv.writer(sf,lineterminator='\n');writer.writerow('tick phase level cooldown pulses latches mass_u mass_v input_sum pulse_sum'.split())
        for t in range(steps):
            e.tick()
            for i,c in enumerate(e.cells):
                ks[i]+=c.z;qs[i]+=(c.flags>>1)&1
                if D*qs[i]+c.r!=r0[i]+ks[i]:raise ValueError('Prefix certificate')
            wf.write(struct.pack(f'<{len(e.words)}I',*e.words))
            writer.writerow([t,e.phase,e.level,e.cooldown,sum((c.flags>>1)&1 for c in e.cells),sum(c.flags&1 for c in e.cells),sum(c.u for c in e.cells),sum(c.v for c in e.cells),sum(ks),sum(qs)])
    (out/'final.gbc').write_bytes(e.capsule())
    (out/'counts.bin').write_bytes(b'GBCOUNT4'+struct.pack('<I',e.n)+b''.join(struct.pack('<IQQ',*vs) for vs in zip(r0,ks,qs)))
    (out/'run.json').write_text(json.dumps({'backend':'independent_python','gpu_verified':False,'steps_in_segment':steps})+'\n')
    return e

if __name__=='__main__':
    ap=argparse.ArgumentParser();src=ap.add_mutually_exclusive_group(required=True)
    src.add_argument('--asset',type=Path);src.add_argument('--resume',type=Path)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--steps',type=int,default=64);a=ap.parse_args()
    e=Reference(*decode_asset(a.asset.read_bytes())) if a.asset else from_capsule(a.resume.read_bytes())
    run(e,a.out,a.steps);print('PASS independent Python')
