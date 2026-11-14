"""Aggregate-only eligibility/independence audit; never emit participant identifiers."""
from pathlib import Path
from collections import Counter
import sys,json
import pandas as pd
repo=Path(sys.argv[1]);sys.path.insert(0,str(repo))
from tower.robustness import a1_frames,a1_range,range_method
raw=repo.parent/'oncosys-hackathon-challenge/data/tcga-brca/raw';clinical=pd.read_csv(raw/'clinical.tsv',sep='\t',low_memory=False);protein=pd.read_csv(raw/'protein_rppa.tsv.gz',sep='\t',index_col=0);r=a1_frames(clinical,protein);c=Counter(str(x)[:12] for x in r['samples']);out={'public_release_A':{'eligible_samples':len(r['samples']),'barcode_derived_patients':len(c),'patients_with_multiple_eligible_samples':sum(v>1 for v in c.values()),'maximum_samples_per_patient':max(c.values()),'measured_positive':len(r['pos']),'measured_negative':len(r['neg'])},'method':range_method()}
# Same patient-level values copied into multiple specimens: probes the stated independence assumption only.
import numpy as np
base={'pos':np.array([0.,1.,2.,3.,4.,5.]),'neg':np.array([-1.,0.,1.,2.,3.,4.])};repeat={k:np.repeat(v,10) for k,v in base.items()};lo,hi=a1_range(base);rl,rh=a1_range(repeat);out['synthetic_repeated_specimens']={'independent_patients_per_group':6,'specimens_per_patient':10,'base_interval':[lo,hi],'repeated_specimen_interval':[rl,rh],'base_width':hi-lo,'repeated_specimen_width':rh-rl,'interpretation':'The function treats supplied specimens as independent. This fixture shows the assumption matters; it is not evidence that the public cohort contains these repeats.'}
print(json.dumps(out,indent=2))
