import json,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[2];art=root.parent/'brutalist.art'
for r in sorted((root/'youtube').glob('claude-liam-*-show-tell')):
 print('Brand audio',r.name,flush=True)
 with (r/'brand-audio.log').open('w') as out:
  subprocess.run(['python3',str(art/'runtime/scripts/generate_audio_kokoro.py'),str(r),'--only','BOPEN','BVDT'],stdout=out,stderr=subprocess.STDOUT,check=True)
  subprocess.run(['python3',str(Path(__file__).with_name('lock_audio.py')),str(r)],stdout=out,stderr=subprocess.STDOUT,check=True)
