# Professor Bear Audit: Tripwire / Driftwire

## Review Identity

This is an independent, provisional source-code audit for judge deliberation. It is not an official grade.

- Entry: `Adhithyan245/tripwire`
- Commit: `45df43640836025b40e89fc190f913ad694a6011`
- Organizer reference: `6e15a399a64ffbf80778db0b462ac239e70086b9`
- Product: `cohort-control-tower`; Track 1, Cohort Firewall
- Pass: 1; reviewed 2026-11-14T20:01:26.285443+00:00
- Runtime: **not executed**; official freeze/receipt: **not verified**

## Executive Assessment

Driftwire separates release compatibility from question-specific readiness, checks declared dependencies and can verify supposedly unaffected analyses. The strongest unresolved issues in this source pass are a local adequacy-precedence defect, unresolved review states being counted as decided, and calculation rounding before movement classification. The retained parallel runtime review independently corroborates the first two at helper level, but its tiny-release full API control was Blocked. This supplement therefore does not claim that every undersized cohort is labeled Ready or that the whole application was bypassed.

## Workflow Traced

The public comparison route constructs two releases, detects changes and builds an evidence document. The builder maps changes through file, field and eligible-cohort dependencies, checks required inputs, optionally reruns unaffected analyses, and compares analytical slices. Release compatibility verdicts and research-question card verdicts are separate structures. Repair decisions are validated and copied into an output document without applying them to source releases.

## Findings At A Glance

| ID | Type | Priority | Finding |
|---|---|---|---|
| TW-01 | gap | P1 | Local compatibility can be Ready before adequacy is checked |
| TW-02 | gap | P1 | Recorded review activity is not the same as resolved evidence |
| TW-03 | gap | P2 | Display precision participates in analytical decisions |
| TW-04 | strength | P2 | Missing inputs and empty cohorts are not silently passed |
| TW-05 | strength | P2 | Unaffected analyses have a transparent verification route |
| TW-06 | strength | P2 | Repair decisions require a reason and reviewer role |

## Inspection Scope

The following files informed the implementation-level conclusions in this pass. Other collected files are not automatically treated as reviewed:

- `tripwire/api.py`
- `tripwire/findings.py`
- `tripwire/analyses.py`
- `tripwire/config.py`
- `tripwire/impact.py`
- `tripwire/verdicts.py`
- `tripwire/review.py`
- `tripwire/questions.py`
- `intake_prototype/ai_suggest.py`

## Parallel Review Preservation

Existing reports were read and retained. This is a separately versioned supplement; prior conclusions are not silently replaced.

The retained REPORT.md and TESTS.md were read after the parallel update at review commit 6ff89ad. They report 399 submitted tests passed and 6 skipped, plus helper-level probes; those are another agent's observations, not executions by this reviewer. TW-01 and TW-02 corroborate that report's first two issues with explicitly narrower scope; TW-03 revisits its precision concern. No earlier report or deck was replaced, and no test counts are treated as a score or detection-rate estimate.

This pass does not accept earlier agents' findings as established merely because they were reported. Any correction must identify the earlier claim and the new evidence explicitly.

## Detailed Criterion Review

# Judge review aid: tripwire

Repository: https://github.com/Adhithyan245/tripwire
Commit: `45df43640836025b40e89fc190f913ad694a6011`
Track: 1
Reviewer: Professor Bear / Codex source review

**Not an official result. Source review does not establish runtime behavior.**

Driftwire separates release compatibility from question-specific readiness, checks declared dependencies and can verify supposedly unaffected analyses. The strongest unresolved issues in this source pass are a local adequacy-precedence defect, unresolved review states being counted as decided, and calculation rounding before movement classification. The retained parallel runtime review independently corroborates the first two at helper level, but its tiny-release full API control was Blocked. This supplement therefore does not claim that every undersized cohort is labeled Ready or that the whole application was bypassed.

## Coverage and limitations

Collection: complete_with_exclusions; 125 text files; 8 excluded entries; recursive tree truncated: False.
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

