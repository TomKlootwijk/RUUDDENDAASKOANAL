#!/usr/bin/env python3
"""Regenerate manuscript plots from exact state mapping and disclosed witness.
Optional dependency: matplotlib. No random source and no external request.
"""
from pathlib import Path
import csv,sys
from fractions import Fraction
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from state_sdf import signed_distance
ROOT=Path(__file__).resolve().parents[1]
def main():
    out=ROOT/'manuscript/figures';out.mkdir(exist_ok=True)
    bits=list(map(int,'01011001'))
    xs=[Fraction(k,40) for k in range(-40,1001)]
    fig,ax=plt.subplots(figsize=(9,3.6))
    ax.plot([float(x) for x in xs],[float(signed_distance(bits,x)) for x in xs],label='Exact signed distance')
    ax.axhline(0,linestyle='--',linewidth=0.8)
    centres=[3*j for j in range(1,9)]
    ax.scatter(centres,[float(signed_distance(bits,x)) for x in centres],s=30,zorder=3,label='Bit query centres')
    for j,b in enumerate(bits,1):ax.annotate(str(b),(3*j,float(signed_distance(bits,3*j))),xytext=(0,9),textcoords='offset points',ha='center',fontsize=10)
    ax.set_xlabel('Encoded coordinate x (dimensionless)');ax.set_ylabel('Signed distance')
    ax.set_title('An exact field representation of the binary word 01011001')
    ax.set_ylim(-0.7,6.7);ax.set_xlim(-1,25);ax.legend(loc='upper left',fontsize=9)
    fig.tight_layout();fig.savefig(out/'state_sdf.pdf',metadata={'CreationDate':None,'ModDate':None});plt.close(fig)
    data=list(csv.DictReader((ROOT/'evidence/feedback/trace.csv').open()))[:20]
    t=[int(x['tick']) for x in data]
    fig,ax=plt.subplots(figsize=(9,3.6))
    ax.plot(t,[int(x['baseline_z7']) for x in data],marker='o',markersize=3,label='Baseline')
    ax.plot(t,[int(x['intervention_z7']) for x in data],marker='s',markersize=3,label='One-read intervention')
    ax.axvline(3,linestyle='--',linewidth=1,label='Read altered: tick 3')
    ax.axvline(7,linestyle=':',linewidth=1,label='First output difference: tick 7')
    ax.set_xlabel('Update index (zero-based)');ax.set_ylabel('Cell 7 fast state z (integer units)')
    ax.set_title('Causal feedback: one altered read changes the later output')
    ax.legend(loc='lower right',fontsize=8);ax.set_xticks(range(0,20,2));fig.tight_layout()
    fig.savefig(out/'feedback.pdf',metadata={'CreationDate':None,'ModDate':None});plt.close(fig)
if __name__=='__main__':main()
