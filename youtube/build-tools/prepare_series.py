"""Generate local narration and approved title cards, preserving measured clocks."""
import json, subprocess, shutil
from pathlib import Path
root=Path(__file__).resolve().parents[2]
art=root.parent/'brutalist.art'
for c in json.loads(Path(__file__).with_name('projects.json').read_text()):
    r=root/'youtube'/('claude-liam-'+c['slug']+'-show-tell')
    log=r/'prepare.log'
    print('Preparing',r.name,flush=True)
    with log.open('w') as out:
        sheet=json.loads((r/'beat_sheet.json').read_text())
        if not all(b.get('audio_file') and (r/b['audio_file']).exists() for b in sheet['beats']):
            subprocess.run(['python3',str(art/'runtime/scripts/generate_audio_kokoro.py'),str(r)],stdout=out,stderr=subprocess.STDOUT,check=True)
        subprocess.run(['python3',str(Path(__file__).with_name('lock_audio.py')),str(r)],stdout=out,stderr=subprocess.STDOUT,check=True)
        if not list((r/'opening').glob('example-opening-*.mp4')):
            subprocess.run(['python3',str(art/'skills/make/lecture/templates/title-slide-16x9/build.py'),'--out',str(r/'opening'),'--sheet',str(r/'beat_sheet.json'),'--width','3840'],stdout=out,stderr=subprocess.STDOUT,check=True)
    (r/'media').mkdir(exist_ok=True)
    clips=list((r/'opening').glob('example-opening-*.mp4'))
    if len(clips)!=1: raise RuntimeError(clips)
    shutil.copy2(clips[0],r/'media/BOPEN.mp4')
    (r/'media/BOPEN.source.txt').write_text('Approved Brutalist lecture title template. Generated locally from this beat sheet and approved portrait asset.\n')
    print('Prepared',r.name,flush=True)