- P1 · T1-2 · Local compatibility can be Ready before adequacy is checked: Either check adequacy before compatibility returns or export compatibility and adequacy as distinct, explicitly labeled dimensions. Preserve the outer guards and question checks rather than conflating their meanings.
- P1 · T1-4 · Recorded review activity is not the same as resolved evidence: Represent reviewed, awaiting evidence, rejected, approved and unresolved finding states separately. Require an explicit finding-level disposition when no repair exists and keep evidence requests open until their stated conditions are satisfied.
- P2 · T1-1 · Missing inputs and empty cohorts are not silently passed: Retain these guards and expose their reasons in every consumer. Extend explicit checks to finite measurement counts and clarify where group-level adequacy belongs.
- P2 · T1-2 · Unaffected analyses have a transparent verification route: Keep the explicit reason and expose the verification toggle and its cost. Add an input-slice digest and regression controls when analyses or cohort policies change.
- P2 · T1-3 · Display precision participates in analytical decisions: Keep full-precision analytical fields and format display text separately. Define absolute as well as relative tolerances near zero, and document whether baseline adequacy is assumed or assessed.
- P2 · T1-6 · Repair decisions require a reason and reviewer role: Preserve reason and role validation. For repeated reviews, add timestamped evidence-bound events and derive the current snapshot separately; do not present a role string as authenticated identity.

## T1-1: Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support.

Status: **observed**

Required-file, field and empty-cohort guards are source-supported. No unseen-data recall or false-positive estimate was produced.

### Missing inputs and empty cohorts are not silently passed

strength · P2 · Confidence: High for the inspected preflight branches; runtime behavior was not exercised here.

Before analytical execution, the builder checks required files in both releases, required fields and nonempty eligible cohorts. Each failure appends an explicit Insufficient Evidence analysis result and continues. This is separate from the undersized-but-nonempty adequacy issue above.

