"""Validate the user-requested event-bookend contract and media clocks.
Does not replace visual inspection, Gate T or Gate V.
"""
import argparse,json,subprocess,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--media',action='store_true');a=p.parse_args()
y=Path(__file__).resolve().parents[1];results=[]
for r in sorted(y.glob('claude-liam-*-show-tell')):
 d=json.loads((r/'beat_sheet.json').read_text()); bs=d['beats']; m=d['metadata']; errors=[]
 def require(ok,msg):
  if not ok:errors.append(msg)
 ids=[b['beat_id'] for b in bs];require(len(ids)==len(set(ids)),'duplicate beat ids')
 require(ids[:3]==['BOPEN','BIDEA','BDEFS'],'opening order');require(ids[-3:]==['BVDT','BHTF','BOUT'],'closing order')
 modes={'BOPEN':'open','BIDEA':'idea','BDEFS':'definitions','BVDT':'recap','BHTF':'prompt','BOUT':'outro'}
 for b in bs:
  bid=b['beat_id'];rem=b['shot']['remotion'];props=rem['props']; audio=r/b['audio_file']
  require(b.get('voice')=='am_onyx','wrong voice '+bid);require(audio.is_file(),'audio missing '+bid)
  require(b.get('actual_duration_s',0)>0,'missing measured clock '+bid)
  require(abs(props['durationSeconds']-b['actual_duration_s'])<.05,'scene/audio clock mismatch '+bid)
  if bid in modes:
   require(rem['pattern']=='OncosysLecture' and props['mode']==modes[bid],'event bookend role '+bid)
  if bid in ['BOPEN','BOUT']:
   require(props['title']==m['title'],'project title '+bid);require(bool(props['team'].strip()),'team missing '+bid)
   for sponsor in ['SEIS','OncoSys AI','The Open Accelerator','Red Hat']:require(sponsor in b['narration_text'],'missing spoken sponsor '+sponsor+' '+bid)
   for logo in ['the-open-accelerator-transparent.png','oncosys-ai-transparent-black-wordmark.png','northeastern_university_seis_logo.jpeg','red-hat-logo.png']:
    require(any(x.endswith(logo) for x in props['logos']),'logo missing '+logo)
  if a.media:
   f=r/'media'/f'{bid}.mp4'; require(f.is_file(),'video missing '+bid)
   if f.is_file():
    q=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(f)]));v=next(x for x in q['streams'] if x['codec_type']=='video');require((v['width'],v['height'])==(3840,2160),'not 4K '+bid);require(abs(float(q['format']['duration'])-b['actual_duration_s'])<.12,'media duration '+bid)
 require('Sponsored by' in bs[0]['narration_text'],'opening sponsorship');require('Thank you' in bs[-1]['narration_text'],'closing thanks')
 results.append({'film':r.name,'beats':len(bs),'duration_s':sum(b['actual_duration_s'] for b in bs),'errors':errors})
print(json.dumps(results,indent=2));raise SystemExit(any(x['errors'] for x in results))
