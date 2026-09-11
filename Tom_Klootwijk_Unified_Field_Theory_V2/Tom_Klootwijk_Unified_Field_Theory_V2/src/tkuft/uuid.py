"""UU ID and Agnostic Boundary Horizon, from the supplied 18-page dialogue.

The source scalar equation is kept literally: min(abs(d1-T1), abs(d2-T2)).
Label-preserving outputs and the complete state decoder are explicit V2 constructions.
"""
from __future__ import annotations
from bisect import bisect_left
from dataclasses import dataclass, field
import math
from typing import Sequence
from .engine import Seed, State, tick
from .codec import state_bits, bits_state

def finite(value: float, name: str="value") -> float:
    if isinstance(value, bool) or not isinstance(value,(int,float)) or not math.isfinite(value):
        raise ValueError(f"{name} must be a finite real number")
    return float(value)

def relation(raw: float, threshold: float) -> str:
    d,t=finite(raw),finite(threshold)
    return "<" if d<t else ">" if d>t else "="

def boundary_delta(raw: float, threshold: float) -> float:
    result=abs(finite(raw)-finite(threshold))
    if not math.isfinite(result): raise ValueError("Boundary delta overflow")
    return result

def uu_id(d1: float, t1: float, d2: float, t2: float) -> float:
    """The source's two-input Double Set / Identity Disjunction operator."""
    return min(boundary_delta(d1,t1), boundary_delta(d2,t2))

def uu_fold(deltas: Sequence[float]) -> float:
    """Pointwise minimum of normalized nonnegative horizons; empty identity is +inf."""
    vals=[finite(x) for x in deltas]
    if any(x<0 for x in vals): raise ValueError("Normalized horizons must be nonnegative")
    return min(vals,default=math.inf)

def horizon_bit(raw: float, threshold: float, tolerance: float=0.0) -> int:
    """S3 p.12 convention: 0 at the horizon, 1 away; tolerance is explicit."""
    eps=finite(tolerance)
    if eps<0: raise ValueError("Negative tolerance")
    return int(boundary_delta(raw,threshold)>eps)

def source_bit(raw_distance: float) -> int:
    """S3 pp.10–11 convention: 0 at the source, 1 away from the source."""
    d=finite(raw_distance)
    if d<0: raise ValueError("Raw distance must be nonnegative")
    return int(d>0)

@dataclass(frozen=True)
class SphereHorizon:
    id: str
    centre: tuple[float,...]
    threshold: float
    def __post_init__(self):
        if not isinstance(self.id,str) or not self.id: raise ValueError("A horizon ID is required")
        if not self.centre: raise ValueError("A nonempty coordinate vector is required")
        object.__setattr__(self,"centre",tuple(finite(x) for x in self.centre))
        r=finite(self.threshold)
        if r<0: raise ValueError("Sphere radius must be nonnegative")
        object.__setattr__(self,"threshold",r)
    def raw(self,point: Sequence[float]) -> float:
        if len(point)!=len(self.centre): raise ValueError("Coordinate dimension mismatch")
        p=tuple(finite(x) for x in point)
        return finite(math.dist(p,self.centre),"distance")
    def delta(self,point: Sequence[float]) -> float:
        return boundary_delta(self.raw(point),self.threshold)
    def record(self) -> dict:
        return {"id":self.id,"kind":"sphere_horizon","centre":list(self.centre),"threshold":self.threshold,"capabilities":["EXACT_UNSIGNED_BOUNDARY_DISTANCE"]}

