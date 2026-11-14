"""Check actual exported media, sample it, and produce a visual-review contact sheet."""
import json,subprocess,sys,math
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw
r=Path(sys.argv[1]).resolve();s=json.loads((r/'beat_sheet.json').read_text());f=r/'exports/landscape'/f'{r.name}.mp4';out=r/'_qc/master';out.mkdir(parents=True,exist_ok=True)
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(f)]));v=next(x for x in probe['streams'] if x['codec_type']=='video');a=next(x for x in probe['streams'] if x['codec_type']=='audio');duration=float(probe['format']['duration']);expected=sum(b['actual_duration_s'] for b in s['beats']);errors=[]
if (v['width'],v['height'])!=(3840,2160):errors.append('not 3840x2160')
if abs(duration-expected)>len(s['beats'])/24+.25:errors.append('duration mismatch')
decode=subprocess.run(['ffmpeg','-v','error','-i',str(f),'-f','null','-'],capture_output=True,text=True)
if decode.returncode or decode.stderr.strip():errors.append('decode errors: '+decode.stderr[-1000:])
raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(f),'-vf','fps=2,scale=320:180,format=gray','-f','rawvideo','-']);frames=np.frombuffer(raw,dtype=np.uint8).reshape((-1,180,320));blank=[i/2+.25 for i,frame in enumerate(frames) if frame.std()<3]
# fps=2 selects around half-second-bin centers. BrowserCapture intentionally
# springs from zero opacity during its first ~0.3 s; do not call that a missing scene.
starts=[];clock=0
for beat in s['beats']:
 if beat['shot']['remotion']['pattern']=='BrowserCapture':starts.append((clock,beat['beat_id']))
 clock+=math.ceil(beat['actual_duration_s']*24)/24
transitions=[{'time_s':t,'beat':bid} for t in blank for start,bid in starts if 0<=t-start<=.35]
persistent=[t for t in blank if not any(x['time_s']==t for x in transitions)]
if persistent:errors.append('unexplained nearly blank samples '+str(persistent))
t=0;tiles=[]
for b in s['beats']:
 dur=math.ceil(b['actual_duration_s']*24)/24
 for frac in [.15,.5,.85]:
  target=out/f"{b['beat_id']}-{int(frac*100)}.jpg"
  subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t+dur*frac),'-i',str(f),'-frames:v','1','-vf','scale=640:360',str(target)],check=True)
  im=Image.open(target).convert('RGB'); tile=Image.new('RGB',(640,390),'white');tile.paste(im,(0,0));ImageDraw.Draw(tile).text((10,368),f"{b['beat_id']} @ {frac:.0%}",fill='black');tiles.append(tile)
 t+=dur
sheet=Image.new('RGB',(1920,390*math.ceil(len(tiles)/3)),'white')
for i,tile in enumerate(tiles):sheet.paste(tile,((i%3)*640,(i//3)*390))
sheet.save(out/'contact.jpg',quality=88)
result={'file':str(f),'bytes':f.stat().st_size,'video':[v['width'],v['height']],'audio_codec':a['codec_name'],'duration_s':duration,'audio_timeline_s':expected,'sampled_frames':len(frames),'blank_samples':blank,'explained_capture_entrances':transitions,'decoded_without_errors':decode.returncode==0 and not decode.stderr.strip(),'errors':errors,'visual_review':'Contact sheet generated; human/model inspection must be recorded separately.'}
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));raise SystemExit(bool(errors))
