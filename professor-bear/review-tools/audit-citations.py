from pathlib import Path
from urllib.parse import urlparse,unquote
import re,subprocess,json,datetime,argparse
root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description='Check pinned source citation paths and line bounds against local Git clones; does not execute submissions.')
parser.add_argument('--books-dir',type=Path,default=root.parent.parent,help='Parent folder containing the named submission clones')
books=parser.parse_args().books_dir.resolve()
mapping={'a7ussein/readyset-control-tower':'readyset-control-tower','adhithyan245/tripwire':'tripwire','aravindkumar2504/identity-crisis-control-tower':'identity-crisis-control-tower','giorgikarazanashvili/busybeavers':'BusyBeavers','tammy357/oncosys-cohort-studio':'oncosys-cohort-studio','saigunavardhan/sns-cohort-control-tower':'sns-cohort-control-tower','dislevek/oncosys-hackathon-challenge':'oncosys-hackathon-challenge'}
cache={};refs=[];fail=[]
for p in root.glob('*/*.md'):
 if not (p.name=='REPORT.md' or p.name.startswith('audit-') or p.name.startswith('coverage-') or p.name.startswith('runtime-reconciliation-')):continue
 for url in sorted(set(re.findall(r'https://github\.com/[^\s)<>]+',p.read_text()))):
  u=urlparse(url);a=u.path.strip('/').split('/');key='/'.join(a[:2]).lower()
  if len(a)<5 or a[2]!='blob' or key not in mapping:continue
  sha=a[3];path=unquote('/'.join(a[4:]));ck=(key,sha,path)
  if ck not in cache:
   got=subprocess.run(['git','show',f'{sha}:{path}'],cwd=books/mapping[key],text=True,capture_output=True);cache[ck]=got.stdout.splitlines() if got.returncode==0 else None
  lines=cache[ck];nums=[int(x) for x in re.findall(r'L(\d+)',u.fragment)];ok=lines is not None and all(1<=n<=len(lines) for n in nums);row={'document':str(p.relative_to(root)),'url':url,'line_count':len(lines) if lines is not None else None,'valid_path_and_lines':ok};refs.append(row)
  if not ok:fail.append(row)
out={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'All recognized pinned GitHub blob links in primary reports, companion audits, coverage notes and runtime reconciliation notes. Verifies local Git object/path and cited line bounds, not scientific correctness or whether claims follow from cited code.','references':len(refs),'distinct_files':len(cache),'invalid':fail,'checks':refs};(root/'review-tools/citation-audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'references':len(refs),'distinct_files':len(cache),'invalid':fail},indent=2))
