import pathlib,sys,json,tempfile
repo=pathlib.Path(sys.argv[1]).resolve();sys.path.insert(0,str(repo));raw=repo.parent/'oncosys-hackathon-challenge/data/tcga-brca/raw';out={'source':repo.name,'input':'verified frozen public A compared with itself','uses_sealed_input':False}
if repo.name=='readyset-control-tower':
 from control_tower.compare import compare
 doc=compare(str(raw),str(raw))
elif repo.name=='BusyBeavers':
 from detection.engine import analyze_releases
 with tempfile.TemporaryDirectory() as t:doc=analyze_releases(str(raw),str(raw),str(pathlib.Path(t)/'findings.json'))
elif repo.name=='sns-cohort-control-tower':
 sys.path.insert(0,str(repo/'sns'))
 from engine.release import load_release
 from engine.diff import compare_releases
 from engine.impact import assess
 from engine.findings import build_document
 a=load_release(raw);b=load_release(raw,reuse=a);d=compare_releases(a,b);impact=assess(raw.parent/'reference_analyses.py',a,b,raw,raw,d);doc=build_document(d,a,b,'public-A','public-A',impact,team='Independent review')
out.update(verdict=doc['verdict'],finding_count=len(doc['findings']),analyses=[{k:v for k,v in a.items() if k in ('id','status','verdict')} for a in doc['analyses']])
print(json.dumps(out,indent=2))
