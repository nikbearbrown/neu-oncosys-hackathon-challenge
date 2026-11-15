"""Record a completed master only after automated checks and explicit visual review."""
import json,re,sys,hashlib
from pathlib import Path
r=Path(sys.argv[1]).resolve();note=sys.argv[2];v=json.loads((r/'_qc/master/verification.json').read_text());t=(r/'TYPECHECK.md').read_text();g=(r/'_qc/REPORT.md').read_text();s=json.loads((r/'beat_sheet.json').read_text())
assert not v['errors'] and v['decoded_without_errors'],v
assert 'Overall: PASS' in t,t[:300]
assert re.search(r'BLOCKER:\s*0.*MAJOR:\s*0',g,re.S),g[:300]
f=r/'exports/landscape'/f'{r.name}.mp4';v['file']=str(f.relative_to(r));v['sha256']=hashlib.sha256(f.read_bytes()).hexdigest();v['visual_review']=note;v['gate_t']=f"PASS: {len(s['beats'])} beats";v['gate_v']='PASS: zero blockers and zero major findings on the clean master';v['audio_check']='Local narration, measured per beat, AAC stream decoded. Opening/closing checked by cached local Whisper; ASR spellings of proper names are approximate.'
(r/'VERIFICATION.json').write_text(json.dumps(v,indent=2)+'\n')
(r/'BUILD-LOG.md').write_text(f'''# Completed local 4K review master

{s['metadata']['title']}: {v['duration_s']:.3f} seconds, 3840×2160, AAC narration. {len(s['beats'])} filled beats. Gate T passed; Gate V on the clean master reports no blockers or major findings. Full decoding produced no errors. {v['sampled_frames']} frames were sampled at two frames per second; brief entrance transitions are identified separately in VERIFICATION.json.

Visual review: {note}

The film is a selective promotional introduction. Actual tool demonstrations are synthetic, and next steps are proposals. ClearAnswer is interface-only; Cohort Firewall shows actual CLI outputs. Source pins and limitations remain in SOURCES.md, SESSION.md and the independent review.

The user-requested event cards are checked through the event-specific six-role contract in build-tools/verify_films.py. The legacy Claude-only bookend-template test is incompatible and is not claimed as a pass. Pixel typography and full-frame checks remain active. Source-render geometry is separated from glyphs through explicit text inventories; mixed-color app contrast is checked against real text regions, not averaged panel colors.

Media stays local and excluded from GitHub. No YouTube upload or cluster transfer is claimed.
''')
print(r.name,'verified',v['duration_s'])