class TaggedUnion:
    """V2 record-preserving composition; its scalar projection is exactly UU ID."""
    def __init__(self,layers: Sequence[SphereHorizon]):
        by_id={}
        for layer in layers:
            if layer.id in by_id and by_id[layer.id]!=layer: raise ValueError("Conflicting definitions under the same horizon ID")
            by_id[layer.id]=layer
        self.layers=tuple(by_id[k] for k in sorted(by_id))
        if self.layers and len({len(x.centre) for x in self.layers})!=1: raise ValueError("Mixed field dimensions")
    def evaluate(self,point: Sequence[float]) -> dict:
        # JSON-safe empty output uses null, with an explicit empty-family status.
        rows=[]
        for layer in self.layers:
            raw=layer.raw(point);delta=boundary_delta(raw,layer.threshold)
            rows.append({"id":layer.id,"raw":raw,"threshold":layer.threshold,"relation":relation(raw,layer.threshold),"delta":delta})
        if not rows:return {"status":"empty","value":None,"witnesses":[],"layers":[]}
        value=min(r["delta"] for r in rows)
        return {"status":"defined","value":value,"witnesses":[r["id"] for r in rows if r["delta"]==value],"layers":rows}
    def merge(self,other:TaggedUnion) -> TaggedUnion:
        return TaggedUnion(self.layers+other.layers)

@dataclass(frozen=True)
class StateHorizon:
    """Exact distance to the boundary of the C13 interval family.

    The permanent anchor is included. b[j-1] is located at coordinate 3*j.
    A binary search over endpoints evaluates the same minimum as UU ID.
    """
    bits: tuple[int,...]
    endpoints: tuple[float,...] = field(init=False,repr=False)
    def __post_init__(self):
        bits=tuple(self.bits)
        if any(type(b) is not int or b not in (0,1) for b in bits): raise ValueError("A binary word is required")
        object.__setattr__(self,"bits",bits)
        centres=[0]+[3*j for j,b in enumerate(bits,1) if b]
        object.__setattr__(self,"endpoints",tuple(x for c in centres for x in (c-.25,c+.25)))
    def evaluate(self,x:float) -> float:
        x=finite(x);k=bisect_left(self.endpoints,x)
        return min(abs(x-self.endpoints[j]) for j in (k-1,k) if 0<=j<len(self.endpoints))
    def decode(self,tolerance:float=.25) -> tuple[int,...]:
        tau=finite(tolerance)
        if not .25<=tau<2.75: raise ValueError("Decoder threshold must be in [1/4,11/4)")
        return tuple(int(self.evaluate(3*j)<=tau) for j in range(1,len(self.bits)+1))
    def active_centres(self) -> tuple[int,...]:
        return (0,)+tuple(3*j for j,b in enumerate(self.bits,1) if b)

def encode_horizon(seed:Seed,state:State) -> StateHorizon:
    return StateHorizon(state_bits(seed,state))

def decode_horizon(seed:Seed,horizon:StateHorizon) -> State:
    return bits_state(seed,horizon.decode())

def tick_horizon(seed:Seed,horizon:StateHorizon) -> tuple[StateHorizon,dict]:
    """Executable conjugate J_U E T (J_U E)^-1 on its image."""
    next_state,summary=tick(seed,decode_horizon(seed,horizon))
    return encode_horizon(seed,next_state),summary

def cell_bit_position(cell:int,local_bit:int) -> int:
    """One-based complete-word bit position (includes the 27 control bits)."""
    if type(cell) is not int or cell<0 or type(local_bit) is not int or not 0<=local_bit<118:raise ValueError("Invalid bit address")
    return 28+118*cell+local_bit

def previous_pulse_position(cell:int) -> int:
    return cell_bit_position(cell,115)

def open_engine_sample(field:int) -> tuple[int,int]:
    """V2 order-preserving lift of the admitted signed effective field."""
    if type(field) is not int or not -65536<=field<=65535:raise ValueError("Effective field outside admitted range")
    return field+65536,65536

def open_latch(old:int,raw:int,threshold:int,H:int) -> tuple[int,int,int]:
    """Relational form of the unchanged engine hinge; retains side information."""
    if old not in (0,1) or any(type(x) is not int for x in (raw,threshold,H)) or H<=0:raise ValueError("Invalid open hinge")
    new=1 if raw<=threshold-H else 0 if raw>=threshold+H else old
    return new,old^new,int(raw<=threshold)
