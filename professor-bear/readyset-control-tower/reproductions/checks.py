#!/usr/bin/env python3
"""Independent synthetic regression probes. Run only in the documented sandbox.
No event data, sealed inputs, credentials or external API calls are used.
Source checkout and output directory are explicit positional arguments.
Exit 1 means proposed acceptance checks fail, not that the probe crashed.
"""
import gzip,json,os,sys,tempfile,threading,urllib.request
from pathlib import Path
from unittest.mock import patch
src=Path(sys.argv[1]).resolve();out=Path(sys.argv[2]).resolve();out.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(src))
from control_tower.compare import compare,_size
from control_tower.release import path_of,PROTEIN,CLINICAL
from control_tower.webserver import make_server
from control_tower.understand_ai import _ask_claude
from tests.tiny_release import TinyRelease,P1,N1
results=[];documents={}
root=Path(tempfile.mkdtemp(prefix='independent-'))
def add(id,expect,observed,passes):
 results.append({'id':id,'recommended_expectation':expect,'observed':observed,'passes':bool(passes)})
def brief(doc):
 return {'verdict':doc['verdict'],'findings':len(doc['findings']),'analyses':[{k:v for k,v in a.items() if k in ('id','status','after')} for a in doc['analyses']]}
def pair(name,release=None):
 d=root/name;d.mkdir();a=release or TinyRelease();return a.write(str(d/'A')),a.copy().write(str(d/'B'))
for name,setup in [('empty-folders',None),('missing-required-both','missing'),('identical-zero-byte','empty'),('identical-invalid-bytes','invalid')]:
 try:
  if setup is None:
   a=root/name/'A';b=root/name/'B';a.mkdir(parents=True);b.mkdir();a,b=str(a),str(b)
  else:
   a,b=pair(name,TinyRelease().without_file(CLINICAL).without_file(PROTEIN) if setup=='missing' else None)
   if setup in ('empty','invalid'):
    for folder in [a,b]:
     for name_file in [CLINICAL,PROTEIN]:(Path(folder)/name_file).write_bytes(b'' if setup=='empty' else b'not a table\n')
  doc=compare(a,b);documents[name]=doc
  add(name,'Insufficient Evidence when required inputs cannot establish the requested result',brief(doc),doc['verdict']=='Insufficient Evidence')
 except Exception as e:add(name,'Insufficient Evidence without crash',{'exception':type(e).__name__,'message':str(e)},False)
a,b=pair('preexisting-duplicate',TinyRelease().copy_as(PROTEIN,P1,N1));doc=compare(a,b);documents['preexisting-duplicate']=doc
add('preexisting-duplicate','A separate baseline-quality gate detects or explicitly withholds fitness for an existing duplicate',brief(doc),doc['verdict']!='Ready')
a,b=pair('blank-measurement')
p=Path(b)/PROTEIN
with gzip.open(p,'rt') as f:lines=f.read().splitlines()
with gzip.open(p,'wt') as f:f.write('\n'.join('\t'.join([l.split('\t')[0]]+['']*l.count('\t')) if l.startswith('ERALPHA\t') else l for l in lines)+'\n')
doc=compare(a,b);documents['blank-measurement']=doc
add('blank-measurement','Blocked or Insufficient Evidence when no target measurement remains',brief(doc),doc['verdict'] in ('Blocked','Insufficient Evidence'))
size=_size({'difference':0.0},{'difference':0.01})
add('zero-baseline','Relative change is undefined at zero; use explicit absolute tolerance',{'size_measure_fraction':size},size[2]!=1.0)
size=_size({'difference':2.9,'n_samples':1000},{'difference':2.9,'n_samples':1})
add('sample-count-collapse','Loss of 999/1000 samples receives a separate adequacy gate',{'size_measure_fraction':size},size[0]=='large')
from control_tower.analyses import REGISTRY
r=TinyRelease();x=r.copy()
for s in [P1,'TCGA-T1-0002-01','TCGA-T1-0003-01']:
 x.set_cell(PROTEIN,'ERALPHA',s,str(float(r.by_col[PROTEIN][2][s][0])+0.0004))
