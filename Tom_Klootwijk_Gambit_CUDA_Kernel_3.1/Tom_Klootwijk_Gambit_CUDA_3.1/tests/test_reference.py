from pathlib import Path
import hashlib,json,struct,sys,unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from reference import Reference,Cell,load_asset,trunc_div,mix32,D
ROOT=Path(__file__).resolve().parents[1]
class ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.p,cls.lut=load_asset(ROOT/'assets/verify_xy.gblut')
    def engine(self,**kw):return Reference(self.p,self.lut,**kw)
    def test_signed_division(self):self.assertEqual([trunc_div(x,256) for x in [-257,-256,-255,-1,0,255,256] ],[-1,-1,0,0,0,0,1])
    def test_manifest_hashes(self):
        for a in (ROOT/'assets').glob('*.gblut'):self.assertEqual(hashlib.sha256(a.read_bytes()).hexdigest(),json.loads(a.with_suffix('.json').read_text())['sha256'])
    def test_header(self):self.assertEqual((self.p['width'],self.p['height'],self.p['levels']),(64,33,5))
    def test_cover_packing(self):
        for v in self.lut:self.assertEqual(v>>16,max(0,min(65535,32768-16*((v&65535)-32768))))
    def test_pair_assets_differ(self):
        p,x=load_asset(ROOT/'assets/verify_xx.gblut');self.assertNotEqual(x,self.lut);self.assertEqual(p['pair'],0)
    def test_growth_word_counts(self):
        for pair in ['xx','xy']:
            m=json.loads((ROOT/'assets'/f'verify_{pair}.json').read_text())
            for row in m['generations']:
                self.assertEqual(row['word_length'],5*3**row['level']+1);self.assertEqual(row['drawing_symbols'],2*3**row['level'])
    def test_nonzero_initial_mass(self):self.assertGreater(self.engine().initial_mass,0)
    def test_parity_replay(self):
        x=self.engine();y=self.engine()
        for _ in range(8):x.step();y.step();self.assertEqual(x.words,y.words)
    def test_latch_events(self):
        x=self.engine();prev=[0]*(x.n//32)
        for _ in range(8):
            x.step();nw=x.n//32;self.assertEqual([a^b for a,b in zip(prev,x.words[nw:2*nw])],x.words[2*nw:3*nw]);prev=x.words[nw:2*nw]
    def test_output_parity(self):
        x=self.engine();x.step();nw=x.n//32;self.assertEqual([w.bit_count()%2 for w in x.words[:nw]],x.words[4*nw:])
    def test_mass_and_prefix(self):
        x=self.engine()
        for _ in range(16):
            x.step();self.assertEqual(sum(c.u+c.v for c in x.cells),x.initial_mass)
            for c in x.cells:self.assertEqual(D*c.qo+c.r,c.ki)
    def test_memory_bounds(self):
        x=self.engine()
        for _ in range(8):x.step();self.assertTrue(all(0<=c.z<=D and 0<=c.m<=D for c in x.cells))
    def test_pulse_feedback_effect(self):
        x=self.engine();y=self.engine(feedback=0);changed=False
        for _ in range(8):x.step();y.step();changed|=x.words!=y.words
        self.assertTrue(changed)
    def test_intervention_causality(self):
        x=self.engine();y=self.engine(inject_step=3,inject_cell=7)
        for _ in range(3):x.step();y.step();self.assertEqual(x.cells,y.cells)
        x.step();y.step();self.assertNotEqual(x.cells[7].z,y.cells[7].z)
    def test_growth_causal_schedule(self):
        x=self.engine();observed=[]
        for _ in range(64):
            r=x.step()
            if r[3]:observed.append(r[0]+1)
        self.assertEqual(observed,[16,32,48]);self.assertEqual(x.level,4)
    def test_material_to_memory_coupling(self):
        x=self.engine();y=self.engine();i=next(i for i,c in enumerate(y.cells) if c.u>c.v>0)
        c=y.cells[i];y.cells[i]=Cell(c.v,c.u,c.z,c.m,c.r,c.flags,c.ki,c.qo)
        x.step();y.step();self.assertNotEqual(x.cells[i].z,y.cells[i].z)
        self.assertEqual(sum(c.u+c.v for c in x.cells),sum(c.u+c.v for c in y.cells))
    def test_serialization(self):
        x=self.engine();x.step();s=x.serialize_state();self.assertEqual(len(s),24+40*x.n);self.assertEqual(s[:8],b'GBSTAT31')
    def test_reduced_word_not_full_state(self):
        # Same just-emitted q=0 may leave residuals 0 and D-1. A common k=1 distinguishes the next bit.
        q1=(0+1)>=D;q2=(D-1+1)>=D;self.assertNotEqual(q1,q2)
    def test_mixer_range(self):
        for x in [0,1,0xffffffff,20260911]:self.assertTrue(0<=mix32(x)<=0xffffffff)
if __name__=='__main__':unittest.main(verbosity=2)
