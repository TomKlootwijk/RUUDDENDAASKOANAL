"""Pure, deterministic metadata projection. No sensor, network or identity inference.

All permissions and subject links here are locally supplied assertions. This module
is not an authentication service, a secure vault, or a government credential issuer.
"""
from __future__ import annotations
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable

VERSION = '2.1.1'
FACET_IDS = tuple(f'F{i:02d}' for i in range(1,36))
REQUIRED = {'record_id','holder_ref','facet_id','source_ref','source_kind','permission',
            'link_status','observed_at','received_at','payload_sha256','byte_size','assertion_kind'}
OPTIONAL = {'supersedes','permission_ref'}
KINDS = {'synthetic','holder_export','holder_measurement','holder_declaration'}


def canonical(value: Any) -> bytes:
    return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def utc(value: str) -> datetime:
    if not isinstance(value,str) or not value.endswith('Z'):
        raise ValueError('time_must_be_explicit_UTC_Z')
    try:
        t=datetime.fromisoformat(value[:-1]+'+00:00')
    except (ValueError,TypeError) as exc:
        raise ValueError('invalid_timestamp') from exc
    return t.astimezone(timezone.utc)


def uu_id(values: Iterable[tuple[Fraction,Fraction]]) -> Fraction | None:
    """V2 minimum of absolute threshold deviations; None denotes empty."""
    terms=[abs(v-t) for v,t in values]
    return min(terms) if terms else None


def validate_record(record: dict, holder: str) -> dict:
    if not isinstance(record,dict):raise ValueError('record_not_object')
    if not REQUIRED.issubset(record) or set(record)-REQUIRED-OPTIONAL:
        raise ValueError('record_fields')
    r=deepcopy(record)
    for k in ('record_id','holder_ref','facet_id','source_ref','source_kind','permission','link_status','assertion_kind'):
        if not isinstance(r[k],str) or not r[k] or len(r[k])>240:raise ValueError('invalid_text_field')
    if r['holder_ref']!=holder:raise ValueError('holder_mismatch')
    if r['facet_id'] not in FACET_IDS:raise ValueError('unknown_facet')
    if r['source_kind'] not in KINDS:raise ValueError('unsupported_acquisition_source')
    if r['permission']!='granted':raise ValueError('permission_not_granted')
    if r['link_status']!='holder_confirmed':raise ValueError('unresolved_subject_link')
    if r['assertion_kind'] not in ('source_record','measurement','self_report','synthetic'):
        raise ValueError('unsupported_inference')
    if r['facet_id']=='F30' and r['assertion_kind'] not in ('self_report','synthetic'):
        raise ValueError('declaration_must_be_self_reported')
    if type(r['byte_size']) is not int or not 0<=r['byte_size']<=2**53-1:raise ValueError('invalid_byte_size')
    if not isinstance(r['payload_sha256'],str) or not re.fullmatch('[0-9a-f]{64}',r['payload_sha256']):
        raise ValueError('invalid_payload_digest')
    utc(r['received_at'])
    if r['observed_at'] is not None:utc(r['observed_at'])
    if r.get('supersedes') is not None and not re.fullmatch('[0-9a-f]{64}',str(r['supersedes'])):
        raise ValueError('invalid_predecessor_digest')
    if 'permission_ref' in r and (not isinstance(r['permission_ref'],str) or not r['permission_ref']):
        raise ValueError('invalid_permission_reference')
    return r


