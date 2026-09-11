#!/usr/bin/env python3
"""Generate a self-contained offline HTML viewer from the synthetic replay."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'));sys.path.insert(0,str(ROOT/'tools'))
from uu_prism.core import Prism,load_registry
from demo import make_inputs,HOLDER,AS_OF
reg=load_registry(ROOT/'spec/facets.json')
plan={f['id']:1 for f in reg['facets']};plan['F01']=2;plan['F05']=0
p=Prism(HOLDER,reg,plan);frames=[p.snapshot(AS_OF)]
for r in make_inputs():p.add(r);frames.append(p.snapshot(AS_OF))
final=json.loads((ROOT/'verification/demo/snapshot.json').read_text())
frames.append(final)
source=(ROOT/'app/viewer_template.html').read_text()
data=json.dumps({'registry':reg,'frames':frames},ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
(ROOT/'app/index.html').write_text(source.replace('__FIXTURE_DATA__',data))
print('Built local HTML viewer with',len(frames),'replay frames')
