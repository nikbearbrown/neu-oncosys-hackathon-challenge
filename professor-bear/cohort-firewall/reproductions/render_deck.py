"""Render local review deck with installed Playwright/Chrome; no network needed."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json
root=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless=True)
 page=browser.new_page(viewport={'width':1440,'height':1050},device_scale_factor=1)
 page.route('http://**/*',lambda route:route.abort())
 page.route('https://**/*',lambda route:route.abort())
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto((root/'slides.html').as_uri()); page.evaluate('document.fonts.ready');page.emulate_media(reduced_motion='reduce')
 records=[]
 for i in range(page.locator('.slide').count()):
  page.evaluate(f'show({i})')
  page.locator('.slide.active').screenshot(path=str(root/'evidence'/f'slide-{i+1:02}.png'))
  records.append(page.locator('.slide.active').evaluate('''el=>{const b=el.getBoundingClientRect();return {title:el.querySelector('h1').textContent,overflow:el.scrollHeight>el.clientHeight+1,headlineLines:el.querySelector('h1').getBoundingClientRect().height/parseFloat(getComputedStyle(el.querySelector('h1')).lineHeight),outside:[...el.querySelectorAll('*')].filter(x=>{const r=x.getBoundingClientRect();return r.bottom>b.bottom+1||r.right>b.right+1}).map(x=>x.tagName)}}'''))
 page.pdf(path=str(root/'slides.pdf'),prefer_css_page_size=True,print_background=True)
 page.set_viewport_size({'width':390,'height':844});page.evaluate('show(5)')
 mobile=page.evaluate('({width:innerWidth,scroll:document.documentElement.scrollWidth})')
 (root/'evidence'/'deck-qa.json').write_text(json.dumps({'slides':records,'page_errors':errors,'mobile':mobile},indent=2))
 browser.close()
from PIL import Image,ImageOps,ImageDraw
files=sorted((root/'evidence').glob('slide-*.png'))
thumbs=[]
for f in files:
 im=Image.open(f).convert('RGB');im.thumbnail((480,270));thumbs.append(im)
canvas=Image.new('RGB',(1440,300*((len(thumbs)+2)//3)), '#dedede');d=ImageDraw.Draw(canvas)
for i,im in enumerate(thumbs):
 x=(i%3)*480;y=(i//3)*300;canvas.paste(im,(x,y));d.text((x+8,y+274),str(i+1),fill='black')
canvas.save(root/'evidence'/'deck-contact-sheet.png')
try:
 import fitz
 pdf=fitz.open(root/'slides.pdf')
 (root/'evidence'/'pdf-qa.json').write_text(json.dumps({'pages':len(pdf),'page_sizes':[[p.rect.width,p.rect.height] for p in pdf],'empty_pages':[i+1 for i,p in enumerate(pdf) if not p.get_text().strip()]},indent=2))
except ImportError: pass
print('Rendered',len(files),'slides')
