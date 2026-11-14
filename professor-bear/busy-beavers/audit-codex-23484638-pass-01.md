# Professor Bear Audit: Busy Beavers Cohort Firewall

## Review Identity

This is an independent, provisional source-code audit for judge deliberation. It is not an official grade.

- Entry: `GiorgiKarazanashvili/BusyBeavers`
- Commit: `bfb369f231bf97a1d3aa21abade3ba4b1406a355`
- Organizer reference: `6e15a399a64ffbf80778db0b462ac239e70086b9`
- Product: `cohort-control-tower`; Track 1, Cohort Firewall
- Pass: 1; reviewed 2026-11-14T19:55:26.890585+00:00
- Runtime: **not executed**; official freeze/receipt: **not verified**

## Executive Assessment

The submission has a clear API boundary and withholds invalid findings rather than presenting a mock as a real result. This deeper source pass identifies two additional detector blind spots: duplicate sample IDs are removed before their dedicated detector, and equality after four-decimal rounding bypasses the stated tolerance check. Repair/evidence truncation also needs explicit coverage. No runtime result or numerical accuracy estimate is claimed.

## Workflow Traced

The API resolves a configured real detector, calls the cfw comparison and analysis-slice layer, converts raw events to v0.2 findings, reruns affected organizer analyses and packages the result through schema validation. The detector's final policy distinguishes rerun failure, affecting findings and no affecting findings. It does not itself implement an effect-magnitude Blocked branch. The dashboard and repair-export routes are distinct from detection.

## Findings At A Glance

| ID | Type | Priority | Finding |
|---|---|---|---|
| BB-01 | gap | P1 | Duplicate IDs are removed before the duplicate-ID detector |
| BB-02 | gap | P1 | Rounded-hash equality bypasses the finer tolerance check |
| BB-03 | gap | P1 | A display cap also truncates the actionable repair scope |
| BB-04 | strength | P2 | Invalid schema output is withheld from the successful findings route |
| BB-05 | strength | P2 | Proposed repairs retain explicit limitations and analysis impact reasons |
| BB-06 | strength | P2 | Impact mapping uses the actual analysis input slice |

## Inspection Scope

The following files informed the implementation-level conclusions in this pass. Other collected files are not automatically treated as reviewed:

- `cfw/compare.py`
- `cfw/fingerprint.py`
- `cfw/diff.py`
- `cfw/impact.py`
- `detection/engine.py`
- `backend/services/comparison.py`
- `backend/services/detector_adapter.py`

## Parallel Review Preservation

Existing reports were read and retained. This is a separately versioned supplement; prior conclusions are not silently replaced.

The retained REPORT.md already discusses missing-input preflight, the absent Blocked branch, easy-export approval semantics, the 500-target limit and optional Q&A payloads. This supplement does not count those as five new discoveries. It independently follows the 500-target construction and adds the duplicate-ID ordering and rounded-hash screening findings below. Earlier runtime-pending findings remain runtime-pending; no prior report or deck was replaced.

This pass does not accept earlier agents' findings as established merely because they were reported. Any correction must identify the earlier claim and the new evidence explicitly.

## Detailed Criterion Review

# Judge review aid: busy-beavers

Repository: https://github.com/GiorgiKarazanashvili/BusyBeavers
Commit: `bfb369f231bf97a1d3aa21abade3ba4b1406a355`
Track: 1
Reviewer: Professor Bear / Codex source review

**Not an official result. Source review does not establish runtime behavior.**

The submission has a clear API boundary and withholds invalid findings rather than presenting a mock as a real result. This deeper source pass identifies two additional detector blind spots: duplicate sample IDs are removed before their dedicated detector, and equality after four-decimal rounding bypasses the stated tolerance check. Repair/evidence truncation also needs explicit coverage. No runtime result or numerical accuracy estimate is claimed.

## Coverage and limitations

