# Professor Bear Audit: SNS Control Tower: Reconstruction Follow-Through

## Review Identity

This is an independent, provisional source-code audit for judge deliberation. It is not an official grade.

- Entry: `saigunavardhan/sns-cohort-control-tower`
- Commit: `c1e8b79a2987cee6087d847867f9895deaa109a4`
- Organizer reference: `6e15a399a64ffbf80778db0b462ac239e70086b9`
- Product: `cohort-control-tower`; Track 1, Cohort Firewall
- Pass: 3; reviewed 2026-11-14T20:19:52.111587+00:00
- Runtime: **not executed**; official freeze/receipt: **not verified**

## Executive Assessment

Following the cohort export through its standalone reconstruction reveals three additional source-level concerns: missing required filter inputs leave membership unchanged, the main engine and reconstruction use different clinical-file fallback policies, and the A2 specification embeds JSON true in Python source. These findings concern the exported workflow, not the separate detector's measured accuracy. No submission or generated program was executed in this pass.

## Workflow Traced

The built-in A1/A2 specifications include require_value steps. The main cohort engine loads clinical data from B or falls back to A, conditionally applies those filters, and returns membership and a step log. The CLI writes the cohort and generates a standalone Python script by concatenating source strings. The web route invokes this CLI and treats a successful process plus an existing CSV as a successful cohort export.

## Findings At A Glance

| ID | Type | Priority | Finding |
|---|---|---|---|
| SN-08 | gap | P1 | A missing required filter input silently leaves the cohort unchanged |
| SN-09 | gap | P1 | The main cohort and reconstruction use different clinical inputs |
| SN-10 | gap | P1 | The A2 reconstruction embeds a JSON boolean as a Python name |

## Inspection Scope

The following files informed the implementation-level conclusions in this pass. Other collected files are not automatically treated as reviewed:

- `sns/engine/cohort.py`
- `sns/cohort.py`
- `sns/server.py`

## Parallel Review Preservation

Existing reports were read and retained. This is a separately versioned supplement; prior conclusions are not silently replaced.

The existing REPORT.md, TESTS.md and codex-23484638 pass-01 supplement remain unchanged. Their repair-authority, flag-restoration, verdict and layout concerns are not new findings here. This focused follow-through adds SN-08 through SN-10 from the same pinned source commit. Parallel runtime results in earlier reports are not claimed as this reviewer's observations, and none of the three new fixtures was executed here.

This pass does not accept earlier agents' findings as established merely because they were reported. Any correction must identify the earlier claim and the new evidence explicitly.

## Detailed Criterion Review

# Judge review aid: sns-cohort-control-tower

Repository: https://github.com/saigunavardhan/sns-cohort-control-tower
Commit: `c1e8b79a2987cee6087d847867f9895deaa109a4`
Track: 1
Reviewer: Professor Bear / Codex source review

**Not an official result. Source review does not establish runtime behavior.**

Following the cohort export through its standalone reconstruction reveals three additional source-level concerns: missing required filter inputs leave membership unchanged, the main engine and reconstruction use different clinical-file fallback policies, and the A2 specification embeds JSON true in Python source. These findings concern the exported workflow, not the separate detector&\#x27;s measured accuracy. No submission or generated program was executed in this pass.

## Coverage and limitations

Collection: complete_with_exclusions; 56 text files; 82 excluded entries; recursive tree truncated: False.
Runtime: not tested by this toolkit. Git blob identity and evidence line/quote consistency were checked.

Challenge reference: https://github.com/disleveK/oncosys-hackathon-challenge/tree/6e15a399a64ffbf80778db0b462ac239e70086b9

Product: cohort-control-tower

Product review route: Trace changes between releases to affected analyses, preserve unaffected analyses with reasons, and inspect findings.json in shared format v0.2. Equal row counts do not establish equal membership.

- Pinned local checkout, not a verified official final-submission receipt; branch names and later changes are outside this pass.
- Static source analysis only. No submission code, tests, installers, workflows, notebook, server, hosted endpoint or model was executed.
- No sealed envelopes, answer keys or raw clinical datasets were accessed. Numerical correctness, performance, accessibility and fresh-machine setup remain untested.
- Source-derived control-flow consequences are labeled as such. Proposed acceptance checks are not observed test results.
- The collected text budget is 160 files, 200 KB/file and 4 MB/entry. Complete\_with\_exclusions is not an exhaustive audit; exclusions and focused follow-ups are recorded.
- No official score, cross-team ranking, clinical validity or regulatory/accessibility certification is asserted.

