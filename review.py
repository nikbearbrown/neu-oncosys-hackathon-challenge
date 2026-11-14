#!/usr/bin/env python3
"""Bounded, non-executing Git object inspection and evidence-checked reports."""
import argparse
import base64
import hashlib
import html
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from datetime import datetime, timezone
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
RUBRICS = json.loads((ROOT / 'rubrics.json').read_text())
RULES = json.loads((ROOT / 'rule-index.json').read_text())
MAX_FILE = 200_000
MAX_TOTAL = 4_000_000
MAX_FILES = 160
TEXT_EXT = {'.md','.txt','.py','.js','.jsx','.ts','.tsx','.json','.yaml','.yml','.toml','.css','.html','.sql','.sh','.r','.rs','.go','.java','.vue','.svelte'}
STATES = {'observed','not_found_in_scope','not_tested','needs_human_judgment'}
KINDS = {'strength','gap','question'}
SECRET = re.compile(r"(?i)(?:gh[pousr]_[A-Za-z0-9_]{16,}|github_pat_[A-Za-z0-9_]{16,}|sk-[A-Za-z0-9_-]{16,}|AKIA[A-Z0-9]{16}|-----BEGIN [^-]*PRIVATE KEY-----|(?:password|passwd|secret|api[_-]?key|access[_-]?token)[\"']?\s*[=:]\s*[^\s,;]+)")


def redact(text):
    # Suppress the whole affected line, preserving line numbers, not fragments.
    text = re.sub(r'-----BEGIN [^-]*PRIVATE KEY-----.*?-----END [^-]*PRIVATE KEY-----', lambda m: '\n'.join('[REDACTED: private key]' for _ in m.group().split('\n')), text, flags=re.S)
    return '\n'.join('[REDACTED: possible credential]' if SECRET.search(line) else line for line in text.split('\n'))


def safe_text(value):
    text = html.escape(redact(str(value))).replace('\x1b', '').replace('|', '&#124;')
    return re.sub(r'([\\`*_{\[\]()#!])', r'\\\1', text)


def run(argv, cwd=None):
    env = {k:v for k,v in os.environ.items() if not k.startswith('GIT_')}
    env.update({'GIT_TERMINAL_PROMPT':'0','GIT_CONFIG_NOSYSTEM':'1','GIT_CONFIG_GLOBAL':os.devnull,'GIT_NO_REPLACE_OBJECTS':'1'})
    try:
        p = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, timeout=60)
    except (subprocess.TimeoutExpired, OSError) as exc:
        raise ValueError('Source command unavailable or timed out; no code executed.') from exc
    if p.returncode:
        # Remote stderr can contain credentials or hostile text. Do not echo it.
        raise ValueError('Source could not be read (access, missing object, or network failure); review incomplete.')
    return p.stdout


def git(repo, *args):
    return run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args],cwd=repo)


def api(endpoint):
    return json.loads(run(['gh','api',endpoint]))


def valid_path(path):
    p = PurePosixPath(path)
    return bool(path) and not p.is_absolute() and '..' not in p.parts and not any(ord(c)<32 for c in path) and '\\' not in path


def excluded(path):
    p = PurePosixPath(path)
    names = {x.lower() for x in p.parts}
    if not valid_path(path): return 'unsafe path'
    if any(x.startswith('.env') for x in names) or names & {'secrets','credentials','private','answer-keys','answer_keys','sealed','envelopes','raw','data','datasets','node_modules','vendor','.git'}:
        return 'sensitive, data, sealed, or dependency path'
    if any(x in p.name.lower() for x in ('secret','credential','answer-key','answer_key','private-key','lock.')) or p.name.endswith('.lock'):
        return 'sensitive or generated filename'
    if p.suffix.lower() not in TEXT_EXT and p.name.lower() not in {'dockerfile','makefile','license'}:
        return 'non-allowlisted file type'
    return None


