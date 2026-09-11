#!/usr/bin/env python3
"""Independent record checker. Recounts pulses, parity, hinge events and endpoint certificates.
It does NOT reconstruct every k from the final count record. Cross-implementation
replay and native per-step checks provide the separate transition evidence.
"""
from pathlib import Path
import argparse,struct,json
from reference import from_capsule,D

def audit(path:Path):
    first=from_capsule((path/'initial.gbc').read_bytes());last=from_capsule((path/'final.gbc').read_bytes())
    if first.asset_bytes()!=last.asset_bytes() or first.feedback!=last.feedback:raise ValueError('Immutable seed changed')
    raw=(path/'words.bin').read_bytes()
    if len(raw)<28:raise ValueError('Truncated word header')
    magic,w,h,steps,planes,nw=struct.unpack_from('<8s5I',raw)
    if (magic,w,h,planes,nw)!=(b'GBWORD40',first.p['width'],first.p['height'],5,first.n//32) or not 1<=steps<=4096 or len(raw)!=28+steps*20*nw:raise ValueError('Word format')
    pulses=[0]*first.n;latches=first.words[nw:2*nw];last_words=None
    for t in range(steps):
        words=struct.unpack_from(f'<{5*nw}I',raw,28+t*20*nw)
        for j in range(nw):
            if words[4*nw+j]!=words[j].bit_count()%2:raise ValueError('Parity failure')
            if words[2*nw+j] != latches[j]^words[nw+j]:raise ValueError('Hinge-event telescope failure')
            latches[j]=words[nw+j]
            mask=words[j]
            while mask:
                low=mask&-mask;pulses[32*j+low.bit_length()-1]+=1;mask^=low
        last_words=words
    if list(last_words)!=last.words:raise ValueError('Final flags/word mismatch')
    counts=(path/'counts.bin').read_bytes()
    if counts[:8]!=b'GBCOUNT4' or len(counts)!=12+20*first.n or struct.unpack_from('<I',counts,8)[0]!=first.n:raise ValueError('Count format')
    total_k=0
    for i,(a,b) in enumerate(zip(first.cells,last.cells)):
        r0,k,q=struct.unpack_from('<IQQ',counts,12+20*i)
        if r0!=a.r or q!=pulses[i] or D*q+b.r!=r0+k or k>steps*D:raise ValueError('Per-cell count certificate failure')
        total_k+=k
    if last.phase!=(first.phase+steps*first.p['phase_stride'])%first.p['width']:raise ValueError('Phase projection')
    return {'status':'PASS','steps':steps,'cells':first.n,'pulse_bits':steps*first.n,'ones':sum(pulses),
            'total_input':total_k,'mass':first.mass0,'endpoint_count_certificate':True,'parity_and_events':True,
            'complete_historical_input_reconstructed':False}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('run',type=Path);a=p.parse_args();print(json.dumps(audit(a.run),indent=2))