## Priorities

- P1 · T1-1 · A missing required filter input silently leaves the cohort unchanged: Validate every required table and field before applying cohort steps. On missing evidence, stop the approved export or emit a visibly incomplete diagnostic result with an explicit skipped/error step and reason. Do not treat a missing prerequisite as a successful no-op.
- P1 · T1-5 · The main cohort and reconstruction use different clinical inputs: Share one versioned transformation implementation or serialize the exact resolved input map into the reconstruction. Make any cross-release fallback explicit and hash-bound, or reject missing B prerequisites consistently in both paths. Compare exact membership, not just row count.
- P1 · T1-5 · The A2 reconstruction embeds a JSON boolean as a Python name: Embed a safely quoted JSON string and call json.loads at runtime, or use repr for a supported Python-literal structure. Apply the same serialization rule to applied repairs and test booleans, null values, quotes and non-ASCII descriptions as data.

## T1-1: Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support.

Status: **observed**

This focused pass traces missing eligibility fields. A skipped prerequisite must remain distinguishable from a valid filtering decision.

### A missing required filter input silently leaves the cohort unchanged

gap · P1 · Confidence: High for the conditional branch and export caller. Full CLI and UI outcomes remain untested in this source pass.

Built-in A1 requires a usable ER status and A2 requires a nonempty subtype call. The require\_value branch filters working only if a clinical table exists and contains the requested column. There is no else error or unavailable state. With an existing recognized table lacking that column, the step can be logged with unchanged counts and the CLI proceeds to write the cohort.

[Source lines 9–20](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L9-L20)