[Source lines 153–173](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/findings.py#L153-L173)

>         rerun = imp.affected or verify
>         if not all\(release\_a.has\(f\) and release\_b.has\(f\) for f in a.files\):
>             analyses\_out.append\(\{&quot;id&quot;: a.id, &quot;status&quot;: &quot;not\_rerun&quot;, &quot;verdict&quot;: &quot;Insufficient Evidence&quot;,
>                                  &quot;why&quot;: f&quot;Missing input file\(s\): \{a.files}&quot;, &quot;title&quot;: a.title}\)
>             verdicts\[a.id\] = &quot;Insufficient Evidence&quot;
>             continue
>         gaps = \[f&quot;release \{r.name} has no \{g}&quot; for r in \(release\_a, release\_b\) for g in missing\_inputs\(a, r\)\]
>         if gaps:  \# a field this analysis needs was dropped: say so instead of crashing
>             analyses\_out.append\(\{&quot;id&quot;: a.id, &quot;status&quot;: &quot;not\_rerun&quot;, &quot;verdict&quot;: &quot;Insufficient Evidence&quot;,
>                                  &quot;why&quot;: f&quot;Can&\#x27;t rerun \{a.id}: &quot; + &quot;; &quot;.join\(gaps\) + &quot;.&quot;, &quot;title&quot;: a.title,
>                                  &quot;impact&quot;: impacts\[a.id\].why\(len\(changes\)\), &quot;inputs&quot;: a.files, &quot;cohort&quot;: a.cohort}\)
>             verdicts\[a.id\] = &quot;Insufficient Evidence&quot;
>             continue
>         empty = \[r.name for r in \(release\_a, release\_b\) if not \_eligible\(a, r\)\]
>         if empty:  \# nothing to analyse is not evidence that nothing changed: never Ready on an empty cohort
>             analyses\_out.append\(\{&quot;id&quot;: a.id, &quot;status&quot;: &quot;not\_rerun&quot;, &quot;verdict&quot;: &quot;Insufficient Evidence&quot;,
>                                  &quot;why&quot;: f&quot;Can&\#x27;t rerun \{a.id}: no samples in its cohort \(\{a.cohort}\) in release &quot;
>                                         f&quot;\{&\#x27; or &\#x27;.join\(empty\)}.&quot;, &quot;title&quot;: a.title,
>                                  &quot;impact&quot;: impacts\[a.id\].why\(len\(changes\)\), &quot;inputs&quot;: a.files, &quot;cohort&quot;: a.cohort}\)
>             verdicts\[a.id\] = &quot;Insufficient Evidence&quot;
>             continue

[Source lines 26–34](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/analyses.py#L26-L34)

> def missing\_inputs\(a: &quot;Analysis&quot;, r: Release\) -&gt; list\[str\]:
>     &quot;&quot;&quot;Fields an analysis needs that this release doesn&\#x27;t have, e.g. &\#x27;protein\_rppa.tsv.gz: ERALPHA&\#x27;.&quot;&quot;&quot;
>     out = \[\]
>     for name, need in a.fields.items\(\):
>         if not need or not r.has\(name\):
>             continue
>         have = set\(r.clinical.columns\) if name == &quot;clinical.tsv&quot; else set\(r.table\(name\).index\)
>         out += \[f&quot;\{name}: \{f}&quot; for f in sorted\(set\(need\) - have\)\]
>     return out

Supplemental rules: None cited; official criterion above applies.

Impact: A missing modality, dropped target field or empty cohort has an interpretable evidence-gap route rather than being equated with no detected change. The distinction prevents overgeneralizing TW-01 into a missing-input claim that the source contradicts.

Concrete change: Retain these guards and expose their reasons in every consumer. Extend explicit checks to finite measurement counts and clarify where group-level adequacy belongs.

Acceptance check: Independently omit a required file, drop ERALPHA, remove all eligible samples and supply valid inputs. Verify the first three name the missing evidence and the valid control reaches analysis execution.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-2: Reasoning for the research question. Changes its result appropriately when the research question or intended use changes.

Status: **observed**

Question cards, dependency mapping and verification reruns are meaningful strengths. Local compatibility versus adequacy and precision policy need explicit interpretation.

### Local compatibility can be Ready before adequacy is checked

gap · P1 · Confidence: High for branch ordering; end-to-end generalization is explicitly limited by the retained counterexample.

release\_verdict handles the unaffected branch before movement.insufficient. With an unmoved result and unchanged input slice it returns Ready even if the movement object reports insufficient samples. The builder rejects missing files, missing fields and empty cohorts first, and question readiness is separate. This is a local compatibility-field issue, not evidence that all small-cohort end-to-end results are Ready.

[Source lines 24–45](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/verdicts.py#L24-L45)

> def release\_verdict\(affected: bool, movement: Movement &\#124; None, inputs=None\) -&gt; AnalysisVerdict:
>     &quot;&quot;&quot;movement is None when the analysis wasn&\#x27;t rerun. inputs: a SliceDiff of exactly what it reads, if computed.&quot;&quot;&quot;
>     if movement is None:
>         return AnalysisVerdict\(&quot;Ready&quot;, &quot;Nothing this analysis uses changed; not rerun.&quot;\)
>     if not affected:
>         if movement.moved:
>             return AnalysisVerdict\(&quot;Blocked&quot;, &quot;The result moved although no detected change touches this &quot;
>                                    f&quot;analysis: something changed that the detector didn&\#x27;t report \(\{movement.magnitude}\).&quot;\)
>         if inputs is not None and inputs.any:
>             return AnalysisVerdict\(&quot;Conditional&quot;, &quot;Data this analysis reads changed with no detected change to explain it, &quot;
>                                    f&quot;though the result didn&\#x27;t move \(\{movement.magnitude}\).&quot;\)
>         same = f&quot;the \{inputs.identical} samples it reads are identical in both releases; &quot; if inputs is not None else &quot;&quot;
>         return AnalysisVerdict\(&quot;Ready&quot;, f&quot;Nothing this analysis uses changed: \{same}a check rerun confirms it \(\{movement.magnitude}\).&quot;\)
>     if movement.insufficient:
>         return AnalysisVerdict\(&quot;Insufficient Evidence&quot;, f&quot;Too few samples left in a group after the change \(\{movement.magnitude}\).&quot;\)
>     if movement.flipped:
>         return AnalysisVerdict\(&quot;Blocked&quot;, f&quot;The conclusion flipped \(\{movement.magnitude}\).&quot;\)
>     if movement.beyond\_tolerance:
>         return AnalysisVerdict\(&quot;Blocked&quot;, f&quot;The result moved beyond tolerance \(\{movement.magnitude}\).&quot;\)
>     if movement.moved:
>         return AnalysisVerdict\(&quot;Conditional&quot;, f&quot;Inputs changed; the result moved within tolerance \(\{movement.magnitude}\).&quot;\)
>     return AnalysisVerdict\(&quot;Conditional&quot;, f&quot;Inputs changed but the result did not move \(\{movement.magnitude}\).&quot;\)

[Source lines 153–173](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/findings.py#L153-L173)

>         rerun = imp.affected or verify
>         if not all\(release\_a.has\(f\) and release\_b.has\(f\) for f in a.files\):
>             analyses\_out.append\(\{&quot;id&quot;: a.id, &quot;status&quot;: &quot;not\_rerun&quot;, &quot;verdict&quot;: &quot;Insufficient Evidence&quot;,
>                                  &quot;why&quot;: f&quot;Missing input file\(s\): \{a.files}&quot;, &quot;title&quot;: a.title}\)
>             verdicts\[a.id\] = &quot;Insufficient Evidence&quot;
>             continue
>         gaps = \[f&quot;release \{r.name} has no \{g}&quot; for r in \(release\_a, release\_b\) for g in missing\_inputs\(a, r\)\]
>         if gaps:  \# a field this analysis needs was dropped: say so instead of crashing
>             analyses\_out.append\(\{&quot;id&quot;: a.id, &quot;status&quot;: &quot;not\_rerun&quot;, &quot;verdict&quot;: &quot;Insufficient Evidence&quot;,
>                                  &quot;why&quot;: f&quot;Can&\#x27;t rerun \{a.id}: &quot; + &quot;; &quot;.join\(gaps\) + &quot;.&quot;, &quot;title&quot;: a.title,
>                                  &quot;impact&quot;: impacts\[a.id\].why\(len\(changes\)\), &quot;inputs&quot;: a.files, &quot;cohort&quot;: a.cohort}\)
>             verdicts\[a.id\] = &quot;Insufficient Evidence&quot;
>             continue
>         empty = \[r.name for r in \(release\_a, release\_b\) if not \_eligible\(a, r\)\]
>         if empty:  \# nothing to analyse is not evidence that nothing changed: never Ready on an empty cohort
>             analyses\_out.append\(\{&quot;id&quot;: a.id, &quot;status&quot;: &quot;not\_rerun&quot;, &quot;verdict&quot;: &quot;Insufficient Evidence&quot;,
>                                  &quot;why&quot;: f&quot;Can&\#x27;t rerun \{a.id}: no samples in its cohort \(\{a.cohort}\) in release &quot;
>                                         f&quot;\{&\#x27; or &\#x27;.join\(empty\)}.&quot;, &quot;title&quot;: a.title,
>                                  &quot;impact&quot;: impacts\[a.id\].why\(len\(changes\)\), &quot;inputs&quot;: a.files, &quot;cohort&quot;: a.cohort}\)
>             verdicts\[a.id\] = &quot;Insufficient Evidence&quot;
>             continue

[Source lines 119–127](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/analyses.py#L119-L127)

> def a1\_compare\(b: dict, a: dict\) -&gt; Movement:
>     db, da = b\[&quot;difference&quot;\], a\[&quot;difference&quot;\]
>     rel = abs\(da - db\) / abs\(db\) if db else float\(&quot;inf&quot;\)
>     tol = CONFIG\[&quot;A1\_difference\_rel\_tolerance&quot;\]
>     flipped = \(db &gt; 0\) \!= \(da &gt; 0\)
>     moved = \_strip\(b\) \!= \_strip\(a\) or set\(b\[&quot;sample\_ids&quot;\]\) \!= set\(a\[&quot;sample\_ids&quot;\]\)
>     insufficient = min\(a\[&quot;n\_positive&quot;\], a\[&quot;n\_negative&quot;\]\) &lt; CONFIG\[&quot;min\_samples\_per\_group&quot;\]
>     return Movement\(moved, rel &gt; tol, flipped, insufficient,
>                     f&quot;difference \{db} -&gt; \{da} \(\{rel:.1%} relative; tolerance \{tol:.0%}\)&quot;\)

[Source lines 5–10](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/config.py#L5-L10)

>     \# A1: relative change in the Positive-minus-Negative ER-alpha difference that still counts as &quot;moved within tolerance&quot;
>     &quot;A1\_difference\_rel\_tolerance&quot;: 0.05,
>     \# A2: largest shift in any subtype&\#x27;s share, in percentage points
>     &quot;A2\_percent\_pp\_tolerance&quot;: 1.0,
>     \# Fewer than this many samples in any compared group -&gt; Insufficient Evidence
>     &quot;min\_samples\_per\_group&quot;: 20,

Supplemental rules: None cited; official criterion above applies.

Impact: A consumer reading only an analysis compatibility field could interpret stability as adequate evidence. The parallel reviewer reproduced this helper behavior but observed Blocked in its tiny-release full API control, so the broader bypass is not established.

Concrete change: Either check adequacy before compatibility returns or export compatibility and adequacy as distinct, explicitly labeled dimensions. Preserve the outer guards and question checks rather than conflating their meanings.

Acceptance check: Trace an unchanged nonempty cohort below the configured minimum through the helper, A1/A2 fields, selected question and overall output. Require a visible adequacy warning wherever compatibility is Ready, and retain a sufficiently sized unchanged control.

### Unaffected analyses have a transparent verification route

strength · P2 · Confidence: High for dependency and rerun structure; performance and detection coverage remain unmeasured.

The impact map evaluates relevant files, fields and the union of eligible samples from both releases. verify\_unaffected defaults to true, so the builder can rerun supposedly unaffected analyses and compare actual slices. Exported rerun\_reason distinguishes affected execution from verification rather than disguising verification as required work.

[Source lines 47–66](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/impact.py#L47-L66)

> def touches\(ch: Change, a: Analysis, eligible: set\[str\]\) -&gt; tuple\[bool, str\]:
>     if ch.file not in a.files:
>         return False, f&quot;in a file it doesn&\#x27;t read \(\{ch.file}\)&quot;
>     used = a.fields.get\(ch.file, set\(\)\)  \# None = reads every row of that file
>     if ch.fields and used is not None and not \(set\(ch.fields\) &amp; used\):
>         return False, f&quot;change fields it doesn&\#x27;t use \(\{ch.file}: \{&\#x27;, &\#x27;.join\(sorted\(ch.fields\)\)\[:80\]}\)&quot;
>     if not \(\_ids\(ch\) &amp; eligible\):
>         return False, &quot;are samples outside its cohort&quot;
>     return True, &quot;&quot;
> 
> 
> def \_eligible\(a: Analysis, r: Release\) -&gt; set\[str\]:
>     &quot;&quot;&quot;The analysis cohort in one release, or empty when that release lacks its inputs. A missing file or field
>     is reported later as Insufficient Evidence with the reason \(findings.build\); it must not crash the map.&quot;&quot;&quot;
>     if not all\(r.has\(f\) for f in a.files\):
>         return set\(\)
>     try:
>         return a.eligible\(r\)
>     except \(KeyError, ValueError, OSError\):
>         return set\(\)

[Source lines 69–82](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/impact.py#L69-L82)

> def map\_impact\(changes: list\[Change\], release\_a: Release, release\_b: Release,
>                analyses: list\[Analysis\] = ANALYSES\) -&gt; dict\[str, Impact\]:
>     out = \{}
>     for a in analyses:
>         eligible = \_eligible\(a, release\_a\) &\#124; \_eligible\(a, release\_b\)
>         imp = Impact\(a\)
>         for i, ch in enumerate\(changes\):
>             hit, reason = touches\(ch, a, eligible\)
>             if hit:
>                 imp.touched\_by.append\(i\)
>             else:
>                 imp.skipped\[reason\] += 1
>         out\[a.id\] = imp
>     return out

[Source lines 19–21](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/config.py#L19-L21)

>     \# Rerun the analyses the impact map says are unaffected, to check the map. If one moved anyway,
>     \# something changed that the detector didn&\#x27;t report, and the analysis is Blocked.
>     &quot;verify\_unaffected&quot;: True,

[Source lines 174–190](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/findings.py#L174-L190)

>         before = after = mv = sd = None
>         if rerun:
>             before, after = a.run\(release\_a\), a.run\(release\_b\)
>             mv = a.compare\(before, after\)
>             sd = slice\_diff\(a.slice\(release\_a\), a.slice\(release\_b\)\)
>         v = release\_verdict\(imp.affected, mv, sd\)
>         verdicts\[a.id\] = v.verdict
>         if mv is not None and not imp.affected and \(mv.moved or sd.any\):
>             unexplained.append\(\(a, mv, sd\)\)
>         entry = \{&quot;id&quot;: a.id, &quot;status&quot;: &quot;not\_rerun&quot; if mv is None else \(&quot;changed&quot; if mv.moved else &quot;unchanged&quot;\),
>                  &quot;title&quot;: a.title, &quot;verdict&quot;: v.verdict, &quot;why&quot;: v.reason, &quot;impact&quot;: imp.why\(len\(changes\)\),
>                  &quot;inputs&quot;: a.files, &quot;cohort&quot;: a.cohort}
>         if mv is not None:
>             entry\[&quot;before&quot;\], entry\[&quot;after&quot;\] = public\(before\), public\(after\)
>             entry\[&quot;rerun\_reason&quot;\] = &quot;affected by detected changes&quot; if imp.affected else \\
>                 &quot;verification rerun: the impact map said unaffected&quot;
>             entry\[&quot;input\_changes&quot;\] = sd.counts\(\)  \# sample by sample, exactly what it reads

Supplemental rules: None cited; official criterion above applies.

Impact: This can detect a missed dependency when an allegedly unaffected result moves. Extra verification work is an intentional cross-check here, not by itself a failure to understand selective recomputation.

Concrete change: Keep the explicit reason and expose the verification toggle and its cost. Add an input-slice digest and regression controls when analyses or cohort policies change.

Acceptance check: Change an unused field, then an A1 field in an eligible sample. Compare runs with verification enabled and disabled; show which executions were necessary, which were cross-checks, and how unexplained movement is surfaced.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-3: Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion.

Status: **observed**

Pinned source references and input-slice evidence improve traceability. Rounded calculation fields should not control full-precision scientific conclusions.

### Display precision participates in analytical decisions

gap · P2 · Confidence: High for precision flow; no numerical fixture or organizer parity test was executed by this reviewer.

A1 rounds means and the group difference to three decimals before a1\_compare computes relative movement and direction. Its input slice retains repr of the numeric value, so a slice change can still be visible even when the displayed analytical difference is quantized. The concern is classification fidelity, not a claim that every small input change is wholly undetected.

[Source lines 91–110](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/analyses.py#L91-L110)

> def a1\_run\(r: Release\) -&gt; dict:
>     er = \_clinical\(r\).set\_index\(&quot;sampleID&quot;\)\[ER\_COL\]
>     samples = \[s for s in r.protein.columns if is\_primary\(s\) and er.get\(s\) in \(&quot;Positive&quot;, &quot;Negative&quot;\)\]
>     vals = r.protein.loc\[&quot;ERALPHA&quot;, samples\]
>     pos = vals\[\[s for s in samples if er\[s\] == &quot;Positive&quot;\]\]
>     neg = vals\[\[s for s in samples if er\[s\] == &quot;Negative&quot;\]\]
>     mp, mn = float\(pos.mean\(\)\), float\(neg.mean\(\)\)
>     return \{&quot;n\_samples&quot;: len\(samples\), &quot;n\_positive&quot;: int\(pos.size\), &quot;n\_negative&quot;: int\(neg.size\),
>             &quot;mean\_positive&quot;: round\(mp, 3\), &quot;mean\_negative&quot;: round\(mn, 3\), &quot;difference&quot;: round\(mp - mn, 3\),
>             &quot;sample\_ids&quot;: sorted\(samples\)}
> 
> 
> def a1\_slice\(r: Release\) -&gt; dict\[str, tuple\]:
>     er = \_clinical\(r\).set\_index\(&quot;sampleID&quot;\)\[ER\_COL\]
>     row = r.protein.loc\[&quot;ERALPHA&quot;\]
>     out = \{}
>     for s in r.protein.columns:
>         if is\_primary\(s\) and er.get\(s\) in \(&quot;Positive&quot;, &quot;Negative&quot;\):
>             v = float\(row\[s\]\)
>             out\[s\] = \(\(er\[s\], repr\(v\)\), f&quot;ER \{er\[s\]}, ERALPHA \{v:.3f}&quot;\)

[Source lines 119–127](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/analyses.py#L119-L127)

> def a1\_compare\(b: dict, a: dict\) -&gt; Movement:
>     db, da = b\[&quot;difference&quot;\], a\[&quot;difference&quot;\]
>     rel = abs\(da - db\) / abs\(db\) if db else float\(&quot;inf&quot;\)
>     tol = CONFIG\[&quot;A1\_difference\_rel\_tolerance&quot;\]
>     flipped = \(db &gt; 0\) \!= \(da &gt; 0\)
>     moved = \_strip\(b\) \!= \_strip\(a\) or set\(b\[&quot;sample\_ids&quot;\]\) \!= set\(a\[&quot;sample\_ids&quot;\]\)
>     insufficient = min\(a\[&quot;n\_positive&quot;\], a\[&quot;n\_negative&quot;\]\) &lt; CONFIG\[&quot;min\_samples\_per\_group&quot;\]
>     return Movement\(moved, rel &gt; tol, flipped, insufficient,
>                     f&quot;difference \{db} -&gt; \{da} \(\{rel:.1%} relative; tolerance \{tol:.0%}\)&quot;\)

Supplemental rules: None cited; official criterion above applies.

Impact: Near-zero effects can cross a sign or relative-tolerance boundary because of rounding, while other changes can disappear from the numerical summary. Input-change evidence does not restore the lost full-precision effect used in the verdict.

Concrete change: Keep full-precision analytical fields and format display text separately. Define absolute as well as relative tolerances near zero, and document whether baseline adequacy is assumed or assessed.

Acceptance check: Compare full-precision near-zero effects on either side of a tolerance and a zero-crossing boundary. Changing display precision must not change classification, and input-slice evidence must remain visible even when the final aggregate is unchanged.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-4: Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review.

Status: **observed**

Missing required question checks become unavailable rather than pass. Review activity must remain distinguishable from resolved evidence and approval.

### Recorded review activity is not the same as resolved evidence

gap · P1 · Confidence: High for the inspected list construction; parallel helper reproductions are attributed in the retained TESTS.md.

review\_status considers any repair ID appearing in decisions to be decided, regardless of whether its decision is request\_more\_evidence. A flagged finding with no linked repair also disappears from open because all over an empty list is true. apply\_decisions explicitly permits request\_more\_evidence. These are helper semantics; a user-interface approval bypass was not established here.

[Source lines 10–17](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L10-L17)

> DECISIONS = \(&quot;approve&quot;, &quot;reject&quot;, &quot;request\_more\_evidence&quot;\)
> LABELS = \{&quot;approve&quot;: &quot;Approve&quot;, &quot;reject&quot;: &quot;Reject&quot;, &quot;request\_more\_evidence&quot;: &quot;Request more evidence&quot;}
> 
> 
> def apply\_decisions\(doc: dict, decisions: dict\[str, dict\]\) -&gt; dict:
>     &quot;&quot;&quot;decisions: repair\_id -&gt; \{&quot;decision&quot;, &quot;reason&quot;, &quot;reviewer\_role&quot;}. Returns a new document; the input is untouched.
> 
>     Raises ValueError for an unknown repair, an unknown decision, or a missing reason or role.&quot;&quot;&quot;

[Source lines 21–34](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L21-L34)

>         if rid not in repairs:
>             raise ValueError\(f&quot;unknown repair \{rid\!r}&quot;\)
>         if d.get\(&quot;decision&quot;\) not in DECISIONS:
>             raise ValueError\(f&quot;\{rid}: decision must be one of \{DECISIONS}&quot;\)
>         reason, role = \(d.get\(&quot;reason&quot;\) or &quot;&quot;\).strip\(\), \(d.get\(&quot;reviewer\_role&quot;\) or &quot;&quot;\).strip\(\)
>         if not reason:
>             raise ValueError\(f&quot;\{rid}: a reason is required&quot;\)
>         if not role:
>             raise ValueError\(f&quot;\{rid}: the reviewer&\#x27;s role is required&quot;\)
>         out.append\(\{&quot;repair\_id&quot;: rid, &quot;decision&quot;: d\[&quot;decision&quot;\], &quot;reason&quot;: reason, &quot;reviewer\_role&quot;: role,
>                     &quot;original\_preserved&quot;: True}\)
>     new = copy.deepcopy\(doc\)
>     new\[&quot;decisions&quot;\] = sorted\(out, key=lambda x: \[r\[&quot;id&quot;\] for r in doc\[&quot;repairs&quot;\]\].index\(x\[&quot;repair\_id&quot;\]\)\)
>     return new

[Source lines 37–46](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L37-L46)

> def review\_status\(doc: dict\) -&gt; dict:
>     &quot;&quot;&quot;Which findings flagged for review still have an undecided repair.&quot;&quot;&quot;
>     decided = \{d\[&quot;repair\_id&quot;\] for d in doc.get\(&quot;decisions&quot;, \[\]\)}
>     by\_finding: dict\[str, list\[str\]\] = \{}
>     for r in doc.get\(&quot;repairs&quot;, \[\]\):
>         for f in r.get\(&quot;addresses&quot;, \[\]\):
>             by\_finding.setdefault\(f, \[\]\).append\(r\[&quot;id&quot;\]\)
>     flagged = \[f\[&quot;id&quot;\] for f in doc.get\(&quot;findings&quot;, \[\]\) if f.get\(&quot;needs\_human\_review&quot;\)\]
>     open\_ = \[f for f in flagged if not all\(rid in decided for rid in by\_finding.get\(f, \[\]\)\)\]
>     return \{&quot;flagged&quot;: flagged, &quot;open&quot;: open\_, &quot;decided\_repairs&quot;: sorted\(decided\)}

Supplemental rules: None cited; official criterion above applies.

Impact: The open list can conceal a continuing evidence obligation or a finding without a repair. A record of reviewer activity should not imply that the underlying concern has been resolved or approved.

Concrete change: Represent reviewed, awaiting evidence, rejected, approved and unresolved finding states separately. Require an explicit finding-level disposition when no repair exists and keep evidence requests open until their stated conditions are satisfied.

Acceptance check: Use synthetic documents with a flagged finding and no repair, then a linked repair with request\_more\_evidence, reject and approve. Verify each exported state communicates its distinct meaning and that requesting evidence never appears as authorization to proceed.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-5: Working tool and clear setup. Judges can run the core workflow from the submitted repository.

Status: **not_tested**

Another agent&\#x27;s retained TESTS.md reports a passing submitted suite with skips and limits. This source reviewer did not execute the app, reproduce that suite or verify a hosted demo.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T1-6: Useful next steps. Suggested fixes are specific and match the size and importance of the problem.

Status: **observed**

Validated repair decisions preserve originals. State semantics and evidence-bound review history remain important follow-ups.

### Repair decisions require a reason and reviewer role

strength · P2 · Confidence: High for helper validation and copying; authentication, persistence and UI behavior remain untested.

apply\_decisions rejects unknown repair IDs, unsupported decisions, blank reasons and blank reviewer roles. It deep-copies the document and records original\_preserved without applying the repair to source data. The resulting decisions field is a current snapshot, not an immutable history.

[Source lines 14–34](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L14-L34)

> def apply\_decisions\(doc: dict, decisions: dict\[str, dict\]\) -&gt; dict:
>     &quot;&quot;&quot;decisions: repair\_id -&gt; \{&quot;decision&quot;, &quot;reason&quot;, &quot;reviewer\_role&quot;}. Returns a new document; the input is untouched.
> 
>     Raises ValueError for an unknown repair, an unknown decision, or a missing reason or role.&quot;&quot;&quot;
>     repairs = \{r\[&quot;id&quot;\] for r in doc.get\(&quot;repairs&quot;, \[\]\)}
>     out = \[\]
>     for rid, d in decisions.items\(\):
>         if rid not in repairs:
>             raise ValueError\(f&quot;unknown repair \{rid\!r}&quot;\)
>         if d.get\(&quot;decision&quot;\) not in DECISIONS:
>             raise ValueError\(f&quot;\{rid}: decision must be one of \{DECISIONS}&quot;\)
>         reason, role = \(d.get\(&quot;reason&quot;\) or &quot;&quot;\).strip\(\), \(d.get\(&quot;reviewer\_role&quot;\) or &quot;&quot;\).strip\(\)
>         if not reason:
>             raise ValueError\(f&quot;\{rid}: a reason is required&quot;\)
>         if not role:
>             raise ValueError\(f&quot;\{rid}: the reviewer&\#x27;s role is required&quot;\)
>         out.append\(\{&quot;repair\_id&quot;: rid, &quot;decision&quot;: d\[&quot;decision&quot;\], &quot;reason&quot;: reason, &quot;reviewer\_role&quot;: role,
>                     &quot;original\_preserved&quot;: True}\)
>     new = copy.deepcopy\(doc\)
>     new\[&quot;decisions&quot;\] = sorted\(out, key=lambda x: \[r\[&quot;id&quot;\] for r in doc\[&quot;repairs&quot;\]\].index\(x\[&quot;repair\_id&quot;\]\)\)
>     return new

Supplemental rules: None cited; official criterion above applies.

Impact: The helper has a useful human accountability boundary and avoids silently mutating input evidence. Its benefit should be retained while adding the unresolved-evidence states identified in TW-02.

Concrete change: Preserve reason and role validation. For repeated reviews, add timestamped evidence-bound events and derive the current snapshot separately; do not present a role string as authenticated identity.

Acceptance check: Attempt an unknown repair and blank reason/role, then record an authorized decision. Verify invalid requests fail, the original document remains unchanged, and later revisions preserve a distinguishable history if history is claimed.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-7: Communication. Someone without specialist knowledge can understand the result and next step.

Status: **not_tested**

Communicate compatibility, evidence adequacy and question readiness separately. User comprehension and accessibility are untested in this pass.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## Excluded scope

- .github/CODEOWNERS: non-allowlisted file type
- .gitignore: non-allowlisted file type
- .python-version: non-allowlisted file type
- redteam/answer\_key\_TEMPLATE.md: sensitive or generated filename
- redteam/results/.gitkeep: non-allowlisted file type
- redteam/results/report.html: file-size limit
- site/.gitignore: non-allowlisted file type
- site/data/practice.replay.json: sensitive, data, sealed, or dependency path

## Judge Follow-Up Sequence

1. Verify the official final commit and product declaration.
2. Start with the highest-priority synthetic acceptance checks above.
3. Follow one finding through evidence, affected versus unaffected analyses, proposed repair and human decision.
4. Verify the exported artifact against the organizer contract without reading sealed answers.
5. Record actual results separately from this static audit; revise only claims the new evidence supports.
