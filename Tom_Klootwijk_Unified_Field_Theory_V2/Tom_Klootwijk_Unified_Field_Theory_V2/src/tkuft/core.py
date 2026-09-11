"""Literal definitions, finite dependency resolution and retained corpus operators."""
from __future__ import annotations
from copy import deepcopy
import hashlib
import heapq
import json
import math
from typing import Any, Iterable, Sequence

AUTHOR = {"name": "Tom Klootwijk", "identifier": "NL200678942", "date_of_birth": "10-07-1990"}
PHASES = ("parse", "normalize", "resolve", "construct", "transform", "support", "compatibility", "guard", "transition", "lineage")

def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")

def content_hash(record: dict) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes({k:v for k,v in record.items() if k != "content_hash"})).hexdigest()

def seal(record: dict) -> dict:
    result = deepcopy(record)
    result["content_hash"] = content_hash(result)
    return result

def verify(record: dict) -> bool:
    return record.get("content_hash") == content_hash(record)

class Registry:
    """An immutable-by-interface, validated finite definition DAG."""
    def __init__(self, records: Iterable[dict]):
        self._records = {}
        for raw in records:
            d = deepcopy(raw)
            required = ("id", "kind", "domain", "codomain", "dependencies", "evaluation_phase", "parameters", "provenance", "content_hash")
            if any(k not in d for k in required): raise ValueError("Incomplete definition")
            if not isinstance(d["id"], str) or not d["id"] or d["id"] in self._records: raise ValueError("Invalid or duplicate ID")
            if type(d["evaluation_phase"]) is not int or not 0 <= d["evaluation_phase"] < 10: raise ValueError("Invalid phase")
            deps = d["dependencies"]
            if not isinstance(deps,list) or any(type(x) is not str for x in deps) or len(set(deps)) != len(deps): raise ValueError("Invalid dependencies")
            if not verify(d): raise ValueError("Definition content-address mismatch")
            self._records[d["id"]] = d
        children = {k:[] for k in self._records}
        degree = {k:len(d["dependencies"]) for k,d in self._records.items()}
        for key,d in self._records.items():
            for dep in d["dependencies"]:
                if dep not in children: raise ValueError(f"Unknown dependency: {dep}")
                children[dep].append(key)
        ready = [k for k,v in degree.items() if v == 0]; heapq.heapify(ready)
        order = []
        while ready:
            key = heapq.heappop(ready); order.append(key)
            for child in sorted(children[key]):
                degree[child] -= 1
                if degree[child] == 0: heapq.heappush(ready, child)
        if len(order) != len(degree): raise ValueError("Cyclic definition graph")
        self._order = tuple(order)
    def definition_at(self,key: str) -> dict: return deepcopy(self._records[key])
    def definition_order(self) -> tuple[str,...]: return self._order
    def verify_definition(self,key: str) -> bool: return verify(self._records[key])
    def explain_reference(self,key: str) -> dict:
        d=self.definition_at(key)
        return {k:d[k] for k in ("id","dependencies","evaluation_phase","provenance","content_hash")}
    def instances_of(self,key: str,instances: Sequence[dict]) -> list[dict]:
        if key not in self._records: raise KeyError(key)
        return deepcopy([x for x in instances if x.get("definition_ref") == key])

def natural(n: int) -> int:
    if type(n) is not int or n < 0: raise ValueError("A nonnegative integer is required")
    return n

def radix_digits(n: int,base: int=2) -> tuple[int,...]:
    natural(n)
    if type(base) is not int or base < 2: raise ValueError("Base must be an integer at least two")
    if n == 0: return (0,)
    out=[]
    while n:
        n,r=divmod(n,base);out.append(r)
    return tuple(reversed(out))

def active_bits(n: int) -> tuple[int,...]:
    natural(n)
    return tuple(k for k in range(n.bit_length()) if n >> k & 1)

def pascal_parity(n: int,k: int) -> int:
    natural(n);natural(k)
    return int(k <= n and k & ~n == 0)

def pulse_polygon(m: int,radius: float=1.0,phase: float=0.0) -> tuple[tuple[float,float],...]:
    if type(m) is not int or m < 1 or not math.isfinite(radius) or radius <= 0 or not math.isfinite(phase): raise ValueError("Invalid polygon parameters")
    return tuple((radius*math.cos(phase+2*math.pi*j/m),radius*math.sin(phase+2*math.pi*j/m)) for j in range(m))

