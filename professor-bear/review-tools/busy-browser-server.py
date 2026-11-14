from pathlib import Path
import sys
b=Path(__file__).resolve().parent;repo=b/'BusyBeavers';sys.path.insert(0,str(repo))
import pandas as pd
from backend import config
root=b/'busy-browser-fixtures';root.mkdir(exist_ok=True);ids=[f'TCGA-ZZ-{i:04d}-01' for i in range(40)]
for name,swap in [('baseline',False),('releases/synthetic-swap',True)]:
 p=root/name;p.mkdir(parents=True,exist_ok=True);pd.DataFrame({'sampleID':ids,'breast_carcinoma_estrogen_receptor_status':['Positive']*20+['Negative']*20,'PAM50Call_RNAseq':['LumA']*20+['Basal']*20}).to_csv(p/'clinical.tsv',sep='\t',index=False)
 vals=[3+i*.01 if i<20 else 1+i*.01 for i in range(40)]
 if swap:vals[0],vals[20]=vals[20],vals[0]
 pd.DataFrame([vals],index=['ERALPHA'],columns=ids).to_csv(p/'protein_rppa.tsv.gz',sep='\t',compression={'method':'gzip','mtime':0})
 pd.DataFrame({'sample':ids,'OS':[0]*40,'OS.time':[100]*40}).to_csv(p/'survival.tsv',sep='\t',index=False)
 for fname in ['mutation_gene_level.tsv.gz','copy_number_gistic.tsv.gz']:
  pd.DataFrame([[i%2 for i in range(40)]],index=['SYNTHETIC_GENE'],columns=ids).to_csv(p/fname,sep='\t',compression={'method':'gzip','mtime':0})
config.BASELINE_DIR=root/'baseline';config.GENERATED_RELEASES_DIR=root/'releases';config.ENVELOPES_OPENED_DIR=root/'no-envelopes';config.OUTPUT_DIR=b/'busy-browser-outputs';config.RUNS_DIR=config.OUTPUT_DIR/'runs';config.UPLOADS_DIR=config.OUTPUT_DIR/'uploads'
from backend.main import app
import uvicorn
uvicorn.run(app,host='127.0.0.1',port=38743,access_log=False)
