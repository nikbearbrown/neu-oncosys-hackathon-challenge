from pathlib import Path
from playwright.sync_api import sync_playwright
import json,time
b=Path('/tmp/oncosys-first-pass');assets={x['url']:x for x in json.loads((b/'sns-browser-assets/manifest.json').read_text())};out=b/'sns-browser-qa';out.mkdir(exist_ok=True)
checks=[];errors=[];blocked=[]
def check(name,actual):checks.append({'check':name,'passed':bool(actual)})
with sync_playwright() as p:
 browser=p.chromium.launch(channel='chrome',headless=True)
 ctx=browser.new_context(viewport={'width':1440,'height':1000},reduced_motion='reduce')
 def route(r):
  u=r.request.url
  if u.startswith('http://127.0.0.1:18796/'):
   if '/api/unseal' in u:r.abort();blocked.append('unseal route blocked by reviewer')
   else:r.continue_()
  elif u in assets:r.fulfill(path=assets[u]['file'],content_type='application/javascript')
  else:blocked.append(u);r.abort()
 ctx.route('**/*',route);page=ctx.new_page();page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:18796/',wait_until='networkidle');page.get_by_role('button',name='Saved',exact=True).click();page.get_by_role('button',name='synthetic-sign-change').click()
 check('Synthetic saved release selectable',page.get_by_role('button',name='Run check',exact=True).is_enabled())
 with page.expect_response(lambda r:r.url.endswith('/api/run'),timeout=60000) as response:page.get_by_role('button',name='Run check',exact=True).click()
 data=response.value.json();check('Full run API succeeded',response.value.status==200 and data.get('ok'));check('Synthetic sign change displayed as Blocked',data.get('doc',{}).get('verdict')=='Blocked')
 page.get_by_role('heading',name='Impact on the analyses').wait_for();check('Evidence view present',page.locator('#evidence').count()==1)
 page.locator('main').screenshot(path=str(out/'results-synthetic.png'))
 page.get_by_role('link',name='Export',exact=True).click()
 for aid in ['A1','A2']:
  with page.expect_response(lambda r:'/cohort' in r.url and r.request.method=='POST',timeout=60000) as response:page.get_by_role('button',name='Build cohort for '+aid,exact=True).click()
  answer=response.value.json();check(aid+' cohort export API succeeded',response.value.status==200 and answer.get('ok'))
  if answer.get('ok'):check(aid+' cohort has unique samples',answer.get('n_duplicates')==0)
 page.locator('#export').screenshot(path=str(out/'export-synthetic.png'))
 page.get_by_role('button',name='Switch color theme').click();check('Theme switch works',page.locator('html').get_attribute('data-theme')=='dark')
 page.set_viewport_size({'width':390,'height':844});page.evaluate('window.scrollTo(0,0)');page.screenshot(path=str(out/'mobile-synthetic.png'));check('Mobile page has no document horizontal overflow',page.evaluate('document.documentElement.scrollWidth <= innerWidth'))
 check('No browser execution errors',len(errors)==0)
 browser.close()
report={'data':'Invented TCGA-ZZ fixtures only; no event patient data or sealed inputs','checks':checks,'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'browser_errors':errors,'blocked_outbound_requests':sorted(set(blocked)),'limitations':'Smoke test only; no screen reader, hosted deployment, auth or clinical validity verification. CDN scripts served from recorded fixed local files; fonts blocked.'}
(out/'browser-qa.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
