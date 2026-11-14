"""Validate selected supplemental source findings using invented data only."""
from pathlib import Path
from unittest.mock import patch
import sys,tempfile,json,subprocess,ast
import pandas as pd
repo=Path(sys.argv[1]).resolve();sys.path.insert(0,str(repo));out=[]
def rec(name,expected,actual):out.append({'check':name,'expected':expected,'observed':actual,'safeguard_met':expected==actual})
with tempfile.TemporaryDirectory(prefix='supplement-') as td:
 t=Path(td)
 if repo.name=='BusyBeavers':
  from cfw.diff import diff_file
  from cfw.fingerprint import rows_close
  from detection.engine import analyze_releases
  a=pd.DataFrame({'value':[1.0,2.0]},index=['synthetic-1','synthetic-2'])
  for duplicate_value in [1.0,99.0]:
   b=pd.concat([a,pd.DataFrame({'value':[duplicate_value]},index=['synthetic-1'])])
   events=diff_file('synthetic',a,b);rec(f'Repeated identifier with value {duplicate_value} reported',True,any(x['type']=='duplicate_id' for x in events));out.append({'observation':'duplicate-ID events','value':duplicate_value,'events':events})
  x=pd.DataFrame({'value':[1.00001]},index=['synthetic-1']);y=pd.DataFrame({'value':[1.00004]},index=['synthetic-1'])
  rec('Tolerance function rejects difference',False,rows_close(x.iloc[0],y.iloc[0]));rec('Detector reports difference beyond its tolerance',True,bool(diff_file('synthetic',x,y)))
  rec('Within-tolerance noise is quiet',[],diff_file('synthetic',x,x+1e-8))
  rec('Larger change is detected',True,bool(diff_file('synthetic',x,x+.1)))
  ids=[f'TCGA-ZZ-{i:04d}-01' for i in range(40)]
  for folder,v in [(t/'A',1.00001),(t/'B',1.00004)]:
   folder.mkdir();pd.DataFrame({'sampleID':ids,'breast_carcinoma_estrogen_receptor_status':['Positive']*20+['Negative']*20,'PAM50Call_RNAseq':['LumA']*20+['Basal']*20}).to_csv(folder/'clinical.tsv',sep='\t',index=False)
   vals=[v if i==0 else 2+i*.0001 if i<20 else i*.0001 for i in range(40)];pd.DataFrame([vals],index=['ERALPHA'],columns=ids).to_csv(folder/'protein_rppa.tsv.gz',sep='\t',compression={'method':'gzip','mtime':0})
  doc=analyze_releases(str(t/'A'),str(t/'B'),str(t/'findings.json'));out.append({'observation':'full engine quantization probe','verdict':doc['verdict'],'finding_count':len(doc['findings']),'analysis_statuses':[{'id':a['id'],'status':a['status']} for a in doc['analyses']]})
 elif repo.name=='oncosys-cohort-studio':
  from tests.make_fixture import build
  from cohort_studio.data import DataStore
  from cohort_studio import engine,exports
  build(t/'data');store=DataStore(t/'data');spec={'request':'Synthetic primary tumors','steps':[{'op':'sample_type','values':['Primary Tumor']}]};result=engine.run(spec,store);script=t/'reproduce.py';script.write_text(exports.reproduce_script(result,store));ast.parse(script.read_text())
  # Generated source was inspected: pure pandas/pathlib operations and local CSV output.
  for mode in ['unchanged','changed-manifest']:
   if mode=='changed-manifest':
    manifest=t/'data/sample_manifest.csv';df=pd.read_csv(manifest);df.iloc[1:].to_csv(manifest,index=False)
   target=t/(mode+'.csv');p=subprocess.run([sys.executable,str(script),str(t/'data'),str(target)],capture_output=True,text=True,timeout=30)
   out.append({'observation':'reconstruction hash policy','mode':mode,'exit':p.returncode,'warning_printed':'WARNING:' in p.stdout,'output_exists':target.exists(),'output_rows':len(pd.read_csv(target)) if target.exists() else None,'error':p.stderr.splitlines()[-1] if p.returncode else None})
   rec(mode+' strict reconstruction result',mode=='unchanged',p.returncode==0 and target.exists())
print(json.dumps(out,indent=2,default=str))
