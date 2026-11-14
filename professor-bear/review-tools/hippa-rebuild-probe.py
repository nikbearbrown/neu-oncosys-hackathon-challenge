import os,sys,tempfile,json,subprocess
from pathlib import Path
b=Path(__file__).resolve().parent;root=b/'HIPPA-cratic';sys.path.insert(0,str(root))
from cohort_studio.export import rebuild_script,cohort_definition
from cohort_studio.engine import run
p=Path(tempfile.mkdtemp(dir=b/'tmp'));a=p/'a';c=p/'b';a.mkdir();c.mkdir()
(a/'sample_manifest.csv').write_text('sample_id,patient_id,sample_type\nS1,P1,Biopsy\nS2,P2,Blood\n')
(c/'sample_manifest.csv').write_text('sample_id,patient_id,sample_type\nS3,P3,Biopsy\n')
os.environ['ONCOSYS_DATA']=str(a)
df,res=run([]);definition=cohort_definition([],'Invented review cohort',res)
script=root/'review_rebuild_synthetic.py';script.write_text(rebuild_script([],'Invented review cohort'))
outputs=[]
for label,d in [('same_source_control',a),('different_source',c)]:
 env=dict(os.environ,ONCOSYS_DATA=str(d));r=subprocess.run([sys.executable,str(script)],cwd=p,env=env,capture_output=True,text=True,timeout=20)
 outputs.append({'case':label,'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'exported_csv':(p/'cohort_samples.csv').read_text() if (p/'cohort_samples.csv').exists() else None})
print(json.dumps({'original_rows':len(df),'recorded_source':definition['data_dir'],'recorded_hashes_present':bool(definition['input_sha256']),'runs':outputs},indent=2))
