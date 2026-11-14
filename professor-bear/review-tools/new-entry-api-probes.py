from pathlib import Path
import sys,json,os,copy,tempfile
b=Path(__file__).resolve().parent;repo=sys.argv[1];root=b/repo;sys.path.insert(0,str(root));os.chdir(root)
out=[]
def record(name,**kw):out.append({'check':name,**kw})
if repo=='cohort-firewall':
 os.environ['CF_SIGNING_KEY_PATH']=str(b/'cohort-firewall-api-review-key.pem');os.environ['CF_LEDGER_PATH']=str(b/'cohort-firewall-api-ledger.jsonl')
 from fastapi.testclient import TestClient
 from api.main import app
 client=TestClient(app,raise_server_exceptions=False)
 spec={'question_text':'Describe invented feature values','task_type':'descriptive','intended_use':'research','feature_columns':['x']}
 for name,data,dct,s in [('list_spec',b'id,x\nS1,2\n',{},['bad']),('list_dictionary',b'id,x\nS1,2\n',['bad'],spec),('incompatible_filter',b'id,x\nS1,2\n',{},dict(spec,population_filters=[{'column':'x','op':'>','value':'word'}])),('empty_csv',b'',{},spec)]:
  r=client.post('/evaluate',files={'dataset':('synthetic.csv',data,'text/csv'),'dictionary':('dictionary.json',json.dumps(dct),'application/json')},data={'spec':json.dumps(s)})
  record(name,status=r.status_code,verdict=r.json().get('verdict') if r.headers.get('content-type','').startswith('application/json') else None)
 from cohort_firewall.engine import evaluate_dataset
 from cohort_firewall import review
 review.REVIEWS=b/'cohort-firewall-api-reviews'
 v=root/'data/variants/clean'
 result=evaluate_dataset((v/'data.csv').read_bytes(),json.loads((v/'dictionary.json').read_text()),spec=json.loads((v/'spec.json').read_text()))
 body={'result':result,'reviewer':'Synthetic reviewer','decision':'approve'}
 r=client.post('/review/question',json=body);record('original_question_control',status=r.status_code)
 result['spec']['question_text']='Different synthetic question after certification'
 r=client.post('/review/question',json=body);record('changed_question_review',status=r.status_code,stored_question=r.json().get('review',{}).get('subject',{}).get('question'))
else:
 from agents.verifier import VerifierAgent
 v=VerifierAgent.__new__(VerifierAgent)
 r=v._build_result('50.1% are LumA and 90% are Basal',{'verdict':'contradicted','correct_value':'50% are LumA; 10% are Basal','reasoning':'Synthetic compound claim'},[])
 record('compound_full_assembly',verdict=r.claim_verdict,evidence=[vars(x) for x in r.evidence])
 r=v._build_result('Invented measurement',{'verdict':'supported','reasoning':'Synthetic model assertion','evidence_files':['not-queried.csv']},[])
 record('unqueried_file_evidence',verdict=r.claim_verdict,evidence=[vars(x) for x in r.evidence])
 import app
 c=app.app.test_client()
 audit={'format_version':'0.2','producer':{'team':'synthetic-review','product':'claim-auditor','track':'evidence-navigator'},'data':{'releases':[{'name':'invented','files':[]}]},'question':'Invented test question','findings':[{'id':'F1','summary':'Invented unsupported claim','claim_text':'Invented unsupported claim','claim_verdict':'insufficient_evidence','confidence':'low','evidence':[],'needs_human_review':True}]}
 app._jobs['synthetic-review']={'state':'done','result':audit,'error':None,'claims':[]}
 record('missing_job_control',status=c.post('/api/export/missing').status_code)
 for name,body in [('plain_export',{}),('reasonless_override',{'overrides':[{'finding_id':'F1','decision':'override','verdict':'supported'}]})]:
  r=c.post('/api/export/synthetic-review',json=body)
  exported=c.get('/api/export/download/synthetic-review')
  record(name,status=r.status_code,validation=r.json.get('valid'),download_status=exported.status_code,exported_finding=json.loads(exported.data)['findings'][0])
 # Manifests may intentionally describe all releases; make the discrepancy explicit.
 from core.loader import TCGARelease
 t=Path(tempfile.mkdtemp(dir=b/'tmp'));a=t/'raw';a.mkdir()
 (t/'sample_manifest.csv').write_text('sample_id,sample_type\nS1,Primary Tumor\nS2,Primary Tumor\n')
 (a/'clinical.tsv').write_text('sampleID\tPAM50Call_RNAseq\nTCGA-XX-0001-01\tLumA\n')
 d=TCGARelease(a)
 record('manifest_release_scope',manifest_count=d.count_primary_tumors(),actual_clinical_rows=len(d.primary_tumors('clinical')),checksummed_files=list(d.file_checksums()))
print(json.dumps(out,indent=2))
