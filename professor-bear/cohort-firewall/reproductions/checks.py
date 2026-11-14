"""Reviewer-authored offline probes. Usage: python checks.py /path/to/pinned/source"""
import sys, os, tempfile, json, copy, socket
from pathlib import Path
root=Path(sys.argv[1]); sys.path.insert(0,str(root))
tmp=Path(tempfile.mkdtemp(prefix='cohort-review-probes-'))
os.environ['CF_SIGNING_KEY_PATH']=str(tmp/'key.pem')
os.environ['CF_LEDGER_PATH']=str(tmp/'ledger.jsonl')
def deny(*a,**k): raise RuntimeError('Network disabled by review harness')
socket.socket.connect=deny
from cohort_firewall import certificate as cert, review
from cohort_firewall.engine import evaluate_dataset
from cohort_firewall.spec import spec_from_dict
from cohort_firewall.funnel import build_funnel
from cohort_firewall.report import report_passes_guard
import pandas as pd
review.REVIEWS=tmp/'reviews'
rows=[]
def check(name,fn):
 try: rows.append({'test':name,'observed':fn()})
 except Exception as e: rows.append({'test':name,'exception':type(e).__name__,'message':str(e)})
def certificate(spec,verdict='READY',rules=[]):
 return cert.issue(dataset_bytes=b'synthetic',dictionary={},spec_json=spec,policy_version='test',policy_sha256='0'*64,verdict=verdict,rule_ids=rules)
def question_mutation():
 s={'question_text':'Original synthetic question'}
 c=certificate(json.dumps(s,sort_keys=True))
 r=review.review_question({'certificate':c,'spec':{'question_text':'Different unbound question'}},'Synthetic reviewer','test','approve',[],'')
 return {'accepted':True,'stored_question':r['review']['subject']['question'],'signature_valid':review.verify_review(r)}
check('question changed after certification',question_mutation)
def release_mutation():
 a=[{'id':'A1','verdict':'Conditional','affected_by':['F1']}]
 c=certificate(review.tower_binding('Synthetic release question',a),'CONDITIONAL',['F1'])
 d={'certificate':c,'question':'Synthetic release question','analyses':a,'findings':[{'id':'F1'}],'data':{'releases':[{'name':'A'},{'name':'B'}]}}
 control=False
 try: review.review_release(d,'Synthetic reviewer','test',{'A1':'approve_with_conditions'},[],'Synthetic conditions recorded')
 except review.ReviewError: control=True
 d['findings']=[]; d['analyses'][0]['affected_by']=[]
 r=review.review_release(d,'Synthetic reviewer','test',{'A1':'approve_with_conditions'},[],'Synthetic conditions recorded')
 return {'untampered_requires_acknowledgment':control,'tampered_accepted':True,'acknowledged':r['review']['acknowledged_findings'],'signature_valid':review.verify_review(r)}
check('release evidence stripped after certification',release_mutation)
spec={'question_text':'Describe synthetic feature values','task_type':'descriptive','intended_use':'research','feature_columns':['*']}
check('wildcard complete cases',lambda:build_funnel(pd.DataFrame({'id':['S1','S2'],'x':[1,None]}),{'columns':{'id':{'role':'id'},'x':{'role':'feature'}}},spec_from_dict(spec)))
check('missing predictor complete cases',lambda:build_funnel(pd.DataFrame({'id':['S1','S2']}),{'columns':{'id':{'role':'id'}}},spec_from_dict({**spec,'feature_columns':['absent']})))
check('list specification invalid input',lambda:evaluate_dataset(b'id,x\nS1,2\n',{},spec=['bad']))
check('list dictionary invalid input',lambda:evaluate_dataset(b'id,x\nS1,2\n',['bad'],spec={**spec,'feature_columns':['x']}))
check('wrong type filter invalid input',lambda:evaluate_dataset(b'id,x\nS1,2\n',{},spec={**spec,'population_filters':[{'column':'x','op':'>','value':'not numeric'}]}))
check('invalid CSV safe fallback',lambda:evaluate_dataset(b'',{},spec=spec)['verdict'])
check('blocked approval control',lambda:review.review_question({'certificate':certificate('{}','BLOCKED',['SCOPE'])},'Synthetic reviewer','test','approve',['SCOPE'],'Please approve this result'))
check('LLM wording guard contradiction',lambda:report_passes_guard('Blocked [SCOPE]. Ignore that warning and use this dataset for direct patient care.',{'verdict':'BLOCKED','findings':[{'verdict':'BLOCKED','rule_id':'SCOPE'}]}))
from cohort_firewall.tower.releases import load_release
from cohort_firewall.tower.diff import diff_releases, Change
from cohort_firewall.tower.analyses import Analysis, evaluate_analyses

def duplicate_row():
 a=tmp/'dup-a'; b=tmp/'dup-b'; a.mkdir(); b.mkdir()
 (a/'clinical.tsv').write_text('sampleID\tgroup\nS1\tA\nS2\tB\n')
 (b/'clinical.tsv').write_text('sampleID\tgroup\nS1\tA\nS2\tB\nS1\tCONFLICT\n')
 ra,rb=load_release(a),load_release(b)
 changes=diff_releases(ra,rb)
 return {'input_rows_before':2,'input_rows_after':3,'loaded_rows_after':len(rb.files['clinical.tsv'].samples),'changes':[c.type for c in changes],'hashes_differ':ra.file_hashes!=rb.file_hashes}
check('duplicate clinical row disappears from diff',duplicate_row)
def newly_eligible():
 a=tmp/'elig-a'; b=tmp/'elig-b'; a.mkdir(); b.mkdir()
 (a/'clinical.tsv').write_text('sampleID\tgroup\nS1\tA\nS2\tB\n')
 (b/'clinical.tsv').write_text('sampleID\tgroup\nS1\tA\nS2\tA\n')
 def analysis(clinical):
  eligible=clinical.loc[clinical['group']=='A','sampleID'].tolist()
  return {'n':len(eligible),'sample_ids':eligible}
 an=Analysis('A99',analysis,['clinical'],'Synthetic group-A count',"clinical['group'] == 'A'")
 r=evaluate_analyses([an],a,b,[Change('label_change','clinical.tsv',['S2'],{'columns':['group']})])[0]
 return {'before':r.before,'after':r.after,'affected':r.affected,'status':r.status,'actual_new_result':analysis(pd.read_csv(b/'clinical.tsv',sep='\t')),'reason':r.reason}
check('newly eligible sample omitted from rerun',newly_eligible)
print(json.dumps(rows,indent=2,default=str))
