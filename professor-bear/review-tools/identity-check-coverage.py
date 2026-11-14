from pathlib import Path
import sys,json,datetime
b=Path(__file__).resolve().parent;sys.path.insert(0,str(b/'identity-browser/identity-crisis-control-tower'));from tower.checks import load_all,CHECKS,LOAD_ERRORS
from tower.cards import list_cards
load_all();cards=list_cards();out={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'registered_checks':sorted(CHECKS),'load_errors':LOAD_ERRORS,'cards':[{'id':c['id'],'required':c.get('checks',[]),'missing_registered':[n for n in c.get('checks',[]) if n not in CHECKS]} for c in cards],'scope':'Actual module imports in isolated Python3.14.6 test environment; availability is not correctness of each check.'};(b/'identity-check-coverage.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
