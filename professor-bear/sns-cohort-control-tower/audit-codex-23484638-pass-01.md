# Professor Bear Audit: SNS Cohort Control Tower

## Review Identity

This is an independent, provisional source-code audit for judge deliberation. It is not an official grade.

- Entry: `saigunavardhan/sns-cohort-control-tower`
- Commit: `c1e8b79a2987cee6087d847867f9895deaa109a4`
- Organizer reference: `6e15a399a64ffbf80778db0b462ac239e70086b9`
- Product: `cohort-control-tower`; Track 1, Cohort Firewall
- Pass: 1; reviewed 2026-11-14T20:07:34.133368+00:00
- Runtime: **not executed**; official freeze/receipt: **not verified**

## Executive Assessment

SNS connects content fingerprints, detected changes, per-analysis before/after results, repair simulations and a concrete cohort export. The key concerns are the authority boundary between proposed and approved repairs, flagging that also restores membership, a no-finding Ready branch that bypasses movement checks, and a hard size boundary in wide-table recognition. The retained parallel review provides targeted helper reproductions; this supplement traces their source and limits rather than claiming a full live-application exploit or a measured detection rate.

## Workflow Traced

Release tables are recognized and hashed, compared for identity/value changes, and associated with analysis context. The analysis layer runs baseline, candidate and a temporary repaired release. Findings export numerical comparisons, dependency hints and a release verdict. A separate cohort path parses repairs into sets, applies membership operations and writes a derived sample table; its behavior must be distinguished from merely displaying proposed actions.

## Findings At A Glance

| ID | Type | Priority | Finding |
|---|---|---|---|
| SN-01 | gap | P1 | Cohort repair parsing does not consult approval decisions |
| SN-02 | gap | P1 | Flagging an absent sample can also restore it |
| SN-03 | gap | P1 | No detected finding bypasses movement and adequacy checks |
| SN-04 | gap | P2 | Wide-table recognition depends on having more than ten samples |
| SN-05 | strength | P2 | A failed candidate analysis has an explicit uncertainty route |
| SN-06 | strength | P2 | Release provenance includes named content hashes |
| SN-07 | strength | P2 | Before, after and simulated repair results are inspectable |

## Inspection Scope

The following files informed the implementation-level conclusions in this pass. Other collected files are not automatically treated as reviewed:

- `sns/engine/cohort.py`
- `sns/engine/release.py`
- `sns/engine/impact.py`
- `sns/engine/findings.py`
- `sns/server.py`

## Parallel Review Preservation

Existing reports were read and retained. This is a separately versioned supplement; prior conclusions are not silently replaced.

The existing REPORT.md and TESTS.md were read after the parallel update and remain unchanged. They report eight targeted safeguards, including positive controls, with six unmet and two met; these are not representative accuracy estimates. No submitted test suite was identified in their inspected scope, which is not proof that the team performed no testing. SN-01 through SN-04 independently trace the same concerns, with helper versus full-workflow scope made explicit. No submission code or probes were executed by this reviewer.

This pass does not accept earlier agents' findings as established merely because they were reported. Any correction must identify the earlier claim and the new evidence explicitly.

## Detailed Criterion Review

# Judge review aid: sns-cohort-control-tower

Repository: https://github.com/saigunavardhan/sns-cohort-control-tower
Commit: `c1e8b79a2987cee6087d847867f9895deaa109a4`
Track: 1
Reviewer: Professor Bear / Codex source review

**Not an official result. Source review does not establish runtime behavior.**

SNS connects content fingerprints, detected changes, per-analysis before/after results, repair simulations and a concrete cohort export. The key concerns are the authority boundary between proposed and approved repairs, flagging that also restores membership, a no-finding Ready branch that bypasses movement checks, and a hard size boundary in wide-table recognition. The retained parallel review provides targeted helper reproductions; this supplement traces their source and limits rather than claiming a full live-application exploit or a measured detection rate.

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

