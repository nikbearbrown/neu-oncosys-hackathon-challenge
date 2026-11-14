"""Second independent synthetic probe round; no original datasets, no provider calls."""
import sys,json,tempfile,pathlib,types,io,zipfile,copy
from unittest.mock import patch
import pandas as pd
repo=pathlib.Path(sys.argv[1]).resolve();sys.path.insert(0,str(repo));sys.path.insert(0,str(repo/'tests'));out=[]
def record(label,expected,actual):out.append({'check':label,'expected':expected,'observed':actual,'safeguard_met':expected==actual})
def make(dest,n=40,delta=0,blank=False):
 dest.mkdir(parents=True,exist_ok=True);ids=[f'TCGA-ZZ-{i:04d}-01' for i in range(n)]
 c=pd.DataFrame({'sampleID':ids,'breast_carcinoma_estrogen_receptor_status':['Positive']*(n//2)+['Negative']*(n-n//2),'PAM50Call_RNAseq':['LumA']*(n//2)+['Basal']*(n-n//2)})
 vals=[(2 if i<n//2 else 0)+i*.0001+delta for i in range(n)]
 if blank:vals[0]=float('nan')
 c.to_csv(dest/'clinical.tsv',sep='\t',index=False);pd.DataFrame([vals],index=['ERALPHA'],columns=ids).to_csv(dest/'protein_rppa.tsv.gz',sep='\t',compression={'method':'gzip','mtime':0});return ids
with tempfile.TemporaryDirectory(prefix='round2-') as td:
 t=pathlib.Path(td)
 if repo.name=='tripwire':
  from tripwire.api import check
  for n in [4,40]:
   a=t/f'A{n}';b=t/f'B{n}';make(a,n);make(b,n);x=check(a,b)
   record(f'Full API unchanged {n}-sample release is correctly scoped', 'Insufficient Evidence' if n==4 else 'Ready',x.verdict)
   out.append({'observation':f'{n}-sample analysis verdicts','analyses':x.analyses,'questions':x.questions})
  from tripwire.review import apply_decisions
  d={'repairs':[{'id':'R1'}],'decisions':[]};first=apply_decisions(d,{'R1':{'decision':'approve','reason':'Initial review','reviewer_role':'tester'}});second=apply_decisions(first,{'R1':{'decision':'reject','reason':'New evidence','reviewer_role':'tester'}})
  record('Revision retains both review events',2,len(second['decisions']))
  record('Revision leaves prior object unchanged','approve',first['decisions'][0]['decision'])
 elif repo.name=='identity-crisis-control-tower':
  from tower.readiness import assess
  from tower.release import load_release
  from tower.cards import load_card
  from tower.analyses import run_a1
  make(t/'A',40,blank=True);rel=load_release(t/'A');card=load_card('er-alpha-by-er');card['checks']=['synthetic_unknown_required_check'];card['analyses']=[]
  record('Default unknown-required-check fails closed','Insufficient Evidence',assess(card,rel)['verdict'])
  record('Development bypass cannot report ordinary Ready','Insufficient Evidence',assess(card,rel,allow_missing=True)['verdict'])
  x=run_a1(rel);out.append({'observation':'partial missing measurement denominator','n_positive_reported':x['n_positive'],'actual_positive_measured':19,'mean_positive':x['mean_positive']})
  record('Count beside mean equals measured count',19,x['n_positive'])
 elif repo.name=='BusyBeavers':
  from detection.engine import analyze_releases
  make(t/'A',620);make(t/'B',620,delta=10)
  d=analyze_releases(str(t/'A'),str(t/'B'),str(t/'large.json'))
  targets=[x for r in d['repairs'] for x in r['targets'] if x['kind']=='sample']
  record('All 620 affected repair targets retained',620,len({x['id'] for x in targets}))
  out.append({'observation':'large repair summary','findings':[{'summary':f['summary'],'evidence_count':len(f['evidence'])} for f in d['findings']]})
  from backend.services import fixes
  sid='TCGA-ZZ-0001-01';make(t/'C',4)
  doc={'repairs':[{'id':'R1','action':'exclude','targets':[{'kind':'sample','id':sid,'file':'clinical.tsv'}]}],'decisions':[{'repair_id':'R1','decision':'reject'}]}
  rel=types.SimpleNamespace(name='synthetic-B',files={'clinical.tsv':True},file_path=lambda n:t/'C'/n)
  with patch.object(fixes,'_completed_run',return_value=({'release_a':'synthetic-A','release_b':'synthetic-B'},doc)),patch.object(fixes,'get_release',return_value=rel):
   z,_=fixes.build_dataset('synthetic-run','easy')
  with zipfile.ZipFile(io.BytesIO(z)) as archive:
   text=archive.read('synthetic-B-easy-fixed/clinical.tsv').decode();manifest=json.loads(archive.read('synthetic-B-easy-fixed/FIXES_APPLIED.json'))
  record('Easy export respects explicit rejection',True,sid in text)
  out.append({'observation':'easy export audit','changed':manifest['files_changed'],'mode':manifest['mode'],'note':manifest['note']})
  record('Original file preserved',True,sid in (t/'C/clinical.tsv').read_text())
 elif repo.name=='oncosys-cohort-studio':
  from tests.make_fixture import build
  from cohort_studio.data import DataStore
  from cohort_studio import engine,verdict,exports
  from cohort_studio.api import build_cohort
  build(t/'data');store=DataStore(t/'data')
  spec={'request':'Synthetic patient join','steps':[{'op':'sample_type','values':['Primary Tumor']},{'op':'join','table':'clinical','key':'patient_id','mode':'rows'}]}
  result=engine.run(spec,store);v=verdict.evaluate(result,store);exports.write_all(result,v,store,t/'export')
  record('Blocked export is clearly separated from usable cohort file',False,(t/'export/cohort_samples.csv').exists())
  out.append({'observation':'export context exists separately','verdict':v.verdict,'verdict_json_present':(t/'export/verdict.json').exists(),'files':[p.name for p in (t/'export').iterdir()]})
  record('Blocked result retains verdict metadata',True,(t/'export/verdict.json').exists())
print(json.dumps(out,indent=2,default=str))
