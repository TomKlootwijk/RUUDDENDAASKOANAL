"""Complete state words and the self-contained, edition-specific TKUFT2 capsule."""
from __future__ import annotations
import base64
from dataclasses import asdict
import hashlib
import json
from .core import canonical_bytes
from .engine import Cell,State,Seed,Parameters,validate_state

CELL_FIELDS=(("U",32),("V",32),("z",17),("m",17),("r",16),("flags",4))
CONTROL_FIELDS=(("a",11),("g",3),("cooldown",13))

def state_bit_count(seed:Seed)->int:return 118*seed.parameters.N+27

def encode_state(seed:Seed,state:State)->bytes:
    validate_state(seed,state)
    data=bytearray();buffer=used=0
    fields=[(getattr(state,k),w) for k,w in CONTROL_FIELDS]
    fields.extend((getattr(c,k),w) for c in state.cells for k,w in CELL_FIELDS)
    for value,width in fields:
        if not 0<=value<1<<width:raise ValueError("Field width exceeded")
        buffer|=value<<used;used+=width
        while used>=8:data.append(buffer&255);buffer>>=8;used-=8
    if used:data.append(buffer)
    return bytes(data)

def decode_state(seed:Seed,data:bytes)->State:
    count=state_bit_count(seed)
    if len(data)!=(count+7)//8:raise ValueError("Incorrect payload length")
    if count%8 and data[-1]>>(count%8):raise ValueError("Nonzero payload padding")
    position=0
    def get(width):
        nonlocal position
        out=sum(((data[(position+j)//8]>>((position+j)%8))&1)<<j for j in range(width));position+=width;return out
    control=[get(w) for _,w in CONTROL_FIELDS]
    cells=tuple(Cell(*(get(w) for _,w in CELL_FIELDS)) for _ in range(seed.parameters.N))
    state=State(*control,cells);validate_state(seed,state);return state

def state_bits(seed:Seed,state:State)->tuple[int,...]:
    raw=encode_state(seed,state)
    return tuple((raw[j//8]>>(j%8))&1 for j in range(state_bit_count(seed)))

def bits_state(seed:Seed,bits:tuple[int,...])->State:
    if len(bits)!=state_bit_count(seed) or any(type(b) is not int or b not in (0,1) for b in bits):raise ValueError("Incorrect binary word")
    raw=bytes(sum(b<<j for j,b in enumerate(bits[k:k+8])) for k in range(0,len(bits),8))
    return decode_state(seed,raw)

def encode_capsule(seed:Seed,state:State)->bytes:
    seed.validate()
    payload={"format":"TKUFT2","version":"2.0.0","seed_name":seed.name,"parameters":asdict(seed.parameters),"lut":list(seed.lut),"initial_mass":seed.initial_mass,"state_bit_count":state_bit_count(seed),"state_base64":base64.b64encode(encode_state(seed,state)).decode("ascii")}
    return canonical_bytes({"payload":payload,"sha256":hashlib.sha256(canonical_bytes(payload)).hexdigest()})+b"\n"

def decode_capsule(data:bytes)->tuple[Seed,State]:
    try:
        obj=json.loads(data)
        if set(obj)!={"payload","sha256"}:raise ValueError("Unexpected capsule envelope")
        payload=obj["payload"]
        if obj["sha256"]!=hashlib.sha256(canonical_bytes(payload)).hexdigest():raise ValueError("Capsule checksum mismatch")
        required={"format","version","seed_name","parameters","lut","initial_mass","state_bit_count","state_base64"}
        if set(payload)!=required or payload["format"]!="TKUFT2" or payload["version"]!="2.0.0":raise ValueError("Unsupported capsule")
        seed=Seed(Parameters(**payload["parameters"]),tuple(payload["lut"]),payload["initial_mass"],payload["seed_name"]);seed.validate()
        if payload["state_bit_count"]!=state_bit_count(seed):raise ValueError("Declared bit count mismatch")
        return seed,decode_state(seed,base64.b64decode(payload["state_base64"],validate=True))
    except (KeyError,TypeError,json.JSONDecodeError) as exc:raise ValueError("Malformed capsule") from exc
