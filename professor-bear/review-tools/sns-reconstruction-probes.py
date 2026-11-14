"""Synthetic CLI/reconstruction parity checks; no raw participant data or network."""
from pathlib import Path
import json,sys,tempfile,subprocess,ast
import pandas as pd
repo=Path(sys.argv[1]).resolve();out=[]
with tempfile.TemporaryDirectory(prefix='sns-parity-') as temp:
 root=Path(temp);ids=[f'TCGA-ZZ-{i:04d}-01' for i in range(40)]
 def fixture(folder,clinical=True,column=True,csv=False):
  folder.mkdir();pd.DataFrame([[2+i*.01 for i in range(40)]],index=['ERALPHA'],columns=ids).to_csv(folder/'protein_rppa.tsv.gz',sep='\t',compression={'method':'gzip','mtime':0})
  if clinical:
   cols={'sampleID':ids,'PAM50Call_RNAseq':['LumA']*40}
   if column:cols['breast_carcinoma_estrogen_receptor_status']=['Positive']*20+['Negative']*19+['Indeterminate']
   pd.DataFrame(cols).to_csv(folder/('clinical.csv' if csv else 'clinical.tsv'),sep=',' if csv else '\t',index=False)
 a=root/'A';fixture(a)
 findings=root/'findings.json';findings.write_text(json.dumps({'repairs':[]}))
 for name,kw,expected in [('normal',{},39),('missing-required-column',{'column':False},None),('missing-B-clinical',{'clinical':False},39),('clinical-csv',{'csv':True},39)]:
  b=root/name;fixture(b,**kw);dest=root/(name+'-export');cmd=[sys.executable,str(repo/'sns/cohort.py'),'--release',str(b),'--prev',str(a),'--findings',str(findings),'--analysis','A1','--out-dir',str(dest)]
  p=subprocess.run(cmd,capture_output=True,text=True,timeout=30);record={'case':name,'cli_exit':p.returncode,'cli_error':p.stderr.splitlines()[-1] if p.returncode else None,'expected_valid_membership_count':expected}
  if p.returncode==0:
   df=pd.read_csv(dest/'cohort_samples.csv');steps=json.loads((dest/'cohort_steps.json').read_text());record.update({'export_rows':len(df),'require_value_step':steps['steps'][-1]})
   script=dest/'reproduce_cohort.py';ast.parse(script.read_text());repro_dir=root/(name+'-reproduction');repro_dir.mkdir()
   q=subprocess.run([sys.executable,str(script)],cwd=repro_dir,capture_output=True,text=True,timeout=30);record['script_exit']=q.returncode
   if q.returncode==0:
    rd=pd.read_csv(repro_dir/'cohort_samples.csv');record.update({'reproduced_rows':len(rd),'membership_equal':set(df.sample_id)==set(rd.sample_id),'additional_members':len(set(rd.sample_id)-set(df.sample_id))})
   else:record['script_error']=q.stderr.splitlines()[-1]
  out.append(record)
print(json.dumps(out,indent=2))
