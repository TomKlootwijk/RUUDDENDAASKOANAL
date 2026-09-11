#!/usr/bin/env python3
"""Print deterministic pulse/latch/event words in increasing cell order."""
import argparse,struct,json
from pathlib import Path
def display(file:Path,word:int,steps:int)->str:
    with file.open('rb') as f:
        if f.read(8)!=b'GBWORD31':raise ValueError('Bad trace')
        w,h,total,planes,nw=struct.unpack('<5I',f.read(20))
        if not 0<=word<nw or not 1<=steps<=total or planes!=5:raise ValueError('Invalid slice')
        meta=file.parent/'run.json'
        backend=json.loads(meta.read_text()).get('backend','unknown') if meta.is_file() else 'unknown'
        lines=[f'Gambit 3.1 | {w} x {h} | word {word} | cells {32*word}..{32*word+31}',
               f'Printed order: cell offset 0 first (LSB first). Recorded backend: {backend}.']
        for t in range(steps):
            x=struct.unpack(f'<{5*nw}I',f.read(20*nw))
            bits=lambda p:''.join(str((x[p*nw+word]>>j)&1) for j in range(32))
            lines.append(f'{t:03d} pulse={bits(0)} latch={bits(1)} event={bits(2)} parity={x[4*nw+word]}')
    return '\n'.join(lines)+'\n'
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('trace',type=Path);ap.add_argument('--word',type=int,default=17);ap.add_argument('--steps',type=int,default=8)
    a=ap.parse_args();print(display(a.trace,a.word,a.steps),end='')