- P1 · T1-2 · No detected finding bypasses movement and adequacy checks: Assess result validity, required evidence and unexplained movement before the no-finding Ready return. Export both compatibility and adequacy states if they answer different questions.
- P1 · T1-4 · Cohort repair parsing does not consult approval decisions: For approved exports, accept only explicit approved decisions bound to the exact findings digest. Retain a separately labeled simulation mode for proposals and make its non-approved status travel with every output file.
- P1 · T1-6 · Flagging an absent sample can also restore it: Keep flagging and restoration as separate operations. An absent sample should remain absent unless an explicit restore proposal is approved with evidence explaining why the earlier membership is authoritative.
- P2 · T1-1 · Wide-table recognition depends on having more than ten samples: Use declared schema or robust header semantics independent of sample count. Record every discovered but unsupported file and prevent omission from being mistaken for absence or a clean comparison.
- P2 · T1-3 · Release provenance includes named content hashes: Keep content fingerprints and add a complete discovered-file inventory, including unsupported or skipped files. Bind review decisions and derived cohorts to the same evidence manifest.
- P2 · T1-4 · A failed candidate analysis has an explicit uncertainty route: Preserve this error-first behavior and extend typed execution states to baseline failure, nonfinite results and missing expected analyses. Avoid interpreting a missing error key as proof that numerical outputs are valid.
- P2 · T1-7 · Before, after and simulated repair results are inspectable: Label the third result as a baseline-recovery simulation and state the trust assumption beside it. Require independent evidence and human authorization before using simulated recovery as an approved repair.

## T1-1: Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support.

Status: **observed**

Layer recognition and the complete input inventory need explicit small-cohort checks. No unseen-input detection rate was measured.

### Wide-table recognition depends on having more than ten samples

gap · P2 · Confidence: High for the hard boundary; the parallel TESTS.md reports 1/10/11-sample probes and the 11-sample positive control.

load\_layer recognizes a TCGA-wide layout only with more than ten TCGA-named columns and the stated proportion. A smaller wide table falls through to long-format ID detection and may return None. load\_release retains only non-None layers, without an explicit unsupported-file result in that loop.

