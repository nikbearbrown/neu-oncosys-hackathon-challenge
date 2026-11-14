"""Author selective promotional films; never modify independent review findings."""
import copy, json, shutil
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[2]
base = json.loads((root/'youtube/claude-liam-readyset-show-tell/beat_sheet.json').read_text())
templates = {b['beat_id']: b for b in base['beats']}
projects = json.loads(Path(__file__).with_name('projects.json').read_text())

for c in projects:
    slug = 'claude-liam-'+c['slug']+'-show-tell'
    r = root/'youtube'/slug
    r.mkdir(exist_ok=True)
    if (r/'beat_sheet.json').exists():
        raise RuntimeError(f'Refusing to overwrite authored film: {r}')
    (r/'captures').mkdir(exist_ok=True)
    beats = []
    def add(template, bid, narration, props=None, act=None):
        b = copy.deepcopy(templates[template])
        for k in list(b):
            if k not in ['beat_id','act','lane','proof_gate','narration_text','estimated_duration_s','voice','engine','shot','lead_silence_s','tail_silence_s','kind','qc']:
                del b[k]
        b['beat_id'], b['narration_text'] = bid, narration
        b['estimated_duration_s'] = round(len(narration.split())/2.6, 2)
        if act: b['act'] = act
        for k in list(b['shot']):
            if k not in ['type','source','visual_intent','motion_claim','show','remotion','template','narration_contract','motion']:
                del b['shot'][k]
        if props is not None:
            b['shot']['remotion']['props'] = props
        if 'remotion' in b['shot']:
            b['shot']['remotion'] = {k:v for k,v in b['shot']['remotion'].items() if k in ['pattern','props']}
            b['shot']['remotion']['props'].pop('durationSeconds',None)
        beats.append(b)
        return b
    def flow(bid,narr,title,labels,act='The Useful Idea',note='Conceptual illustration'):
        return add('B01',bid,narr,dict(title=title,labels=labels,objectKinds=['document','adapter','monitor'],diagramStyle='show-tell-isometric',mode='flow',note=note,cues=[.1,.28,.65,.82]),act)
    add('BOPEN','BOPEN',c['title']+'. '+c['payoff']+'.')
    add('BIDEA','BIDEA','Hallo. This is Liam, in for Bear. '+c['idea'],dict(text=c['payoff']+'.',triggerWords='inspectable evidence',replacementWords='evidence supports action',fontSize=66,charMs=22,hesitateBetween=6,hesitateWithin=1,mistakeRate=2,jitter=20,seed=slug,banner=''))
    add('BDEFS','BDEFS','Three terms. '+' '.join(t+' means '+m[0].lower()+m[1:]+'.' for t,m in c['terms']),dict(title='Terms In This Film',terms=[dict(term=t,meaning=m) for t,m in c['terms']],folderLabel='@NikBearBrown'))
    flow('B01',c['framework'],c['payoff'],c['labels'])
    sources=[]
    for i,(file,narr) in enumerate(c['shots']):
        p=r/'captures'/file
        if not p.exists():
            source=root/'professor-bear'/c['slug']/'evidence'/file
            shutil.copy2(source,p)
            sources.append(str(source.relative_to(root)))
        else: sources.append('captures/'+file)
        w,h=Image.open(p).size
        # Full first view, then focus on a different area of repeated screenshots.
        focus = (.5,.40,1.15) if i==0 else (.5,.67,1.3)
        if c['slug']=='clearanswer': focus=(.5,.35,1.3)
        add('B03','B'+str(i+2).zfill(2),narr,dict(url='Local research prototype',image=f'oncosys-films/{slug}/{file}',imageAspect=w/h,caption=c['name']+' · actual local '+('interface only' if c['slug']=='clearanswer' else 'synthetic demonstration'),moves=[dict(at=0,x=.5,y=.5,scale=1),dict(at=.22,x=focus[0],y=focus[1],scale=focus[2])],moveSeconds=.8))
    if c['slug']=='cohort-firewall':
        text=Path('/tmp/oncosys-runtime-k2vhjg41/cohort-film-output.txt').read_text()
        (r/'captures/cli-output.txt').write_text(text)
        for bid,narr,lines in [
            ('B02','Here is an actual local command-line result using the supplied synthetic clean variant. The engine returns Ready, with no findings, and its certificate verifies. This is an engine demonstration, not evidence of clinical readiness.',['$ evaluate_dataset(clean)','clean: READY','Certificate verifies: True','Findings: 0']),
            ('B03','Now the supplied synthetic missingness variant returns Conditional, with one finding. The certificate verifies here too. A valid signature and a favorable readiness verdict answer different questions. The interface should keep that distinction clear.',['$ evaluate_dataset(feature_missingness)','feature_missingness: CONDITIONAL','Certificate verifies: True','Findings: 1'])]:
            b=add('B03',bid,narr,dict(title='Cohort Firewall · actual stdout excerpt',lines=lines,fontSize=40,lineGap=18,startCue=.1,windowMargin=90))
            b['shot']['remotion']['pattern']='CCPlainShell'
        sources.append('captures/cli-output.txt')
    flow('B10',c['strength'],'Build On The Foundation',c['labels'])
    flow('B11',c['next1'],'Next: Strengthen The Contract',['Evidence','Decision','Record'],'Build On The Foundation','Proposed next step · not a completed feature')
    flow('B12',c['next2'],'Next: Test The Boundaries',['Input','Check','Explain'],'Build On The Foundation','Proposed next step · not a completed feature')
    flow('B13','Keep the strengths and make the boundaries more explicit. This is a research prototype, and a useful starting point for further development. The linked independent review contains the detailed evidence and remaining limitations.','A Foundation To Build On',['Inspect','Learn','Improve'], 'Build On The Foundation','Research prototype · not clinical or production validation')
    add('BVDT','BVDT',"Let's recap with Claude. "+' '.join(c['recap']),dict(artifactTitle=c['name'],artifactHeading='What To Build On',artifactLines=c['recap'],lectureLayout=True,brandLabel='@NikBearBrown'))
    add('BHTF','BHTF',c['prompt'],dict(greeting='Your turn.',topic='CLAUDE · YOUR TURN',segment='Test The Boundary',command=c['prompt'],runningText='Suggested prompt — not an executed agent response',output=['Check: evidence supports the decision.','Check: unresolved questions remain visible.'],folderLabel='@NikBearBrown',modelLabel='Your chosen model',effortLabel='Review',largeText=True))
    add('BOUT','BOUT',c['title']+'. At Nik Bear Brown.',dict(title=c['title'],slug=slug,handle='@NikBearBrown',subline=''))
    md=copy.deepcopy(base['metadata']);md.pop('build',None)
    md.update(slug=slug,title=c['title'],lecture_opening_description=c['payoff'],source_doc=f"../../professor-bear/{c['slug']}/"+('report.md' if c['slug']=='clearanswer' else 'REPORT.md'),tags=[c['name'],'AI Healthcare Hackathon','Evidence','Research Tools'])
    (r/'beat_sheet.json').write_text(json.dumps(dict(metadata=md,beats=beats),indent=2)+'\n')
    review=f"https://github.com/nikbearbrown/neu-oncosys-hackathon-challenge/tree/main/professor-bear/{c['slug']}"
    (r/'SOURCES.md').write_text(f"# Sources\n\nPinned submission: https://github.com/{c['repo']}/tree/{c['sha']}\n\nIndependent review: {review}\n\nActual local captures: "+', '.join(sources)+". All demonstrated inputs are synthetic. ClearAnswer shows its interface only, without a model audit. Diagrams are conceptual; next-step diagrams are proposals. No clinical validation or official judging score.\n\nLiam: local Kokoro am_onyx; approved Brutalist portrait and registered components. No paid generation or new stock imagery.\n")
    (r/'ACTS.md').write_text('# Selective promotional feedback\n\nThe source reports remain authoritative and unchanged. Opening and definitions establish the terms; the framework precedes actual examples; strengths lead into constructive next steps. The recap and suggested prompt invite further work.\n\nLEFT OUT: exhaustive failure cases, numeric test tables and rubric analysis remain in the linked review. Omission is an editorial choice for the requested promotional introduction, not withdrawal or resolution of findings.\n')
    (r/'FACTCHECK.md').write_text('# Claim review\n\n| Beat | Narration | Basis |\n|---|---|---|\n'+''.join('| '+b['beat_id']+' | '+b['narration_text'].replace('|','/')+' | '+('Proposal or viewer exercise' if b['beat_id'] in ['B11','B12','BHTF'] else 'Pinned independent review and actual captures; concepts/framing are not new empirical claims')+' |\n' for b in beats))
    (r/'SHOTLIST.md').write_text('# Visual work order\n\n'+''.join('- '+b['beat_id']+': '+b['shot'].get('remotion',{}).get('pattern','Approved lecture title')+' — '+b['act']+'\n' for b in beats))
    for name in ['PROMPTS.md','BUILD-PROMPT.md']:
        shutil.copy2(root/'youtube/claude-liam-readyset-show-tell'/name,r/name)
    (r/'BUILD-LOG.md').write_text('# Build log\n\n2026-11-14: authored promotional overview. Local free narration and canonical Remotion renderer. Actual final checks pending.\n')
    (r/'CHECKS-REPORT.md').write_text(f'# Pre-render checks\n\n{len(beats)} beats. Framework before examples. Proposed changes labeled. No official score, clinical endorsement, or fabricated tool result. Final visual, typography and media checks pending.\n')
    print(slug,len(beats))
