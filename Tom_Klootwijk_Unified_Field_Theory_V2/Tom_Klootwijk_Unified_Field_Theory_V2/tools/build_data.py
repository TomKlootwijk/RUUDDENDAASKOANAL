#!/usr/bin/env python3
"""Rebuild V2 literal definitions, source registers and tabular corpus data."""
from pathlib import Path
import csv
import hashlib
import json
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from tkuft.core import AUTHOR,PHASES,dutch_number,seal,Registry

def save(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def csvsave(path,rows):
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader()
        for row in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})

OPERATORS='''Literal definition node|Typed definition record containing operator or object semantics.
Content-addressed definition|Canonical JSON, excluding the content-hash field, determines the SHA-256 address.
Explicit dependency edge|Every composed definition names its dependencies by ID.
Versioned namespace|IDs, schema versions and profile versions distinguish definitions and semantics.
Definition-instance separation|An instance references a definition and carries literal parameters and state.
Acyclic resolution rule|A finite dependency graph admits a deterministic topological order.
Typed implicit-field sign|The inherited implicit-field record declares its signed membership convention.
Exact-SDF capability flag|Exact signed-distance status is declared for the applicable field and metric.
Parametric curve and sweep|A curve, parameter domain, regularity class and transport rule define a family.
Pulse polygon embedding|A positive pulse count maps to a point, segment or regular polygon.
Radix shell chart|Powers of the radix give digit thresholds and addresses for declared nested shells.
Log-polar core chart|The chart carries logarithmic radius, angle and an explicit singular-core flag.
Explicit quotient/gluing map|Ports carry coordinate, orientation and optional sheet transport.
Sheet-aware co-location|Coordinates, sheet, phase, orientation, branch and coupling policy are separate state.
Orientation transport|Orientation follows the declared maps and transitions.
Port and branch routing|An admitted event chooses an output port from an explicit finite routing table.
Split-merge lineage|A split names children; a merge records all parents and their addresses.
Guarded topology change|A topology-class change is committed through its declared transition rule.
Generic hinge tuple|A hinge contains pivot, state, selected map, guard and invariants.
Continuous planar hinge|A pivoted rotation defines position and differentiated velocity.
Discrete parity hinge|A Boolean state selects one of two maps or routes.
Connector hinge|A graph connector carries incidence and its declared numerical contribution.
Non-commutative hinge chain|The stored order of composition is part of the hinge definition.
Invariant subspace contract|Fixed points, axes and preserved quantities are stated in the hinge contract.
Bounded Dutch number profile|A versioned 0–99 lexicon records spelling, segments, morphemes and hinges.
Syllable-pulse operator|Each segment in the declared profile emits one pulse.
Teen suffix hinge|For 13–19, the unit root precedes the suffix tien in the spoken chart.
En connector hinge|Non-multiple tens use the order unit, en, tens.
Spoken-place permutation|An explicit map permutes semantic components and inserts the connector.
Feature-count comparison|A Boolean test compares pronunciation-profile pulses and binary Hamming weight.
Phase-ordered evaluator|The ten phases run from parse and normalization to transition and lineage.
Support-compatibility-guard discipline|Support is evaluated before compatibility and relation-guard solving.
Deterministic trace|Each executed step records definition ID, operator kind and typed output.
Evidence disposition|The provenance record identifies the source or formal construction of each mechanism.
Unknown-reference and cycle rejection|Loading checks unique IDs, resolved references, verified hashes and an acyclic graph.
Package verification contract|Schemas, tests, source hashes, file digests and reproducible examples accompany the corpus.'''
ops=[]
for i,line in enumerate(OPERATORS.splitlines(),1):
    name,contract=line.split('|');ops.append({'id':f'K36-{i:02d}','mechanism':name,'contract':contract,'source':'S1','physical_page':18 if i<=31 else 19})
