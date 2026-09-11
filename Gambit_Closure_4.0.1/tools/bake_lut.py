#!/usr/bin/env python3
"""Offline geometry compilation. NumPy required HERE only, not by the native runtime.

The distributed LUT bytes are the authoritative finite seed. Rebuilding floating
geometry may change boundary rounding on another arithmetic environment. Never
silently replace a shipped asset or its golden hash.
"""
from __future__ import annotations
import argparse, hashlib, json, math, platform, struct, sys
from pathlib import Path
import numpy as np
from geometry_v3 import Pair, grow, turtle, m_field, capsule_field
PARAM_FIELDS = ('width height levels start_level steps threshold feedback_gain '
                'memory_divisor phase_stride feedback_angle open_shift closed_shift '
                'reaction_uv_shift reaction_vu_shift growth_dwell growth_divisor '
                'seed pair device_budget_mib').split()
ROOT=Path(__file__).resolve().parents[1]
def bake(pair: str, width: int, height: int, steps: int, out: Path) -> dict:
    if pair not in ('XX','XY') or width<32 or width>2048 or width&(width-1) or not 2<=height<=2048 or not 1<=steps<=4096:
        raise ValueError('Invalid pair, dimensions or step budget')
    if out.exists() or out.with_suffix('.json').exists(): raise FileExistsError(f'Choose a new output asset: {out}')
    model=json.loads((ROOT/'provenance'/f'upstream_seed_{pair.lower()}.json').read_text())['model']
    params=dict(zip(PARAM_FIELDS,[width,height,5,1,steps,49,8192,256,1,3,3,5,6,7,16,4,20260911,int(pair=='XY'),2048]))
    rho=np.linspace(math.log(1/32),math.log(4),height)
    theta=np.arange(width)*2*math.pi/width
    rr,tt=np.meshgrid(rho,theta,indexing='ij')
    points=np.stack((np.exp(rr)*np.cos(tt),np.exp(rr)*np.sin(tt)),axis=-1)
    arch=m_field(points,model['arc_radius'],model['arc_spacing'],model['arc_thickness'])
    planes=[]; generations=[]
    for g in range(params['levels']):
        word=grow(Pair.parse(pair),g)
        segments=turtle(word,model['turtle_step'],model['turtle_angle'],model['turtle_shrink'])
        segments=model['embedding_scale']*segments+np.array([0,model['embedding_y']])
        field=np.maximum(np.minimum(arch,capsule_field(points,segments,model['capsule_thickness'])),-points[...,1])
        rounded=np.floor(field*4096+0.5)
        codes=np.clip(rounded,-32768,32767).astype(np.int32)
        drive=np.clip(32768-16*codes,0,65535).astype(np.uint32)
        packed=(codes+32768).astype(np.uint32)|(drive<<np.uint32(16))
        planes.append(packed.astype('<u4').tobytes())
        generations.append(dict(level=g,word_length=len(word),drawing_symbols=sum(c in 'XY' for c in word),
            word=word,occupied_bins=int(np.count_nonzero(codes<=0)),saturated_bins=int(np.count_nonzero(rounded!=codes)),
            float_to_code_max_error_unsaturated=float(np.max(np.abs(codes[rounded==codes]/4096-field[rounded==codes])))))
    payload=struct.pack('<8sII19I',b'GBLUT31\0',1,19,*(params[n] for n in PARAM_FIELDS))+b''.join(planes)
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(payload)
    manifest=dict(schema='gambit-lut-3.1',file=out.name,sha256=hashlib.sha256(payload).hexdigest(),params=params,
        author={'name':'Tom Klootwijk','identifier':'NL200678942','date_as_supplied':'10-07-1990'},
        chart={'rho':'natural logarithm r; r0=1','r_min':1/32,'r_max':4,'radial_sampling':'inclusive equally spaced log radius',
               'angular_sampling':'theta=2*pi*j/width; j=0..width-1','origin':'excluded','units':'dimensionless simulation units'},
        format={'low16':'signed-field code plus 32768','high16':'clip(32768 - 16*code, 0, 65535)',
                'distance_scale':4096,'rounding':'floor(4096*float_sample + 0.5); then saturation',
                'array_layout':'[generation][radial][angular]; little-endian uint32'},
        geometry_source='provenance/upstream_seed_'+pair.lower()+'.json; zero incoming memory; tools/geometry_v3.py',
        baked_with={'python':platform.python_version(),'numpy':np.__version__,'platform':platform.platform()},generations=generations,
        scope='Finite sampled field, not an infinite chart or exact continuous-space representation. XX/XY are symbolic tokens.')
    out.with_suffix('.json').write_text(json.dumps(manifest,indent=2)+'\n')
    return manifest
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pair',choices=['XX','XY'],required=True)
    ap.add_argument('--width',type=int,default=512);ap.add_argument('--height',type=int,default=256)
    ap.add_argument('--steps',type=int,default=256);ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();m=bake(a.pair,a.width,a.height,a.steps,a.out);print(m['sha256'],a.out)
