import sys,json,subprocess,shutil
from pathlib import Path
r=Path(sys.argv[1]).resolve();p=r/'beat_sheet.json';s=json.loads(p.read_text());t={}
for b in s['beats']:
 a=r/b['audio_file'];lead=b.get('lead_silence_s',0);tail=b.get('tail_silence_s',0)
 if (lead or tail) and not b.get('audio_padding_applied'):
  out=a.with_name(a.stem+'-padded.mp3');filters=[]
  if lead:filters.append(f'adelay={round(lead*1000)}:all=1')
  if tail:filters.append(f'apad=pad_dur={tail}')
  subprocess.run(['ffmpeg','-v','error','-y','-i',str(a),'-af',','.join(filters),'-c:a','libmp3lame','-q:a','2',str(out)],check=True);out.replace(a);b['audio_padding_applied']={'lead':lead,'tail':tail}
 duration=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',str(a)]));b['actual_duration_s']=duration;t[b['beat_id']]=duration
 rem=b['shot'].get('remotion')
 if rem:rem['props']['durationSeconds']=duration
p.write_text(json.dumps(s,indent=2)+'\n');(r/'mp3/timings.json').write_text(json.dumps(t,indent=2)+'\n')
for image in (r/'captures').glob('*.png'):
 target=r.parents[2]/'brutalist.art/runtime/remotion/public/oncosys-films'/r.name/image.name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(image,target)
print('Measured total:',sum(t.values()))