> BUILTIN\_SPECS = \{
>     &quot;A1&quot;: \[
>         \{&quot;step&quot;: &quot;require\_file&quot;, &quot;file&quot;: &quot;protein\_rppa.tsv.gz&quot;},
>         \{&quot;step&quot;: &quot;filter\_sample\_type&quot;, &quot;type&quot;: &quot;01&quot;},
>         \{&quot;step&quot;: &quot;require\_value&quot;, &quot;column&quot;: &quot;breast\_carcinoma\_estrogen\_receptor\_status&quot;,
>          &quot;allowed&quot;: \[&quot;Positive&quot;, &quot;Negative&quot;\]},
>     \],
>     &quot;A2&quot;: \[
>         \{&quot;step&quot;: &quot;require\_file&quot;, &quot;file&quot;: &quot;clinical.tsv&quot;},
>         \{&quot;step&quot;: &quot;filter\_sample\_type&quot;, &quot;type&quot;: &quot;01&quot;},
>         \{&quot;step&quot;: &quot;require\_value&quot;, &quot;column&quot;: &quot;PAM50Call\_RNAseq&quot;, &quot;not\_empty&quot;: True},
>     \],

[Source lines 166–176](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L166-L176)

>         elif step\_name == &quot;require\_value&quot;:
>             col = step\_def\[&quot;column&quot;\]
>             allowed = step\_def.get\(&quot;allowed&quot;\)
>             not\_empty = step\_def.get\(&quot;not\_empty&quot;, False\)
>             if clinical is not None and col in clinical.columns:
>                 clin\_idx = clinical\[~clinical.index.duplicated\(\)\]
>                 if not\_empty:
>                     valid = \{s for s in working if s in clin\_idx.index and pd.notna\(clin\_idx.at\[s, col\]\)}
>                 else:
>                     valid = \{s for s in working if s in clin\_idx.index and clin\_idx.at\[s, col\] in allowed}
>                 working = valid

[Source lines 198–202](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L198-L202)

>         counts = \_step\_counts\(working\)
>         step\_rec.update\(counts\)
>         steps.append\(step\_rec\)
> 
>     return working, flagged, steps, all\_applied

[Source lines 163–189](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L163-L189)

>     working, flagged, steps, applied\_repairs = run\_cohort\(
>         spec, folder\_b, folder\_a, findings\_doc,
>         slides\_path=args.slides,
>     \)
> 
>     df = build\_cohort\_output\(working, flagged\)
> 
>     \# Duplicate check
>     if df\[&quot;sample\_id&quot;\].duplicated\(\).any\(\):
>         dupes = df\[df\[&quot;sample\_id&quot;\].duplicated\(keep=False\)\]\[&quot;sample\_id&quot;\].tolist\(\)
>         print\(f&quot;WARNING: duplicate sample\_ids detected: \{dupes\[:5\]}&quot;, flush=True\)
> 
>     csv\_path = out\_dir / &quot;cohort\_samples.csv&quot;
>     df.to\_csv\(csv\_path, index=False\)
> 
>     steps\_data = \{
>         &quot;analysis&quot;: analysis\_id,
>         &quot;release\_b&quot;: str\(folder\_b\),
>         &quot;release\_a&quot;: str\(folder\_a\),
>         &quot;steps&quot;: steps,
>         &quot;repairs\_applied&quot;: applied\_repairs,
>         &quot;n\_samples&quot;: len\(df\),
>         &quot;n\_flagged&quot;: int\(df\[&quot;flagged&quot;\].sum\(\)\),
>         &quot;n\_patients&quot;: int\(df\[&quot;patient\_id&quot;\].nunique\(\)\),
>     }
>     steps\_path = out\_dir / &quot;cohort\_steps.json&quot;
>     steps\_path.write\_text\(json.dumps\(steps\_data, indent=2, default=str\), encoding=&quot;utf-8&quot;\)

Supplemental rules: None cited; official criterion above applies.

Impact: Membership can include samples whose required eligibility cannot be evaluated. An unchanged count does not tell the researcher that the promised filter was skipped. This is a source-derived path for missing inputs, not an observed output on the event dataset.

Concrete change: Validate every required table and field before applying cohort steps. On missing evidence, stop the approved export or emit a visibly incomplete diagnostic result with an explicit skipped/error step and reason. Do not treat a missing prerequisite as a successful no-op.

Acceptance check: Use a valid invented clinical table with sample IDs but omit the ER column, then the subtype column. The corresponding built-in cohort must identify an unavailable eligibility test and must not present an ordinary filtered success. Retain a valid-field control.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-2: Reasoning for the research question. Changes its result appropriately when the research question or intended use changes.

Status: **not_tested**

A1/A2 built-in eligibility is explicit, but missing fields can bypass its intended meaning. Broader question reasoning remains in the retained first pass.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T1-3: Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion.

Status: **not_tested**

Record exactly which release and clinical table supplied each filter. A declared RELEASE\_A variable does not establish that reconstruction actually uses it.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T1-4: Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review.

Status: **not_tested**

These source paths raise evidence and reproducibility concerns. No deployed exploit, clinical harm, source-data mutation or official penalty is asserted.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T1-5: Working tool and clear setup. Judges can run the core workflow from the submitted repository.

Status: **observed**

Traceability reaches the actual CLI, web caller and generated script. Three concrete synthetic acceptance checks remain unexecuted by this reviewer.

### The main cohort and reconstruction use different clinical inputs

gap · P1 · Confidence: High for divergent source policies. The proposed parity fixture has not been executed.

run\_cohort falls back to clinical data from release A when none is loaded from B. The generated script looks only for B/clinical.tsv and skips require\_value when that clinical object is None. Although it declares RELEASE\_A, the generated clinical-loading and filter path does not reproduce the main engine&\#x27;s fallback.

[Source lines 140–142](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L140-L142)

>     clinical = \_load\_clinical\(folder\_b\)
>     if clinical is None and folder\_a:
>         clinical = \_load\_clinical\(folder\_a\)

[Source lines 166–176](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L166-L176)

>         elif step\_name == &quot;require\_value&quot;:
>             col = step\_def\[&quot;column&quot;\]
>             allowed = step\_def.get\(&quot;allowed&quot;\)
>             not\_empty = step\_def.get\(&quot;not\_empty&quot;, False\)
>             if clinical is not None and col in clinical.columns:
>                 clin\_idx = clinical\[~clinical.index.duplicated\(\)\]
>                 if not\_empty:
>                     valid = \{s for s in working if s in clin\_idx.index and pd.notna\(clin\_idx.at\[s, col\]\)}
>                 else:
>                     valid = \{s for s in working if s in clin\_idx.index and clin\_idx.at\[s, col\] in allowed}
>                 working = valid

[Source lines 77–81](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L77-L81)

>         &quot;\# Apply spec filters&quot;,
>         &quot;clinical\_path = next\(\(RELEASE\_B / f for f in \[&\#x27;clinical.tsv&\#x27;\] if \(RELEASE\_B / f\).exists\(\)\), None\)&quot;,
>         &quot;clinical = pd.read\_csv\(clinical\_path, sep=&\#x27;\\\\t&\#x27;\) if clinical\_path else None&quot;,
>         &quot;if clinical is not None:&quot;,
>         &quot;    clinical = clinical.set\_index\(&\#x27;sampleID&\#x27;\) if &\#x27;sampleID&\#x27; in clinical.columns else clinical&quot;,

[Source lines 116–128](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L116-L128)

>         &quot;    elif step\[&\#x27;step&\#x27;\] == &\#x27;require\_value&\#x27;:&quot;,
>         &quot;        col = step\[&\#x27;column&\#x27;\]&quot;,
>         &quot;        if clinical is not None and col in clinical.columns:&quot;,
>         &quot;            if step.get\(&\#x27;not\_empty&\#x27;\):&quot;,
>         &quot;                working = \{s for s in working if s in clinical.index and pd.notna\(clinical.at\[s, col\]\)}&quot;,
>         &quot;            else:&quot;,
>         &quot;                allowed = set\(step\[&\#x27;allowed&\#x27;\]\)&quot;,
>         &quot;                working = \{s for s in working if s in clinical.index and clinical.at\[s, col\] in allowed}&quot;,
>         &quot;&quot;,
>         &quot;rows = \[\{&\#x27;sample\_id&\#x27;: s, &\#x27;patient\_id&\#x27;: s\[:12\], &\#x27;flagged&\#x27;: s in flagged} for s in sorted\(working\)\]&quot;,
>         &quot;out = pd.DataFrame\(rows\)&quot;,
>         &quot;out.to\_csv\(&\#x27;cohort\_samples.csv&\#x27;, index=False\)&quot;,
>         f&quot;print\(f&\#x27;cohort\_samples.csv: \{\{len\(out\)}} samples&\#x27;\)&quot;,

[Source lines 191–193](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L191-L193)

>     reproduce\_path = \_make\_reproduce\_script\(
>         out\_dir, folder\_b, folder\_a, spec, applied\_repairs
>     \)

Supplemental rules: None cited; official criterion above applies.

Impact: For A1 with a recognized protein layer in B, no clinical table in B and a usable clinical table in A, the main export can filter with A while reconstruction leaves the clinical filter unapplied. The two artifacts can therefore have different membership under this explicit source-derived condition. It is not a claim that the normal full release triggers this case.

Concrete change: Share one versioned transformation implementation or serialize the exact resolved input map into the reconstruction. Make any cross-release fallback explicit and hash-bound, or reject missing B prerequisites consistently in both paths. Compare exact membership, not just row count.

Acceptance check: Create invented A labels that exclude at least one B protein sample, omit B clinical data and run the A1 export and reconstruction in an authorized isolated environment. Both must either refuse the same missing evidence or produce identical sorted sample IDs with the same declared input provenance.

### The A2 reconstruction embeds a JSON boolean as a Python name

gap · P1 · Confidence: High for the generator and built-in A2 literal. No generated code was executed or represented as a passed/failed runtime test by this reviewer.

The generator writes SPEC = followed by json.dumps\(spec\). The built-in A2 spec contains not\_empty=True, which JSON serializes as lowercase true. In Python source, that token is a name rather than the True literal, and the generated script shown here defines no name true. The ordinary A2 specification therefore contains an unresolved name in the reconstructed Python assignment.

[Source lines 17–29](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L17-L29)

> def \_make\_reproduce\_script\(out\_dir, folder\_b, folder\_a, spec, applied\_repairs\):
>     &quot;&quot;&quot;Write a standalone pandas script that rebuilds cohort\_samples.csv.&quot;&quot;&quot;
>     lines = \[
>         &\#x27;&quot;&quot;&quot;Standalone script: rebuilds cohort\_samples.csv from the release folder.&quot;&quot;&quot;&\#x27;,
>         &quot;import pandas as pd&quot;,
>         &quot;from pathlib import Path&quot;,
>         &quot;&quot;,
>         f&\#x27;RELEASE\_B = Path\(\{repr\(str\(folder\_b\)\)}\)&\#x27;,
>         f&\#x27;RELEASE\_A = Path\(\{repr\(str\(folder\_a\)\)}\)&\#x27;,
>         &quot;&quot;,
>         &quot;SPEC = &quot; + json.dumps\(spec, indent=4\),
>         &quot;&quot;,
>         &quot;REPAIRS = &quot; + json.dumps\(applied\_repairs, indent=4\),

[Source lines 16–20](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L16-L20)

>     &quot;A2&quot;: \[
>         \{&quot;step&quot;: &quot;require\_file&quot;, &quot;file&quot;: &quot;clinical.tsv&quot;},
>         \{&quot;step&quot;: &quot;filter\_sample\_type&quot;, &quot;type&quot;: &quot;01&quot;},
>         \{&quot;step&quot;: &quot;require\_value&quot;, &quot;column&quot;: &quot;PAM50Call\_RNAseq&quot;, &quot;not\_empty&quot;: True},
>     \],

[Source lines 125–132](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L125-L132)

>         &quot;rows = \[\{&\#x27;sample\_id&\#x27;: s, &\#x27;patient\_id&\#x27;: s\[:12\], &\#x27;flagged&\#x27;: s in flagged} for s in sorted\(working\)\]&quot;,
>         &quot;out = pd.DataFrame\(rows\)&quot;,
>         &quot;out.to\_csv\(&\#x27;cohort\_samples.csv&\#x27;, index=False\)&quot;,
>         f&quot;print\(f&\#x27;cohort\_samples.csv: \{\{len\(out\)}} samples&\#x27;\)&quot;,
>     \]
>     path = Path\(out\_dir\) / &quot;reproduce\_cohort.py&quot;
>     path.write\_text\(&quot;\\n&quot;.join\(lines\), encoding=&quot;utf-8&quot;\)
>     return path

Supplemental rules: None cited; official criterion above applies.

Impact: The standalone reconstruction can fail before rebuilding membership even when the main cohort export succeeded. Syntax parsing alone will not catch this particular defect because a bare name is valid Python syntax. This conclusion comes from source and language semantics, not an executed generated script.

Concrete change: Embed a safely quoted JSON string and call json.loads at runtime, or use repr for a supported Python-literal structure. Apply the same serialization rule to applied repairs and test booleans, null values, quotes and non-ASCII descriptions as data.

Acceptance check: Export the built-in A2 specification and run its reconstruction on an authorized synthetic fixture. Verify no unresolved true/false/null names occur and exact membership matches the main engine. Keep a normal A1 control and separate syntax checks from execution checks.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-6: Useful next steps. Suggested fixes are specific and match the size and importance of the problem.

Status: **not_tested**

Quick fixes include fail-explicit required fields and safe literal serialization. Shared versioned transformation semantics are the larger parity improvement.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T1-7: Communication. Someone without specialist knowledge can understand the result and next step.

Status: **not_tested**

A successful file export should not imply that eligibility was evaluated or reconstruction succeeded. Display the exact limits in the exported bundle.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## Excluded scope

- .gitignore: non-allowlisted file type
- assets/hero\_tissue\_ai.jpg: non-allowlisted file type
- data/README.md: sensitive, data, sealed, or dependency path
- data/build\_idc\_manifests.py: sensitive, data, sealed, or dependency path
- data/camelyon17/README.md: sensitive, data, sealed, or dependency path
- data/camelyon17/stages.csv: sensitive, data, sealed, or dependency path
- data/clinical-trials/README.md: sensitive, data, sealed, or dependency path
- data/clinical-trials/fetch.py: sensitive, data, sealed, or dependency path
- data/clinical-trials/fictional\_cases.csv: sensitive, data, sealed, or dependency path
- data/clinical-trials/fictional\_rules.json: sensitive, data, sealed, or dependency path
- data/clinical-trials/replay.py: sensitive, data, sealed, or dependency path
- data/clinical-trials/sources.csv: sensitive, data, sealed, or dependency path
- data/cptac/README.md: sensitive, data, sealed, or dependency path
- data/cptac/lung\_ct\_manifest.csv: sensitive, data, sealed, or dependency path
- data/cptac/protein.py: sensitive, data, sealed, or dependency path
- data/cptac/protein\_sources.csv: sensitive, data, sealed, or dependency path
- data/cptac/protein\_starter.csv: sensitive, data, sealed, or dependency path
- data/cptac/slide\_manifest.csv: file-size limit
- data/depmap/README.md: sensitive, data, sealed, or dependency path
- data/depmap/baseline.py: sensitive, data, sealed, or dependency path
- data/depmap/build.py: sensitive, data, sealed, or dependency path
- data/depmap/sources.csv: sensitive, data, sealed, or dependency path
- data/depmap/starter.csv: sensitive, data, sealed, or dependency path
- data/lidc-idri/README.md: sensitive, data, sealed, or dependency path
- data/lidc-idri/exercise\_patients.csv: sensitive, data, sealed, or dependency path
- data/lidc-idri/fetch\_exercise.py: sensitive, data, sealed, or dependency path
- data/lidc-idri/patient\_manifest.csv: file-size limit
- data/pathmnist/README.md: sensitive, data, sealed, or dependency path
- data/pathmnist/baseline.py: sensitive, data, sealed, or dependency path
- data/pathmnist/fetch.py: sensitive, data, sealed, or dependency path
- data/pathmnist/gallery.py: sensitive, data, sealed, or dependency path
- data/pathmnist/sources.csv: sensitive, data, sealed, or dependency path
- data/tcga-brca/README.md: sensitive, data, sealed, or dependency path
- data/tcga-brca/fetch.py: sensitive, data, sealed, or dependency path
- data/tcga-brca/make\_release.py: sensitive, data, sealed, or dependency path
- data/tcga-brca/practice-B.content.sha256: sensitive, data, sealed, or dependency path
- data/tcga-brca/reference\_analyses.py: sensitive, data, sealed, or dependency path
- data/tcga-brca/sample\_manifest.csv: sensitive, data, sealed, or dependency path
- data/tcga-brca/slide\_manifest.csv: file-size limit
- data/tcga-brca/sources.csv: sensitive, data, sealed, or dependency path
- envelopes/README.md: sensitive, data, sealed, or dependency path
- envelopes/SHA256SUMS: sensitive, data, sealed, or dependency path
- envelopes/sealed/E01.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E02.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E03.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E04.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E05.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E06.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E07.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E08.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E09.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E10.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E11.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E12.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E13.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E14.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E15.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E16.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E17.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E18.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E19.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E20.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E21.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E22.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E23.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/E24.sealed: sensitive, data, sealed, or dependency path
- envelopes/sealed/practice.sealed: sensitive, data, sealed, or dependency path
- envelopes/unseal.py: sensitive, data, sealed, or dependency path
- kickoff/Cancer\_AI\_Lab\_Kickoff.pdf: file-size limit
- products/multimodal-case-room/practice\_cases.csv: non-allowlisted file type
- sns/.gitignore: non-allowlisted file type
- starter/tcga\_starter.ipynb: non-allowlisted file type
- warmup/wisconsin/SHA256SUMS: non-allowlisted file type
- warmup/wisconsin/data/breast-cancer-wisconsin.data: sensitive, data, sealed, or dependency path
- warmup/wisconsin/data/breast-cancer-wisconsin.names: sensitive, data, sealed, or dependency path
- warmup/wisconsin/data/data\_dictionary.csv: sensitive, data, sealed, or dependency path
- warmup/wisconsin/data/wisconsin\_readable.csv: sensitive, data, sealed, or dependency path
- warmup/wisconsin/practice/P1-sorted-with-source-rows/extract.csv: non-allowlisted file type
- warmup/wisconsin/practice/P2-cleaned-extract-no-provenance/extract.csv: non-allowlisted file type
- warmup/wisconsin/practice/SHA256SUMS: non-allowlisted file type
- warmup/wisconsin/starter.ipynb: non-allowlisted file type
- warmup/wisconsin/track1-cohort-firewall/findings\_template.csv: non-allowlisted file type

## Judge Follow-Up Sequence

1. Verify the official final commit and product declaration.
2. Start with the highest-priority synthetic acceptance checks above.
3. Follow one finding through evidence, affected versus unaffected analyses, proposed repair and human decision.
4. Verify the exported artifact against the organizer contract without reading sealed answers.
5. Record actual results separately from this static audit; revise only claims the new evidence supports.
