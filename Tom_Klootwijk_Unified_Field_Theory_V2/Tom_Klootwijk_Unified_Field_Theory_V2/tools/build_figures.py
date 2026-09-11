#!/usr/bin/env python3
"""Generate the manuscript's mathematical plots from explicit V2 data."""
from pathlib import Path
import csv
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tkuft.uuid import StateHorizon
from tkuft.wrap import AddressChart
OUT=ROOT/'report/figures';OUT.mkdir(exist_ok=True)

def finish(fig,name):
    fig.tight_layout();fig.savefig(OUT/(name+'.pdf'));fig.savefig(OUT/(name+'.png'),dpi=175);plt.close(fig)

with (ROOT/'verification/demo/uu_id_samples.csv').open() as f:rows=list(csv.DictReader(f))
x=[float(r['x']) for r in rows]
fig,ax=plt.subplots(figsize=(7.0,3.0))
ax.plot(x,[float(r['delta_A']) for r in rows],linestyle='--',lw=1,label='Horizon A: | |x| - 1 |')
ax.plot(x,[float(r['delta_B']) for r in rows],linestyle=':',lw=1.2,label='Horizon B: | |x - 3| - 1 |')
ax.plot(x,[float(r['uu_id']) for r in rows],lw=2,label='UU ID: pointwise minimum')
ax.set_xlabel('Query coordinate x');ax.set_ylabel('Unsigned boundary distance');ax.set_xlim(-2,5);ax.set_ylim(-.05,4.2)
ax.legend(frameon=False,fontsize=8,loc='upper center');ax.spines[['top','right']].set_visible(False)
finish(fig,'uu_id')

h=StateHorizon((0,1,0,1,1,0,0,1));x=[-1+k*.025 for k in range(1041)]
fig,ax=plt.subplots(figsize=(7.0,3.1));ax.plot(x,[h.evaluate(t) for t in x],lw=1.6,label='Unsigned state horizon U_b')
centres=[3*j for j in range(1,9)];ys=[h.evaluate(t) for t in centres]
ax.scatter(centres,ys,s=22,zorder=3,label='Bit-query centres');ax.axhline(.25,ls='--',lw=.8,label='Exact decoder threshold: 1/4')
for b,xx,yy in zip(h.bits,centres,ys):ax.annotate(str(b),(xx,yy),xytext=(0,8),textcoords='offset points',ha='center',fontsize=10)
ax.set_xlabel('Encoded coordinate x');ax.set_ylabel('Distance to retained interval boundaries');ax.set_xlim(-1,25);ax.set_ylim(-.15,6.3)
ax.legend(frameon=False,fontsize=8,loc='upper right');ax.spines[['top','right']].set_visible(False)
finish(fig,'unsigned_state')

with (ROOT/'verification/demo/feedback.csv').open() as f:rows=list(csv.DictReader(f))[:24]
fig,ax=plt.subplots(figsize=(7.0,3.0));x=[int(r['update']) for r in rows]
ax.plot(x,[int(r['baseline_z7']) for r in rows],marker='o',ms=3,label='Baseline')
ax.plot(x,[int(r['intervened_z7']) for r in rows],marker='s',ms=3,label='One-read intervention')
ax.axvline(3,ls='--',lw=.8,label='Read changed: tick 3');ax.axvline(9,ls=':',lw=.8,label='First output difference: tick 9')
ax.set_xlabel('Update index');ax.set_ylabel('Cell 7 activity z');ax.legend(frameon=False,fontsize=8,loc='upper right');ax.spines[['top','right']].set_visible(False)
finish(fig,'feedback')

chart=AddressChart();points=[chart.centre(28+118*i) for i in range(64)]
fig=plt.figure(figsize=(7.0,3.7));ax=fig.add_subplot(111,projection='3d')
for k in (0,40,80,117):
    ax.scatter([p[0] for p in points],[p[1] for p in points],[k*chart.layer_spacing]*64,s=8,label=f'Local bit layer {k}')
control=[chart.centre(j) for j in range(1,28)]
ax.plot([p[0] for p in control],[p[1] for p in control],[p[2] for p in control],lw=1.6,label='Control axis')
ax.set_xlabel('x');ax.set_ylabel('y');ax.set_zlabel('Bit layer height');ax.view_init(elev=24,azim=36);ax.legend(frameon=False,fontsize=7,loc='upper left')
finish(fig,'logpolar_layers')
print('Built four calculated figure pairs')