[Source lines 60–85](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/release.py#L60-L85)

> def load\_layer\(path, sha=None\):
>     path = Path\(path\)
>     raw = read\_table\(path\)
>     tcga\_cols = \[c for c in raw.columns if str\(c\).startswith\(TCGA\_PREFIX\)\]
>     if len\(tcga\_cols\) &gt; 10 and len\(tcga\_cols\) &gt;= 0.5 \* \(raw.shape\[1\] - 1\):
>         feature\_field = str\(raw.columns\[0\]\)
>         table = raw.set\_index\(raw.columns\[0\]\)\[tcga\_cols\].T
>         layout, id\_field = &quot;wide&quot;, &quot;columns&quot;
>     else:
>         id\_field = \_pick\_id\_column\(raw\)
>         if id\_field is None:
>             return None
>         table = raw.set\_index\(id\_field\)
>         layout, feature\_field = &quot;long&quot;, &quot;columns&quot;
>     table.index = table.index.astype\(str\)
>     table.index.name = &quot;sample\_id&quot;
>     table.columns = \[str\(c\) for c in table.columns\]
>     return Layer\(
>         name=path.name,
>         path=path,
>         layout=layout,
>         id\_field=str\(id\_field\),
>         feature\_field=feature\_field,
>         table=table,
>         sha256=sha or content\_sha256\(path\),
>     \)

[Source lines 88–106](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/release.py#L88-L106)

> def load\_release\(folder, reuse=None, skip\_files=None\):
>     folder = Path\(folder\)
>     reuse = reuse or \{}
>     skip = set\(skip\_files or \[\]\)
>     layers = \{}
>     for path in sorted\(folder.iterdir\(\)\):
>         if not \(path.is\_file\(\) and path.name.lower\(\).endswith\(DATA\_SUFFIXES\)\):
>             continue
>         if path.name in skip:
>             continue
>         sha = content\_sha256\(path\)
>         prev = reuse.get\(path.name\)
>         if prev is not None and prev.sha256 == sha:
>             layers\[path.name\] = replace\(prev, path=path\)
>             continue
>         layer = load\_layer\(path, sha\)
>         if layer is not None:
>             layers\[path.name\] = layer
>     return layers

Supplemental rules: None cited; official criterion above applies.

Impact: Small synthetic or research cohorts can be omitted from recognized input layers instead of being parsed or rejected with a reason. This is a supported-format boundary, not proof that all event files are affected.

Concrete change: Use declared schema or robust header semantics independent of sample count. Record every discovered but unsupported file and prevent omission from being mistaken for absence or a clean comparison.

Acceptance check: Load otherwise equivalent invented wide matrices with 1, 10 and 11 samples. Each must be parsed consistently or explicitly rejected, and the release inventory must retain the file and reason.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-2: Reasoning for the research question. Changes its result appropriately when the research question or intended use changes.

Status: **observed**

Analysis context is visible, but no-finding status must not override observed movement or adequacy. Token-derived dependencies also need review when analysis code changes.

### No detected finding bypasses movement and adequacy checks

gap · P1 · Confidence: High for precedence; the parallel review reports helper probes with a detected-sign-change positive control.

verdict\_for first handles an error in the new-release result, then returns Ready immediately when affected\_by is empty. Minimum group size, sign changes and relative movement are tested only afterward. Exported analysis notes say unaffected analyses were rerun to confirm no movement, but this branch does not require that confirmation.

[Source lines 187–210](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/impact.py#L187-L210)

> def verdict\_for\(affected\_by, before, after, min\_group=10\):
>     if &quot;error&quot; in \(after or \{}\):
>         return &quot;Insufficient Evidence&quot;, f&quot;analysis failed on the new release: \{after\[&\#x27;error&\#x27;\]}&quot;
>     if not affected\_by:
>         return &quot;Ready&quot;, &quot;no finding touches its input files, columns or samples&quot;
>     nb, na = numeric\_fields\(public\(before\)\), numeric\_fields\(public\(after\)\)
>     small = \{
>         k: v for k, v in na.items\(\)
>         if k.split\(&quot;.&quot;\)\[-1\].startswith\(&quot;n\_&quot;\) and v &lt; min\_group
>     }
>     if small:
>         listed = &quot;, &quot;.join\(f&quot;\{k}=\{int\(v\)}&quot; for k, v in small.items\(\)\)
>         return &quot;Insufficient Evidence&quot;, f&quot;too few samples after the change: \{listed} \(minimum \{min\_group}\)&quot;
>     shifts = \[\]
>     for k in sorted\(nb.keys\(\) &amp; na.keys\(\)\):
>         if k.split\(&quot;.&quot;\)\[-1\].startswith\(&quot;n\_&quot;\):
>             continue
>         b, a = nb\[k\], na\[k\]
>         if b == a:
>             continue
>         if b \!= 0 and a \!= 0 and \(b &gt; 0\) \!= \(a &gt; 0\):
>             return &quot;Blocked&quot;, f&quot;\{k} changed sign: \{b:g} in the old release, \{a:g} in the new release&quot;
>         rel = abs\(a - b\) / abs\(b\) if b else float\(&quot;inf&quot;\)
>         shifts.append\(\(rel, k, b, a\)\)

[Source lines 427–450](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/findings.py#L427-L450)

>     analyses, verdicts = \[\], \[\]
>     for aid, c in b.ctx.items\(\):
>         by = \[f\[&quot;id&quot;\] for f in findings if aid in f\[&quot;affects\_analyses&quot;\]\]
>         before = impact\[&quot;before&quot;\].get\(aid, \{}\)
>         after = impact\[&quot;after&quot;\].get\(aid, \{}\)
>         rep = impact\[&quot;repaired&quot;\].get\(aid, \{}\)
>         verdict, reason = verdict\_for\(by, before, after\)
>         verdicts.append\(verdict\)
>         entry = \{
>             &quot;id&quot;: aid,
>             &quot;status&quot;: &quot;changed&quot; if public\(before\) \!= public\(after\) else &quot;unchanged&quot;,
>             &quot;before&quot;: public\(before\),
>             &quot;after&quot;: public\(after\),
>             &quot;after\_repair&quot;: public\(rep\),
>             &quot;repair\_restores\_before&quot;: public\(rep\) == public\(before\),
>             &quot;description&quot;: c\[&quot;description&quot;\],
>             &quot;inputs&quot;: c\[&quot;inputs&quot;\],
>             &quot;uses\_columns&quot;: c\[&quot;used\_features&quot;\],
>             &quot;affected\_by&quot;: by,
>             &quot;verdict&quot;: verdict,
>             &quot;reason&quot;: reason,
>         }
>         if not by:
>             entry\[&quot;note&quot;\] = &quot;not affected by any finding; rerun only to confirm it did not move&quot;

Supplemental rules: None cited; official criterion above applies.

Impact: A missed dependency or detector miss can leave a changed result labeled Ready at this helper boundary. This differs from an intentionally verified stable result and from a guaranteed full-application bypass, which this reviewer did not demonstrate.

Concrete change: Assess result validity, required evidence and unexplained movement before the no-finding Ready return. Export both compatibility and adequacy states if they answer different questions.

Acceptance check: Compare no-finding cases with an unchanged adequate result, an undersized result and a sign change. Keep the valid stable positive control, and ensure absence of a finding alone cannot override the latter evidence problems.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-3: Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion.

Status: **observed**

Named content hashes and per-analysis results help provenance. Unsupported inputs and approval digests should be included in the handoff.

### Release provenance includes named content hashes

strength · P2 · Confidence: High for source construction; cache correctness and served artifact hashes were not verified in a running app.

load\_release computes a content digest and can reuse a parsed layer only when its prior digest matches. The findings document emits each release&\#x27;s file names, SHA-256 values and hash\_of=content. This distinguishes content identity from a directory label or mutable filename.

[Source lines 88–106](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/release.py#L88-L106)

> def load\_release\(folder, reuse=None, skip\_files=None\):
>     folder = Path\(folder\)
>     reuse = reuse or \{}
>     skip = set\(skip\_files or \[\]\)
>     layers = \{}
>     for path in sorted\(folder.iterdir\(\)\):
>         if not \(path.is\_file\(\) and path.name.lower\(\).endswith\(DATA\_SUFFIXES\)\):
>             continue
>         if path.name in skip:
>             continue
>         sha = content\_sha256\(path\)
>         prev = reuse.get\(path.name\)
>         if prev is not None and prev.sha256 == sha:
>             layers\[path.name\] = replace\(prev, path=path\)
>             continue
>         layer = load\_layer\(path, sha\)
>         if layer is not None:
>             layers\[path.name\] = layer
>     return layers

[Source lines 458–470](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/findings.py#L458-L470)

>     def files\(rel\):
>         return \[\{&quot;file&quot;: n, &quot;sha256&quot;: layer.sha256, &quot;hash\_of&quot;: &quot;content&quot;} for n, layer in sorted\(rel.items\(\)\)\]
> 
>     asked = \_join\(f&quot;\{aid} \(\{c\[&\#x27;description&\#x27;\].rstrip\(&\#x27;.&\#x27;\)}\)&quot; for aid, c in b.ctx.items\(\)\)
>     return \{
>         &quot;format\_version&quot;: &quot;0.2&quot;,
>         &quot;producer&quot;: \{&quot;team&quot;: team, &quot;product&quot;: product, &quot;track&quot;: &quot;cohort-firewall&quot;},
>         &quot;data&quot;: \{
>             &quot;dataset&quot;: dataset,
>             &quot;releases&quot;: \[
>                 \{&quot;name&quot;: a\_name, &quot;files&quot;: files\(rel\_a\)},
>                 \{&quot;name&quot;: b\_name, &quot;files&quot;: files\(rel\_b\)},
>             \],

Supplemental rules: None cited; official criterion above applies.

Impact: The export provides useful anchors for reproducing exactly which recognized files were compared. A hash is not a signature, a license check or proof that an earlier release is scientifically correct.

Concrete change: Keep content fingerprints and add a complete discovered-file inventory, including unsupported or skipped files. Bind review decisions and derived cohorts to the same evidence manifest.

Acceptance check: Change one synthetic file byte and confirm its digest and run identity change. Verify a renamed identical file is handled according to the documented identity policy and that unsupported files remain visible.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-4: Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review.

Status: **observed**

Candidate errors explicitly become Insufficient Evidence. Proposed, rejected, awaiting-review and approved repairs must remain separate.

### Cohort repair parsing does not consult approval decisions

gap · P1 · Confidence: High for parser and caller control flow; the parallel TESTS.md reports a rejected-exclusion helper reproduction, not a complete UI run.

parse\_repairs iterates every repair proposal and derives excluded, flagged, restored and relabeled sets without reading decisions. run\_cohort calls that parser and applies its mapping during require\_file steps. The parser does not distinguish an approved proposal from an explicitly rejected or undecided one.

[Source lines 45–69](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L45-L69)

> def parse\_repairs\(findings\_doc\):
>     &quot;&quot;&quot;Return dict: file -&gt; \{excluded, flagged, restored, relabeled}.&quot;&quot;&quot;
>     result = \{}
>     for rep in findings\_doc.get\(&quot;repairs&quot;, \[\]\):
>         action = rep\[&quot;action&quot;\]
>         for t in rep\[&quot;targets&quot;\]:
>             if t\[&quot;kind&quot;\] \!= &quot;sample&quot;:
>                 continue
>             sid = str\(t\[&quot;id&quot;\]\)
>             file = t.get\(&quot;file&quot;\) or &quot;&quot;
>             if file not in result:
>                 result\[file\] = \{&quot;excluded&quot;: set\(\), &quot;flagged&quot;: set\(\),
>                                 &quot;restored&quot;: set\(\), &quot;relabeled&quot;: \{}}
>             if action == &quot;exclude&quot;:
>                 result\[file\]\[&quot;excluded&quot;\].add\(sid\)
>             elif action == &quot;restore\_from\_previous\_release&quot;:
>                 result\[file\]\[&quot;restored&quot;\].add\(sid\)
>             elif action == &quot;flag\_for\_review&quot;:
>                 result\[file\]\[&quot;flagged&quot;\].add\(sid\)
>             elif action == &quot;relabel&quot;:
>                 note = t.get\(&quot;note&quot;, &quot;&quot;\)
>                 if &quot;rename back to&quot; in note:
>                     old\_id = note.split\(&quot;rename back to&quot;\)\[-1\].strip\(\)
>                     result\[file\]\[&quot;relabeled&quot;\]\[sid\] = old\_id
>     return result

[Source lines 123–137](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L123-L137)

> def run\_cohort\(spec, folder\_b, folder\_a, findings\_doc, slides\_path=None\):
>     &quot;&quot;&quot;Execute spec steps. Return \(samples\_df, steps\_log, applied\_repairs\).&quot;&quot;&quot;
>     repairs = parse\_repairs\(findings\_doc\)
>     all\_applied = \[\]
> 
>     \# Collect all samples from B to start
>     all\_b = set\(\)
>     for p in sorted\(Path\(folder\_b\).iterdir\(\)\):
>         if p.is\_file\(\) and p.name.lower\(\).endswith\(\(&quot;.tsv&quot;, &quot;.tsv.gz&quot;, &quot;.csv&quot;, &quot;.csv.gz&quot;\)\):
>             layer = load\_layer\(p\)
>             if layer:
>                 all\_b.update\(layer.table.index\)
> 
>     working = set\(all\_b\)
>     flagged = set\(\)

[Source lines 148–160](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L148-L160)

>         if step\_name == &quot;require\_file&quot;:
>             fname = step\_def\[&quot;file&quot;\]
>             step\_rec\[&quot;params&quot;\]\[&quot;file&quot;\] = fname
>             file\_b = \_file\_samples\(folder\_b, fname\)
>             repaired, new\_flagged, applied = \_apply\_file\_repairs\(file\_b, folder\_a, fname, repairs\)
>             all\_applied.extend\(applied\)
>             flagged &\#124;= new\_flagged
>             working &amp;= repaired
>             \# Flagged samples restored from A may not be in working after the intersect
>             \# Add them back if they&\#x27;re in repaired \(which they are\)
>             for sid in new\_flagged:
>                 if sid in repaired:
>                     working.add\(sid\)

Supplemental rules: None cited; official criterion above applies.

Impact: A derived cohort can reflect a proposal that a reviewer rejected. Original source files remain separate; the concern is the authority and labeling of the derivative, not an allegation that source data were overwritten.

Concrete change: For approved exports, accept only explicit approved decisions bound to the exact findings digest. Retain a separately labeled simulation mode for proposals and make its non-approved status travel with every output file.

Acceptance check: Provide a rejected exclusion, an undecided proposal and an approved repair. Only the approved action may affect an approved cohort; a preview may simulate others but must remain unmistakably unapproved.

### A failed candidate analysis has an explicit uncertainty route

strength · P2 · Confidence: High for the inspected branch; runtime tests were not executed by this reviewer.

Before the no-finding branch, verdict\_for checks the candidate analysis error field and returns Insufficient Evidence with its reason. This prevents a known candidate execution failure from automatically taking the ordinary Ready route.

[Source lines 187–199](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/impact.py#L187-L199)

> def verdict\_for\(affected\_by, before, after, min\_group=10\):
>     if &quot;error&quot; in \(after or \{}\):
>         return &quot;Insufficient Evidence&quot;, f&quot;analysis failed on the new release: \{after\[&\#x27;error&\#x27;\]}&quot;
>     if not affected\_by:
>         return &quot;Ready&quot;, &quot;no finding touches its input files, columns or samples&quot;
>     nb, na = numeric\_fields\(public\(before\)\), numeric\_fields\(public\(after\)\)
>     small = \{
>         k: v for k, v in na.items\(\)
>         if k.split\(&quot;.&quot;\)\[-1\].startswith\(&quot;n\_&quot;\) and v &lt; min\_group
>     }
>     if small:
>         listed = &quot;, &quot;.join\(f&quot;\{k}=\{int\(v\)}&quot; for k, v in small.items\(\)\)
>         return &quot;Insufficient Evidence&quot;, f&quot;too few samples after the change: \{listed} \(minimum \{min\_group}\)&quot;

Supplemental rules: None cited; official criterion above applies.

Impact: The explicit error state is worth retaining even while fixing movement precedence. It does not prove that all invalid numeric values or absent baselines are caught; those require separate coverage.

Concrete change: Preserve this error-first behavior and extend typed execution states to baseline failure, nonfinite results and missing expected analyses. Avoid interpreting a missing error key as proof that numerical outputs are valid.

Acceptance check: Supply an explicit candidate error with no affecting findings and verify Insufficient Evidence. Add baseline-error, nonfinite-output and valid-result controls and document the intended policy for each.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-5: Working tool and clear setup. Judges can run the core workflow from the submitted repository.

Status: **not_tested**

The parallel review found no conventional submitted suite in its scope and reports targeted helper probes. This pass did not run the CLI, servers or hosted UI.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T1-6: Useful next steps. Suggested fixes are specific and match the size and importance of the problem.

Status: **observed**

The cohort export is concrete, but flags must not implicitly restore membership and proposals must not override rejection.

### Flagging an absent sample can also restore it

gap · P1 · Confidence: High for the two membership-addition branches; the retained parallel review reports the helper effect with invented records.

\_apply\_file\_repairs adds a flagged sample back when it is absent from B but present in A, recording flag\_for\_review\_restored. The require\_file caller then explicitly re-adds flagged samples after its intersection. The source therefore assigns a membership-changing behavior to a review flag.

[Source lines 89–113](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L89-L113)

>     \# Flag-for-review: if sample is still in working, mark it; if dropped from B, add from A
>     samples\_a = \_file\_samples\(folder\_a, file\_name\) if folder\_a else set\(\)
>     for sid in sorted\(flagged\_targets\):
>         if sid in working:
>             flagged\_out.add\(sid\)
>             applied.append\(\{&quot;action&quot;: &quot;flag\_for\_review&quot;, &quot;sample&quot;: sid, &quot;file&quot;: file\_name}\)
>         elif sid in samples\_a:
>             working.add\(sid\)
>             flagged\_out.add\(sid\)
>             applied.append\(\{&quot;action&quot;: &quot;flag\_for\_review\_restored&quot;, &quot;sample&quot;: sid, &quot;file&quot;: file\_name}\)
> 
>     for sid in sorted\(restored\):
>         if sid in working:
>             applied.append\(\{&quot;action&quot;: &quot;restore\_from\_previous\_release&quot;, &quot;sample&quot;: sid, &quot;file&quot;: file\_name}\)
> 
>     for new\_id, old\_id in sorted\(relabeled.items\(\)\):
>         if new\_id in working:
>             working.discard\(new\_id\)
>             working.add\(old\_id\)
>             if new\_id in flagged\_out:
>                 flagged\_out.discard\(new\_id\)
>                 flagged\_out.add\(old\_id\)
>             applied.append\(\{&quot;action&quot;: &quot;relabel&quot;, &quot;sample&quot;: new\_id, &quot;renamed\_to&quot;: old\_id}\)
> 
>     return working, flagged\_out, applied

[Source lines 148–160](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L148-L160)

>         if step\_name == &quot;require\_file&quot;:
>             fname = step\_def\[&quot;file&quot;\]
>             step\_rec\[&quot;params&quot;\]\[&quot;file&quot;\] = fname
>             file\_b = \_file\_samples\(folder\_b, fname\)
>             repaired, new\_flagged, applied = \_apply\_file\_repairs\(file\_b, folder\_a, fname, repairs\)
>             all\_applied.extend\(applied\)
>             flagged &\#124;= new\_flagged
>             working &amp;= repaired
>             \# Flagged samples restored from A may not be in working after the intersect
>             \# Add them back if they&\#x27;re in repaired \(which they are\)
>             for sid in new\_flagged:
>                 if sid in repaired:
>                     working.add\(sid\)

Supplemental rules: None cited; official criterion above applies.

Impact: A flag requests investigation; it does not establish that removal from the newer release was erroneous. A documented withdrawal or corrected inclusion can be reversed before the missing evidence is resolved.

Concrete change: Keep flagging and restoration as separate operations. An absent sample should remain absent unless an explicit restore proposal is approved with evidence explaining why the earlier membership is authoritative.

Acceptance check: Use a synthetic sample deliberately absent from B. Flagging alone must not restore it; a separately authorized restore should be traceable and must not overwrite the original releases.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-7: Communication. Someone without specialist knowledge can understand the result and next step.

Status: **observed**

Before/after/repair numbers are useful when clearly labeled as simulations under baseline trust. Fresh-user comprehension and accessibility remain untested.

### Before, after and simulated repair results are inspectable

strength · P2 · Confidence: High for exported comparison fields and temporary simulation structure; numerical correctness and baseline truth remain untested.

Each analysis entry includes baseline, candidate and simulated repaired output, inputs, used features, affecting findings and a repair\_restores\_before equality field. The assessment layer builds a temporary repaired release and removes that temporary directory in finally. These are simulations relative to the assumed baseline, not independent truth checks.

[Source lines 427–450](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/findings.py#L427-L450)

>     analyses, verdicts = \[\], \[\]
>     for aid, c in b.ctx.items\(\):
>         by = \[f\[&quot;id&quot;\] for f in findings if aid in f\[&quot;affects\_analyses&quot;\]\]
>         before = impact\[&quot;before&quot;\].get\(aid, \{}\)
>         after = impact\[&quot;after&quot;\].get\(aid, \{}\)
>         rep = impact\[&quot;repaired&quot;\].get\(aid, \{}\)
>         verdict, reason = verdict\_for\(by, before, after\)
>         verdicts.append\(verdict\)
>         entry = \{
>             &quot;id&quot;: aid,
>             &quot;status&quot;: &quot;changed&quot; if public\(before\) \!= public\(after\) else &quot;unchanged&quot;,
>             &quot;before&quot;: public\(before\),
>             &quot;after&quot;: public\(after\),
>             &quot;after\_repair&quot;: public\(rep\),
>             &quot;repair\_restores\_before&quot;: public\(rep\) == public\(before\),
>             &quot;description&quot;: c\[&quot;description&quot;\],
>             &quot;inputs&quot;: c\[&quot;inputs&quot;\],
>             &quot;uses\_columns&quot;: c\[&quot;used\_features&quot;\],
>             &quot;affected\_by&quot;: by,
>             &quot;verdict&quot;: verdict,
>             &quot;reason&quot;: reason,
>         }
>         if not by:
>             entry\[&quot;note&quot;\] = &quot;not affected by any finding; rerun only to confirm it did not move&quot;

[Source lines 237–254](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/impact.py#L237-L254)

>     before = run\_analyses\(module, funcs, folder\_a\)
>     after = run\_analyses\(module, funcs, folder\_b\)
>     repaired\_dir = build\_repaired\_release\(rel\_a, rel\_b, diff\_report\)
>     try:
>         repaired = run\_analyses\(module, funcs, repaired\_dir\)
>     finally:
>         shutil.rmtree\(repaired\_dir, ignore\_errors=True\)
>     for aid, ctx in context.items\(\):
>         res\_a, res\_b = before.get\(aid, \{}\), after.get\(aid, \{}\)
>         ctx\[&quot;inputs&quot;\] = res\_a.get\(&quot;inputs&quot;\) or res\_b.get\(&quot;inputs&quot;\) or sorted\(ctx\[&quot;used\_features&quot;\]\)
>         ctx\[&quot;samples&quot;\] = set\(res\_a.get\(&quot;sample\_ids&quot;, \[\]\)\) &\#124; set\(res\_b.get\(&quot;sample\_ids&quot;, \[\]\)\)
>     return \{
>         &quot;analysis\_path&quot;: str\(analysis\_path\),
>         &quot;context&quot;: context,
>         &quot;before&quot;: before,
>         &quot;after&quot;: after,
>         &quot;repaired&quot;: repaired,
>     }

Supplemental rules: None cited; official criterion above applies.

Impact: The comparison can help a reviewer understand the numerical consequence of a proposal. Recovering an old number does not establish that restoring old data is factually correct, especially when B contains a legitimate correction.

Concrete change: Label the third result as a baseline-recovery simulation and state the trust assumption beside it. Require independent evidence and human authorization before using simulated recovery as an approved repair.

Acceptance check: Demonstrate a legitimate documented correction in B and a separate erroneous alteration. Both may differ from A, but only evidence and a reviewer decision should authorize reversal; equality with A must not substitute for that evidence.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

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
