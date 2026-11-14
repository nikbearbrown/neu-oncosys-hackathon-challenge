"""Run against the pinned inspected checkout. No app import or model calls."""
import ast, copy, importlib.util, json, sys
from pathlib import Path
root=Path(sys.argv[1])
spec=importlib.util.spec_from_file_location('submitted_tolerance',root/'core/tolerance.py')
tol=importlib.util.module_from_spec(spec);spec.loader.exec_module(tol)
for claim,actual in [('50.1% are LumA and 90% are Basal','50% are LumA; 10% are Basal'),('About 100 patients were reviewed; 99 responded','101 reviewed; 1 responded')]:
 print(json.dumps({'claim':claim,'correct':actual,'observed_note':tol.check_tolerance(claim,actual)}))
module=ast.parse((root/'app.py').read_text())
f=next(n for n in module.body if isinstance(n,ast.FunctionDef) and n.name=='_prepare_for_submission')
ns={'copy':copy};exec(compile(ast.Module(body=[f],type_ignores=[]),'submitted export function','exec'),ns)
a={'findings':[{'id':'F1','claim_verdict':'insufficient_evidence','confidence':'low','evidence':[],'needs_human_review':True}]}
print(json.dumps(ns['_prepare_for_submission'](a)))
print(json.dumps(ns['_prepare_for_submission'](a,[{'finding_id':'F1','decision':'override','verdict':'supported'}])))