def read_snapshot(sub):
    sha = sub['commit']
    if not re.fullmatch(r'[a-f0-9]{40}',sha): raise ValueError('commit must be a full lowercase 40-character Git SHA')
    repo = sub.get('repo','')
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repo): raise ValueError('repo must be owner/name, not a URL or shell command')
    local = sub.get('local_path')
    if local:
        local = str(Path(local).resolve())
        actual = git(local,'rev-parse','--verify',sha+'^{commit}').decode().strip()
        if actual != sha: raise ValueError('commit did not resolve exactly')
        rows = git(local,'ls-tree','-r','-l','-z',sha).split(b'\0')
        tree=[]
        for row in rows:
            if not row: continue
            head,path = row.split(b'\t',1)
            mode,typ,oid,size = head.decode().split()
            tree.append({'path':path.decode('utf-8','replace'),'mode':mode,'type':typ,'sha':oid,'size':int(size) if size!='-' else 0})
        def blob(e): return git(local,'cat-file','blob',e['sha'])
        truncated=False
    else:
        result=api(f'repos/{repo}/commits/{sha}')
        if result['sha'] != sha: raise ValueError('GitHub commit mismatch')
        data=api(f'repos/{repo}/git/trees/{sha}?recursive=1')
        tree=data['tree']; truncated=data.get('truncated',False)
        def blob(e):
            d=api(f'repos/{repo}/git/blobs/{e["sha"]}')
            if d.get('encoding')!='base64': raise ValueError('Unsupported blob encoding')
            return base64.b64decode(d['content'])
    packet={'toolkit_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rubric_sha256':hashlib.sha256((ROOT/'rubrics.json').read_bytes()).hexdigest(),'schema_version':1,'submission':sub['id'],'repo':repo,'commit':sha,'track':sub['track'],
            'collected_at':datetime.now(timezone.utc).isoformat(),'collection':'partial' if truncated else 'complete_with_exclusions',
            'tree_truncated':truncated,'files':{},'skipped':[],'limits':{'file_bytes':MAX_FILE,'total_bytes':MAX_TOTAL,'files':MAX_FILES},
            'runtime':'not_tested','claims':'Source evidence only; no installs, builds, tests, images, datasets or demos executed.'}
    total=0
    for e in sorted(tree,key=lambda e:e['path']):
        if e['type']=='tree': continue
        path=e['path']; reason=excluded(path)
        if e.get('mode') not in {'100644','100755'} or e['type']!='blob': reason='symlink, submodule or non-regular Git entry'
        if e.get('size',MAX_FILE+1)>MAX_FILE: reason='file-size limit'
        if reason:
            packet['skipped'].append({'path':path,'reason':reason}); continue
        if len(packet['files'])>=MAX_FILES or total+e['size']>MAX_TOTAL:
            packet['skipped'].append({'path':path,'reason':'collection budget'}); packet['collection']='partial'; continue
        try:
            b=blob(e)
            if len(b)>MAX_FILE or len(b)!=e['size']: raise ValueError('Blob size mismatch')
            oid=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
            if oid!=e['sha']: raise ValueError('Git blob hash mismatch')
            if b'\x00' in b: raise UnicodeError('binary')
            text=b.decode('utf-8')
        except UnicodeError:
            packet['skipped'].append({'path':path,'reason':'binary or non-UTF-8'}); continue
        except (ValueError, KeyError):
            packet['skipped'].append({'path':path,'reason':'blob unavailable or verification failed'}); packet['collection']='partial'; continue
        clean=redact(text)
        packet['files'][path]={'blob':oid,'source_sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'redacted':clean!=text,'lines':clean.splitlines()}
        total+=len(b)
    packet['collected_bytes']=total
    return packet


def review_template(packet,mode):
    return {'mode':mode,'repo':packet['repo'],'commit':packet['commit'],'track':packet['track'],
            'reviewer':'','summary':'Review not yet performed.','limitations':['Runtime, accessibility, data correctness, demonstrations and unseen inputs have not been tested.'],
            'criteria':[{'id':c['id'],'status':'not_tested','assessment':'Not reviewed yet.','findings':[],
                         'next_check':'Inspect implementation and evidence for: '+c['criterion']} for c in RUBRICS[str(packet['track'])]],
            'judge_scores':None}


def write_json(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')


def inspect(manifest,out):
    m=json.loads(Path(manifest).read_text()); mode=m.get('mode','student')
    if mode not in {'student','judge'}: raise ValueError('mode must be student or judge')
    subs=m['submissions']; ids=[s['id'] for s in subs]
    if len(set(ids))!=len(ids) or any(not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',i) for i in ids): raise ValueError('unique lowercase kebab-case submission IDs required')
    if any(s['track'] not in (1,2) or type(s['track']) is not int for s in subs): raise ValueError('track must be 1 or 2')
    out=Path(out)
    if out.exists(): raise ValueError('Use a new output directory to preserve earlier reviews.')
    out.mkdir(parents=True)
    index=[]
    for sub in subs:
        dest=out/sub['id']
        try:
            packet=read_snapshot(sub)
            write_json(dest/'packet.json',packet)
            write_json(dest/'review.json',review_template(packet,mode))
            state=packet['collection']
        except (ValueError,KeyError) as exc:
            state='incomplete'; write_json(dest/'error.json',{'status':state,'reason':str(exc),'submission':sub['id'],'score':None})
        index.append({'id':sub['id'],'status':state})
    write_json(out/'index.json',index)
    print(f'Prepared {len(index)} submission records. No submission code executed. See {out}/index.json')


def check_evidence(packet,ev):
    path=ev['path']; start=ev['start']; end=ev['end']
    if path not in packet['files']: raise ValueError('Evidence path was not collected')
    lines=packet['files'][path]['lines']
    if type(start) is not int or type(end) is not int or not 1<=start<=end<=len(lines): raise ValueError('Evidence line range invalid')
    if end-start>30: raise ValueError('Keep evidence excerpts to at most 31 lines')
    exact='\n'.join(lines[start-1:end])
    if not exact.strip() or ev['quote']!=exact: raise ValueError('Evidence quote must exactly match the collected lines')
    if '[REDACTED:' in exact: raise ValueError('Do not quote potentially sensitive lines; request confidential review instead')
    return f'https://github.com/{packet["repo"]}/blob/{packet["commit"]}/{quote(path,safe="/")}#L{start}-L{end}'


def validate_review(packet,review):
    if review['mode'] not in {'student','judge'}: raise ValueError('Invalid mode')
    for key in ['repo','commit','track']:
        if review[key]!=packet[key]: raise ValueError('Review/packet identity mismatch')
    rubric=RUBRICS[str(packet['track'])]
    if [c['id'] for c in review['criteria']] != [c['id'] for c in rubric]: raise ValueError('All seven criteria required in rubric order')
    for c in review['criteria']:
        if c['status'] not in STATES or not c['assessment'].strip() or not c['next_check'].strip(): raise ValueError('Criterion needs status, assessment and next check')
        if c['status']=='observed' and not c['findings']: raise ValueError('Observed criterion requires evidence-backed findings')
        for f in c['findings']:
            if f['kind'] not in KINDS or f['priority'] not in {'P0','P1','P2'}: raise ValueError('Invalid finding kind or priority')
            for key in ['title','observation','impact','recommendation','acceptance_check','confidence']:
                if not isinstance(f.get(key),str) or not f[key].strip(): raise ValueError('Finding missing '+key)
            if not f['evidence']: raise ValueError('Every finding needs evidence; use not_found_in_scope or not_tested for absent evidence')
            for ev in f['evidence']: check_evidence(packet,ev)
            if any(r not in RULES for r in f.get('rules',[])): raise ValueError('Unknown supplemental rule ID')
    scores=review.get('judge_scores')
    if scores is not None:
        if review['mode']!='judge': raise ValueError('Student feedback cannot contain judge scores')
        if scores.get('human_reviewed') is not True or not scores.get('reviewer','').strip(): raise ValueError('Scores require explicit human review attribution')
        if set(scores['values'])!={c['id'] for c in rubric}: raise ValueError('Scores must cover all seven criteria')
        for c in rubric:
            val=scores['values'][c['id']]
            if isinstance(val,bool) or not isinstance(val,(int,float)) or not math.isfinite(val) or not 0<=val<=c['points']: raise ValueError('Score outside allowed range')
    return True


def render(packet,review):
    validate_review(packet,review)
    title='Student feedback' if review['mode']=='student' else 'Judge review aid'
    out=[f'# {title}: {safe_text(packet["submission"])}','',f'Repository: https://github.com/{packet["repo"]}',f'Commit: `{packet["commit"]}`',f'Track: {packet["track"]}',f'Reviewer: {safe_text(review["reviewer"] or "not assigned")}',
         '', '**Not an official result. Source review does not establish runtime behavior.**','',safe_text(review['summary']),'',
         '## Coverage and limitations','',f'Collection: {packet["collection"]}; {len(packet["files"])} text files; {len(packet["skipped"])} excluded entries; recursive tree truncated: {packet["tree_truncated"]}.',
         'Runtime: not tested by this toolkit. Git blob identity and evidence line/quote consistency were checked.', '']
    out.extend('- '+safe_text(x) for x in review['limitations'])
    out+=['','## Priorities','']
    findings=[(c,f) for c in review['criteria'] for f in c['findings']]
    for c,f in sorted(findings,key=lambda cf:cf[1]['priority']): out.append(f'- {f["priority"]} · {c["id"]} · {safe_text(f["title"])}: {safe_text(f["recommendation"])}')
    if not findings: out.append('No reviewed findings yet. Complete the evidence review before sharing conclusions.')
    for c,rule in zip(review['criteria'],RUBRICS[str(packet['track'])]):
        out+=['',f'## {c["id"]}: {rule["criterion"]}','',f'Status: **{c["status"]}**', '',safe_text(c['assessment']),'']
        for f in c['findings']:
            out += [f'### {safe_text(f["title"])}', '',f'{f["kind"]} · {f["priority"]} · Confidence: {safe_text(f["confidence"])}','',safe_text(f['observation']),'']
            for ev in f['evidence']:
                link=check_evidence(packet,ev)
                out+=[f'[Source lines {ev["start"]}–{ev["end"]}]({link})','']
                out += ['> '+safe_text(line) for line in ev['quote'].splitlines()]
                out+=['']
            out += ['Supplemental rules: '+(', '.join(f.get('rules',[])) or 'None cited; official criterion above applies.'),'']
            out += ['Impact: '+safe_text(f['impact']),'','Concrete change: '+safe_text(f['recommendation']),'','Acceptance check: '+safe_text(f['acceptance_check']),'']
        out+=['Next evidence/check: '+safe_text(c['next_check'])]
    if review.get('judge_scores'):
        scores=review['judge_scores'];out+=['','## Human-reviewed proposed scores','',f'Reviewer: {safe_text(scores["reviewer"])}. Final organizer decision remains separate.','']
        for c in RUBRICS[str(packet['track'])]: out.append(f'- {c["id"]}: {scores["values"][c["id"]]}/{c["points"]}')
        out+=['',f'Total: {sum(scores["values"].values())}/100']
    out+=['','## Excluded scope','']
    out.extend(f'- {safe_text(s["path"])}: {safe_text(s["reason"])}' for s in packet['skipped'])
    return '\n'.join(out)+'\n'


def report(packet_path,review_path,out):
    packet=json.loads(Path(packet_path).read_text()); review=json.loads(Path(review_path).read_text())
    rendered=render(packet,review)
    out=Path(out);out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('x') as f: f.write(rendered)


def report_all(work,out):
    work=Path(work);out=Path(out)
    if out.exists(): raise ValueError('Use a new report directory.')
    out.mkdir(parents=True);index=['# Submission review index','','No automatic ranking or official scores.','']
    for entry in json.loads((work/'index.json').read_text()):
        name=entry['id']; folder=work/name
        try:
            if (folder/'error.json').exists(): raise ValueError('Source unavailable; review incomplete')
            report(folder/'packet.json',folder/'review.json',out/(name+'.md'))
            index.append(f'- [{name}]({name}.md) — evidence record rendered; judge review still required')
        except (ValueError,OSError,KeyError) as exc:
            index.append(f'- {safe_text(name)} — INCOMPLETE: {safe_text(exc)}; no score')
    (out/'README.md').write_text('\n'.join(index)+'\n')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    sp=p.add_subparsers(dest='cmd')
    sp.add_parser('help',help='Show overview and tutorial location')
    a=sp.add_parser('inspect',help='Read pinned Git objects without checkout or execution');a.add_argument('--manifest',required=True);a.add_argument('--out',required=True)
    a=sp.add_parser('report',help='Validate evidence and render a reviewer-completed record');a.add_argument('--packet',required=True);a.add_argument('--review',required=True);a.add_argument('--out',required=True)
    a=sp.add_parser('report-all',help='Render all completed records and an index');a.add_argument('--work',required=True);a.add_argument('--out',required=True)
    args=p.parse_args()
    try:
        if args.cmd=='inspect': inspect(args.manifest,args.out)
        elif args.cmd=='report': report(args.packet,args.review,args.out)
        elif args.cmd=='report-all': report_all(args.work,args.out)
        else:
            p.print_help(); print('\nTutorial: docs/tutorial.md\nReviewer workflow: prompts/reviewer.md\nNo submission code is executed. No automatic scores.')
    except (ValueError,KeyError,OSError,json.JSONDecodeError) as exc:
        print('Cannot complete: '+redact(str(exc)),file=sys.stderr);return 2
    return 0

if __name__=='__main__': sys.exit(main())