def rotate(point: Sequence[float],pivot: Sequence[float],angle: float) -> tuple[float,float]:
    x,y=point[0]-pivot[0],point[1]-pivot[1];c,s=math.cos(angle),math.sin(angle)
    return pivot[0]+c*x-s*y,pivot[1]+s*x+c*y

def orientation_wrap(y: float,height: float,orientation: int,sheet: int=0) -> tuple[float,int,int]:
    if height <= 0 or not 0 <= y <= height or orientation not in (-1,1) or sheet not in (0,1): raise ValueError("Invalid port state")
    return height-y,-orientation,sheet^1

def grammar_word(axiom: str,generation: int,budget: int=1000000) -> str:
    natural(generation)
    rules={"X":"X[+X]Y","Y":"Y[-Y]X","+":"+","-":"-","[":"[","]":"]"}
    if any(c not in rules for c in axiom) or budget < 1 or generation > budget or len(axiom)>budget: raise ValueError("Invalid grammar or budget")
    w=axiom
    for _ in range(generation):
        if sum(len(rules[c]) for c in w)>budget: raise ValueError("Grammar budget exceeded")
        w="".join(rules[c] for c in w)
    return w

_UNITS={0:("nul",["nul"]),1:("een",["een"]),2:("twee",["twee"]),3:("drie",["drie"]),4:("vier",["vier"]),5:("vijf",["vijf"]),6:("zes",["zes"]),7:("zeven",["ze","ven"]),8:("acht",["acht"]),9:("negen",["ne","gen"])}
_TEENS={10:("tien",["tien"]),11:("elf",["elf"]),12:("twaalf",["twaalf"]),13:("dertien",["der","tien"]),14:("veertien",["veer","tien"]),15:("vijftien",["vijf","tien"]),16:("zestien",["zes","tien"]),17:("zeventien",["ze","ven","tien"]),18:("achttien",["acht","tien"]),19:("negentien",["ne","gen","tien"])}
_TENS={20:("twintig",["twin","tig"]),30:("dertig",["der","tig"]),40:("veertig",["veer","tig"]),50:("vijftig",["vijf","tig"]),60:("zestig",["zes","tig"]),70:("zeventig",["ze","ven","tig"]),80:("tachtig",["tach","tig"]),90:("negentig",["ne","gen","tig"])}

def dutch_number(n: int) -> dict:
    if type(n) is not int or not 0 <= n <= 99: raise ValueError("The declared Dutch profile covers 0 through 99")
    if n < 10:
        word,segments=_UNITS[n]; place=spoken=[n]; kind="atomic";morph=[word]
    elif n < 20:
        word,segments=_TEENS[n]
        if n >= 13: place,spoken,kind,morph=[10,n-10],[n-10,"tien"],"teen_suffix",["".join(segments[:-1]),"tien"]
        else: place=spoken=[n];kind="irregular" if n in (11,12) else "atomic";morph=[word]
    elif n%10 == 0:
        word,segments=_TENS[n];place=spoken=[n];kind="atomic";morph=[word]
    else:
        t,u=10*(n//10),n%10;uw,us=_UNITS[u];tw,ts=_TENS[t]
        word=uw+("ën" if u in (2,3) else "en")+tw;segments=us+["en"]+ts
        place,spoken,kind,morph=[t,u],[u,"en",t],"en_connector",[uw,"en",tw]
    bits=active_bits(n)
    return {"profile_id":"nl-TKUFT-0-99-v2","value":n,"orthography":word,"segments":list(segments),"morphemes":morph,"place_order":place,"spoken_order":spoken,"hinge_kind":kind,"pulse_count":len(segments),"binary":"".join(map(str,radix_digits(n))),"active_bit_positions":list(bits),"popcount":len(bits),"count_match":len(segments)==len(bits)}

def chart_value(items: Sequence[int|str]) -> int:
    total=0
    for x in items:
        if type(x) is int: total+=x
        elif x=="tien": total+=10
        elif x!="en": raise ValueError("Unknown chart token")
    return total
