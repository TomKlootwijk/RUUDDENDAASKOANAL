from pathlib import Path
from copy import deepcopy
from fractions import Fraction
import unittest,json,sys,hashlib,tempfile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from demo import make_inputs,AS_OF,HOLDER,run
from inventory import inventory
from uu_prism.core import Prism,canonical,digest,utc,uu_id,load_registry,validate_record
REG=load_registry(ROOT/'spec/facets.json')

def state():return Prism(HOLDER,REG,{f'F{i:02d}':1 for i in range(1,36)})

class AlgebraTests(unittest.TestCase):
    def test_empty(self):self.assertIsNone(uu_id([]))
    def test_definition(self):self.assertEqual(uu_id([(Fraction(2),Fraction(3)),(Fraction(5),Fraction(8))]),1)
    def test_commutative(self):
        a=[(Fraction(1,4),Fraction(1)),(Fraction(3,5),Fraction(1))]
        self.assertEqual(uu_id(a),uu_id(reversed(a)))
    def test_duplicate_idempotence(self):
        a=[(Fraction(1,4),Fraction(1))];self.assertEqual(uu_id(a),uu_id(a+a))
    def test_scalar_not_complete(self):
        p=state();p.add(make_inputs()[0]);s=p.snapshot(AS_OF)
        self.assertEqual(s['uu_minimum'],{'numerator':0,'denominator':1});self.assertFalse(s['declared_plan_complete'])
    def test_hamming_collision(self):self.assertEqual(0b0011.bit_count(),0b1100.bit_count());self.assertNotEqual(3,12)
    def test_parity_even_mask(self):
        for w in range(256):self.assertEqual(w.bit_count()%2,(w^3).bit_count()%2)
    def test_latch_history_collision(self):
        a=[0,0,0];b=[0,1,0]
        self.assertEqual(a[-1],b[-1]);self.assertEqual((a[0]^a[1])^(a[1]^a[2]),(b[0]^b[1])^(b[1]^b[2]))
    def test_canonical_keys(self):self.assertEqual(canonical({'b':1,'a':2}),canonical({'a':2,'b':1}))
    def test_finite_json(self):
        with self.assertRaises(ValueError):canonical({'x':float('nan')})

class RegistryTests(unittest.TestCase):
    def test_bands(self):self.assertEqual([b['code'] for b in REG['bands']],list('ROYGBIV'))
    def test_facets(self):self.assertEqual(len(REG['facets']),35);self.assertEqual(len({f['id'] for f in REG['facets']}),35)
    def test_five_per_band(self):
        for b in 'ROYGBIV':self.assertEqual(sum(f['band']==b for f in REG['facets']),5)
    def test_disabled_defaults(self):self.assertTrue(all(f['default_enabled'] is False for f in REG['facets']))
    def test_invalid_plan(self):
        with self.assertRaises(ValueError):Prism(HOLDER,REG,{'F99':1})
    def test_invalid_target(self):
        with self.assertRaises(ValueError):Prism(HOLDER,REG,{'F01':-1})
    def test_boolean_target(self):
        with self.assertRaises(ValueError):Prism(HOLDER,REG,{'F01':True})
    def test_registry_copy(self):
        r=deepcopy(REG);p=Prism(HOLDER,r);r['facets'][0]['name']='changed'
        self.assertNotEqual(p.facets['F01']['name'],'changed')