PATTERNS='''Radix threshold ladder|integer → radix thresholds → shell indices
Active-bit pulse simplex|integer → active positions → pulse vertices
Pascal parity mask|(n,k) → binomial coefficient modulo two
Dutch teen suffix hinge|13–19 → unit-root and tien
Dutch en-order hinge|non-multiple tens → unit, en, tens
Cut-open boundary graph|closed edge → explicit pair of cut ports
Loop-to-leg morph|closed arc → interpolated segment and topology record
Split-oval antisymmetry|one loop → two oppositely displaced branches
Overlap-lens domain|two regions → explicitly typed overlap domain
SDF-zero event|field along trajectory → root → transition
Cone support gate|position, axis, radius and angle → local support
Nested-shell relevance|radius → local shell interval
Mobius orientation wrap|boundary crossing → coordinate wrap and orientation reversal
Klein sheet wrap|boundary crossing → wrap, orientation and sheet update
Hourglass route table|guard, sector and parity → branch
Log-polar bitmask|point → core flag, log radius, angle and admission bit
Golden-angle schedule|sample index → declared angular sequence
Bounded grammar recursion|seed and productions → finite budgeted expansion
Event-latched field morph|continuous blend and discrete topology state → guarded commit
Content-addressed definition graph|literal records → hashes → dependency DAG'''
patterns=[]
for i,line in enumerate(PATTERNS.splitlines(),1):
    name,pipeline=line.split('|');patterns.append({'id':f'P36-{i:02d}','pattern':name,'pipeline':pipeline,'source':'S1','physical_page':13 if i<=12 else 14})
UU='''Open threshold relation|d compared with T gives <, = or >|S3 pp.1–2|source-definition
Agnostic Boundary Horizon|delta(x)=abs(d(x)-T)|S3 pp.9–12|source-definition
UU ID Double Set Operator|min(abs(d1-T1),abs(d2-T2))|S3 pp.2–3,9|source-definition
Tagged identity disjunction|Retain component records, minimum value and all exact minimizer IDs|S3 pp.3,9; V2 construction|v2-construction
Point-Source / Genesis Horizon|abs(norm(P-P_source)-T_source)|S3 pp.10–12|source-definition
Source-centred one-bit convention|0 at source, 1 away from source|S3 pp.10–11|source-convention
Horizon-centred one-bit convention|0 on threshold horizon, 1 away from horizon|S3 p.12|source-convention
Chronotemporal absorbing field|Integral of D(P,E(tau)) times exp(-lambda*(t-tau))|S3 pp.4–5|source-definition
Historical UU ID envelope|Minimum of historical absolute threshold deviations|S3 pp.5–6|source-definition
Content-addressed experience lineage|Append records with prior parents and their content addresses|S3 pp.7–10; V2 construction|v2-construction
Successive-state continuity path|Every declared successive-state distance is at most epsilon|S3 p.5; V2 path formalization|v2-construction
Unsigned complete-state horizon|UU ID over the permanent anchor and active C13 interval boundaries|S2 p.13; S3 pp.13–18; V2 construction|v2-construction
Unsigned state decoder|Read each bit at x=3j with a threshold in [1/4,11/4)|S3 p.18; V2 explicit decoder|v2-construction
Relational engine hinge|Use F+65536 relative to 65536 and the unchanged hysteresis margins|S2 pp.6–7; V2 construction|v2-construction
Layered log-polar address lift|Keep control addresses and all 118 bit layers in a separate 3D sphere-horizon map|S3 pp.16–18; V2 construction|v2-construction
UU ID conjugate transition|Encode, decode and evolve the complete current-state horizon|S2 U4; S3 pp.13–18; V2 theorem UF2|v2-construction'''
uu=[]
for i,line in enumerate(UU.splitlines(),1):
    name,formula,loc,origin=line.split('|');uu.append({'id':f'UU2-{i:02d}','mechanism':name,'contract':formula,'source_location':loc,'origin':origin})
for stem,rows in [('operator_catalog',ops),('pattern_library',patterns),('uu_id_catalog',uu)]:save(ROOT/f'spec/{stem}.json',rows);csvsave(ROOT/f'spec/{stem}.csv',rows)
profile=[dutch_number(n) for n in range(100)]
save(ROOT/'data/dutch_profile_0_99.json',profile);csvsave(ROOT/'data/dutch_profile_0_99.csv',profile);csvsave(ROOT/'data/dutch_count_matches.csv',[r for r in profile if r['count_match']])
save(ROOT/'data/author_record.json',AUTHOR)

