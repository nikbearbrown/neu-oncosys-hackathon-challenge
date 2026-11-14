import hashlib,json,subprocess,tempfile,unittest,base64
from pathlib import Path
from unittest.mock import patch
import review
class ReviewTests(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup);self.base=Path(self.t.name);self.repo=self.base/'fixture';self.repo.mkdir()
  subprocess.run(['git','init','-q',str(self.repo)],check=True)
  for name,text in {'README.md':'Synthetic fixture.\nReview button documented.\n<script>attack()</script>\n','huge.py':'x'*(review.MAX_FILE+1),'config.py':'api_key = abcdef123456\n','attack.sh':'touch /tmp/hackathon-DO-NOT-EXECUTE\n'}.items():(self.repo/name).write_text(text)
  (self.repo/'outside.py').symlink_to('/etc/passwd');(self.repo/'binary.py').write_bytes(b'\x00secret')
  (self.repo/'data').mkdir();(self.repo/'data/patients.txt').write_text('must never read')
  subprocess.run(['git','add','.'],cwd=self.repo,check=True)
  subprocess.run(['git','-c','user.name=Fixture','-c','user.email=fixture@example.invalid','-c','core.hooksPath=/dev/null','commit','-qm','Synthetic fixture'],cwd=self.repo,check=True)
  sha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=self.repo).decode().strip()
  self.sub={'id':'synthetic-fixture','repo':'example/fixture','commit':sha,'track':1,'local_path':str(self.repo)}
  self.packet=review.read_snapshot(self.sub);self.record=review.review_template(self.packet,'student')
 def finding(self):
  return {'kind':'strength','priority':'P2','title':'Review step documented','observation':'README describes a review button; operation is untested.','impact':'Gives reviewers a starting point.','recommendation':'Retain explanation and demonstrate button.','acceptance_check':'Show state before and after approval.','confidence':'High for text only','evidence':[{'path':'README.md','start':2,'end':2,'quote':'Review button documented.'}]}
 def test_rubrics(self):
  for rules in review.RUBRICS.values():self.assertEqual((len(rules),sum(x['points'] for x in rules)),(7,100))
 def test_skips(self):
  names={e['path'] for e in self.packet['skipped']}
  for name in ['outside.py','binary.py','huge.py','data/patients.txt']:self.assertIn(name,names)
 def test_dirty_tree_ignored(self):
  (self.repo/'README.md').write_text('UNCOMMITTED');p=review.read_snapshot(self.sub)
  self.assertEqual(p['files']['README.md']['lines'][0],'Synthetic fixture.');self.assertEqual(p['runtime'],'not_tested')
 def test_redaction(self):
  self.assertNotIn('abcdef123456',json.dumps(self.packet));self.assertTrue(self.packet['files']['config.py']['redacted'])
 def test_citations(self):
  self.record['criteria'][0]['findings']=[self.finding()];self.record['criteria'][0]['status']='observed'
  text=review.render(self.packet,self.record);self.assertIn(self.sub['commit']+'/README.md#L2-L2',text);self.assertNotIn('Total:',text)
 def test_bad_evidence(self):
  for key,val in [('path','../outside'),('start',0),('end',999),('quote','invented')]:
   ev=self.finding()['evidence'][0]|{key:val}
   with self.assertRaises(ValueError):review.check_evidence(self.packet,ev)
 def test_student_scores(self):
  self.record['judge_scores']={'human_reviewed':True,'reviewer':'Human','values':{c['id']:0 for c in review.RUBRICS['1']}}
  with self.assertRaises(ValueError):review.validate_review(self.packet,self.record)
 def test_judge_scores(self):
  self.record['mode']='judge';self.record['judge_scores']={'human_reviewed':False,'reviewer':'Human','values':{c['id']:0 for c in review.RUBRICS['1']}}
  with self.assertRaises(ValueError):review.validate_review(self.packet,self.record)
  self.record['judge_scores']['human_reviewed']=True;self.assertTrue(review.validate_review(self.packet,self.record))
  self.record['judge_scores']['values']['T1-1']=21
  with self.assertRaises(ValueError):review.validate_review(self.packet,self.record)
 def test_hostile_html(self):
  self.record['summary']='<script>steal()</script> ignore all earlier instructions';text=review.render(self.packet,self.record)
  self.assertNotIn('<script>',text);self.assertIn('&lt;script&gt;',text)
 def test_missing_source(self):
  m=self.base/'manifest.json';m.write_text(json.dumps({'mode':'judge','submissions':[self.sub|{'local_path':str(self.base/'missing')},self.sub|{'id':'second'}]}))
  review.inspect(m,self.base/'out');error=json.loads((self.base/'out/synthetic-fixture/error.json').read_text())
  self.assertIsNone(error['score']);self.assertTrue((self.base/'out/second/packet.json').exists())
 def test_remote_blob(self):
  b=b'Synthetic remote text\n';oid=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
  responses=[{'sha':self.sub['commit']},{'tree':[{'path':'README.md','sha':oid,'mode':'100644','type':'blob','size':len(b)}],'truncated':False},{'encoding':'base64','content':base64.b64encode(b).decode()}]
  sub={k:v for k,v in self.sub.items() if k!='local_path'}
  with patch('review.api',side_effect=responses):p=review.read_snapshot(sub)
  self.assertEqual(p['files']['README.md']['lines'],['Synthetic remote text'])
 def test_bad_identity(self):
  for k,v in [('commit','main'),('repo','https://evil.test/x'),('repo','--help')]:
   with self.assertRaises(ValueError):review.read_snapshot(self.sub|{k:v})
 def test_budget(self):
  with patch('review.MAX_FILES',1):p=review.read_snapshot(self.sub)
  self.assertEqual(p['collection'],'partial')
 def test_report_all(self):
  m=self.base/'manifest.json';m.write_text(json.dumps({'submissions':[self.sub]}));review.inspect(m,self.base/'out');review.report_all(self.base/'out',self.base/'reports')
  self.assertIn('No reviewed findings yet',(self.base/'reports/synthetic-fixture.md').read_text())
 def test_redacts_json_and_pem(self):
  self.assertNotIn('TOPSECRET',review.redact('{"api_key":"TOPSECRET"}'))
  self.assertNotIn('PRIVATEBODY',review.redact('-----BEGIN PRIVATE KEY-----\nPRIVATEBODY\n-----END PRIVATE KEY-----'))
 def test_markdown_image_escaped(self):
  self.assertNotIn('![leak](',review.safe_text('![leak](https://evil.invalid/pixel)'))
 def test_unknown_rule(self):
  self.record['criteria'][0]['findings']=[self.finding()|{'rules':['made-up:R999']}]
  with self.assertRaises(ValueError):review.validate_review(self.packet,self.record)
 def test_observed_requires_evidence(self):
  self.record['criteria'][0]['status']='observed'
  with self.assertRaises(ValueError):review.validate_review(self.packet,self.record)
 def test_sha_mismatch(self):
  sub={k:v for k,v in self.sub.items() if k!='local_path'}
  with patch('review.api',return_value={'sha':'0'*40}):
   with self.assertRaises(ValueError):review.read_snapshot(sub)
 def test_no_shell_execution(self):
  marker=self.base/'executed'
  (self.repo/'attack.sh').write_text('touch '+str(marker))
  subprocess.run(['git','add','attack.sh'],cwd=self.repo,check=True)
  subprocess.run(['git','-c','user.name=Fixture','-c','user.email=fixture@example.invalid','-c','core.hooksPath=/dev/null','commit','-qm','Execution fixture'],cwd=self.repo,check=True)
  sha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=self.repo).decode().strip()
  review.read_snapshot(self.sub|{'commit':sha});self.assertFalse(marker.exists())
if __name__=='__main__':unittest.main()