class Prism:
    """Single-holder record view plus ordered, hash-chained local audit events."""
    def __init__(self,holder: str,registry: dict,targets: dict[str,int] | None=None,max_records: int=10000):
        if not isinstance(holder,str) or not holder or len(holder)>240:raise ValueError('invalid_holder')
        if type(max_records) is not int or max_records<1:raise ValueError('invalid_budget')
        self.holder=holder;self.registry=deepcopy(registry)
        self.facets={f['id']:deepcopy(f) for f in registry['facets']}
        if set(self.facets)!=set(FACET_IDS):raise ValueError('facet_registry_mismatch')
        for f in self.facets.values():
            if type(f['freshness_seconds']) is not int or f['freshness_seconds']<0:raise ValueError('invalid_freshness')
        targets=targets or {}
        if set(targets)-set(FACET_IDS):raise ValueError('unknown_plan_facet')
        if any(type(n) is not int or n<0 for n in targets.values()):raise ValueError('invalid_plan_target')
        self.targets={f:targets.get(f,0) for f in FACET_IDS};self.max_records=max_records
        self.records:dict[str,dict]={};self.withdrawn:set[str]=set();self.events:list[dict]=[]
        self.rejections:list[dict]=[];self.duplicates=0

    def _event(self,kind: str,record: dict) -> None:
        row={'sequence':len(self.events)+1,'kind':kind,'previous':self.events[-1]['event_hash'] if self.events else '0'*64,'body':deepcopy(record)}
        row['event_hash']=digest(row);self.events.append(row)

    def add(self,record: dict) -> str:
        """Invalid rows are quarantined; equal retries do not duplicate audit events."""
        try:
            r=validate_record(record,self.holder)
            key=r['record_id'];old=self.records.get(key)
            if old==r:
                self.duplicates+=1;return 'duplicate'
            if old is not None:
                if r.get('supersedes')!=digest(old):raise ValueError('conflicting_record_id')
                if utc(r['received_at'])<utc(old['received_at']):raise ValueError('correction_time_regression')
            elif r.get('supersedes') is not None:raise ValueError('missing_predecessor')
            elif len(self.records)>=self.max_records:raise ValueError('record_budget_exceeded')
            # A hash with inconsistent lengths is not accepted as a content alias.
            for v in self.records.values():
                if v['payload_sha256']==r['payload_sha256'] and v['byte_size']!=r['byte_size']:
                    raise ValueError('digest_length_conflict')
            self.records[key]=r;self.withdrawn.discard(key)
            self._event('correct' if old else 'admit',r)
            return 'corrected' if old else 'accepted'
        except (ValueError,TypeError,KeyError) as exc:
            self.rejections.append({'quarantine_sequence':len(self.rejections)+1,'reason':str(exc)})
            return 'quarantined'

    def revoke(self,key: str,at: str) -> bool:
        utc(at)
        if key not in self.records:raise ValueError('unknown_record')
        if key in self.withdrawn:return False
        if utc(at)<utc(self.records[key]['received_at']):raise ValueError('revocation_time_regression')
        self.withdrawn.add(key);self._event('withdraw',{'record_id':key,'at':at})
        return True

    def check_chain(self) -> bool:
        previous='0'*64
        for i,e in enumerate(self.events,1):
            if e.get('sequence')!=i or e.get('previous')!=previous:return False
            if e.get('event_hash')!=digest({k:v for k,v in e.items() if k!='event_hash'}):return False
            previous=e['event_hash']
        return True

    def snapshot(self,as_of: str) -> dict:
        now=utc(as_of)
        # State is a current committed view, not a historical-query engine.
        if any(utc(r['received_at'])>now for r in self.records.values()):raise ValueError('as_of_precedes_committed_record')
        if any(e['kind']=='withdraw' and utc(e['body']['at'])>now for e in self.events):raise ValueError('as_of_precedes_withdrawal')
        active=[r for k,r in self.records.items() if k not in self.withdrawn]
        rows=[];horizons=[];complete_flags=[]
        for f in FACET_IDS:
            items=[r for r in active if r['facet_id']==f]
            target=self.targets[f];n=len(items)
            count_status='not_planned' if target==0 else 'complete' if n>=target else 'partial' if n else 'missing'
            ratio=min(Fraction(n,target),Fraction(1)) if target else None
            if ratio is not None:horizons.append((ratio,Fraction(1)));complete_flags.append(n>=target)
            times=[utc(r['observed_at']) for r in items if r['observed_at'] is not None]
            latest=max(times) if times else None
            if not items:status='withdrawn' if any(r['facet_id']==f and k in self.withdrawn for k,r in self.records.items()) else 'missing'
            elif latest is None:status='time_unknown'
            elif latest>now:status='clock_conflict'
            elif (now-latest).total_seconds()<=self.facets[f]['freshness_seconds']:status='fresh'
            else:status='stale'
            rows.append({'facet_id':f,'band':self.facets[f]['band'],'name':self.facets[f]['name'],
              'count':n,'target':target,'plan_status':count_status,'data_status':status,
              'coverage':None if ratio is None else {'numerator':ratio.numerator,'denominator':ratio.denominator},
              'latest_observed_at':latest.isoformat().replace('+00:00','Z') if latest else None,
              'age_seconds':int((now-latest).total_seconds()) if latest and latest<=now else None,
              'record_ids':sorted(r['record_id'] for r in items)})
        u=uu_id(horizons);objects={r['payload_sha256']:r['byte_size'] for r in active}
        result={'format':'UU-PRISM-SNAPSHOT','version':VERSION,'holder_ref':self.holder,
          'purpose':'personal_archive_migration','credential_status':'not_issued','as_of':as_of,
          'registry_hash':digest(self.registry),'plan':deepcopy(self.targets),'facets':rows,
          'active_links':len(active),'active_objects':len(objects),'active_unique_bytes':sum(objects.values()),
          'withdrawn_links':len(self.withdrawn),'quarantined_attempts':len(self.rejections),
          'duplicate_attempts':self.duplicates,'event_count':len(self.events),
          'event_root':self.events[-1]['event_hash'] if self.events else '0'*64,
          'uu_minimum':None if u is None else {'numerator':u.numerator,'denominator':u.denominator},
          'declared_plan_complete':all(complete_flags) if complete_flags else None,
          'coverage_scope':'declared metadata slots only; not all data about the holder'}
        result['snapshot_hash']=digest(result)
        return result

    def export(self,as_of: str) -> dict:
        return {'snapshot':self.snapshot(as_of),'registry':deepcopy(self.registry),
          'records':deepcopy(self.records),'withdrawn':sorted(self.withdrawn),'events':deepcopy(self.events),
          'rejections':deepcopy(self.rejections),'duplicates':self.duplicates,'max_records':self.max_records}

    @classmethod
    def restore(cls,document: dict) -> 'Prism':
        d=deepcopy(document);s=d['snapshot']
        if s['snapshot_hash']!=digest({k:v for k,v in s.items() if k!='snapshot_hash'}):raise ValueError('snapshot_digest_mismatch')
        p=cls(s['holder_ref'],d['registry'],s['plan'],d['max_records'])
        p.events=d['events']
        if not p.check_chain():raise ValueError('event_chain_invalid')
        p.events=[]
        for e in d['events']:
            if e['kind'] in ('admit','correct'):
                status=p.add(e['body'])
                if status not in ('accepted','corrected'):raise ValueError('event_replay_failed')
            elif e['kind']=='withdraw':p.revoke(e['body']['record_id'],e['body']['at'])
            else:raise ValueError('unknown_event')
        if p.records!=d['records'] or sorted(p.withdrawn)!=d['withdrawn']:raise ValueError('view_replay_mismatch')
        p.rejections=d['rejections'];p.duplicates=d['duplicates']
        if p.snapshot(s['as_of'])!=s:raise ValueError('snapshot_replay_mismatch')
        return p


def load_registry(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding='utf-8'))