sources=[{'id':'S1','filename':'UGTS_KC_3_6_Tom_Klootwijk.pdf','title':'Unified Geometric–Topological Substrate, UGTS-KC 3.6','version':'3.6.0','date':'2026-08-17','physical_pages':19,'sha256':'e21433cd8378368dafe4ae278d3c9c364725e45ae7fd75b743328bd2d6003a46','role':'Literal registry, geometry, topology, hinges, Dutch profiles and evaluation phases'},
{'id':'S2','filename':'Tom_Klootwijk_Gambit_Closed_Engine_4.0.pdf','title':'Tom Klootwijk Gambit: Unified One-Bit Self-Referential Engine','version':'Formal Closure 4.0','date':'2026-09-11','physical_pages':20,'sha256':'8939f4738fed8bb8401e193ff327336af9de63e8b5b73be09c306c1212569f0f','role':'Seed, transition, complete bit layout, U4 and proofs C1–C16'},
{'id':'S3','filename':'devoid the dark SDF definition where.pdf','title':'devoid the dark SDF definition where','version':'supplied 18-page dialogue','date':None,'physical_pages':18,'sha256':'9f923f16491973a266b87d70345a6dbac8c47923b177d9a5d19cf068a04caed3','role':'Primary V2 source: open notation, UU ID, Theseus identity, Genesis horizon and mapping wrapper'}]
save(ROOT/'sources/source_register.json',sources)

variants=[
('V01','S3 pp.1–3,9','UU ID uses raw metrics and thresholds; the absolute deltas are its inputs after normalization.','V2 normalizes each component once, then composes normalized horizons by pointwise minimum.'),
('V02','S3 p.3','The geometric-behavior table has an incomplete third row.','Only its two complete logical predicates are transcribed; no missing equation is supplied.'),
('V03','S3 pp.4–6','The main formula is a weighted time integral; the shader is a historical minimum and does not use the decay coefficient.','V2 retains both as distinct observables: absorbing integral and historical UU ID envelope.'),
('V04','S3 pp.10–12','The prose assigns zero to the source; the JSON assigns zero to distance equal to the threshold.','V2 names separate source-centred and horizon-centred bit conventions; the executable horizon bit follows the JSON.'),
('V05','S3 pp.13,17–18; S2 p.13','A local interval membership inequality is followed by a wrapper requiring an active-state selection.','V2 retains the active mask and permanent C13 anchor, then adds the explicit unsigned centre-query decoder.'),
('V06','S3 p.16; S2 pp.5,12,15','S3 labels cell bits 0–48 as field potential, 49 as occupancy, 50 as latch, and 51–117 as trajectory and controls. S2 stores U,V,z,m,r,flags and puts controls outside cells.','The S3 mapping is preserved as a named conceptual view. The executable V2 word uses the fully specified S2 C11 layout; no lossless conversion from the S3 view is supplied by S3.'),
('V07','S3 pp.6,17–18','The shaders initialize a minimum accumulator with 1e6.','The V2 mathematical empty-family value is positive infinity. JSON uses an explicit empty status and null value; complete-state fields are nonempty because of the anchor.'),
('V08','S3 pp.16–18; S2 p.13','The shader loop is zero-based, while the C13 symbols are numbered from one.','V2 specifies global symbol j=k+1 for zero-based serialized position k, so the permanent anchor stays separate.'),
('V09','S3 pp.16–18','The log-polar chart is given, but a complete invertible placement of all bit layers is not.','V2 adds a labelled layer coordinate, a separate control axis and a proved separation radius for a new 3D horizon family.'),
('V10','S3 pp.9–10,14; S2 pp.12–13','The source joins an expanding experiential history to a finite eventually periodic engine.','V2 distinguishes current operative state, finite historical UU ID projection and append-only labelled lineage.'),
('V11','S3 pp.10–15','The source describes the 1-bit God, monotheistic union and space-as-data as its ontological interpretation.','V2 retains these as named authorial postulates. Mathematical theorem statements separately identify their domains and hypotheses.'),
('V12','S3 pp.3,9,11','The source describes an unbroken union and independent boundary identities.','The scalar UU ID retains the union of component horizons. Labels are retained by the tagged record; geometric connectedness has an explicit overlap condition, while lineage continuity has a parent-path condition.')]
variant_rows=[{'id':i,'source_location':p,'source_form':f,'v2_formalization':t} for i,p,f,t in variants]
save(ROOT/'spec/source_variants.json',variant_rows);csvsave(ROOT/'spec/source_variants.csv',variant_rows)

