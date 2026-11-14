"""Browser smoke checks against an already isolated synthetic local server."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import csv,io,json,datetime
from PIL import Image
out=Path('/tmp/oncosys-first-pass/studio-browser-qa');out.mkdir(exist_ok=True);checks=[];observations={}
assets=Path('/tmp/oncosys-first-pass/studio-browser-assets');asset_map={x['url']:assets/x['name'] for x in json.loads((assets/'manifest.json').read_text())}
def check(name,condition):checks.append({'check':name,'passed':bool(condition)})
with sync_playwright() as p:
 b=p.chromium.launch(channel='chrome',headless=True);c=b.new_context(viewport={'width':1440,'height':1000},reduced_motion='reduce',accept_downloads=True);blocked=[]
 def route(r):
  if r.request.url in asset_map:r.fulfill(body=asset_map[r.request.url].read_bytes(),content_type='application/javascript')
  elif r.request.url.startswith('http://127.0.0.1:38741/'):r.continue_()
  else:blocked.append(r.request.url);r.abort()
 c.route('**/*',route);page=c.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:38741/');page.wait_for_selector('#ai-model:has-text("off")');check('AI-off state visible',page.locator('#ai-model').inner_text()=='off')
 page.locator('#user').fill('synthetic-review');page.locator('#user').press('Tab');page.locator('#use-ai').uncheck();page.locator('#q').fill('Primary tumors');page.get_by_role('button',name='Build cohort',exact=True).click();run=page.get_by_role('button',name='Run protocol',exact=True);run.wait_for();check('Human can inspect protocol before running',run.is_visible() and 'Keep primary tumor samples' in page.locator('#notebook').inner_text())
 run.click();page.wait_for_selector('#notebook a:has-text("Download cohort_samples.csv")');text=page.locator('#notebook').inner_text();check('Eight samples and eight patients shown','8\nSAMPLES · 8 PATIENTS' in text);check('Small-cohort Blocked state visible','BLOCKED' in text and 'minimum 20' in text);check('12 to 8 flow and four exclusions visible','n = 12' in text and 'Excluded n = 4' in text and 'n = 8' in text)
 with page.expect_download() as event:page.get_by_role('link',name='Download cohort_samples.csv',exact=True).click()
 download=event.value;download.save_as(out/'cohort_samples.csv');rows=list(csv.DictReader((out/'cohort_samples.csv').open()));check('Downloaded cohort has eight unique samples',len(rows)==8 and len({r['sample_id'] for r in rows})==8)
 # Audit and verdict are explicit same-origin links discovered in the rendered result.
 audit_href=page.get_by_role('link',name='Audit trail',exact=True).get_attribute('href');resp=page.request.get('http://127.0.0.1:38741'+audit_href);audit=list(csv.DictReader(io.StringIO(resp.text())));check('Audit export accounts for 12 input samples',resp.ok and len(audit)==12)
 verdict_link=page.locator('#notebook a').filter(has_text='verdict.json');v=page.request.get('http://127.0.0.1:38741'+verdict_link.get_attribute('href'));vd=v.json();observations['verdict_export_keys']=list(vd);observations['verdict_export']=vd.get('verdict');check('Separate verdict export retains Blocked',v.ok and vd.get('verdict')=='Blocked')
 initial_theme=page.locator('html').get_attribute('data-theme');page.get_by_role('button',name='Switch colour theme').click();check('Theme toggle changes theme',page.locator('html').get_attribute('data-theme')!=initial_theme);page.get_by_role('button',name='Switch colour theme').click()
 page.locator('#toasts').wait_for(state='visible');page.wait_for_function("document.querySelector('#toasts').children.length === 0",timeout=15000);page.evaluate('window.scrollTo(0,0)');box=page.locator('#notebook').bounding_box();page.screenshot(path=str(out/'full-synthetic.png'),full_page=True);im=Image.open(out/'full-synthetic.png');im.crop((int(box['x']),int(box['y']),int(box['x']+box['width']),int(box['y']+box['height']))).save(out/'result-synthetic.png')
 page.get_by_role('button',name='Advanced search',exact=False).click();check('Advanced-search dialog opens',page.locator('#advanced').is_visible());page.get_by_role('button',name='Close advanced search').click();check('Advanced-search dialog closes',not page.locator('#advanced').is_visible())
 page.set_viewport_size({'width':390,'height':844});page.screenshot(path=str(out/'mobile-synthetic.png'),full_page=True);dims=page.evaluate('({width:innerWidth,documentWidth:document.documentElement.scrollWidth})');observations['mobile_dimensions']=dims;check('No document horizontal overflow at 390px',dims['documentWidth']<=dims['width']);check('No browser script errors',not errors)
 result={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_commit':'54aeacb6f6f355a1dcaa42d7abf2ce174315ad69','browser':b.version,'fixture':'Submitted invented 12-sample/8-patient fixture; local-only AI disabled','external_requests_blocked':sorted(set(blocked)),'checks':checks,'script_errors':errors,'observations':observations,'limits':'No hosted demo, real patient rows, external model or full accessibility audit. Four exact pinned CDN scripts were served from recorded local copies; Google fonts were blocked, with fallback fonts. Reduced motion enabled.'};(out/'browser-qa.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));b.close()
