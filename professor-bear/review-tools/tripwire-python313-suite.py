from pathlib import Path
import subprocess,os,json,time,datetime,xml.etree.ElementTree as ET
b=Path(__file__).parent
env={'PATH':'/opt/homebrew/bin:/usr/bin:/bin','TMPDIR':str(b/'tmp'),'PYTHONNOUSERSITE':'1','PYTEST_DISABLE_PLUGIN_AUTOLOAD':'1'}
cmd=['/usr/bin/sandbox-exec','-f',str(b/'sandbox.sb'),str(b/'venv313/bin/python3'),'-m','pytest','-q','--tb=short','--disable-warnings','--junitxml='+str(b/'tripwire313-junit.xml'),'tests']
t=time.time()
with (b/'tripwire313-tests.log').open('w') as f:
 try:r=subprocess.run(cmd,cwd=b/'tripwire',env=env,stdout=f,stderr=subprocess.STDOUT,timeout=360);code=r.returncode
 except subprocess.TimeoutExpired:code='timeout'
counts=[]
if (b/'tripwire313-junit.xml').exists():
 for s in ET.parse(b/'tripwire313-junit.xml').getroot().iter('testsuite'):counts.append({k:s.get(k) for k in ['tests','failures','errors','skipped','time']})
versions=subprocess.check_output([str(b/'venv313/bin/python3'),'-c','import sys,importlib.metadata,json; print(json.dumps({"python":sys.version,"packages":{p:importlib.metadata.version(p) for p in ["pandas","numpy","jsonschema","cryptography","streamlit","pytest"]}}))'],env=env,text=True)
out={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':'45df43640836025b40e89fc190f913ad694a6011','exit_code':code,'seconds':round(time.time()-t,2),'suites':counts,'environment':json.loads(versions),'command':cmd,'env_keys':list(env),'scope':'Same submitted suite and verified frozen public files in isolated disposable copy; exact six direct requirements, Python3.13 macOS ARM64; transitive packages resolved today; no hosted or sealed inputs.'}
(b/'tripwire313-run.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));print((b/'tripwire313-tests.log').read_text()[-1200:])