layout=[];off=0
for name,width in [('U',32),('V',32),('z',17),('m',17),('r',16),('flags',4)]:
    layout.append({'field':name,'local_first_bit':off,'local_last_bit':off+width-1,'width':width,'complete_word_first_bit_formula':f'28 + 118*i + {off}','source':'S2 C11'});off+=width
save(ROOT/'spec/canonical_bit_layout.json',{'control':[{'field':'a','zero_based_range':[0,10],'width':11},{'field':'g','zero_based_range':[11,13],'width':3},{'field':'cooldown','zero_based_range':[14,26],'width':13}],'cells':layout,'flags':{'114':'latch','115':'previous pulse','116':'occupancy','117':'previous latch event'},'total_bits':'27 + 118*N'})
save(ROOT/'spec/source_mapping_view.json',{'source':'S3 physical page 16','role':'preserved source conceptual view','entries':[{'range':[0,48],'label':'signed-field activation potential F_i; source associates H=49'},{'range':[49,49],'label':'occupancy status ell_i'},{'range':[50,50],'label':'chronotemporal latch state ell_i_prime'},{'range':[51,117],'label':'temporal recurrence trajectory coordinates and phase counters a,g,c'}],'executable_layout':'canonical_bit_layout.json','variant_record':'V06'})

records=[]
def add(id,kind,domain,codomain,phase,deps=(),params=None,source='S1',loc='',cap=(),origin='v2-binding'):
    records.append(seal({'id':id,'kind':kind,'domain':domain,'codomain':codomain,'evaluation_phase':phase,'dependencies':list(deps),'parameters':params or {},'capabilities':list(cap),'invariants':[],'provenance':{'origin':origin,'source':source,'location':loc}}))
