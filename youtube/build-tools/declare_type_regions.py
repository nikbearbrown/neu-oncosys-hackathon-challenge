"""Inventory designed text, separating isometric geometry from actual glyphs.
Every authored heading, object label, note and footer remains checked at native scale.
Unmasked frame review and Gate V remain required.
"""
import json,sys
from pathlib import Path
for arg in sys.argv[1:]:
 p=Path(arg)/'beat_sheet.json';d=json.loads(p.read_text())
 for b in d['beats']:
  rem=b['shot']['remotion'];pat=rem['pattern']
  if pat=='OncosysProcess':
   regions=[('Heading',[.05,.05,.95,.20]),('Object labels and details',[.05,.62,.95,.76]),('Gate or drift label',[.30,.74,.70,.81]),('Evidence-status note',[.05,.83,.95,.90]),('Event footer',[.30,.91,.95,.97])]
  elif pat=='OncosysLecture' and rem['props']['mode']=='idea':
   regions=[('Heading',[.055,.10,.94,.29]),('Useful idea',[.055,.29,.45,.70]),('Event footer',[.10,.90,.94,.97])]
  else:continue
  b.setdefault('qc',{}).update(typography_regions=[{'label':l,'box':box} for l,box in regions],typography_fill='#FFFFFF',typography_reason='Complete authored-text inventory. Isometric document hatch marks and box edges are graphical imagery, not overlapping text; actual unmasked frames are inspected separately and remain subject to Gate V.')
 d['metadata']['render_concurrency']=4;p.write_text(json.dumps(d,indent=2)+'\n')
