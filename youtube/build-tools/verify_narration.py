"""Check the delivered audio stream for long gaps; not a pronunciation test."""
import json, re, subprocess, sys
from pathlib import Path

r = Path(sys.argv[1]).resolve()
master = r / 'exports/landscape' / f'{r.name}.mp4'
p = subprocess.run([
    'ffmpeg', '-hide_banner', '-i', str(master), '-vn',
    '-af', 'silencedetect=noise=-45dB:d=2,volumedetect',
    '-f', 'null', '-'
], capture_output=True, text=True)
starts = [float(v) for v in re.findall(r'silence_start: ([0-9.]+)', p.stderr)]
durations = [float(v) for v in re.findall(r'silence_duration: ([0-9.]+)', p.stderr)]
mean = re.search(r'mean_volume: ([-\w.]+) dB', p.stderr)
peak = re.search(r'max_volume: ([-\w.]+) dB', p.stderr)
errors = []
if p.returncode: errors.append('audio decode failed')
if not mean or not peak: errors.append('missing volume measurement')
if starts: errors.append('silence of at least two seconds requires review')
result = {
    'file': str(master.relative_to(r)), 'threshold_db': -45,
    'minimum_gap_s': 2, 'long_gap_starts_s': starts,
    'long_gap_durations_s': durations,
    'mean_volume_db': mean.group(1) if mean else None,
    'peak_volume_db': peak.group(1) if peak else None,
    'errors': errors,
    'scope': 'Signal continuity only; does not establish correct pronunciation or replace listening.'
}
out = r / '_qc/audio-verification.json'
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(result, indent=2) + '\n')
print(r.name, json.dumps(result))
raise SystemExit(bool(errors))