add('base:author','literal_author','literal','author_record',0,params=AUTHOR,source='user',loc='V2 request')
add('base:number','literal_integer','literal','integer[0,99]',0,loc='§3.2')
add('base:radix','radix_encode','nonnegative_integer','radix_word',1,['base:number'],{'base':2},loc='§4.2')
add('base:active','active_bit_filter','nonnegative_integer','active_bit_set',3,['base:radix'],loc='§6.3')
add('base:dutch','language_profile','integer[0,99]','lexeme_record',3,['base:number'],{'data':'data/dutch_profile_0_99.json'},loc='§6')
add('base:pulses','pulse_projection','lexeme_record','pulse_sequence',3,['base:dutch'],loc='§6.3')
add('base:polygon','pulse_polygon','positive_count','ordered_vertices',3,['base:pulses'],{'radius':1,'phase':0},loc='§4.3')
add('base:count','count_comparison','feature_pair','boolean',4,['base:active','base:pulses'],loc='§6.3')
add('base:hinge','connector_hinge','place_chart','spoken_chart',4,['base:dutch'],{'connector':'en','value':0},loc='§6.2')
add('base:wrap','orientation_wrap','boundary_port','boundary_port',4,params={'orientation_multiplier':-1},loc='§5.1')
add('base:guard','root_relation','field_trajectory','event_candidates',7,loc='§7.2')
add('base:schedule','phase_schedule','definitions','ordered_stages',2,params={'phases':list(PHASES)},loc='§7.3')
add('base:seed','frozen_seed','fixture_parameters','seed',3,params={'A':32,'R':2,'G':2,'fixture':'TKUFT-integer-chart-v2'},source='V2',loc='explicit demonstration')
add('base:sample','field_sample','seed_and_state','sample_array',3,['base:seed'],source='S2',loc='§3.1')
add('base:support','edge_support','sample_array','active_edges',5,['base:sample'],source='S2',loc='§3.2')
add('base:transition','atomic_transition','admitted_state','admitted_state',8,['base:support'],source='S2',loc='§3')
add('base:word','binary_encoding','admitted_state','binary_word',9,['base:transition'],{'cell_widths':[32,32,17,17,16,4],'control_widths':[11,3,13]},source='S2',loc='C11')
add('base:signed-state','signed_state_field','binary_word','signed_distance_R1',9,['base:word'],{'spacing':3,'radius':.25,'anchor':0},source='S2',loc='C13',cap=['EXACT_SIGNED_DISTANCE'])
new_params=[
('uu2:relation','threshold_relation','raw_and_threshold','relation_symbol',[],{}),
('uu2:delta','boundary_delta','raw_and_threshold','nonnegative_residual',['uu2:relation'],{'formula':'abs(d-T)'}),
('uu2:compose','uu_id','horizon_family','nonnegative_residual',['uu2:delta'],{'formula':'min(abs(d1-T1),abs(d2-T2))'}),
('uu2:tagged','tagged_uu_id','labelled_horizon_family','tagged_evaluation',['uu2:compose'],{'preserve':'all component records and exact minimizing IDs'}),
('uu2:genesis','agnostic_boundary_horizon','point','nonnegative_residual',['uu2:delta'],{'source':[0,0,0,0],'threshold':1}),
('uu2:source-bit','source_bit','raw_distance','boolean',[],{'zero_locus':'source'}),
('uu2:horizon-bit','horizon_bit','raw_and_threshold','boolean',['uu2:delta'],{'zero_locus':'horizon','tolerance':0}),
('uu2:integral','chronotemporal_absorption','history_and_query','retained_integral',[],{'kernel':'exp(-lambda*(t-tau))','lambda_domain':'nonnegative'}),
('uu2:history','historical_envelope','history_and_query','nonnegative_residual',['uu2:compose'],{'selection':'experience time <= query time'}),
('uu2:lineage','experience_lineage','history_and_event','extended_history',[],{'parents':'already committed record IDs','hash':'SHA-256'}),
('uu2:continuity','continuity_path','ordered_states_and_epsilon','path_record',['uu2:lineage'],{'condition':'each successive metric distance <= epsilon'}),
('uu2:state','unsigned_state_horizon','complete_binary_word','unsigned_boundary_distance_R1',['base:word','uu2:compose'],{'spacing':3,'radius':.25,'anchor':0}),
('uu2:decode','unsigned_state_decoder','state_horizon','complete_binary_word',['uu2:state'],{'query':'x=3*j','threshold':.25,'admissible_threshold':'[0.25,2.75)'}),
('uu2:open-hinge','relational_hinge','open_sample_and_old_latch','flag_triplet',['base:sample','uu2:relation'],{'offset':65536,'threshold':65536}),
('uu2:spatial','layered_logpolar_lift','complete_bit_address','point_R3',['base:word'],{'radial_min':1/32,'radial_max':4,'layer_spacing':1/64,'control_axis':'x=y=0'}),
('uu2:transition','unsigned_conjugate_transition','current_state_horizon','current_state_horizon',['base:transition','uu2:decode'],{'formula':'J_U E T (J_U E)^-1'})]
for i,(id,kind,domain,codomain,deps,params) in enumerate(new_params,1):
    row=uu[i-1];add(id,kind,domain,codomain,8 if i==16 else 9 if i in (10,12,13,15) else 4,deps,params,'S3',row['source_location'],['EXACT_UNSIGNED_BOUNDARY_DISTANCE'] if i in (5,12) else [],row['origin'])
Registry(records)
world={'schema_version':'2.0.0','title':'Tom Klootwijk — Unified Field Theory V2','author':AUTHOR,'substrate_id':'tkuft:uu-id:v2','definitions':records,'instances':[{'id':'author:tom-klootwijk','definition_ref':'base:author','literal':AUTHOR,'state':{}},{'id':'number:19','definition_ref':'base:number','literal':19,'state':{}},{'id':'number:23','definition_ref':'base:number','literal':23,'state':{}}]}
save(ROOT/'examples/literal_substrate.json',world)