Collection: complete_with_exclusions; 85 text files; 84 excluded entries; recursive tree truncated: False.
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

- P1 · T1-1 · Duplicate IDs are removed before the duplicate-ID detector: Inspect and report duplicate identifiers before deduplication. Keep conflicting rows as evidence and prevent ambiguous records from contributing to an approved analytical slice until a documented selection policy or reviewer decision resolves them.
- P1 · T1-2 · Rounded-hash equality bypasses the finer tolerance check: Use an exact or lossless canonical hash for screening, then apply the explicit numeric tolerance to candidate differences. Alternatively define one consistent, field-specific quantization policy and disclose the information it intentionally discards.
- P1 · T1-3 · A display cap also truncates the actionable repair scope: Separate a bounded evidence preview from the authoritative complete target set. Export total counts, explicit truncation status and a hash-bound complete target artifact, or refuse to represent a partial repair as complete.
- P2 · T1-2 · Impact mapping uses the actual analysis input slice: Preserve the explicit dependency slices, fix their equality screening and record which slice policy was used in each run. Keep new analyses from silently inheriting A1/A2 assumptions.
- P2 · T1-4 · Invalid schema output is withheld from the successful findings route: Retain this failed-versus-completed distinction and keep the rejected file available only as a clearly marked diagnostic. Bind validation to the same bytes served to the next team.
- P2 · T1-6 · Proposed repairs retain explicit limitations and analysis impact reasons: Keep the event-level evidence and uncertainty wording. Apply the same proposal-versus-approved distinction to every downstream derivative export and avoid treating restoration of a baseline number as proof of factual truth.

## T1-1: Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support.

Status: **observed**

The duplicate-ID branch is undermined by preceding deduplication. Other event detectors exist, but no unseen-input accuracy or false-positive rate was measured.

### Duplicate IDs are removed before the duplicate-ID detector

gap · P1 · Confidence: High for the inspected ordering and index propagation; end-to-end runtime behavior remains untested.

diff\_file removes duplicate indices from both input frames before hashing. profile\_hashes then assigns the already-deduplicated frame index to its output. The later b.index.duplicated check therefore cannot detect the duplicate indices discarded at the beginning of the function. This is a source-level ordering defect; no duplicate-ID fixture was executed here.

