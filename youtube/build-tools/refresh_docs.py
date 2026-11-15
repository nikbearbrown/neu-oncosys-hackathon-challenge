"""Refresh narration records from measured authored sheets; never edits media or sheets."""
import json,shutil
from pathlib import Path
root=Path(__file__).resolve().parents[2]; y=root/'youtube'; art=root.parent/'brutalist.art'
for r in sorted(y.glob('claude-liam-*-show-tell')):
 d=json.loads((r/'beat_sheet.json').read_text());m=d['metadata']
 scope='The browser demonstration uses actual captured synthetic sessions described in the linked review/test records. Camera movement is editorial presentation of captured frames, not newly executed app interaction.'
 if r.name=='claude-liam-clearanswer-show-tell':scope='ClearAnswer shows its actual landing interface only; no model-driven audit or external model call was run for this film.'
 elif r.name=='claude-liam-cohort-firewall-show-tell':scope='Cohort Firewall shows verbatim local CLI result excerpts, not a browser demo.'
 elif r.name=='claude-liam-hippa-cratic-show-tell':scope="HIPPA-cratic's SQL cross-check returned 16 matching sample identifiers and step counts in the observed synthetic example. This is distinct from the other team's Cohort Studio. Camera movement presents captured frames, not newly executed interaction."
 text='# '+m['title']+'\n\nLocal Liam narration (Kokoro am_onyx). Promotional introduction; detailed audit remains separately available.\n\n'
 for b in d['beats']:text+='## '+b['beat_id']+'\n\n'+b['narration_text']+'\n\n'
 (r/'SCRIPT.md').write_text(text.rstrip()+'\n')
 (r/'FACTCHECK.md').write_text('''# Film evidence ledger

This selective promotional introduction does not replace the independent review. Source pins and actual capture locations are in [SOURCES.md](SOURCES.md); observed runs are in [SESSION.md](SESSION.md). No official judging score, clinical validation or production readiness is claimed.

| Beat | Narration | Evidence category |
|---|---|---|
'''+''.join('| '+b['beat_id']+' | '+b['narration_text'].replace('|','\\|')+' | '+('Supplied sponsor identity and pinned README team attribution' if b['beat_id'] in ['BOPEN','BOUT'] else 'Actual recorded local interface or command output; read scope below' if b['shot']['remotion']['pattern'] in ['BrowserCapture','CCPlainShell'] else 'Proposed development or suggested exercise, not a completed feature' if b['beat_id'] in ['B06','B07','B11','B12','BHTF'] else 'Source-grounded explanation/interpretation; conceptual visual')+' |\n' for b in d['beats'])+'''
## Scope for this film

All demonstrated data are invented/synthetic. '''+scope+'''

The suggested prompt is not shown as an executed agent response. Conceptual animations explain structure; they are not simulated app results. Next steps preserve the concerns in the full reviews and do not imply fixes have been implemented.
''')
for name in ['OncosysLecture.tsx','OncosysProcess.tsx','BrowserCapture.tsx']:
 shutil.copy2(art/'runtime/remotion/src/scenes'/name,y/'render-source'/name)
print('Refreshed nine scripts/evidence ledgers and renderer source snapshots.')