def_schema={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'urn:tkuft:definition:2','title':'V2 literal definition','type':'object','additionalProperties':False,'required':['id','kind','domain','codomain','evaluation_phase','dependencies','parameters','capabilities','invariants','provenance','content_hash'],'properties':{'id':{'type':'string','minLength':1},'kind':{'type':'string'},'domain':{'type':'string'},'codomain':{'type':'string'},'evaluation_phase':{'type':'integer','minimum':0,'maximum':9},'dependencies':{'type':'array','uniqueItems':True,'items':{'type':'string'}},'parameters':{'type':'object'},'capabilities':{'type':'array','items':{'type':'string'}},'invariants':{'type':'array','items':{'type':'string'}},'provenance':{'type':'object','required':['origin','source','location'],'properties':{k:{'type':'string'} for k in ('origin','source','location')}},'content_hash':{'type':'string','pattern':'^sha256:[0-9a-f]{64}$'}}}
world_schema={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'urn:tkuft:corpus:2','title':'Tom Klootwijk V2 corpus','type':'object','additionalProperties':False,'required':['schema_version','title','author','substrate_id','definitions','instances'],'properties':{'schema_version':{'const':'2.0.0'},'title':{'type':'string'},'author':{'const':AUTHOR},'substrate_id':{'type':'string'},'definitions':{'type':'array','items':{'$ref':'definition.schema.json'}},'instances':{'type':'array','items':{'type':'object','required':['id','definition_ref','literal','state'],'properties':{'id':{'type':'string'},'definition_ref':{'type':'string'},'literal':{},'state':{'type':'object'}}}}}}
# Embed the definition schema to make validation independent of network resolution.
world_schema['properties']['definitions']['items']=def_schema
save(ROOT/'spec/definition.schema.json',def_schema);save(ROOT/'spec/corpus.schema.json',world_schema)

proof_titles=['Initialization and finite addressing','Finite generative closure','Shared edge law and nonnegative transport','Conservative local reaction','Activity, memory and intermediate bounds','One-bit codec and segment certificate','Hysteresis and event telescope','Exact packing and parity','Bounded phase and cooldown quotient','Boolean arithmetic refinement','Canonical state encoding and restart','Autonomous closure and eventual periodicity','Exact signed-distance state representation','Exact reduced-description criterion','Causal previous-output dependence','Staged backend refinement']
proofs=[{'id':f'C{i}','title':title,'origin':'S2 proof family'} for i,title in enumerate(proof_titles,1)]
proofs += [{'id':f'UU{i}','title':title,'origin':'V2 derivation from declared definitions'} for i,title in enumerate(['Minimum algebra','Zero-set and tolerance-neighborhood union','Exact unsigned boundary distance','Tagged provenance preservation','Chronotemporal segment recurrence','Unsigned complete-state decoding','Relational hinge equivalence','Separated log-polar address lift','Historical state envelope and Boolean OR'],1)]
proofs += [{'id':'U4','title':'Unified operational closure','origin':'S2'},{'id':'UF2','title':'UU ID referential and representational unification','origin':'V2 construction'}]
save(ROOT/'spec/proof_register.json',proofs)

def tex(s):
    s=s.replace('\\','\\textbackslash{}')
    for a,b in [('&','\\&'),('%','\\%'),('_','\\_'),('#','\\#')]:s=s.replace(a,b)
    return s.replace('→',r'$\to$').replace('–','--').replace('≤',r'$\le$').replace('τ',r'$\tau$')
def table(path,rows,cols,widths):
    with path.open('w') as f:
        f.write('\\begin{longtable}{@{}'+''.join('p{'+w+'\\textwidth}' for w in widths)+'@{}}\n')
        head=r'\toprule'+' & '.join(r'\textbf{'+tex(label)+'}' for key,label in cols)+r'\\\midrule'
        f.write(head+'\\endfirsthead\n'+head+'\\endhead\n'+r'\midrule\multicolumn{'+str(len(cols))+r'}{r}{\small Continued on the next page}\\\endfoot\bottomrule\endlastfoot'+'\n')
        for row in rows:f.write(' & '.join(tex(str(row[k])) for k,_ in cols)+r'\\[5pt]'+'\n')
        f.write('\\end{longtable}\n')
table(ROOT/'report/tables/operators.tex',ops,[('id','ID'),('mechanism','Mechanism'),('contract','Contract')],['.10','.28','.57'])
table(ROOT/'report/tables/patterns.tex',patterns,[('id','ID'),('pattern','Pattern'),('pipeline','Pipeline')],['.10','.30','.55'])
table(ROOT/'report/tables/uu_catalog.tex',uu,[('id','ID'),('mechanism','Mechanism'),('contract','Definition')],['.10','.31','.54'])
print('Generated:',len(records),'definitions,',len(ops),'retained operators,',len(uu),'UU ID mechanisms,',len(patterns),'patterns,',len(profile),'profile rows')