class AdmissionTests(unittest.TestCase):
    def setUp(self):self.p=state();self.r=make_inputs()[0]
    def test_admit(self):self.assertEqual(self.p.add(self.r),'accepted')
    def test_retry(self):self.p.add(self.r);self.assertEqual(self.p.add(self.r),'duplicate');self.assertEqual(len(self.p.events),1)
    def test_cross_holder(self):self.r['holder_ref']='other';self.assertEqual(self.p.add(self.r),'quarantined')
    def test_permission(self):self.r['permission']='withheld';self.assertEqual(self.p.add(self.r),'quarantined')
    def test_unresolved_link(self):self.r['link_status']='unresolved';self.assertEqual(self.p.add(self.r),'quarantined')
    def test_unknown_facet(self):self.r['facet_id']='F99';self.assertEqual(self.p.add(self.r),'quarantined')
    def test_covert_source(self):self.r['source_kind']='intercept';self.assertEqual(self.p.add(self.r),'quarantined')
    def test_inferred_traits(self):self.r['assertion_kind']='inferred';self.assertEqual(self.p.add(self.r),'quarantined')
    def test_self_report_rule(self):self.r.update(facet_id='F30',assertion_kind='measurement');self.assertEqual(self.p.add(self.r),'quarantined')
    def test_bad_digest(self):self.r['payload_sha256']='x';self.assertEqual(self.p.add(self.r),'quarantined')
    def test_byte_size(self):self.r['byte_size']=-1;self.assertEqual(self.p.add(self.r),'quarantined')
    def test_unknown_fields(self):self.r['sexuality_inferred']='x';self.assertEqual(self.p.add(self.r),'quarantined')
    def test_missing_field(self):del self.r['holder_ref'];self.assertEqual(self.p.add(self.r),'quarantined')
    def test_copy_on_admission(self):self.p.add(self.r);self.r['source_ref']='changed';self.assertNotEqual(self.p.records['demo:F01']['source_ref'],'changed')
    def test_conflict(self):self.p.add(self.r);self.r['source_ref']='changed';self.assertEqual(self.p.add(self.r),'quarantined')
    def test_correction(self):
        self.p.add(self.r);r=dict(self.r,source_ref='corrected',supersedes=digest(self.r))
        self.assertEqual(self.p.add(r),'corrected');self.assertEqual(len(self.p.events),2)
    def test_missing_predecessor(self):self.r['supersedes']='0'*64;self.assertEqual(self.p.add(self.r),'quarantined')
    def test_budget(self):
        p=Prism(HOLDER,REG,max_records=1);p.add(self.r);self.assertEqual(p.add(make_inputs()[1]),'quarantined')
    def test_hash_size_conflict(self):
        self.p.add(self.r);r=dict(self.r,record_id='different',byte_size=self.r['byte_size']+1)
        self.assertEqual(self.p.add(r),'quarantined')
    def test_quarantine_minimizes(self):
        self.r['holder_ref']='private-other-name';self.p.add(self.r)
        self.assertNotIn('private-other-name',json.dumps(self.p.rejections))

class TimeAndViewTests(unittest.TestCase):
    def test_no_timezone(self):
        with self.assertRaises(ValueError):utc('2026-09-11T12:00:00')
    def test_invalid_date(self):
        with self.assertRaises(ValueError):utc('2026-99-11T12:00:00Z')
    def test_fresh(self):
        p=state();p.add(make_inputs()[2]);self.assertEqual(p.snapshot(AS_OF)['facets'][2]['data_status'],'fresh')
    def test_stale(self):
        p=state();p.add(make_inputs()[0]);self.assertEqual(p.snapshot(AS_OF)['facets'][0]['data_status'],'stale')
    def test_unknown_time(self):
        p=state();p.add(make_inputs()[13]);self.assertEqual(p.snapshot(AS_OF)['facets'][29]['data_status'],'time_unknown')
    def test_future_clock(self):
        p=state();p.add(make_inputs()[4]);self.assertEqual(p.snapshot(AS_OF)['facets'][7]['data_status'],'clock_conflict')
    def test_missing(self):self.assertEqual(state().snapshot(AS_OF)['facets'][0]['data_status'],'missing')
    def test_no_plan(self):self.assertIsNone(Prism(HOLDER,REG).snapshot(AS_OF)['declared_plan_complete'])
    def test_empty_hash_chain(self):self.assertTrue(state().check_chain())
    def test_asof_before_record(self):
        p=state();p.add(make_inputs()[0])
        with self.assertRaises(ValueError):p.snapshot('2026-01-01T00:00:00Z')
    def test_same_blob_multiple_facets(self):
        p=state();p.add(make_inputs()[0]);p.add(make_inputs()[1]);s=p.snapshot(AS_OF)
        self.assertEqual((s['active_links'],s['active_objects']),(2,1))
    def test_unknown_not_zero_value(self):
        s=state().snapshot(AS_OF)['facets'][0]
        self.assertIsNone(s['age_seconds']);self.assertIsNone(s['latest_observed_at'])

