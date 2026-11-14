from pathlib import Path
import shutil,sys
b=Path(__file__).resolve().parent;root=b/'identity-browser';root.mkdir(exist_ok=True);src=b/'identity-crisis-control-tower';dst=root/src.name
shutil.copytree(src,dst,ignore=shutil.ignore_patterns('__pycache__','.git','out'),dirs_exist_ok=True)
org=root/'oncosys-hackathon-challenge'
for rel in ['format/validate.py','format/findings.schema.json','data/tcga-brca/reference_analyses.py']:
 p=org/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(b/'oncosys-hackathon-challenge'/rel,p)
p=org/'envelopes/unseal.py';p.parent.mkdir(parents=True,exist_ok=True);p.write_text('raise RuntimeError("Envelope access disabled in synthetic review environment")\n')
sys.path.insert(0,str(dst));from tests.synth import frames,write,copy,P,sid
fr=frames(120);write(org/'data/tcga-brca/raw',fr);new=copy(fr);c1,c2=sid(0),sid(3);new[P][[c1,c2]]=new[P][[c2,c1]].to_numpy();write(org/'data/tcga-brca/releases/synthetic-swap',new)
print('Synthetic 120-tumor plus 4-normal releases prepared; no sealed input present.')
