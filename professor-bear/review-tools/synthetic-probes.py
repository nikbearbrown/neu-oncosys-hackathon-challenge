"""Independent synthetic safeguards. Run inside the documented sandbox, never on original data."""
import sys,json,tempfile,pathlib,copy,ast,types
from unittest.mock import patch
repo=pathlib.Path(sys.argv[1]).resolve();sys.path.insert(0,str(repo));sys.path.insert(0,str(repo/'tests'))
out=[]
def check(label,expected,actual):
 out.append({'check':label,'expected':expected,'observed':actual,'safeguard_met':actual==expected})
with tempfile.TemporaryDirectory(prefix='independent-') as td:
 t=pathlib.Path(td)
 if repo.name=='tripwire':
  from tripwire.analyses import Movement
  from tripwire.verdicts import release_verdict,question_verdict
  from tripwire.review import review_status,apply_decisions
  from tripwire.api import check as api
  from conftest import make_release
  m=Movement(False,False,False,True,'one member in each group')
  check('Insufficient unchanged movement is not Ready','Insufficient Evidence',release_verdict(False,m).verdict)
  check('Affected insufficient movement is rejected','Insufficient Evidence',release_verdict(True,m).verdict)
  check('Unexplained movement blocks','Blocked',release_verdict(False,Movement(True,True,False,False,'large change')).verdict)
  d={'findings':[{'id':'F1','needs_human_review':True}],'repairs':[]}
  check('Flagged finding without repair stays open',['F1'],review_status(d)['open'])
  d['repairs']=[{'id':'R1','addresses':['F1']}]
  d=apply_decisions(d,{'R1':{'decision':'request_more_evidence','reason':'Need source','reviewer_role':'independent tester'}})
  check('Request-more-evidence stays unresolved',['F1'],review_status(d)['open'])
  make_release(t/'A',n=3);make_release(t/'B',n=3)
  result=api(t/'A',t/'B')
  check('End-to-end unchanged tiny release is not Ready',False,result.verdict=='Ready')
  out.append({'observation':'tiny release verdicts','overall':result.verdict,'analyses':result.analyses})
  check('Empty readiness checks do not pass','Insufficient Evidence',question_verdict([]).verdict)
 elif repo.name=='identity-crisis-control-tower':
  from tower import review
  from tower.readiness import assess
  from tower.release import load_release
  from tower.cards import load_card
  import synth
  rel=load_release(synth.write(t/'A',synth.frames()))
  ready=assess(load_card('er-alpha-by-er'),rel)
  signed=review.signed(ready,None,{}, {},'Synthetic Reviewer','reviewer','Approve use as stated','Synthetic test only')
  message=review.save(t/'saved',signed,{'findings':[],'repairs':[]},None,t/'missing-validator.py')
  check('Missing validator prevents validated sign-off artifacts',False,(t/'saved/readiness.signed.json').exists())
  out.append({'observation':'save return explicitly discloses missing validator','message':message})
  card=load_card('er-alpha-by-er');card['checks']=['synthetic_unknown_required_check']
  # Isolate missing-registration handling: the card schema may use required_checks, inspect before treating as end-to-end.
  from tower.checks import run_checks
  import inspect
  out.append({'observation':'pending-check test deferred','reason':'Requires card-shape-specific construction; no runtime claim made'})
  with patch('tower.readiness.conclusion',side_effect=ValueError('synthetic robustness failure')):
   result=assess(load_card('er-alpha-by-er'),rel)
  check('Robustness exception has explicit error state',True,'synthetic robustness failure' in json.dumps(result))
 elif repo.name=='BusyBeavers':
  from cfw.compare import compare
  from detection.engine import analyze_releases
  for n in ['A','B']:(t/n).mkdir()
  result=analyze_releases(str(t/'A'),str(t/'B'),str(t/'empty.json'))
  check('Empty release directories are not Ready',False,result['verdict']=='Ready')
  out.append({'observation':'empty release analyses','analyses':result['analyses']})
  for n in ['A','B']:
   (t/n/'clinical.tsv').write_bytes(b'')
   (t/n/'protein_rppa.tsv.gz').write_bytes(b'')
  result=analyze_releases(str(t/'A'),str(t/'B'),str(t/'invalid.json'))
  check('Identical zero-byte required inputs are not Ready',False,result['verdict']=='Ready')
  # Test the actual detector on valid synthetic releases, with a sign-changing target shift.
  import pandas as pd
  ids=[f'TCGA-ZZ-{i:04d}-01' for i in range(1,41)]
  c=pd.DataFrame({'sampleID':ids,'breast_carcinoma_estrogen_receptor_status':['Positive']*20+['Negative']*20,'PAM50Call_RNAseq':['LumA']*20+['Basal']*20})
  for n in ['C','D']:
   (t/n).mkdir();c.to_csv(t/n/'clinical.tsv',sep='\t',index=False)
   vals=([float(i)/100+2 for i in range(20)]+[float(i)/100 for i in range(20)])
   if n=='D':vals=[v-10 if i<20 else v for i,v in enumerate(vals)]
   pd.DataFrame([vals],index=['ERALPHA'],columns=ids).to_csv(t/n/'protein_rppa.tsv.gz',sep='\t')
  result=analyze_releases(str(t/'C'),str(t/'D'),str(t/'shift.json'))
  check('Sign-changing target shift is Blocked','Blocked',result['verdict'])
  out.append({'observation':'shift analyses','analyses':result['analyses'],'finding_count':len(result['findings'])})
 elif repo.name=='oncosys-cohort-studio':
  from tests.make_fixture import build
  from cohort_studio.data import DataStore
  from cohort_studio import engine,verdict,exports
  from cohort_studio.parse import parse_request
  build(t/'data');(t/'data/sources.csv').unlink()
  store=DataStore(t/'data');spec=parse_request('primary tumors with clinical data',store);result=engine.run(spec,store)
  v=verdict.evaluate(result,store)
  checks=[c for c in v.checks if 'frozen checksums' in c.name]
  check('Absent expected checksum is unknown','unknown',checks[0].status)
  out.append({'observation':'unknown checksum detail','detail':checks[0].detail,'overall_verdict':v.verdict,'clinical_verified':store.file_status['clinical.tsv']['verified']})
  normal=exports.reproduce_script(result,store);ast.parse(normal)
  check('Ordinary generated reproduction script parses',True,True)
  for text in ['A request mentioning triple quotes: """', 'First line\n"""\nreview_marker = "injected-data-not-code"\n"""']:
   bad=copy.deepcopy(result);bad.spec['request']=text;generated=exports.reproduce_script(bad,store)
   try:
    tree=ast.parse(generated)
    assigned=any(isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='review_marker' for x in n.targets) for n in tree.body)
    check('Request text cannot become executable statement',False,assigned)
   except SyntaxError as e:
    check('Quoted request still produces valid Python',True,False)
  out.append({'observation':'generated malformed/injected scripts were parsed only, never executed'})
 elif repo.name=='sns-cohort-control-tower':
  from sns.engine.impact import verdict_for
  from sns.engine.release import load_layer
  from sns.engine.cohort import parse_repairs,_apply_file_repairs
  import pandas as pd
  check('No detected finding does not override undersized group','Insufficient Evidence',verdict_for([],{'n_positive':1,'difference':1},{'n_positive':1,'difference':1})[0])
  check('Unexplained sign change is blocked','Blocked',verdict_for([],{'n_positive':20,'difference':1},{'n_positive':20,'difference':-1})[0])
  check('Detected sign change is blocked','Blocked',verdict_for(['F1'],{'n_positive':20,'difference':1},{'n_positive':20,'difference':-1})[0])
  for n in [1,10,11]:
   f=t/f'wide-{n}.tsv';pd.DataFrame([[1.]*n],index=['ERALPHA'],columns=[f'TCGA-ZZ-{i:04d}-01' for i in range(n)]).to_csv(f,sep='\t')
   check(f'Valid {n}-sample wide matrix is recognized',True,load_layer(f) is not None)
  sid='TCGA-ZZ-0001-01';f='clinical.tsv';pd.DataFrame({'sampleID':[sid],'value':[1]}).to_csv(t/f,sep='\t',index=False)
  d={'repairs':[{'id':'R1','action':'exclude','targets':[{'kind':'sample','id':sid,'file':f}]}],'decisions':[{'repair_id':'R1','decision':'reject'}]}
  rep=parse_repairs(d);working,_,_= _apply_file_repairs({sid},t,f,rep)
  check('Rejected exclusion is not applied',True,sid in working)
  d['repairs'][0]['action']='flag_for_review';d['decisions']=[]
  working,_,applied=_apply_file_repairs(set(),t,f,parse_repairs(d))
  check('Flag-for-review does not restore absent record',False,sid in working)
  out.append({'observation':'flag repair actions','actions':applied})
print(json.dumps(out,indent=2,default=str))