class LedgerTests(unittest.TestCase):
    def setUp(self):self.p=state();self.p.add(make_inputs()[0])
    def test_revoke(self):self.assertTrue(self.p.revoke('demo:F01',AS_OF));self.assertEqual(self.p.snapshot(AS_OF)['active_links'],0)
    def test_revoke_idempotent(self):self.p.revoke('demo:F01',AS_OF);self.assertFalse(self.p.revoke('demo:F01',AS_OF))
    def test_revoke_unknown(self):
        with self.assertRaises(ValueError):self.p.revoke('absent',AS_OF)
    def test_withdrawal_status(self):
        self.p.revoke('demo:F01',AS_OF);self.assertEqual(self.p.snapshot(AS_OF)['facets'][0]['data_status'],'withdrawn')
    def test_retained_audit(self):
        self.p.revoke('demo:F01',AS_OF);self.assertEqual(len(self.p.events),2);self.assertIn('demo:F01',self.p.records)
    def test_chain_tampering(self):
        self.p.events[0]['body']['byte_size']+=1;self.assertFalse(self.p.check_chain())
    def test_restore(self):self.assertEqual(Prism.restore(self.p.export(AS_OF)).export(AS_OF),self.p.export(AS_OF))
    def test_snapshot_tampering(self):
        d=self.p.export(AS_OF);d['snapshot']['active_links']=90
        with self.assertRaises(ValueError):Prism.restore(d)
    def test_view_tampering(self):
        d=self.p.export(AS_OF);d['records']['demo:F01']['source_ref']='altered'
        with self.assertRaises(ValueError):Prism.restore(d)
    def test_replay_determinism(self):
        with tempfile.TemporaryDirectory() as a,tempfile.TemporaryDirectory() as b:
            self.assertEqual(run(Path(a)),run(Path(b)))

class InventoryTests(unittest.TestCase):
    def test_hash_and_size(self):
        with tempfile.TemporaryDirectory() as p:
            root=Path(p);(root/'a.txt').write_bytes(b'abc');x=inventory(root)
            self.assertEqual(x['total_bytes'],3);self.assertEqual(x['files'][0]['payload_sha256'],hashlib.sha256(b'abc').hexdigest())
    def test_budget(self):
        with tempfile.TemporaryDirectory() as p:
            root=Path(p);(root/'a').write_bytes(b'12345');x=inventory(root,4)
            self.assertEqual(x['file_count'],0);self.assertEqual(len(x['skipped']),1)
    def test_symlink(self):
        with tempfile.TemporaryDirectory() as p:
            root=Path(p);(root/'a').write_bytes(b'abc');(root/'b').symlink_to(root/'a');x=inventory(root)
            self.assertEqual(x['file_count'],1)
    def test_no_payload_copy(self):
        with tempfile.TemporaryDirectory() as p:
            root=Path(p);(root/'a').write_bytes(b'secret');x=inventory(root)
            self.assertNotIn('secret',json.dumps(x));self.assertEqual(len(list(root.iterdir())),1)
    def test_file_out_exclusion(self):
        with tempfile.TemporaryDirectory() as p:
            root=Path(p);(root/'a').write_bytes(b'1');(root/'out.json').write_bytes(b'old');x=inventory(root,excluded=root/'out.json')
            self.assertEqual(x['file_count'],1)
    def test_no_auto_facet(self):
        with tempfile.TemporaryDirectory() as p:
            root=Path(p);(root/'religion.txt').write_bytes(b'example');x=inventory(root)
            self.assertIsNone(x['files'][0]['facet_id'])

if __name__=='__main__':unittest.main()
