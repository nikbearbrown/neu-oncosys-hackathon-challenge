"""Targeted local probes; synthetic fixtures and mocked provider transports only."""
import sys,json,tempfile,pathlib,copy,subprocess,ast
from unittest.mock import patch
import pandas as pd
repo=pathlib.Path(sys.argv[1]).resolve();sys.path.insert(0,str(repo));out=[]
def record(label,expected,actual):out.append({'check':label,'expected':expected,'observed':actual,'safeguard_met':expected==actual})
def make(dest,n=40,positive_delta=0):
 dest.mkdir(parents=True,exist_ok=True);ids=[f'TCGA-ZZ-{i:04d}-01' for i in range(n)]
 c=pd.DataFrame({'sampleID':ids,'breast_carcinoma_estrogen_receptor_status':['Positive']*(n//2)+['Negative']*(n-n//2),'PAM50Call_RNAseq':['LumA']*(n//2)+['Basal']*(n-n//2)})
 vals=[(2+positive_delta if i<n//2 else 0)+i*.0001 for i in range(n)]
 c.to_csv(dest/'clinical.tsv',sep='\t',index=False);pd.DataFrame([vals],index=['ERALPHA'],columns=ids).to_csv(dest/'protein_rppa.tsv.gz',sep='\t',compression={'method':'gzip','mtime':0});return ids
with tempfile.TemporaryDirectory(prefix='round3-') as td:
 t=pathlib.Path(td)
 if repo.name=='sns-cohort-control-tower':
  sys.path.insert(0,str(repo/'sns'))
  from engine.release import load_release
  from engine.diff import compare_releases
  from engine.impact import assess
  from engine.findings import build_document
  reference=repo.parent/'oncosys-hackathon-challenge/data/tcga-brca/reference_analyses.py'
  for n in [4,40]:
   for delta in [0,-10]:
    a=t/f'A{n}{delta}';b=t/f'B{n}{delta}';make(a,n);make(b,n,delta)
    ra=load_release(a);rb=load_release(b,reuse=ra);diff=compare_releases(ra,rb);impact=assess(reference,ra,rb,a,b,diff);doc=build_document(diff,ra,rb,'synthetic-A','synthetic-B',impact,team='Synthetic review')
    brief={'n':n,'positive_delta':delta,'loaded_files':list(rb),'verdict':doc['verdict'],'findings':len(doc['findings']),'analyses':[{k:v for k,v in x.items() if k in ('id','verdict','status','reason','before','after')} for x in doc['analyses']]}
    for x in brief['analyses']:
     for side in ['before','after']:
      if isinstance(x.get(side),dict):x[side].pop('sample_ids',None)
    out.append({'observation':'full engine synthetic result',**brief})
    expected='Insufficient Evidence' if n==4 else ('Ready' if delta==0 else 'Blocked')
    record(f'Full engine {n} samples delta {delta}',expected,doc['verdict'])
  from cohort import _make_reproduce_script
  from engine.cohort import BUILTIN_SPECS,run_cohort
  a=t/'script-A';b=t/'script-B';make(a,40);make(b,40)
  for aid in ['A1','A2']:
   dest=t/aid;dest.mkdir();script=_make_reproduce_script(dest,b,a,BUILTIN_SPECS[aid],[])
   tree=ast.parse(script.read_text());imports=[ast.unparse(x) for x in ast.walk(tree) if isinstance(x,(ast.Import,ast.ImportFrom))]
   assert set(imports)=={'import pandas as pd','from pathlib import Path'},imports
   proc=subprocess.run([sys.executable,str(script)],cwd=dest,capture_output=True,text=True,timeout=30)
   error=proc.stderr.strip().splitlines()[-1] if proc.returncode else None
   out.append({'observation':'generated reproduction script','analysis':aid,'exit':proc.returncode,'error':error,'json_boolean_name_in_ast':any(isinstance(x,ast.Name) and x.id=='true' for x in ast.walk(tree))})
   record(f'{aid} generated script executes',0,proc.returncode)
 elif repo.name=='tripwire':
  from tripwire.release import Release
  from tripwire.analyses import a1_run,a1_compare
  from tripwire.api import check
  make(t/'A',40);make(t/'B',40,.0004)
  before=a1_run(Release(t/'A'));after=a1_run(Release(t/'B'));m=a1_compare(before,after)
  out.append({'observation':'rounding before effect comparison','true_positive_mean_change':.0004,'before_mean':before['mean_positive'],'after_mean':after['mean_positive'],'before_difference':before['difference'],'after_difference':after['difference'],'moved':m.moved,'magnitude':m.magnitude})
  record('Display precision does not erase calculated change',True,after['difference']!=before['difference'])
  full=check(t/'A',t/'B');out.append({'observation':'full pipeline guard','verdict':full.verdict,'analyses':full.analyses})
  from intake_prototype.ai_suggest import suggest_mappings
  calls=[]
  with patch('intake_prototype.ai_suggest.urllib.request.urlopen',side_effect=lambda *a,**kw:calls.append('network')):
   try:suggest_mappings(['sampleID'],40,consent=False)
   except ValueError:pass
  record('No consent means no provider call',[],calls)
 elif repo.name=='oncosys-cohort-studio':
  from tests.make_fixture import build
  from cohort_studio.data import DataStore
  from cohort_studio.api import build_cohort
  from cohort_studio import llm
  build(t/'data');store=DataStore(t/'data')
  spec={'request':'Synthetic patient join','steps':[{'op':'sample_type','values':['Primary Tumor']},{'op':'join','table':'clinical','key':'patient_id','mode':'rows'}]}
  run=build_cohort(spec,store=store,ai='off',write=False)
  out.append({'observation':'default API fix','original_steps':spec['steps'],'returned_steps':run.spec['steps'],'fixes':run.fixes,'first_inflated':any(s.inflated for s in run.first_result.steps),'final_inflated':any(s.inflated for s in run.result.steps),'verdict':run.verdict.verdict,'route':run.route['used']})
  record('Default API preserves proposed operation until acceptance',spec['steps'],run.spec['steps'])
  control=build_cohort(spec,store=store,ai='off',fix=False,write=False)
  record('Explicit fix=False preserves operation',spec['steps'],control.spec['steps'])
  calls=[]
  def own(*a,**kw):calls.append('own');return None
  def hosted(request):calls.append('hosted');return {'spec':copy.deepcopy(spec),'model':'synthetic-mock'}
  with patch.object(llm,'own_model',side_effect=own),patch.object(llm.hosted,'draft',side_effect=hosted):
   llm.draft_spec('Primary tumors',store,ai='off');record('AI-off calls no provider',[],calls.copy());calls.clear()
   _,route=llm.draft_spec('Primary tumors',store,ai='auto');out.append({'observation':'auto routing with mocked providers','calls':calls.copy(),'route':route['used'],'actual_network_calls':0})
 elif repo.name=='BusyBeavers':
  from detection import qa
  marker='TCGA-ZZ-0001-01';note='SYNTHETIC EVIDENCE NOTE'
  doc={'verdict':'Conditional','findings':[{'id':'F01','kind':'missing_data','summary':'Invented finding','evidence':[{'kind':'sample','id':marker,'note':note}]}],'repairs':[],'analyses':[]}
  context=qa.build_context(doc,'Explain F01');encoded=json.dumps(context)
  out.append({'observation':'model context construction','synthetic_id_present':marker in encoded,'synthetic_note_present':note in encoded,'actual_network_calls':0})
  record('Context omits sample identifiers by default',False,marker in encoded)
  record('Known-id check rejects invented citation',True,qa._validate(doc,'See F99',['F99']) is not None)
  record('Known-id check accepts existing citation',None,qa._validate(doc,'See F01',['F01']))
print(json.dumps(out,indent=2,default=str))
