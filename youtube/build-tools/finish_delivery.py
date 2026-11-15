"""Build the delivery index from observed, verified local masters only."""
import hashlib, json, shutil
from datetime import datetime, timezone
from pathlib import Path

y = Path(__file__).resolve().parents[1]
slugs = ['readyset', 'busy-beavers', 'clearanswer', 'cohort-firewall',
         'hippa-cratic', 'identity-crisis-control-tower',
         'oncosys-cohort-studio', 'sns-cohort-control-tower', 'tripwire']
asr = json.loads((y / 'narration-asr.json').read_text())['results']
records = []
for slug in slugs:
    r = y / f'claude-liam-{slug}-show-tell'
    s = json.loads((r / 'beat_sheet.json').read_text())
    v = json.loads((r / 'VERIFICATION.json').read_text())
    a = json.loads((r / '_qc/audio-verification.json').read_text())
    assert not v['errors'] and not a['errors'], r
    assert 'GATE LOUDNESS: PASS' in (r / 'LOUDNESS.md').read_text(), r
    master = r / v['file']
    assert hashlib.sha256(master.read_bytes()).hexdigest() == v['sha256'], r
    for b in s['beats']:
        if b['beat_id'] in ('BOPEN', 'BOUT'):
            assert hashlib.sha256((r / b['audio_file']).read_bytes()).hexdigest() == asr[r.name][b['beat_id']]['sha256'], r
    v['audio_signal_check'] = a
    v['loudness_check'] = 'PASS; measured integrated loudness, true peak and every narration beat in LOUDNESS.md'
    (r / 'VERIFICATION.json').write_text(json.dumps(v, indent=2) + '\n')
    shutil.copy2(r / '_qc/master/midpoints.jpg', r / 'PREVIEW.jpg')
    shutil.copy2(r / '_qc/REPORT.md', r / 'VISUAL-QC.md')
    records.append({'folder': r.name, 'title': s['metadata']['title'],
                    'beats': len(s['beats']), 'duration_s': v['duration_s'],
                    'bytes': v['bytes'], 'sampled_frames': v['sampled_frames'],
                    'sha256': v['sha256']})

total = sum(r['duration_s'] for r in records)
stamp = datetime.now(timezone.utc).isoformat()
summary = {'completed_utc': stamp, 'films': records,
           'total_duration_s': total, 'total_beats': sum(r['beats'] for r in records),
           'total_master_bytes': sum(r['bytes'] for r in records),
           'video_dimensions': [3840, 2160], 'uploaded_to_youtube': False,
           'transferred_to_cluster': False}
(y / 'DELIVERY.json').write_text(json.dumps(summary, indent=2) + '\n')
readme = '''# Hackathon project films

**All nine local 4K review masters are complete.** These promotional Show Tell lectures use Liam's local Kokoro am_onyx narration, verified strengths, real captured tools and constructive next steps. Detailed independent reviews remain unchanged in [professor-bear](../professor-bear/README.md).

[Full-path open commands for all nine films](WATCH.md) · [Verified team credits](CREDITS.md) · [Delivery manifest](DELIVERY.json)

The MP4s stay on the Mac and are excluded from GitHub. This repository contains the scripts, measured beat sheets, source notes, captured frames, preview sheets and verification records. No YouTube upload or cluster transfer is claimed.

| Film | Length | Materials | Checks |
|---|---:|---|---|
'''
watch = '# Watch all nine local 4K films\n\nRun these commands individually on Bear’s Mac. Each master has a matching SHA-256 and verification record in its project folder.\n\n'
for r in records:
    seconds = round(r['duration_s']); dur = f'{seconds // 60}:{seconds % 60:02d}'
    f = r['folder']
    readme += f"| {r['title']} | {dur} | [Script]({f}/SCRIPT.md) · [Preview]({f}/PREVIEW.jpg) | [Verification]({f}/VERIFICATION.json) · [Type size]({f}/TYPECHECK.md) · [Visual]({f}/VISUAL-QC.md) · [Audio]({f}/LOUDNESS.md) |\n"
    watch += f"## {r['title']}\n\n```sh\nopen \"{y / f / 'exports/landscape' / (f + '.mp4')}\"\n```\n\n"
readme += f'''
## What was checked

The nine masters contain {summary['total_beats']} filled beats and {total / 60:.1f} minutes of material. All are 3840×2160 with AAC narration. Every complete file decoded without errors. Automated sampling covered {sum(r['sampled_frames'] for r in records):,} frames at two frames per second; bounded entrance transitions are identified in each verification record. Every final beat midpoint was visually inspected, with larger inspection of application details and sponsor cards. The type-size check and final-frame checks passed; no final-frame blocker or major finding remains.

Audio checks measured integrated loudness and true peak and confirmed narration in every beat. No gap of two seconds or longer was detected at the documented −45 dB threshold. Cached local Whisper checked the opening and closing audio; its approximate proper-name spellings in narration-asr.json are not canonical credits. The scripts and CREDITS.md retain the verified spellings. This is not a claim of full human listening or a pronunciation audit.

## Visuals and scope

Authored visuals use Northeastern/SEIS red, black, white and Lato. Actual applications retain their own appearance. First and last beats identify the project and verified team and credit Northeastern University/SEIS, OncoSys AI, The Open Accelerator and Red Hat, using the supplied marks with their proportions preserved.

Application footage presents real captured synthetic sessions with editorial camera movement. ClearAnswer shows its landing interface only, without an external model audit. Cohort Firewall shows literal local CLI outputs. HIPPA-cratic's Cohort Studio is a different submission from the other Cohort Studio; their teams and captures are kept distinct. Conceptual animations and suggested next steps are labeled. No clinical validity, production readiness, implemented fixes or official judging scores are claimed.

The event-specific six-role bookend contract is checked by build-tools/verify_films.py. The legacy Claude-only bookend-template check does not recognize these requested event cards and is not claimed as a pass. Definition and recap cards retain non-blocking narration-redundancy advisories. Pixel typography and full-frame checks remain active. Declared contrast regions evaluate actual text instead of treating beige panels or dark buttons as glyphs; they do not certify the whole captured application's accessibility.

## Rebuild

Use the established Brutalist Show Tell and Lecture skills and the integration notes in [render-source](render-source/README.md). Generate local narration, measure it with build-tools/lock_audio.py, and render through canonical remotion_scenes.py. Run the type-size check, final-frame checks and audio checks, and inspect actual frames before recording a verified master. The current beat sheets are the final authored source; do not rerun the initial authoring scripts over finished work. Do not edit a sheet while its renderer or compiler is active.
'''
(y / 'README.md').write_text(readme.rstrip() + '\n')
(y / 'WATCH.md').write_text(watch.rstrip() + '\n')
print(json.dumps(summary, indent=2))
