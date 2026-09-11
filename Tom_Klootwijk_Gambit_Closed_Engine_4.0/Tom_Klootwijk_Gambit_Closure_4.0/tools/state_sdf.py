#!/usr/bin/env python3
"""Exact rational SDF representation of a finite binary word, not an acoustic model.
A permanent anchor interval makes the all-zero word well-defined.
"""
from fractions import Fraction

def intervals(bits):
    if any(b not in (0,1) for b in bits):raise ValueError('A Boolean word is required')
    radius=Fraction(1,4)
    return [(Fraction(0)-radius,Fraction(0)+radius)]+[(3*j-radius,3*j+radius) for j,b in enumerate(bits,1) if b]

def signed_distance(bits,x):
    x=Fraction(x);ds=[]
    for lo,hi in intervals(bits):
        if lo<=x<=hi:return -min(x-lo,hi-x)
        ds.append(min(abs(x-lo),abs(x-hi)))
    return min(ds)

def recover(bits):return [int(signed_distance(bits,3*j)<0) for j in range(1,len(bits)+1)]

if __name__=='__main__':
    import argparse,json
    p=argparse.ArgumentParser();p.add_argument('word');a=p.parse_args()
    if set(a.word)-{'0','1'}:p.error('Only 0 and 1 are admitted')
    bits=[int(c) for c in a.word]
    print(json.dumps({'word':a.word,'intervals':[[str(x),str(y)] for x,y in intervals(bits)],'recovered':''.join(map(str,recover(bits))),'scope':'Exact representation theorem, no physical field simulation'},indent=2))
