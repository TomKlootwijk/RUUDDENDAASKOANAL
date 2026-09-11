from pathlib import Path
import json, csv, sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parents[1]
figdir=p/'manuscript/figures';figdir.mkdir(exist_ok=True)
sys.path.insert(0,str(p/'tools'))
from reference import load_asset
w=json.loads((p/'evidence/feedback_witness.json').read_text())
r=w['records']
plt.figure(figsize=(7.6,3.9))
plt.plot([x['step'] for x in r],[x['baseline_cell7']['z'] for x in r],label='Unmodified packed feedback')
plt.plot([x['step'] for x in r],[x['intervention_cell7']['z'] for x in r],label='One read flipped at step 3',linestyle='--')
plt.axvline(3,linestyle=':',label='Read intervention')
plt.xlabel('Update index (zero-based)');plt.ylabel('Cell 7 fast state (integer code)')
plt.title('A causal output-to-state feedback witness')
plt.xlim(0,25);plt.legend(fontsize=8);plt.grid(alpha=.2);plt.tight_layout()
plt.savefig(figdir/'feedback_state.pdf');plt.savefig(figdir/'feedback_state.png',dpi=160);plt.close()
plt.figure(figsize=(7.6,3.5))
plt.step([x['step'] for x in r],[x['pulse_bits_different'] for x in r],where='mid')
plt.xlabel('Update index (zero-based)');plt.ylabel('Differing pulse bits in this frame')
plt.title('A single feedback-read change alters later packed words')
plt.grid(alpha=.2);plt.tight_layout();plt.savefig(figdir/'feedback_bits.pdf');plt.savefig(figdir/'feedback_bits.png',dpi=160);plt.close()
plt.figure(figsize=(7.6,3.9))
for case,label in [('verify_xy','Pulse feedback enabled'),('verify_xy_no_pulse_feedback','Pulse-feedback ablation')]:
    rows=list(csv.DictReader((p/'evidence/cpu'/case/'summary.csv').open()))
    plt.plot([int(x['step']) for x in rows],[int(x['pulses'])/2112 for x in rows],label=label)
plt.xlabel('Update index (zero-based)');plt.ylabel('Fraction of cells emitting a pulse')
plt.title('Same XY asset, different declared feedback law')
plt.legend(fontsize=8);plt.grid(alpha=.2);plt.tight_layout();plt.savefig(figdir/'ablation.pdf');plt.savefig(figdir/'ablation.png',dpi=160);plt.close()
par,tex=load_asset(p/'assets/laptop_xy.gblut')
z=((np.array(tex,dtype=np.uint32).reshape(5,256,512)[4]&65535).astype(np.int32)-32768)/4096
plt.figure(figsize=(7.6,4.1))
plt.imshow(z,origin='lower',aspect='auto',extent=[0,360,np.log(1/32),np.log(4)])
plt.colorbar(label='Quantized field code / 4096')
plt.xlabel('Angular bin position (degrees)');plt.ylabel('Log-radius rho')
plt.title('Released XY log-polar atlas, generation 4')
plt.tight_layout();plt.savefig(figdir/'polar_lut.pdf');plt.savefig(figdir/'polar_lut.png',dpi=160);plt.close()
print('Four evidence figures exported; no hardware performance plot generated.')
