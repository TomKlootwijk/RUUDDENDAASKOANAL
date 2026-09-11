"""Independent exact-integer realization of Gambit 4.0, supplied PDF §§2–3.

The directly specified integer-chart seed is an edition construction. Old-to-new
stages and arithmetic are unchanged by the V2 UU ID representation wrapper.
"""
from __future__ import annotations
from dataclasses import dataclass,asdict
D=65536

def clip(x: int,lo: int,hi: int) -> int: return max(lo,min(hi,x))

def trunc0(a: int,b: int) -> int:
    if type(a) is not int or type(b) is not int or b <= 0: raise ValueError("Integer numerator and positive divisor required")
    return -((-a)//b) if a<0 else a//b

@dataclass(frozen=True)
class Parameters:
    A:int=32
    R:int=2
    G:int=2
    s_feedback:int=3
    memory_divisor:int=256
    gamma:int=8192
    s_open:int=3
    s_closed:int=4
    s_uv:int=6
    s_vu:int=7
    H:int=49
    stride:int=1
    dwell:int=16
    growth_divisor:int=4
    feedback:bool=True
    @property
    def N(self)->int:return self.A*self.R
    def validate(self)->None:
        if any(type(v) is not int for k,v in asdict(self).items() if k!="feedback") or type(self.feedback) is not bool:raise ValueError("Invalid parameter types")
        if not 32<=self.A<=2048 or self.A & (self.A-1):raise ValueError("Invalid angular count")
        if not 2<=self.R<=2048 or not 1<=self.G<=5:raise ValueError("Invalid radial or generation count")
        if not 1<=self.dwell<=4096 or not 1<=self.memory_divisor<=65536:raise ValueError("Invalid dwell/divisor")
        if not all(3<=s<=31 for s in (self.s_open,self.s_closed)):raise ValueError("Transport shift out of range")
        if not all(1<=s<=31 for s in (self.s_uv,self.s_vu)):raise ValueError("Reaction shift out of range")
        if not 1<=self.H<=65536 or not 0<=self.gamma<=65536:raise ValueError("Field coefficient out of range")
        if not 0<=self.s_feedback<self.A or not 0<=self.stride<self.A:raise ValueError("Angular offset out of range")
        if not 1<=self.growth_divisor<=65536:raise ValueError("Growth divisor out of range")

@dataclass(frozen=True)
class Cell:
    U:int
    V:int
    z:int
    m:int
    r:int
    flags:int
    @property
    def latch(self)->int:return self.flags&1
    @property
    def pulse(self)->int:return (self.flags>>1)&1

@dataclass(frozen=True)
class State:
    a:int
    g:int
    cooldown:int
    cells:tuple[Cell,...]

@dataclass(frozen=True)
class Seed:
    parameters:Parameters
    lut:tuple[int,...]
    initial_mass:int
    name:str="TKUFT-integer-chart-v2"
    def validate(self)->None:
        p=self.parameters;p.validate()
        if len(self.lut)!=p.N*p.G or any(type(w) is not int or not 0<=w<2**32 for w in self.lut):raise ValueError("Invalid LUT")
        if type(self.initial_mass) is not int or not 0<self.initial_mass<2**32:raise ValueError("Invalid material total")

def material(s:State)->int:return sum(c.U+c.V for c in s.cells)

def validate_state(seed:Seed,s:State)->None:
    p=seed.parameters
    if any(type(v) is not int for v in (s.a,s.g,s.cooldown)):raise ValueError("Control must be integer")
    if not 0<=s.a<p.A or not 0<=s.g<p.G or not 0<=s.cooldown<=p.dwell:raise ValueError("Invalid control")
    if len(s.cells)!=p.N:raise ValueError("Incorrect cell count")
    for c in s.cells:
        if any(type(v) is not int for v in (c.U,c.V,c.z,c.m,c.r,c.flags)):raise ValueError("Invalid cell types")
        if not (0<=c.U<2**32 and 0<=c.V<2**32 and 0<=c.z<=D and 0<=c.m<=D and 0<=c.r<D and 0<=c.flags<16):raise ValueError("Invalid cell range")
    if material(s)!=seed.initial_mass:raise ValueError("Global material invariant failed")

def neighbours(i:int,p:Parameters)->tuple[int,...]:
    y,x=divmod(i,p.A);out=[y*p.A+(x-1)%p.A,y*p.A+(x+1)%p.A]
    if y:out.append(i-p.A)
    if y+1<p.R:out.append(i+p.A)
    return tuple(out)

def pack_planes(s:State)->dict[str,list[int]]:
    out={}
    for name,bit in (("pulse",1),("latch",0),("event",3),("occupancy",2)):
        out[name]=[sum(((c.flags>>bit)&1)<<j for j,c in enumerate(s.cells[start:start+32])) for start in range(0,len(s.cells),32)]
    out["parity"]=[w.bit_count()&1 for w in out["pulse"]]
    return out

def sample_all(seed:Seed,s:State,intervention:int|None=None)->tuple[tuple[int,int],...]:
    p=seed.parameters
    if intervention is not None and (type(intervention) is not int or not 0<=intervention<p.N):raise ValueError("Invalid intervention address")
    old=pack_planes(s)["pulse"];out=[]
    for i,c in enumerate(s.cells):
        q=(old[i//32]>>(i%32))&1
        if i==intervention:q^=1
        y,x=divmod(i,p.A);j=(x+s.a+(q*p.s_feedback if p.feedback else 0))%p.A
        word=seed.lut[(s.g*p.R+y)*p.A+j];d,drive=(word&65535)-32768,word>>16
        h=trunc0(c.m-D//2,p.memory_divisor) if p.feedback else 0
        out.append((d-h,clip(drive+16*h+(p.gamma*(2*q-1) if p.feedback else 0),0,D)))
    return tuple(out)

def pulse_codec(r:int,k:int)->tuple[int,int]:
    if type(r) is not int or type(k) is not int or not 0<=r<D or not 0<=k<=D:raise ValueError("Invalid codec domain")
    q=int(r+k>=D);return q,r+k-D*q

def latch_step(old:int,field:int,H:int)->tuple[int,int,int]:
    if old not in (0,1) or H<=0:raise ValueError("Invalid hinge")
    new=1 if field<=-H else 0 if field>=H else old
    return new,old^new,int(field<=0)

def tick(seed:Seed,old:State,intervention:int|None=None)->tuple[State,dict]:
    validate_state(seed,old);p=seed.parameters;samples=sample_all(seed,old,intervention);cells=[]
    for i,c in enumerate(old.cells):
        U,V=c.U,c.V
        if samples[i][0]<=0:
            for j in neighbours(i,p):
                if samples[j][0]<=0:
                    cj=old.cells[j];shift=p.s_open if c.latch or cj.latch else p.s_closed
                    U+=(cj.U>>shift)-(c.U>>shift);V+=(cj.V>>shift)-(c.V>>shift)
        ar,br=U>>p.s_uv,V>>p.s_vu;Up,Vp=U-ar+br,V-br+ar;total=Up+Vp
        B=D*Up//total if total else D//2;v=(3*samples[i][1]+B)//4
        z=(3*c.z+v)//4;m=(15*c.m+z)//16;q,r=pulse_codec(c.r,z)
        latch,event,occupancy=latch_step(c.latch,samples[i][0],p.H)
        cells.append(Cell(Up,Vp,z,m,r,latch|(q<<1)|(occupancy<<2)|(event<<3)))
        if D*q+r!=c.r+z:raise ArithmeticError("Local codec certificate failed")
    pulses=sum(c.pulse for c in cells);cooldown,g=min(old.cooldown+1,p.dwell),old.g
    if g+1<p.G and cooldown==p.dwell and pulses*p.growth_divisor>=p.N:g,cooldown=g+1,0
    new=State((old.a+p.stride)%p.A,g,cooldown,tuple(cells));validate_state(seed,new)
    return new,{"mass":material(new),"pulses":pulses,"events":sum(c.flags>>3&1 for c in cells),"occupancy":sum(c.flags>>2&1 for c in cells),"phase":new.a,"generation":g,"cooldown":cooldown,"sum_z":sum(c.z for c in cells),"sum_memory":sum(c.m for c in cells)}

def integer_chart_fixture(feedback:bool=True)->tuple[Seed,State]:
    p=Parameters(feedback=feedback);words=[]
    for g in range(p.G):
        for y in range(p.R):
            for x in range(p.A):
                d=128*abs(((x+8)%32)-16)+96*y-1152-256*g
                words.append(d+32768|(clip(32768-16*d,0,65535)<<16))
    cells=[]
    for i in range(p.N):
        active=(words[i]&65535)-32768<=0
        cells.append(Cell(256+17*((11*i+3)%13) if active else 0,128+7*((5*i+1)%11) if active else 0,D//2,D//2,0,0))
    state=State(0,0,0,tuple(cells));seed=Seed(p,tuple(words),material(state))
    seed.validate();validate_state(seed,state);return seed,state