[Source lines 8–20](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/diff.py#L8-L20)

> def diff\_file\(name, a\_df, b\_df\):
>     a\_df, b\_df = a\_df\[~a\_df.index.duplicated\(\)\], b\_df\[~b\_df.index.duplicated\(\)\]
>     a, b = profile\_hashes\(a\_df\), profile\_hashes\(b\_df\)
>     groups\_a, groups\_b = \_dup\_groups\(a\), \_dup\_groups\(b\)
>     out = \[\]
>     added, removed = b.index.difference\(a.index\), a.index.difference\(b.index\)
>     if len\(added\):   out.append\(dict\(type=&quot;samples\_added&quot;, file=name, sample\_ids=sorted\(added\)\)\)
>     if len\(removed\): out.append\(dict\(type=&quot;samples\_removed&quot;, file=name, sample\_ids=sorted\(removed\)\)\)
>     if b.index.duplicated\(\).any\(\):
>         out.append\(dict\(type=&quot;duplicate\_id&quot;, file=name, sample\_ids=sorted\(set\(b.index\[b.index.duplicated\(\)\]\)\)\)\)
>     a, b = a\[~a.index.duplicated\(\)\], b\[~b.index.duplicated\(\)\]
>     common = a.index.intersection\(b.index\)
>     changed = \[i for i in common if a\[i\] \!= b\[i\] and not rows\_close\(a\_df.loc\[i\], b\_df.loc\[i\]\)\]

[Source lines 4–8](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/fingerprint.py#L4-L8)

> def profile\_hashes\(df\):
>     d = df.reindex\(sorted\(df.columns, key=str\), axis=1\).round\(4\)
>     h = pd.util.hash\_pandas\_object\(d, index=False\)
>     h.index = df.index
>     return h\[~d.isna\(\).all\(axis=1\)\]

Supplemental rules: None cited; official criterion above applies.

Impact: Ambiguous repeated records can be silently reduced to the first record instead of being reported for human review. This can hide the exact join or identity problem the workflow is meant to expose.

Concrete change: Inspect and report duplicate identifiers before deduplication. Keep conflicting rows as evidence and prevent ambiguous records from contributing to an approved analytical slice until a documented selection policy or reviewer decision resolves them.

Acceptance check: Use a synthetic table with one repeated ID and conflicting values, plus an identical-duplicate case and a unique-ID control. Confirm the repeated ID is reported, both records remain inspectable and an arbitrary first row is not silently accepted.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-2: Reasoning for the research question. Changes its result appropriately when the research question or intended use changes.

Status: **observed**

Actual input slices are a strength. Rounded screening and the lack of a documented effect-magnitude blocking policy need explicit review rather than an automatic scoring deduction.

### Rounded-hash equality bypasses the finer tolerance check

gap · P1 · Confidence: High for the predicate mismatch; the proposed fixture has not been run.

Profile hashes are computed after rounding every column to four decimals. The changed-row predicate calls rows\_close only when hashes differ, although rows\_close uses rtol=1e-6 and atol=1e-9. Distinct values that round to the same four-decimal value never reach that tolerance check. The analysis-slice impact calculation repeats this pattern.

[Source lines 4–8](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/fingerprint.py#L4-L8)

> def profile\_hashes\(df\):
>     d = df.reindex\(sorted\(df.columns, key=str\), axis=1\).round\(4\)
>     h = pd.util.hash\_pandas\_object\(d, index=False\)
>     h.index = df.index
>     return h\[~d.isna\(\).all\(axis=1\)\]

[Source lines 11–24](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/fingerprint.py#L11-L24)

> def rows\_close\(ra, rb, rtol=1e-6, atol=1e-9\):
>     &quot;&quot;&quot;True if two sample rows hold the same values up to float noise \(text must match exactly\).
> 
>     Hash-after-rounding can flip on values sitting exactly on a rounding boundary, so whenever two
>     hashes differ we confirm with this tolerance check before reporting a change.
>     &quot;&quot;&quot;
>     cols = ra.index.intersection\(rb.index\)
>     x, y = ra\[cols\], rb\[cols\]
>     xn, yn = pd.to\_numeric\(x, errors=&quot;coerce&quot;\), pd.to\_numeric\(y, errors=&quot;coerce&quot;\)
>     num = xn.notna\(\) &amp; yn.notna\(\)
>     if not np.isclose\(xn\[num\].astype\(float\), yn\[num\].astype\(float\), rtol=rtol, atol=atol\).all\(\):
>         return False
>     rest = ~num
>     return bool\(\(\(\(x\[rest\] == y\[rest\]\) &\#124; \(x\[rest\].isna\(\) &amp; y\[rest\].isna\(\)\)\)\).all\(\)\)

[Source lines 18–20](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/diff.py#L18-L20)

>     a, b = a\[~a.index.duplicated\(\)\], b\[~b.index.duplicated\(\)\]
>     common = a.index.intersection\(b.index\)
>     changed = \[i for i in common if a\[i\] \!= b\[i\] and not rows\_close\(a\_df.loc\[i\], b\_df.loc\[i\]\)\]

[Source lines 26–34](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/impact.py#L26-L34)

>         sa, sb = spec\[&quot;slice&quot;\]\(A\), spec\[&quot;slice&quot;\]\(B\)
>         if sa is None or sb is None:
>             res\[k\] = dict\(affected=True, reason=&quot;input file missing in one release&quot;, sample\_ids=\[\]\); continue
>         ha, hb = profile\_hashes\(sa\), profile\_hashes\(sb\)
>         sa\_ids, sb\_ids = set\(ha.index\), set\(hb.index\)
>         ids = sorted\(\(sa\_ids ^ sb\_ids\) &\#124; \{i for i in sa\_ids &amp; sb\_ids if ha\[i\] \!= hb\[i\] and not rows\_close\(sa.loc\[i\], sb.loc\[i\]\)}\)
>         res\[k\] = dict\(affected=bool\(ids\), sample\_ids=ids,
>                       reason=\(f&quot;\{len\(ids\)} sample\(s\) changed inside the slice it reads \(\{spec\[&\#x27;reads&\#x27;\]}\)&quot; if ids else
>                               f&quot;slice it reads is identical after rounding across \{len\(ha\)} samples \(\{spec\[&\#x27;reads&\#x27;\]}\)&quot;\)\)

Supplemental rules: None cited; official criterion above applies.

Impact: The implementation can call a profile or analysis slice unchanged even when its values differ beyond the finer stated tolerance. The scientific significance depends on the field and question; this is not a claim of harm or a measured miss rate on TCGA.

Concrete change: Use an exact or lossless canonical hash for screening, then apply the explicit numeric tolerance to candidate differences. Alternatively define one consistent, field-specific quantization policy and disclose the information it intentionally discards.

Acceptance check: Compare authorized synthetic values 1.00001 and 1.00004. They round alike at four decimals but differ by more than 1e-6 relative tolerance. Check both detection and analysis impact, and retain a genuinely within-tolerance noise control.

### Impact mapping uses the actual analysis input slice

strength · P2 · Confidence: High for source structure; numerical parity with organizer reference functions remains untested.

A1&\#x27;s slice combines primary-tumor protein values with ER labels, while A2&\#x27;s slice uses primary-tumor subtype labels. The impact function compares sample membership and row values in those slices rather than treating every changed file as equally relevant.

[Source lines 7–20](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/impact.py#L7-L20)

> def slice\_a1\(rel\):
>     if &quot;clinical&quot; not in rel or &quot;protein\_rppa&quot; not in rel: return None
>     er, pr = rel\[&quot;clinical&quot;\]\[ER\], rel\[&quot;protein\_rppa&quot;\]\[&quot;ERALPHA&quot;\]
>     ids = \[s for s in \_primary\(pr.index\) if er.get\(s\) in \(&quot;Positive&quot;, &quot;Negative&quot;\)\]
>     return pd.DataFrame\(\{&quot;er&quot;: er.loc\[ids\], &quot;eralpha&quot;: pr.loc\[ids\]}\)
> 
> def slice\_a2\(rel\):
>     if &quot;clinical&quot; not in rel: return None
>     c = rel\[&quot;clinical&quot;\]\[&quot;PAM50Call\_RNAseq&quot;\]
>     return c\[\_primary\(c.index\)\].dropna\(\).to\_frame\(\)
> 
> ANALYSES = \{
>     &quot;A1&quot;: dict\(slice=slice\_a1, reads=&quot;clinical\[%s\] + protein\[ERALPHA\], primary tumors with Positive/Negative ER&quot; % ER\),
>     &quot;A2&quot;: dict\(slice=slice\_a2, reads=&quot;clinical\[PAM50Call\_RNAseq\], primary tumors&quot;\),

[Source lines 23–34](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/impact.py#L23-L34)

> def impact\(A, B\):
>     res = \{}
>     for k, spec in ANALYSES.items\(\):
>         sa, sb = spec\[&quot;slice&quot;\]\(A\), spec\[&quot;slice&quot;\]\(B\)
>         if sa is None or sb is None:
>             res\[k\] = dict\(affected=True, reason=&quot;input file missing in one release&quot;, sample\_ids=\[\]\); continue
>         ha, hb = profile\_hashes\(sa\), profile\_hashes\(sb\)
>         sa\_ids, sb\_ids = set\(ha.index\), set\(hb.index\)
>         ids = sorted\(\(sa\_ids ^ sb\_ids\) &\#124; \{i for i in sa\_ids &amp; sb\_ids if ha\[i\] \!= hb\[i\] and not rows\_close\(sa.loc\[i\], sb.loc\[i\]\)}\)
>         res\[k\] = dict\(affected=bool\(ids\), sample\_ids=ids,
>                       reason=\(f&quot;\{len\(ids\)} sample\(s\) changed inside the slice it reads \(\{spec\[&\#x27;reads&\#x27;\]}\)&quot; if ids else
>                               f&quot;slice it reads is identical after rounding across \{len\(ha\)} samples \(\{spec\[&\#x27;reads&\#x27;\]}\)&quot;\)\)

Supplemental rules: None cited; official criterion above applies.

Impact: This directly supports the product&\#x27;s affected-versus-unaffected analysis workflow. It is a useful design even though the rounded-hash screening concern above limits the implementation&\#x27;s guarantees.

Concrete change: Preserve the explicit dependency slices, fix their equality screening and record which slice policy was used in each run. Keep new analyses from silently inheriting A1/A2 assumptions.

Acceptance check: Alter an unrelated protein row, then ERALPHA for an eligible sample, and then a subtype label. Verify the impact decisions differ for defensible reasons, with baseline and candidate sample sets visible.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-3: Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion.

Status: **observed**

Evidence, reasons and validation are present. A 500-record cap must not silently narrow authoritative repair coverage.

### A display cap also truncates the actionable repair scope

gap · P1 · Confidence: High for the explicit slices; downstream export behavior has not been executed.

The exported finding evidence is sliced to MAX\_EVIDENCE and the repair&\#x27;s targets are independently sliced to the same limit. MAX\_EVIDENCE is 500. There is no complete target-set reference or truncation marker in this construction, while summary text can describe the full event.

[Source lines 25–29](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L25-L29)

> ENGINE\_NAME = &quot;cohort-firewall-cfw&quot;
> MAX\_EVIDENCE = 500
> REF\_PATH = ROOT / &quot;data&quot; / &quot;tcga-brca&quot; / &quot;reference\_analyses.py&quot;
> \# stems \(cfw names files by stem\) each analysis reads; used for file-level findings
> ANALYSIS\_FILES = \{&quot;A1&quot;: \{&quot;clinical&quot;, &quot;protein\_rppa&quot;}, &quot;A2&quot;: \{&quot;clinical&quot;}}

[Source lines 257–268](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L257-L268)

>         findings.append\(\{
>             &quot;id&quot;: fid, &quot;kind&quot;: ev\[&quot;kind&quot;\], &quot;summary&quot;: ev\[&quot;summary&quot;\], &quot;severity&quot;: sev, &quot;confidence&quot;: ev\[&quot;confidence&quot;\],
>             &quot;evidence&quot;: ev\[&quot;evidence&quot;\]\[:MAX\_EVIDENCE\],
>             &quot;affects\_analyses&quot;: affects, &quot;not\_affected\_analyses&quot;: not\_affects,
>             &quot;limitation&quot;: ev\[&quot;limitation&quot;\], &quot;needs\_human\_review&quot;: sev in \(&quot;high&quot;, &quot;medium&quot;\),
>             &quot;impact\_reasons&quot;: why,
>         }\)
>         r = ev\[&quot;repair&quot;\]
>         targets = \[\_ptr\(i, name\_b, r\[&quot;file&quot;\]\) for i in r\[&quot;ids&quot;\]\]\[:MAX\_EVIDENCE\] or \[\_ptr\(r\[&quot;file&quot;\], name\_b, r\[&quot;file&quot;\], kind=&quot;file&quot;\)\]
>         repairs.append\(\{&quot;id&quot;: f&quot;R\{n:02d}&quot;, &quot;action&quot;: r\[&quot;action&quot;\], &quot;targets&quot;: targets,
>                         &quot;justification&quot;: r\[&quot;why&quot;\] + &quot; Proposal only; no release file is modified.&quot;,
>                         &quot;addresses&quot;: \[fid\]}\)

Supplemental rules: None cited; official criterion above applies.

Impact: A downstream consumer cannot infer that an apparently complete repair covers only the first 500 records. The prior report already identified this concern; this pass corroborates the exact source construction rather than claiming a new runtime result.

Concrete change: Separate a bounded evidence preview from the authoritative complete target set. Export total counts, explicit truncation status and a hash-bound complete target artifact, or refuse to represent a partial repair as complete.

Acceptance check: Create a synthetic 501-target event and inspect exported evidence, repair targets and summary counts. Either all intended targets must be addressable or the operation must be visibly partial and non-approvable as a complete repair.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-4: Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review.

Status: **observed**

The API withholds schema-invalid output and findings retain limitations. Existing concerns about human approval in derivative exports remain open and were not executed here.

### Invalid schema output is withheld from the successful findings route

strength · P2 · Confidence: High for the service&\#x27;s control flow; the API and validator were not run.

The comparison service packages the detector output, calls write\_document and checks returned validation errors. On errors it renames the result to findings.invalid.json, marks the run failed and returns before findings\_available is set. findings\_path only exposes a completed run with an available file.

[Source lines 100–123](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/backend/services/comparison.py#L100-L123)

>     try:
>         progress\(f&quot;Calling detection engine with \{rel\_a.name} and \{rel\_b.name}&quot;\)
>         raw, info = detector\_adapter.run\(rel\_a.path, rel\_b.path, \(rel\_a.name, rel\_b.name\), work, progress\)
>         progress\(&quot;Packaging findings.json \(format v0.2\)&quot;\)
>         doc, notes = report\_export.build\_document\(raw, rel\_a, rel\_b, info.to\_dict\(\)\)
>         progress\(&quot;Validating with format/validate.py&quot;\)
>         target = work / &quot;findings.json&quot;
>         errors = report\_export.write\_document\(doc, target\)
>         summary = build\_summary\(doc, rel\_a, rel\_b, notes\)
>         if errors:
>             target.replace\(work / &quot;findings.invalid.json&quot;\)
>             \_update\(run\_id, status=&quot;failed&quot;, finished\_at=\_now\(\), detector=info.to\_dict\(\), summary=summary,
>                     validation=\{&quot;valid&quot;: False, &quot;errors&quot;: errors\[:50\], &quot;validator&quot;: &quot;format/validate.py&quot;},
>                     error=f&quot;Engine output failed the official validator \(\{len\(errors\)} problem\(s\)\); findings.json withheld.&quot;\)
>             return
>         progress\(&quot;Done: findings.json is valid&quot;\)
>         \_update\(run\_id, status=&quot;completed&quot;, finished\_at=\_now\(\), detector=info.to\_dict\(\),
>                 validation=\{&quot;valid&quot;: True, &quot;errors&quot;: \[\], &quot;validator&quot;: &quot;format/validate.py&quot;},
>                 findings\_available=True, verdict=doc.get\(&quot;verdict&quot;\), summary=summary\)
>     except detector\_adapter.DetectorError as e:
>         \_update\(run\_id, status=&quot;failed&quot;, finished\_at=\_now\(\), error=str\(e\)\)
>     except Exception as e:  \# unexpected: report honestly
>         \_update\(run\_id, status=&quot;failed&quot;, finished\_at=\_now\(\), error=f&quot;\{type\(e\).\_\_name\_\_}: \{e}&quot;,
>                 traceback=traceback.format\_exc\(limit=4\)\)

[Source lines 139–144](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/backend/services/comparison.py#L139-L144)

> def findings\_path\(run\_id: str\) -&gt; Path &\#124; None:
>     rec = get\_run\(run\_id\)
>     p = run\_dir\(run\_id\) / &quot;findings.json&quot;
>     if rec\[&quot;status&quot;\] == &quot;completed&quot; and rec.get\(&quot;findings\_available&quot;\) and p.is\_file\(\):
>         return p
>     return None

Supplemental rules: None cited; official criterion above applies.

Impact: This prevents a format-invalid export from silently taking the successful handoff route. Schema validation still does not prove detector correctness, but it is a useful independent packaging boundary.

Concrete change: Retain this failed-versus-completed distinction and keep the rejected file available only as a clearly marked diagnostic. Bind validation to the same bytes served to the next team.

Acceptance check: Supply a synthetic detector response that fails the organizer schema. Verify the run is failed and the successful findings endpoint does not serve it; then repeat with a valid positive control.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-5: Working tool and clear setup. Judges can run the core workflow from the submitted repository.

Status: **not_tested**

A real-engine adapter, API and dashboard exist in source. This pass did not install dependencies, start them, run tests or verify the live deployment.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T1-6: Useful next steps. Suggested fixes are specific and match the size and importance of the problem.

Status: **observed**

Repair proposals contain reasons and preserve uncertainty about which release is authoritative. Approved repairs and unapproved previews must remain distinct.

### Proposed repairs retain explicit limitations and analysis impact reasons

strength · P2 · Confidence: High for the inspected detector/export path; derivative export and reviewer UI behavior remain untested.

Event construction includes source pointers and per-kind limitations, then computes analysis-specific impact reasons. The exported finding retains those reasons and a human-review flag, and repair justification says the action is a proposal that does not modify a release file in this path.

[Source lines 76–89](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L76-L89)

>         if typ == &quot;swap&quot;:
>             pairs = \[it\[&quot;sample\_ids&quot;\] for it in items\]
>             ev = \[\]
>             for x, y in pairs:
>                 ev.append\(\_ptr\(x, name\_b, file\_b, f&quot;\{file\_b}: profile equals \{y}&\#x27;s profile in release A \(and vice versa\)&quot;\)\)
>                 ev.append\(\_ptr\(y, name\_b, file\_b, f&quot;\{file\_b}: profile equals \{x}&\#x27;s profile in release A \(and vice versa\)&quot;\)\)
>             events.append\(dict\(
>                 kind=&quot;sample\_swap&quot;, file=stem, ids=ids, severity\_hi=&quot;high&quot;, severity\_lo=&quot;medium&quot;, confidence=&quot;high&quot;,
>                 summary=f&quot;\{file\_b}: \{len\(pairs\)} pair\(s\) of samples exchanged their measurements &quot;
>                         f&quot;\(\{&\#x27;; &\#x27;.join\(&\#x27; &lt;-&gt; &\#x27;.join\(p\) for p in pairs\[:3\]\)}\{&\#x27; ...&\#x27; if len\(pairs\) &gt; 3 else &\#x27;&\#x27;}\).&quot;,
>                 evidence=ev,
>                 limitation=&quot;Exact profile identity shows the labels moved, not which release is correct.&quot;,
>                 repair=dict\(action=&quot;restore\_from\_previous\_release&quot;, ids=ids, file=file\_b,
>                             why=f&quot;Restore the release A profiles for these samples in \{file\_b}, or exclude them until the provider confirms the correct assignment.&quot;\)\)\)

[Source lines 240–268](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L240-L268)

>     findings, repairs = \[\], \[\]
>     for n, ev in enumerate\(events, 1\):
>         fid = f&quot;F\{n:02d}&quot;
>         idset = set\(ev\[&quot;ids&quot;\]\)
>         affects, not\_affects, why = \[\], \[\], \{}
>         for aid, res in imp.items\(\):
>             if idset:
>                 hit = sorted\(idset &amp; set\(res\[&quot;sample\_ids&quot;\]\)\)
>                 hit\_flag = bool\(hit\) and ev\[&quot;file&quot;\] in ANALYSIS\_FILES.get\(aid, set\(\)\)
>                 why\[aid\] = \(f&quot;\{len\(hit\)} of this finding&\#x27;s samples sit inside the slice \{aid} reads&quot; if hit\_flag
>                             else f&quot;none of this finding&\#x27;s samples are inside the slice \{aid} reads&quot;
>                                  f&quot; \(or the file is not an input of \{aid}\)&quot;\)
>             else:  \# file-level finding
>                 hit\_flag = res\[&quot;affected&quot;\] and ev\[&quot;file&quot;\] in ANALYSIS\_FILES.get\(aid, set\(\)\)
>                 why\[aid\] = f&quot;\{ev\[&\#x27;file&\#x27;\]} is \{&\#x27;an input&\#x27; if hit\_flag else &\#x27;not an input&\#x27;} of \{aid}&quot;
>             \(affects if hit\_flag else not\_affects\).append\(aid\)
>         sev = ev\[&quot;severity\_hi&quot;\] if affects else ev\[&quot;severity\_lo&quot;\]
>         findings.append\(\{
>             &quot;id&quot;: fid, &quot;kind&quot;: ev\[&quot;kind&quot;\], &quot;summary&quot;: ev\[&quot;summary&quot;\], &quot;severity&quot;: sev, &quot;confidence&quot;: ev\[&quot;confidence&quot;\],
>             &quot;evidence&quot;: ev\[&quot;evidence&quot;\]\[:MAX\_EVIDENCE\],
>             &quot;affects\_analyses&quot;: affects, &quot;not\_affected\_analyses&quot;: not\_affects,
>             &quot;limitation&quot;: ev\[&quot;limitation&quot;\], &quot;needs\_human\_review&quot;: sev in \(&quot;high&quot;, &quot;medium&quot;\),
>             &quot;impact\_reasons&quot;: why,
>         }\)
>         r = ev\[&quot;repair&quot;\]
>         targets = \[\_ptr\(i, name\_b, r\[&quot;file&quot;\]\) for i in r\[&quot;ids&quot;\]\]\[:MAX\_EVIDENCE\] or \[\_ptr\(r\[&quot;file&quot;\], name\_b, r\[&quot;file&quot;\], kind=&quot;file&quot;\)\]
>         repairs.append\(\{&quot;id&quot;: f&quot;R\{n:02d}&quot;, &quot;action&quot;: r\[&quot;action&quot;\], &quot;targets&quot;: targets,
>                         &quot;justification&quot;: r\[&quot;why&quot;\] + &quot; Proposal only; no release file is modified.&quot;,
>                         &quot;addresses&quot;: \[fid\]}\)

Supplemental rules: None cited; official criterion above applies.

Impact: This gives a reviewer an interpretable handoff and preserves the important distinction between detecting a difference and proving which release is correct.

Concrete change: Keep the event-level evidence and uncertainty wording. Apply the same proposal-versus-approved distinction to every downstream derivative export and avoid treating restoration of a baseline number as proof of factual truth.

Acceptance check: Follow one synthetic swap from source pointers through affected and unaffected analyses to a reviewer decision. Confirm original input files remain unchanged and the derivative, if any, is explicitly labeled with approval state.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-7: Communication. Someone without specialist knowledge can understand the result and next step.

Status: **not_tested**

The first report&\#x27;s communication concerns remain separately retained. Unguided comprehension, labels, keyboard behavior and accessibility are untested in this pass.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## Excluded scope

- .env.example: sensitive, data, sealed, or dependency path
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
- outputs/.gitkeep: non-allowlisted file type
- products/multimodal-case-room/practice\_cases.csv: non-allowlisted file type
- pytest.ini: non-allowlisted file type
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
