"""Apply the user's event-brand revision; credit must be explicitly supplied."""
import argparse,copy,json
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--credit',required=True);a=ap.parse_args()
root=Path(__file__).resolve().parents[2]
teams={
'readyset':('Team Automyte','Team Automyte'),
'tripwire':('Team Skill issue','Team Skill issue'),
'identity-crisis-control-tower':('Team Identity_Crisis','Team Identity Crisis'),
'busy-beavers':('Team Busy Beavers','Team Busy Beavers'),
'oncosys-cohort-studio':('Lily Tammy · Seth Barribeau · Hriday Desai\nAayam Raj Shakya · Yanyun Ma','Lily Tammy, Seth Barribeau, Hriday Desai, Aayam Raj Shakya, and Yanyun Ma'),
'sns-cohort-control-tower':('Team SNS','Team S N S'),
'hippa-cratic':('Team HIPPA-cratics','Team Hippa cratics'),
'cohort-firewall':('Ninad Rao · Kareesa Rao\nSreelasya Changalasetty · Sanica Chaudhary','Ninad Rao, Kareesa Rao, Sreelasya Changalasetty, and Sanica Chaudhary'),
'clearanswer':('Team clearanswer','Team ClearAnswer')}
for key,(team,spoken) in teams.items():
 r=root/'youtube'/('claude-liam-'+key+'-show-tell');p=r/'beat_sheet.json';s=json.loads(p.read_text())
 archive=r/'beat_sheet.pre-event-brand.json'
 if not archive.exists():archive.write_text(json.dumps(s,indent=2)+'\n')
 s['metadata'].update(palette='neu',typography={'display':'Lato','serif':'Lato'},event_credit=a.credit,team=team,brand_confirmation='pending' if a.credit.endswith('[pending]') else 'confirmed')
 labels=next(b['shot']['remotion']['props']['labels'] for b in s['beats'] if b['beat_id']=='B01')
 for b in s['beats']:
  bid=b['beat_id'];rem=b['shot'].get('remotion',{});old=copy.deepcopy(rem.get('props',{}))
  if rem.get('pattern')=='DesignPipelineClaim':rem['pattern']='OncosysProcess'
  if rem.get('pattern')=='BrowserCapture':
   rem['props'].update(brand='neu',frame='app');rem['props'].pop('url',None)
   if key=='readyset' and bid=='B04':rem['props']['moves'][1].update(x=.5,y=.75,scale=1.4)
  mode={'BOPEN':'open','BIDEA':'idea','BDEFS':'definitions','BVDT':'recap','BHTF':'prompt','BOUT':'outro'}.get(bid)
  if mode:
   lines=[];title=s['metadata']['title']
   if bid=='BIDEA':title='The useful idea';lines=[s['metadata']['lecture_opening_description']]
   if bid=='BDEFS':title='Terms in this film';lines=[x['term']+': '+x['meaning'] for x in old.get('terms',[])]
   if bid=='BVDT':title='What to build on';lines=old.get('artifactLines',[])
   if bid=='BHTF':title='Your turn';lines=[old.get('command','')]
   b['shot']=dict(type='REMOTION',source='own',visual_intent=title,motion_claim='Reveal the idea, terms or project workflow in time with narration',show=[dict(at=0,event='Name the subject'),dict(at=.15,event='Reveal the conceptual process')],remotion=dict(pattern='OncosysLecture',props=dict(mode=mode,title=title,team=team,lines=lines,labels=labels,credit=a.credit,logos=[],durationSeconds=b.get('actual_duration_s',10))))
   b['proof_gate']='SHOW';b.pop('qc',None)
  if bid=='BOPEN':
   b['narration_text']=s['metadata']['title']+'. By '+spoken+'. An AI Healthcare Hackathon project, with The Open Accelerator, OncoSys AI, and '+a.credit+'.'
   b.pop('audio_file',None);b.pop('actual_duration_s',None);b.pop('audio_padding_applied',None)
  if bid=='BVDT':
   b['narration_text']=b['narration_text'].replace("Let's recap with Claude.","Let's recap.")
   b.pop('audio_file',None);b.pop('actual_duration_s',None);b.pop('audio_padding_applied',None)
  b['shot'].pop('rendered',None)
 p.write_text(json.dumps(s,indent=2)+'\n')
 (r/'BRAND-REVISION.md').write_text('# Event-brand revision\n\nUser requested event branding throughout, project and verified team in the first beat, a small project animation, and credits for The Open Accelerator (TOA), OncoSys AI, and '+a.credit+'.\n\nTeam identity comes from the pinned submission README. No nickname is invented where only members are listed. Northeastern logo is the existing supplied official vector. Additional organizer logos remain pending. Actual app screenshots retain their source colors. The body uses a project-specific Northeastern retint of the existing Show Tell isometric geometry; it does not alter the shared Claude brand. Original audit reports are unchanged.\n')
 print(r.name)