a=r.write(str(root/'round-A'));b=x.write(str(root/'round-B'));before=REGISTRY[0].run(a);after=REGISTRY[0].run(b);size=_size(before,after)
add('rounding-before-comparison','Keep full precision for change calculations and round only for display',{'true_positive_mean_change':0.0004,'display_before':before['mean_positive'],'display_after':after['mean_positive'],'size':size},size[0]!='none')
a,b=pair('mtime-choice');changed=TinyRelease().swap(PROTEIN,P1,N1).write(b)
compressed=Path(b)/PROTEIN;alternate=Path(b)/'protein_rppa.tsv'
with gzip.open(Path(a)/PROTEIN,'rt') as f:alternate.write_text(f.read())
os.utime(compressed,(1000,1000));os.utime(alternate,(2000,2000));one=compare(a,b);choice1=Path(path_of(b,PROTEIN)).name
os.utime(compressed,(3000,3000));two=compare(a,b);choice2=Path(path_of(b,PROTEIN)).name
add('mtime-choice','Conflicting aliases require explicit selection independent of mtime',{'first_choice':choice1,'first_verdict':one['verdict'],'second_choice':choice2,'second_verdict':two['verdict'],'file_contents_changed_between_runs':False},one['verdict']==two['verdict'])
a,b=pair('review-api');TinyRelease().swap(PROTEIN,P1,N1).write(b)
review_path=root/'reviews.json';server=make_server('127.0.0.1',0,releases=(a,b),reviews=str(review_path),settings=None,quiet=True)
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();base=f'http://127.0.0.1:{server.server_address[1]}'
def get():
 with urllib.request.urlopen(base+'/api/findings') as f:return json.load(f)
def post(payload):
 req=urllib.request.Request(base+'/api/reviews',data=json.dumps(payload).encode(),method='POST')
 with urllib.request.urlopen(req) as f:return f.status,json.load(f)
try:
 doc=get();key=doc['x_readyset']['review_keys']['F1'];status,_=post({'key':key,'status':'confirmed','fix':'approved'})
 reviewed=get()
 add('anonymous-review','Reject a blank reviewer before changing the review state',{'http_status':status,'stored_reviewer':json.loads(review_path.read_text())[key]['reviewer'],'needs_human_review':reviewed['findings'][0]['needs_human_review']},status>=400)
 post({'key':key,'status':'dismissed','reviewer':'Synthetic reviewer B','note':'second decision'})
 overwritten=json.loads(review_path.read_text());post({'key':key,'status':'cleared'});cleared=json.loads(review_path.read_text())
 add('review-history','Retain prior decision events and a withdrawal event',{'records_after_replacement':len(overwritten),'records_after_clear':len(cleared)},len(cleared)>0)
finally:server.shutdown();server.server_close()
class Reply:
 def __enter__(self):return self
 def __exit__(self,*args):pass
 def read(self):return b'{"content":[{"type":"text","text":"limits"}]}'
requests=[]
def capture(req,**kw):requests.append(json.loads(req.data));return Reply()
with patch('control_tower.understand_ai.urllib.request.urlopen',side_effect=capture):
 _ask_claude('SYNTHETIC USER-TYPED TEXT','synthetic-not-a-real-key')
add('cloud-routing-observation','Outbound question payload matches the disclosed free text, without findings attached',{'typed_text_present':requests[0]['messages'][0]['content']=='SYNTHETIC USER-TYPED TEXT','findings_attached':'findings' in requests[0],'external_network_used':False},requests[0]['messages'][0]['content']=='SYNTHETIC USER-TYPED TEXT' and 'findings' not in requests[0])
# Positive control: a relevant swap should affect A1 but not A2.
a,b=pair('positive-swap');TinyRelease().swap(PROTEIN,P1,N1).write(b);doc=compare(a,b);documents['positive-swap']=doc
add('positive-swap','Detect swap, mark A1 affected and leave A2 unrelated',{'verdict':doc['verdict'],'kinds':[f['kind'] for f in doc['findings']],'affected':[f['affects_analyses'] for f in doc['findings']]},doc['verdict']=='Conditional' and any(f['kind']=='sample_swap' and f['affects_analyses']==['A1'] for f in doc['findings']))
(out/'observations.json').write_text(json.dumps({'source_commit':'4dd07736e99f96dd46cb6199c32bea32465bd20e','data':'synthetic only','checks':results,'passed':sum(x['passes'] for x in results),'failed':sum(not x['passes'] for x in results)},indent=2)+'\n')
for name,doc in documents.items():(out/(name+'.json')).write_text(json.dumps(doc,indent=2)+'\n')
for item in results:print(('PASS' if item['passes'] else 'FAIL'),item['id'],json.dumps(item['observed']))
print('SUMMARY',len(results),'checks;',sum(x['passes'] for x in results),'pass;',sum(not x['passes'] for x in results),'fail')
sys.exit(1 if any(not x['passes'] for x in results) else 0)
