"""Chronotemporal identity: two source observables and explicit V2 lineage.

The weighted integral and the minimum historical envelope are independent
observables. The piecewise-constant quadrature profile and history record format
are V2 constructions, not additional equations silently attributed to the source.
"""
from __future__ import annotations
from copy import deepcopy
import math
from typing import Sequence
from .core import seal,verify
from .uuid import finite,SphereHorizon,TaggedUnion

def retention_gain(duration:float,decay:float) -> float:
    dt,lam=finite(duration),finite(decay)
    if dt<0 or lam<0:raise ValueError("Nonnegative duration and retention coefficient required")
    return dt if lam==0 else -math.expm1(-lam*dt)/lam

def absorbing_step(previous:float,value:float,duration:float,decay:float) -> float:
    old,val,dt,lam=finite(previous),finite(value),finite(duration),finite(decay)
    if old<0 or val<0 or dt<0 or lam<0:raise ValueError("The declared absorption profile is nonnegative")
    result=math.exp(-lam*dt)*old+retention_gain(dt,lam)*val
    return finite(result,"absorbed value")

def integrate_segments(segments:Sequence[tuple[float,float]],decay:float) -> dict:
    """Chronological (duration, constant D-value) segments, evaluated at their end."""
    lam=finite(decay)
    if lam<0:raise ValueError("Negative retention coefficient")
    total=memory=weight=0.0
    for duration,value in segments:
        memory=absorbing_step(memory,value,duration,lam)
        weight=absorbing_step(weight,1.0,duration,lam)
        total+=finite(duration)
    return {"duration":total,"decay":lam,"integral":memory,"retention_mass":weight,
            "normalized_mean":memory/weight if weight else None}

class Lineage:
    """Finite, hash-addressed history DAG with a strict append order.

    Coordinates and payloads are supplied by the caller. No personal experiences
    are inferred from an attribution record or from an engine state.
    """
    def __init__(self,records:Sequence[dict]=()):
        self._records=[];self._by_id={}
        for record in records:self._accept(deepcopy(record))
    def _accept(self,r:dict) -> None:
        required={"id","sequence","time","parents","parent_hashes","payload","content_hash"}
        if set(r)!=required:raise ValueError("Incorrect lineage record fields")
        if not isinstance(r["id"],str) or not r["id"] or r["id"] in self._by_id:raise ValueError("Duplicate or invalid history ID")
        if type(r["sequence"]) is not int or r["sequence"]!=len(self._records):raise ValueError("Nonconsecutive sequence")
        t=finite(r["time"])
        if t<0 or self._records and t<self._records[-1]["time"]:raise ValueError("Nonmonotone history time")
        if not isinstance(r["parents"],list) or any(not isinstance(x,str) for x in r["parents"]) or len(set(r["parents"]))!=len(r["parents"]):raise ValueError("Invalid parent list")
        if any(p not in self._by_id for p in r["parents"]):raise ValueError("Parent has not been committed")
        if r["parent_hashes"]!=[self._by_id[p]["content_hash"] for p in r["parents"]]:raise ValueError("Parent-address mismatch")
        if not verify(r):raise ValueError("History content-address mismatch")
        self._records.append(r);self._by_id[r["id"]]=r
    def append(self,id:str,time:float,parents:Sequence[str],payload:dict) -> dict:
        if any(p not in self._by_id for p in parents):raise ValueError("Unknown parent")
        r=seal({"id":id,"sequence":len(self._records),"time":finite(time),"parents":list(parents),"parent_hashes":[self._by_id[p]["content_hash"] for p in parents],"payload":deepcopy(payload)})
        self._accept(r);return deepcopy(r)
    def records(self) -> list[dict]:return deepcopy(self._records)
    def ancestors(self,id:str) -> tuple[str,...]:
        seen=set();stack=list(self._by_id[id]["parents"])
        while stack:
            key=stack.pop()
            if key not in seen:seen.add(key);stack.extend(self._by_id[key]["parents"])
        return tuple(r["id"] for r in self._records if r["id"] in seen)

def continuity_path(points:Sequence[Sequence[float]],epsilon:float) -> dict:
    eps=finite(epsilon)
    if eps<0:raise ValueError("Negative continuity threshold")
    pts=[tuple(finite(x) for x in p) for p in points]
    if any(not p for p in pts) or len({len(p) for p in pts})>1:raise ValueError("Invalid path dimension")
    distances=[math.dist(a,b) for a,b in zip(pts,pts[1:])]
    return {"epsilon":eps,"edge_distances":distances,"continuous":all(d<=eps for d in distances)}

def history_envelope(events:Sequence[dict],point:Sequence[float],time:float) -> dict:
    now=finite(time);layers=[]
    if now<0:raise ValueError("Negative query time")
    for e in events:
        when=finite(e["time"])
        if when<0:raise ValueError("Negative experience time")
        if when<=now:layers.append(SphereHorizon(e["id"],tuple(e["centre"]),e["threshold"]))
    return TaggedUnion(layers).evaluate(point)
