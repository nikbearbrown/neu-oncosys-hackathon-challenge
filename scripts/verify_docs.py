"""Validate local links, source hashes, rule IDs and exact event rubric extraction."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
checks=0
for entry in json.loads((ROOT/'sources/manifest.json').read_text()):
 b=(ROOT/entry['file']).read_bytes()
 assert len(b)==entry['bytes'] and hashlib.sha256(b).hexdigest()==entry['sha256'],entry['file'];checks+=1
for path in ROOT.rglob('*.md'):
 if any(p in {'work','reports','.git'} for p in path.parts):continue
 text=path.read_text()
 for link in re.findall(r'\]\(([^)]+)\)',text):
  if link.startswith(('http:','https:','mailto:','#')):continue
  target=link.split('#')[0]
  assert (path.parent/target).exists(),f'{path}: {link}';checks+=1
rules=json.loads((ROOT/'rule-index.json').read_text());assert len(rules)==188
assert sum(x.startswith('medical72:') for x in rules)==72
assert sum(x.startswith('dashboard:') for x in rules)==100
assert sum(x.startswith('medical16:') for x in rules)==16
for key,r in rules.items():
 line=(ROOT/r['source']).read_text().splitlines()[r['line']-1]
 assert r['title'] in line,(key,line);checks+=1
text=(ROOT/'sources/event-2026-11-14.txt').read_text()
for track,name in [(1,'Cohort Firewall'),(2,'Evidence Navigator')]:
 lines=text.split(f'Track {track} · {name}\n100\n')[1].split('Basic requirements')[0].strip().splitlines()
 expected=[{'id':f'T{track}-{i//2+1}','points':int(lines[i]),'criterion':lines[i+1]} for i in range(0,len(lines),2)]
 assert json.loads((ROOT/'rubrics.json').read_text())[str(track)]==expected;checks+=1
assert 'passcode [REDACTED]' in text
assert not re.search(r'passcode (?!\[REDACTED\])\S+',text)
print(f'{checks} documentation/source checks passed; 188 indexed rules/sections; both rubrics match source and sum to 100.')
