# Professor Bear Audit: Cohort Firewall Control Tower

## Review Identity

This is an independent, provisional source-code audit for judge deliberation. It is not an official grade.

- Entry: `NinadRao0707/cohort-firewall`
- Commit: `ab5084f7caaa57e68636e2cd3fde97b20a47bf69`
- Organizer reference: `6e15a399a64ffbf80778db0b462ac239e70086b9`
- Product: `cohort-control-tower`; Track 1, Cohort Firewall
- Pass: 1; reviewed 2026-11-14T21:38:33.042334+00:00
- Runtime: **not executed**; official freeze/receipt: **not verified**

## Executive Assessment

The submission combines a release-change Control Tower with a question-readiness engine, versioned policy, signed certificates and explicit human review. The source has useful default-deny paths and content-keyed baseline caching. Important boundaries remain incomplete: missing candidate files can disappear from the comparison before selective rerun, baseline-only sample membership can miss newly eligible existing samples, duplicate IDs are normalized away, and review verifies only part of the evidence document. The latter three areas have separately published narrow synthetic corroboration; this reviewer executed no submission code. The missing-candidate-file path is a new source-derived follow-through that still needs an end-to-end positive/negative control. This is a provisional Track 1 review, not an official score, frozen-submission attestation or security/clinical certification.

## Workflow Traced

run_tower selects candidate-present files, fingerprints the corresponding baseline files and candidate release, checks those baseline hashes against the frozen manifest, detects profile/label/membership changes, loads the organizer's reference-analysis definitions, reruns analyses deemed affected, evaluates a versioned policy and emits v0.2 findings, repairs and before/after evidence. It also signs a payload derived from data hashes, question, analysis verdicts and policy. The API accepts a client-supplied result document for human review. Separately, the readiness engine runs named checks on an editable question spec and evaluates versioned conditions. This audit followed these source paths without importing any submission module, organizer reference module, envelope code, signing key or data file.

## Findings At A Glance

| ID | Type | Priority | Finding |
|---|---|---|---|
| CFT-01 | gap | P1 | Missing candidate inputs can bypass analysis availability checks |
| CFT-02 | gap | P1 | Dependency routing considers baseline members but can miss new entrants |
| CFT-03 | gap | P1 | Duplicate identifiers disappear before detection |
| CFT-04 | gap | P1 | Release review checks verdict binding but not the full evidence document |
| CFT-05 | gap | P1 | Question review records text without checking its signed spec hash |
| CFT-06 | strength | P2 | Policy separates measurements from versioned rules and missing-check states |
| CFT-07 | strength | P2 | Baseline cache identity includes current file-content hashes |
| CFT-08 | strength | P2 | Approval policy distinguishes unavailable results and explicit conditions |

## Inspection Scope

The following files informed the implementation-level conclusions in this pass. Other collected files are not automatically treated as reviewed:

- `README.md`
- `cohort_firewall/certificate.py`
- `cohort_firewall/review.py`
- `cohort_firewall/ledger.py`
- `cohort_firewall/engine.py`
- `cohort_firewall/policy.py`
- `cohort_firewall/tower/releases.py`
- `cohort_firewall/tower/diff.py`
- `cohort_firewall/tower/analyses.py`
- `cohort_firewall/tower/findings.py`
- `cohort_firewall/tower/run.py`
- `rules/tower_v0_1.yaml`
- `api/main.py`
- `tests/test_review.py`

## Parallel Review Preservation

Existing reports were read and retained. This is a separately versioned supplement; prior conclusions are not silently replaced.

The existing REPORT.md, TESTS.md, independent-tests.json and tests/test_review.py were read before this supplement. The parallel review at ecda31d reports 12 invented-data probes and six passing submitted disclosure cases, not a full suite or hosted/browser validation. Its CF-01 newly eligible helper, CF-02 duplicate-row and CF-03/04 review-binding findings overlap CFT-02 through CFT-05 here and must not be counted twice. CFT-01 adds the candidate-file selection/preflight trace. Prior reports, reproduction programs and decks are retained. Author README claims about private/practice results were not independently verified; rehearsal, precomputed outputs, raw data, grading code and answer-bearing documents were conservatively excluded.

This pass does not accept earlier agents' findings as established merely because they were reported. Any correction must identify the earlier claim and the new evidence explicitly.

## Detailed Criterion Review

# Judge review aid: cohort-firewall

Repository: https://github.com/NinadRao0707/cohort-firewall
Commit: `ab5084f7caaa57e68636e2cd3fde97b20a47bf69`
Track: 1
Reviewer: Professor Bear / Codex source review

**Not an official result. Source review does not establish runtime behavior.**

The submission combines a release-change Control Tower with a question-readiness engine, versioned policy, signed certificates and explicit human review. The source has useful default-deny paths and content-keyed baseline caching. Important boundaries remain incomplete: missing candidate files can disappear from the comparison before selective rerun, baseline-only sample membership can miss newly eligible existing samples, duplicate IDs are normalized away, and review verifies only part of the evidence document. The latter three areas have separately published narrow synthetic corroboration; this reviewer executed no submission code. The missing-candidate-file path is a new source-derived follow-through that still needs an end-to-end positive/negative control. This is a provisional Track 1 review, not an official score, frozen-submission attestation or security/clinical certification.

## Coverage and limitations

Collection: complete_with_exclusions; 99 text files; 39 excluded entries; recursive tree truncated: False.
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

- P1 · T1-1 · Missing candidate inputs can bypass analysis availability checks: Preflight each protected analysis&\#x27;s required inputs in A and B before dependency filtering. Represent omitted optional/unneeded modalities separately from missing required inputs. Preserve the not\_compared disclosure, but give an unavailable analysis Insufficient Evidence even if other compared bytes are unchanged. Do not require RNA for an analysis that does not read it.
- P1 · T1-1 · Duplicate identifiers disappear before detection: Validate uniqueness before deduplication and retain occurrence counts, positions and conflicts as evidence. Keep original records intact. If a normalized view is needed for continued diagnostics, label its policy and keep affected analyses unresolved until a person accepts a suitable resolution.
- P1 · T1-2 · Dependency routing considers baseline members but can miss new entrants: Declare eligibility/filter dependencies explicitly and evaluate the relevant candidate population, not only the baseline output IDs. Use the union of before/after potential members or conservatively rerun when an eligibility change cannot be proven irrelevant. Preserve precise reasons for genuinely unrelated changes.
- P1 · T1-3 · Question review records text without checking its signed spec hash: Resolve the original canonical spec from immutable storage, or validate the received canonical spec against the signed spec\_sha256 before saving a review. Bind dataset identity, policy and question together and present older reviews as historical when any bound input changes.
- P1 · T1-4 · Release review checks verdict binding but not the full evidence document: Review an immutable server-side result selected by certificate ID, or bind and verify the complete canonical document used for decisions, including findings, analysis evidence, affected\_by, repairs and release identity. Reject changed decision inputs before constructing the review. Keep the current signed-verdict restrictions and note requirements.
- P2 · T1-3 · Baseline cache identity includes current file-content hashes: Keep content-bound cache keys and explicit hash conventions. Record the selected-file scope and include required-input availability before judging compatibility. Treat a matching hash as byte identity, not confirmation that an analysis or baseline is scientifically suitable.
- P2 · T1-4 · Policy separates measurements from versioned rules and missing-check states: Retain the policy/measurement separation, version hash and explicit unavailable states. Keep malformed-input validation separate and test None/type mismatches rather than assuming the generic evaluator covers every shape. Preserve the parallel report&\#x27;s distinct malformed-input findings.
- P2 · T1-6 · Approval policy distinguishes unavailable results and explicit conditions: Preserve the decision matrix and original records. Bind the complete reviewed subject before applying those rules, and surface ledger-write errors distinctly from a successfully recorded decision. Keep the documented end-truncation limitation visible when presenting the hash-chained ledger.

## T1-1: Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support.

Status: **observed**

Exact profile, label and membership detection is implemented. Duplicate normalization and omitted required candidate inputs need attention. Targeted probes are not recall/false-positive estimates.

### Missing candidate inputs can bypass analysis availability checks

gap · P1 · Confidence: High for the file-selection and rerun control flow; the stated complete-entry outcome remains unexecuted and requires the named control.

run\_tower builds in\_b from files present in the candidate and loads baseline fingerprints only for that set. Files missing from B are listed as not\_compared, so the diff never receives the baseline-only file needed to emit file\_missing. evaluate\_analyses runs the baseline from its full path, but only tries B when a detected relevant change exists. An unchanged carried file plus an omitted required clinical file can therefore leave no relevant change, skip B&\#x27;s analysis and retain the Ready policy fallback when compared baseline hashes verify. A limitation lists the omitted file, but no independent per-analysis candidate-input gate precedes the not\_rerun branch. This is a source-derived full-path inference, not an executed Ready result.

[Source lines 24–37](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/run.py#L24-L37)

>     cache = Path\(\_\_file\_\_\).resolve\(\).parents\[2\] / &quot;outputs&quot; / &quot;cache&quot;
>     \# Compare the files the new release actually has. Envelope releases omit RNA by design, so a
>     \# baseline file the new release doesn&\#x27;t carry is listed as &quot;not compared&quot;, never as a finding.
>     in\_b = \{f for f in LAYOUT if \(b / f\).exists\(\) and \(include\_rna or not f.startswith\(&quot;rna\_&quot;\)\)}
>     not\_compared = sorted\(f for f in LAYOUT if \(a / f\).exists\(\) and f not in in\_b\)
>     rel\_a = load\_release\(a, &quot;frozen-A&quot; if path\_a is None else a.name, include\_rna=include\_rna,
>                          cache\_dir=cache, only=in\_b\)
>     t1 = time.time\(\)
>     rel\_b = load\_release\(b, release\_name\(b\), include\_rna=include\_rna\)
>     frozen = frozen\_checksums\(repo\)
>     unverified = sorted\(f for f, h in rel\_a.file\_hashes.items\(\) if frozen.get\(f\) \!= h\[&quot;file&quot;\]\)
>     changes = diff\_releases\(rel\_a, rel\_b\)
>     analyses = load\_reference\_analyses\(repo\)
>     runs = evaluate\_analyses\(analyses, a, b, changes\)

[Source lines 78–82](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/run.py#L78-L82)

>     doc\[&quot;baseline\_unverified\_files&quot;\] = unverified
>     doc\[&quot;not\_compared&quot;\] = not\_compared
>     if not\_compared:
>         doc\[&quot;limitations&quot;\].append\(f&quot;Not in this release, so not compared: \{&\#x27;, &\#x27;.join\(not\_compared\)}. &quot;
>                                   &quot;An analysis that needs one of these files cannot be rerun and says so.&quot;\)

[Source lines 93–122](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/analyses.py#L93-L122)

>     for an in analyses:
>         run = AnalysisRun\(an\)
>         try:
>             run.before = \_run\(an, path\_a\)
>         except Exception as e:  \# baseline must work, or nothing can be concluded
>             run.error = f&quot;baseline failed: \{type\(e\).\_\_name\_\_}: \{e}&quot;
>             runs.append\(run\)
>             continue
>         used = set\(run.before.get\(&quot;sample\_ids&quot;, \[\]\)\)
>         used\_types = \{s\[13:15\] for s in used}
>         relevant = \[\]
>         for c in changes:
>             if c.file not in an.inputs:
>                 continue
>             if c.type in \{&quot;coverage\_loss&quot;, &quot;count\_masks\_membership&quot;}:
>                 continue                  \# summarize other changes; reported, not counted twice
>             if c.type == &quot;label\_change&quot; and not any\(an.reads\_column\(col\) for col in c.detail.get\(&quot;columns&quot;, \[\]\)\):
>                 continue                  \# this analysis never reads the clinical fields that changed
>             if c.type in SAMPLELESS:
>                 relevant.append\(c\)
>             elif set\(c.samples\) &amp; used:
>                 relevant.append\(c\)
>             elif c.type in \{&quot;added&quot;, &quot;new\_duplicate&quot;} and any\(s\[13:15\] in used\_types for s in c.samples\[:1\]\):
>                 relevant.append\(c\)        \# a new sample of a type this analysis includes
>         run.changes = relevant
>         if not relevant:
>             run.reason = \(&quot;No change touches this analysis&\#x27;s input files &quot;
>                           f&quot;\(\{&\#x27;, &\#x27;.join\(an.inputs\)}\) for the \{len\(used\)} samples it uses.&quot;\)
>             runs.append\(run\)
>             continue

[Source lines 227–236](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/diff.py#L227-L236)

> def diff\_releases\(a: Release, b: Release\) -&gt; list\[Change\]:
>     changes = \[\]
>     for fname in sorted\(set\(a.files\) &\#124; set\(b.files\)\):
>         if fname not in b.files:
>             changes.append\(Change\(&quot;file\_missing&quot;, fname, \[\], \{&quot;missing\_in&quot;: b.name}\)\)
>         elif fname not in a.files:
>             changes.append\(Change\(&quot;file\_added&quot;, fname, \[\], \{&quot;missing\_in&quot;: a.name}\)\)
>         else:
>             changes.extend\(diff\_file\(a.files\[fname\], b.files\[fname\]\)\)
>     return changes + unlinked\_changes\(a, b\) + coverage\_changes\(a, b\)

[Source lines 67–77](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/findings.py#L67-L77)

> def verdicts\(runs: list\[AnalysisRun\], baseline\_unverified: list\[str\]\) -&gt; dict\[str, dict\]:
>     policy = Policy.load\(TOWER\_POLICY\)
>     out = \{}
>     for run in runs:
>         results = \[
>             CheckResult\(&quot;provenance&quot;, &quot;ok&quot;, \{&quot;baseline\_verified&quot;: not baseline\_unverified,
>                                              &quot;unverified\_files&quot;: baseline\_unverified}\),
>             CheckResult\(&quot;impact&quot;, &quot;ok&quot;, \_metrics\(run\)\),
>         \]
>         ev = evaluate\(results, policy, expected=\{&quot;provenance&quot;, &quot;impact&quot;}\)
>         out\[run.analysis.id\] = ev

[Source lines 9–21](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/rules/tower_v0_1.yaml#L9-L21)

>   - id: TWR-PROV-1
>     check: provenance
>     when: \[\{metric: baseline\_verified, op: &quot;==&quot;, value: false}\]
>     verdict: INSUFFICIENT\_EVIDENCE
>     reason: &quot;The baseline release does not match the event&\#x27;s frozen checksums \(\{unverified\_files}\), so changes cannot be attributed to the new release.&quot;
>     remedy: &quot;Re-run fetch.py so the baseline matches sources.csv, then compare again.&quot;
> 
>   - id: TWR-RUN-1
>     check: impact
>     when: \[\{metric: run\_failed, op: &quot;==&quot;, value: true}\]
>     verdict: INSUFFICIENT\_EVIDENCE
>     reason: &quot;The analysis could not be run \(\{error}\).&quot;
>     remedy: &quot;Fix the input files or the analysis, then rerun the comparison.&quot;

Supplemental rules: None cited; official criterion above applies.

Impact: The intentional handling of optional omitted RNA should not imply that every candidate file is optional for every analysis. No relevant detected change and inability to compute the protected analysis are different states. A researcher can receive an unaffected explanation for an analysis whose required candidate input was never established as available.

Concrete change: Preflight each protected analysis&\#x27;s required inputs in A and B before dependency filtering. Represent omitted optional/unneeded modalities separately from missing required inputs. Preserve the not\_compared disclosure, but give an unavailable analysis Insufficient Evidence even if other compared bytes are unchanged. Do not require RNA for an analysis that does not read it.

Acceptance check: With invented complete A and matching public-style expected hashes, compare B containing unchanged protein but no clinical file; verify A1/A2 cannot be labelled unqualified Ready or unaffected. Use valid unchanged A/B as a positive control and omitted RNA with A1/A2 as an optional-modality control. Record the complete run\_tower result rather than only diff\_releases.

### Duplicate identifiers disappear before detection

gap · P1 · Confidence: High for source and the separately reported clinical fixture; no duplicate-header or end-to-end engine run was performed by this reviewer.

The row loader drops duplicate index values with keep=first before creating the sample list and fingerprints. Numeric and text matrix loaders similarly select the first occurrence of each header ID without retaining duplicate diagnostics. diff\_file then compares sets and fingerprints from those normalized views. A parallel invented clinical-row probe reported three input rows reduced to two loaded rows and an empty change list even though the file hash changed. That corroborates the clinical loader/diff case; duplicate matrix headers remain a separate proposed check rather than an executed result here.

[Source lines 100–110](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/releases.py#L100-L110)

> def \_load\_rows\(p: Path, fname: str, idcol: str\) -&gt; FileView:
>     df = pd.read\_csv\(p, sep=&quot;\\t&quot;, dtype=str, keep\_default\_na=False\)
>     if idcol not in df.columns:
>         idcol = df.columns\[0\]
>     df = df.set\_index\(idcol\)
>     df = df\[~df.index.duplicated\(keep=&quot;first&quot;\)\]
>     v = FileView\(fname, p, &quot;rows&quot;, list\(df.columns\), list\(df.index\), \_rows=df, idcol=idcol\)
>     for sid, row in zip\(df.index, df.itertuples\(index=False, name=None\)\):
>         v.fingerprints\[sid\] = \_fp\(row\)
>         if all\(x.strip\(\) in MISSING for x in row\):
>             v.empty.add\(sid\)

[Source lines 119–137](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/releases.py#L119-L137)

>     with \_open\_text\(p\) as f:
>         header = f.readline\(\).rstrip\(&quot;\\n&quot;\).split\(&quot;\\t&quot;\)
>     cols = header\[1:\]
>     first: dict\[str, int\] = \{}
>     for i, c in enumerate\(cols\):
>         first.setdefault\(c, i\)
>     keep = sorted\(first.values\(\)\)
>     df = pd.read\_csv\(p, sep=&quot;\\t&quot;, header=None, skiprows=1, usecols=\[0\] + \[i + 1 for i in keep\],
>                      index\_col=0, dtype=\{0: str}, engine=&quot;c&quot;\)
>     arr = df.to\_numpy\(\)
>     if arr.dtype.kind not in &quot;fiub&quot;:
>         raise ValueError\(&quot;non-numeric values&quot;\)
>     arr = np.ascontiguousarray\(arr.astype\(np.float64\).T\) + 0.0      \# +0.0 turns -0.0 into 0.0
>     samples = \[cols\[i\] for i in keep\]
>     v = FileView\(fname, p, &quot;columns&quot;, \[str\(x\) for x in df.index\], samples\)
>     empty = np.isnan\(arr\).all\(axis=1\)
>     for j, s\_id in enumerate\(samples\):
>         v.fingerprints\[s\_id\] = hashlib.blake2b\(arr\[j\].tobytes\(\), digest\_size=16\).hexdigest\(\)
>         if empty\[j\]:

[Source lines 149–174](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/releases.py#L149-L174)

> def \_load\_matrix\(p: Path, fname: str\) -&gt; FileView:
>     with \_open\_text\(p\) as f:
>         header = f.readline\(\).rstrip\(&quot;\\n&quot;\).split\(&quot;\\t&quot;\)
>         cols = header\[1:\]
>         first = \{}
>         for i, c in enumerate\(cols\):
>             first.setdefault\(c, i\)
>         keep = sorted\(first.values\(\)\)
>         hashers = \[hashlib.sha256\(\) for \_ in keep\]
>         nonmissing = \[False\] \* len\(keep\)
>         features = \[\]
>         for line in f:
>             parts = line.rstrip\(&quot;\\n&quot;\).split\(&quot;\\t&quot;\)
>             features.append\(parts\[0\]\)
>             vals = parts\[1:\]
>             for j, i in enumerate\(keep\):
>                 x = vals\[i\] if i &lt; len\(vals\) else &quot;&quot;
>                 hashers\[j\].update\(\(x + SEP\).encode\(\)\)
>                 if not nonmissing\[j\] and x.strip\(\) not in MISSING:
>                     nonmissing\[j\] = True
>     samples = \[cols\[i\] for i in keep\]
>     v = FileView\(fname, p, &quot;columns&quot;, features, samples\)
>     for j, s in enumerate\(samples\):
>         v.fingerprints\[s\] = hashers\[j\].hexdigest\(\)\[:20\]
>         if not nonmissing\[j\]:
>             v.empty.add\(s\)

[Source lines 77–90](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/diff.py#L77-L90)

>     else:
>         common = a.features
>         fa, fb = a.fingerprints, b.fingerprints
>         get\_a, get\_b = a.values, b.values
>         empty\_a, empty\_b = a.empty, b.empty
> 
>     inv\_a = defaultdict\(set\)
>     for s, h in fa.items\(\):
>         if s not in empty\_a:
>             inv\_a\[h\].add\(s\)
> 
>     A, B = set\(fa\), set\(fb\)
>     changed = sorted\(s for s in A &amp; B if fa\[s\] \!= fb\[s\]\)
>     vals\_a, vals\_b = get\_a\(changed\), get\_b\(changed\)

Supplemental rules: None cited; official criterion above applies.

Impact: Identity ambiguity is removed from the representation the detector inspects. The file hash still identifies changed bytes, so the issue is not a cryptographic hash failure. The missing evidence is a first-class duplicate-ID finding and an explicit policy for which conflicting record, if any, an analysis may use.

Concrete change: Validate uniqueness before deduplication and retain occurrence counts, positions and conflicts as evidence. Keep original records intact. If a normalized view is needed for continued diagnostics, label its policy and keep affected analyses unresolved until a person accepts a suitable resolution.

Acceptance check: Append both identical and conflicting repeated clinical IDs with the first record unchanged. Then repeat a matrix sample header, varying the second profile. Require explicit identity diagnostics and separate analysis status. Include unique-ID unchanged inputs as a quiet control.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-2: Reasoning for the research question. Changes its result appropriately when the research question or intended use changes.

Status: **observed**

Reference-analysis parameters and declared field inspection drive dependency routing; question-readiness specs are separate. Newly eligible existing samples are a concrete impact-map gap, with generic helper corroboration but no event-analysis run by this reviewer.

### Dependency routing considers baseline members but can miss new entrants

gap · P1 · Confidence: High for inspected routing and separately reported generic helper reproduction; protected-analysis prevalence and full application behavior are not established.

evaluate\_analyses takes used from the baseline result&\#x27;s sample\_ids and generally requires changed IDs to intersect that set. Only added/new\_duplicate changes receive a separate sample-type route. A label change on an existing previously excluded row can alter eligibility without intersecting baseline used, so the candidate result is not run. The separately published invented group-count probe reports baseline n=1, actual changed n=2, but affected=false/not\_rerun/after=null. That probe exercises a reviewer-authored analysis, not the actual event A1/A2 functions; this source review traced the generic gate and the corresponding eligibility risk without running it.

[Source lines 101–122](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/analyses.py#L101-L122)

>         used = set\(run.before.get\(&quot;sample\_ids&quot;, \[\]\)\)
>         used\_types = \{s\[13:15\] for s in used}
>         relevant = \[\]
>         for c in changes:
>             if c.file not in an.inputs:
>                 continue
>             if c.type in \{&quot;coverage\_loss&quot;, &quot;count\_masks\_membership&quot;}:
>                 continue                  \# summarize other changes; reported, not counted twice
>             if c.type == &quot;label\_change&quot; and not any\(an.reads\_column\(col\) for col in c.detail.get\(&quot;columns&quot;, \[\]\)\):
>                 continue                  \# this analysis never reads the clinical fields that changed
>             if c.type in SAMPLELESS:
>                 relevant.append\(c\)
>             elif set\(c.samples\) &amp; used:
>                 relevant.append\(c\)
>             elif c.type in \{&quot;added&quot;, &quot;new\_duplicate&quot;} and any\(s\[13:15\] in used\_types for s in c.samples\[:1\]\):
>                 relevant.append\(c\)        \# a new sample of a type this analysis includes
>         run.changes = relevant
>         if not relevant:
>             run.reason = \(&quot;No change touches this analysis&\#x27;s input files &quot;
>                           f&quot;\(\{&\#x27;, &\#x27;.join\(an.inputs\)}\) for the \{len\(used\)} samples it uses.&quot;\)
>             runs.append\(run\)
>             continue

[Source lines 123–133](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/analyses.py#L123-L133)

>         run.affected = True
>         try:
>             run.after = \_run\(an, path\_b\)
>             same = \_comparable\(run.before\) == \_comparable\(run.after\) and \\
>                 set\(run.before.get\(&quot;sample\_ids&quot;, \[\]\)\) == set\(run.after.get\(&quot;sample\_ids&quot;, \[\]\)\)
>             run.status = &quot;unchanged&quot; if same else &quot;changed&quot;
>             run.reason = f&quot;Rerun because \{len\(relevant\)} detected change\(s\) touch its inputs and samples.&quot;
>         except Exception as e:
>             run.error = f&quot;rerun failed: \{type\(e\).\_\_name\_\_}: \{e}&quot;
>             run.reason = &quot;Affected, but the rerun failed.&quot;
>         runs.append\(run\)

[Source lines 38–44](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/analyses.py#L38-L44)

>     def reads\_column\(self, column: str\) -&gt; bool:
>         return not self.source or f&\#x27;&quot;\{column}&quot;&\#x27; in self.source or f&quot;&\#x27;\{column}&\#x27;&quot; in self.source \\
>             or f&quot;.\{column}&quot; in self.source
> 
>     @property
>     def inputs\(self\) -&gt; list\[str\]:
>         return \[PARAM\_FILES\[p\]\[0\] for p in self.params\]

Supplemental rules: None cited; official criterion above applies.

Impact: A correct impact map must account for records that leave or enter the question&\#x27;s cohort. Checking only previous output membership proves neither candidate membership stability nor that an eligibility-field change is irrelevant. This goes to the Control Tower&\#x27;s central affected-versus-unaffected requirement.

Concrete change: Declare eligibility/filter dependencies explicitly and evaluate the relevant candidate population, not only the baseline output IDs. Use the union of before/after potential members or conservatively rerun when an eligibility change cannot be proven irrelevant. Preserve precise reasons for genuinely unrelated changes.

Acceptance check: Start with an existing primary sample excluded for an unknown label, then give it an allowed ER/PAM50 label in B. Demonstrate affected analysis, updated membership and linked evidence; retain an unrelated-field negative control and a still-ineligible label-change case. Verify actual protected analyses in a separately authorized test, not just a generic counting function.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-3: Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion.

Status: **observed**

Versioned policies, explicit file/content hash conventions and structured findings are strong foundations. Full result/question binding and duplicate evidence preservation remain necessary. No hash or signature establishes scientific correctness.

### Question review records text without checking its signed spec hash

gap · P1 · Confidence: High for the missing verification and separately reported changed-text helper fixture; no browser flow or broader mutation matrix was executed.

The engine signs qs.canonical\_json through spec\_sha256. review\_question verifies the certificate and reads verdict/rule IDs from that signed payload, but records question\_text from the supplied result.spec without recomputing its canonical hash. The API accepts that client result. The parallel direct-function probe reports an accepted signed review with a changed question string while the certificate remained from the original question. It does not establish that every field or every UI interaction is similarly accepted, and it does not forge a certificate.

[Source lines 70–72](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/engine.py#L70-L72)

>     cert = issue\(dataset\_bytes=dataset\_bytes, dictionary=dictionary, spec\_json=qs.canonical\_json\(\),
>                  policy\_version=policy.version, policy\_sha256=policy.sha256,
>                  verdict=ev\[&quot;verdict&quot;\], rule\_ids=\[f\[&quot;rule\_id&quot;\] for f in ev\[&quot;findings&quot;\]\]\)

[Source lines 50–63](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/certificate.py#L50-L63)

> def issue\(\*, dataset\_bytes: bytes, dictionary: dict &\#124; None, spec\_json: str,
>           policy\_version: str, policy\_sha256: str, verdict: str, rule\_ids: list\[str\]\) -&gt; dict:
>     payload = \{
>         &quot;cert\_format&quot;: &quot;cohort-firewall/1&quot;,
>         &quot;engine\_version&quot;: ENGINE\_VERSION,
>         &quot;policy\_version&quot;: policy\_version,
>         &quot;policy\_sha256&quot;: policy\_sha256,
>         &quot;dataset\_sha256&quot;: sha256\_bytes\(dataset\_bytes\),
>         &quot;dictionary\_sha256&quot;: sha256\_bytes\(canonical\(dictionary\)\) if dictionary else None,
>         &quot;spec\_sha256&quot;: sha256\_bytes\(spec\_json.encode\(\)\),
>         &quot;verdict&quot;: verdict,
>         &quot;rule\_ids&quot;: sorted\(set\(rule\_ids\)\),
>         &quot;issued\_at&quot;: datetime.now\(timezone.utc\).isoformat\(timespec=&quot;seconds&quot;\),
>     }

[Source lines 69–90](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/review.py#L69-L90)

> def review\_question\(result: dict, reviewer: str, role: str, decision: str,
>                     acknowledged: list\[str\], note: str\) -&gt; dict:
>     c = result.get\(&quot;certificate&quot;\) or \{}
>     if not cert.verify\(c\):
>         raise ReviewError\(&quot;The result&\#x27;s certificate does not verify; it may have been edited.&quot;\)
>     if not reviewer.strip\(\):
>         raise ReviewError\(&quot;Enter the reviewer&\#x27;s name.&quot;\)
>     verdict = c\[&quot;payload&quot;\]\[&quot;verdict&quot;\]
>     required = set\(c\[&quot;payload&quot;\].get\(&quot;rule\_ids&quot;, \[\]\)\)
>     \_check\_one\(verdict, decision, required, set\(acknowledged\), note, &quot;This result&quot;\)
>     payload = \{
>         &quot;review\_id&quot;: uuid.uuid4\(\).hex\[:12\], &quot;type&quot;: &quot;question&quot;,
>         &quot;subject&quot;: \{&quot;cert\_id&quot;: c\[&quot;cert\_id&quot;\], &quot;verdict&quot;: verdict,
>                     &quot;question&quot;: \(result.get\(&quot;spec&quot;\) or \{}\).get\(&quot;question\_text&quot;\),
>                     &quot;dataset\_sha256&quot;: c\[&quot;payload&quot;\]\[&quot;dataset\_sha256&quot;\],
>                     &quot;policy\_version&quot;: c\[&quot;payload&quot;\]\[&quot;policy\_version&quot;\]},
>         &quot;reviewer&quot;: \{&quot;name&quot;: reviewer.strip\(\)\[:80\], &quot;role&quot;: role.strip\(\)\[:80\]},
>         &quot;decision&quot;: decision, &quot;acknowledged\_findings&quot;: sorted\(set\(acknowledged\) &amp; required\),
>         &quot;note&quot;: note.strip\(\)\[:2000\],
>         &quot;created\_at&quot;: datetime.now\(timezone.utc\).isoformat\(timespec=&quot;seconds&quot;\),
>     }
>     return \_save\(\_sign\(payload\)\)

[Source lines 281–299](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/api/main.py#L281-L299)

> class QuestionReview\(BaseModel\):
>     result: dict
>     reviewer: str
>     role: str = &quot;&quot;
>     decision: str
>     acknowledged: list\[str\] = \[\]
>     note: str = &quot;&quot;
> 
> 
> @app.post\(&quot;/review/question&quot;\)
> def post\_question\_review\(req: QuestionReview\):
>     try:
>         rec = review\_question\(req.result, req.reviewer, req.role, req.decision, req.acknowledged, req.note\)
>         r = rec\[&quot;review&quot;\]
>         rec\[&quot;ledger&quot;\] = ledger.append\(&quot;review&quot;, \{&quot;review\_id&quot;: r\[&quot;review\_id&quot;\], &quot;cert\_id&quot;: r\[&quot;subject&quot;\]\[&quot;cert\_id&quot;\],
>                                                  &quot;decision&quot;: r\[&quot;decision&quot;\], &quot;reviewer&quot;: r\[&quot;reviewer&quot;\]\[&quot;name&quot;\]}\)
>         return rec
>     except ReviewError as e:
>         raise HTTPException\(400, str\(e\)\)

Supplemental rules: None cited; official criterion above applies.

Impact: A valid signature can be associated with review prose describing a different research question from the one actually evaluated. The official task depends on intended use and cohort definition, so those inputs must remain the subject of the review rather than editable adjacent context.

Concrete change: Resolve the original canonical spec from immutable storage, or validate the received canonical spec against the signed spec\_sha256 before saving a review. Bind dataset identity, policy and question together and present older reviews as historical when any bound input changes.

Acceptance check: After certification, change question\_text, intended use, filters and predictor lists independently. Require rejection or a new evaluation before review. Reordered equivalent JSON keys should remain valid under canonical serialization, and the untouched signed spec should still be reviewable.

### Baseline cache identity includes current file-content hashes

strength · P2 · Confidence: High for complete cache-key and hash code; no cache read/write or dataset load occurred in this review.

The release cache key combines a cache-version token with file\_sha256 for every selected present file. A same-path content change therefore selects a different cache entry rather than reusing a path-only result. The loader also records both compressed-file and decompressed-content hashes, and the run checks compared baseline file hashes against the frozen checksum map. The verification scope is the selected compared-file set, not a proof of all required candidate inputs or of scientific truth.

[Source lines 181–201](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/releases.py#L181-L201)

> def load\_release\(path: str &\#124; Path, name: str &\#124; None = None, include\_rna: bool = True,
>                  cache\_dir: Path &\#124; None = None, only: set\[str\] &\#124; None = None\) -&gt; Release:
>     &quot;&quot;&quot;Load and fingerprint a release. With cache\_dir, a release whose files are byte-identical
>     to a previous load \(same sha256 per file\) is read from the cache instead of re-fingerprinted.&quot;&quot;&quot;
>     import pickle
>     path = Path\(path\)
>     if cache\_dir is not None:
>         present = \[f for f in LAYOUT if \(path / f\).exists\(\) and \(include\_rna or not f.startswith\(&quot;rna\_&quot;\)\)
>                    and \(only is None or f in only\)\]
>         key = hashlib.sha256\(&quot;&\#124;&quot;.join\(\[CACHE\_VERSION\] + \[f&quot;\{f}:\{file\_sha256\(path / f\)}&quot; for f in present\]\)
>                              .encode\(\)\).hexdigest\(\)\[:24\]
>         cached = Path\(cache\_dir\) / f&quot;release-\{key}.pkl&quot;
>         if cached.exists\(\):
>             rel = pickle.loads\(cached.read\_bytes\(\)\)
>             rel.name, rel.path = name or path.name, path
>             for v in rel.files.values\(\):
>                 v.path = path / v.name
>             return rel
>         rel = load\_release\(path, name, include\_rna, only=only\)
>         Path\(cache\_dir\).mkdir\(parents=True, exist\_ok=True\)
>         cached.write\_bytes\(pickle.dumps\(rel\)\)

[Source lines 208–219](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/releases.py#L208-L219)

>     def work\(job\):
>         fname, orient, idcol = job
>         p = path / fname
>         view = \_load\_rows\(p, fname, idcol\) if orient == &quot;rows&quot; else \_load\_any\_matrix\(p, fname\)
>         return fname, \{&quot;file&quot;: file\_sha256\(p\), &quot;content&quot;: content\_sha256\(p\)}, view
> 
>     \# Files are read in parallel: decompression and pandas&\#x27; parser release the GIL for most of the work.
>     with ThreadPoolExecutor\(max\_workers=max\(1, min\(6, len\(jobs\)\)\)\) as pool:
>         results = list\(pool.map\(work, jobs\)\)
>     files = \{f: v for f, \_, v in results}
>     hashes = \{f: h for f, h, \_ in results}
>     return Release\(name or path.name, path, files, hashes\)

[Source lines 27–35](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/run.py#L27-L35)

>     in\_b = \{f for f in LAYOUT if \(b / f\).exists\(\) and \(include\_rna or not f.startswith\(&quot;rna\_&quot;\)\)}
>     not\_compared = sorted\(f for f in LAYOUT if \(a / f\).exists\(\) and f not in in\_b\)
>     rel\_a = load\_release\(a, &quot;frozen-A&quot; if path\_a is None else a.name, include\_rna=include\_rna,
>                          cache\_dir=cache, only=in\_b\)
>     t1 = time.time\(\)
>     rel\_b = load\_release\(b, release\_name\(b\), include\_rna=include\_rna\)
>     frozen = frozen\_checksums\(repo\)
>     unverified = sorted\(f for f, h in rel\_a.file\_hashes.items\(\) if frozen.get\(f\) \!= h\[&quot;file&quot;\]\)
>     changes = diff\_releases\(rel\_a, rel\_b\)

[Source lines 264–268](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/findings.py#L264-L268)

>         &quot;data&quot;: \{&quot;dataset&quot;: &quot;TCGA-BRCA&quot;, &quot;releases&quot;: \[
>             \{&quot;name&quot;: rel\_a.name, &quot;files&quot;: \[\{&quot;file&quot;: f, &quot;sha256&quot;: h\[&quot;file&quot;\], &quot;hash\_of&quot;: &quot;file&quot;}
>                                            for f, h in sorted\(rel\_a.file\_hashes.items\(\)\)\]},
>             \{&quot;name&quot;: rel\_b.name, &quot;files&quot;: \[\{&quot;file&quot;: f, &quot;sha256&quot;: h\[&quot;content&quot;\], &quot;hash\_of&quot;: &quot;content&quot;}
>                                            for f, h in sorted\(rel\_b.file\_hashes.items\(\)\)\]},

Supplemental rules: None cited; official criterion above applies.

Impact: This is a useful provenance control and a direct contrast to path-only caches. It helps make cache reuse reproducible and explains why a data hash must be interpreted with its hash\_of convention. CFT-01 still needs an independent availability gate.

Concrete change: Keep content-bound cache keys and explicit hash conventions. Record the selected-file scope and include required-input availability before judging compatibility. Treat a matching hash as byte identity, not confirmation that an analysis or baseline is scientifically suitable.

Acceptance check: With invented inputs, reuse an unchanged release, replace a file at the same path, and change only compression metadata. Confirm cache and provenance behavior match the declared file/content conventions. Verify omitted required files are still handled by CFT-01&\#x27;s separate gate.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-4: Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review.

Status: **observed**

Default-deny and signed-verdict decision rules are constructive. Partial review-subject binding can undermine acknowledgments; the separate main report also records malformed-input and optional-wording concerns not rerun here.

### Release review checks verdict binding but not the full evidence document

gap · P1 · Confidence: High for the partial binding and separately reported direct-function reproduction; no application request or key material was accessed.

tower\_binding contains the question and analysis IDs/verdicts only. Certificate creation uses that binding, while review\_release derives required acknowledgments from client-supplied findings and affected\_by arrays that are not covered by it. The API passes the supplied findings document directly to the review function. The parallel synthetic probe reports that original Conditional evidence required F1 acknowledgment, but stripping findings/affected\_by while retaining the valid certificate allowed a signed approve\_with\_conditions record with no acknowledgments. The Blocked-verdict guard still rejected approval; no private key was forged and no HTTP/browser exploit was reproduced.

[Source lines 35–39](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/review.py#L35-L39)

> def tower\_binding\(question: str, analyses: list\[dict\]\) -&gt; str:
>     &quot;&quot;&quot;What a Control Tower certificate&\#x27;s spec hash covers: the question and each analysis verdict.&quot;&quot;&quot;
>     return json.dumps\(\{&quot;question&quot;: question,
>                        &quot;analyses&quot;: \[\{&quot;id&quot;: a\[&quot;id&quot;\], &quot;verdict&quot;: a\[&quot;verdict&quot;\]} for a in analyses\]},
>                       sort\_keys=True, separators=\(&quot;,&quot;, &quot;:&quot;\)\)

[Source lines 93–112](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/review.py#L93-L112)

> def review\_release\(doc: dict, reviewer: str, role: str, decisions: dict\[str, str\],
>                    acknowledged: list\[str\], note: str\) -&gt; dict:
>     c = doc.get\(&quot;certificate&quot;\) or \{}
>     if not cert.verify\(c\):
>         raise ReviewError\(&quot;The findings&\#x27; certificate does not verify; it may have been edited.&quot;\)
>     analyses = doc.get\(&quot;analyses&quot;\) or \[\]
>     bound = hashlib.sha256\(tower\_binding\(doc.get\(&quot;question&quot;, &quot;&quot;\), analyses\).encode\(\)\).hexdigest\(\)
>     if bound \!= c\[&quot;payload&quot;\]\[&quot;spec\_sha256&quot;\]:
>         raise ReviewError\(&quot;The analysis verdicts do not match the signed record; they may have been edited.&quot;\)
>     if not reviewer.strip\(\):
>         raise ReviewError\(&quot;Enter the reviewer&\#x27;s name.&quot;\)
>     finding\_ids = \{f\[&quot;id&quot;\] for f in doc.get\(&quot;findings&quot;, \[\]\)}
>     per = \[\]
>     for a in analyses:
>         d = decisions.get\(a\[&quot;id&quot;\]\)
>         if not d:
>             raise ReviewError\(f&quot;Choose a decision for \{a\[&\#x27;id&\#x27;\]}.&quot;\)
>         required = set\(a.get\(&quot;affected\_by&quot;, \[\]\)\) &amp; finding\_ids
>         \_check\_one\(LABEL\[a\[&quot;verdict&quot;\]\], d, required, set\(acknowledged\), note, a\[&quot;id&quot;\]\)
>         per.append\(\{&quot;analysis&quot;: a\[&quot;id&quot;\], &quot;verdict&quot;: a\[&quot;verdict&quot;\], &quot;decision&quot;: d}\)

[Source lines 285–291](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/findings.py#L285-L291)

>     hashes = json.dumps\(doc\[&quot;data&quot;\], sort\_keys=True\).encode\(\)
>     from ..review import tower\_binding
>     doc\[&quot;certificate&quot;\] = issue\(dataset\_bytes=hashes, dictionary=None,
>                                spec\_json=tower\_binding\(question, analyses\),
>                                policy\_version=Policy.load\(TOWER\_POLICY\).version,
>                                policy\_sha256=Policy.load\(TOWER\_POLICY\).sha256, verdict=overall,
>                                rule\_ids=\[f\[&quot;rule\_id&quot;\] for e in vds.values\(\) for f in e\[&quot;findings&quot;\]\]\)

[Source lines 302–321](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/api/main.py#L302-L321)

> class ReleaseReview\(BaseModel\):
>     findings: dict
>     reviewer: str
>     role: str = &quot;&quot;
>     decisions: dict\[str, str\]
>     acknowledged: list\[str\] = \[\]
>     note: str = &quot;&quot;
> 
> 
> @app.post\(&quot;/review/release&quot;\)
> def post\_release\_review\(req: ReleaseReview\):
>     try:
>         rec = review\_release\(req.findings, req.reviewer, req.role, req.decisions, req.acknowledged, req.note\)
>         r = rec\[&quot;review&quot;\]
>         rec\[&quot;ledger&quot;\] = ledger.append\(&quot;review&quot;, \{&quot;review\_id&quot;: r\[&quot;review\_id&quot;\], &quot;cert\_id&quot;: r\[&quot;subject&quot;\]\[&quot;cert\_id&quot;\],
>                                                  &quot;decision&quot;: \{d\[&quot;analysis&quot;\]: d\[&quot;decision&quot;\] for d in r\[&quot;decisions&quot;\]},
>                                                  &quot;reviewer&quot;: r\[&quot;reviewer&quot;\]\[&quot;name&quot;\]}\)
>         return rec
>     except ReviewError as e:
>         raise HTTPException\(400, str\(e\)\)

Supplemental rules: None cited; official criterion above applies.

Impact: Cryptographic validity establishes exactly what the payload covers, not authenticity of every adjacent field. An evidence-acknowledgment requirement can be reduced through unsigned portions of the submitted document while its verdict remains unchanged. A verified review signature can then describe an incomplete review.

Concrete change: Review an immutable server-side result selected by certificate ID, or bind and verify the complete canonical document used for decisions, including findings, analysis evidence, affected\_by, repairs and release identity. Reject changed decision inputs before constructing the review. Keep the current signed-verdict restrictions and note requirements.

Acceptance check: Change findings, affected\_by, before/after values, repairs and release metadata independently after issuing a certificate. Each changed review request should be rejected or clearly treated as a new unsigned result. The original Conditional result with all required acknowledgments and note is the positive control; Blocked approval must remain rejected.

### Policy separates measurements from versioned rules and missing-check states

strength · P2 · Confidence: High for inspected evaluator controls; no policy tests were run in this pass.

Policy loads YAML with safe\_load and records the rule-file hash. Evaluation produces explicit Insufficient Evidence for missing expected checks, not-evaluable checks and rule references to absent metrics. Conditions use a fixed operator mapping rather than eval. Accepted limitations apply only to allowed Conditional findings, and ignored acceptances remain visible. These paths are useful controls, not a guarantee that all input shapes or metric values are valid.

[Source lines 32–37](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/policy.py#L32-L37)

>     @classmethod
>     def load\(cls, path: str &\#124; Path\) -&gt; &quot;Policy&quot;:
>         raw = Path\(path\).read\_bytes\(\)
>         doc = yaml.safe\_load\(raw\)
>         return cls\(doc\[&quot;version&quot;\], doc.get\(&quot;parameters&quot;, \{}\), doc\[&quot;rules&quot;\],
>                    hashlib.sha256\(raw\).hexdigest\(\), doc.get\(&quot;acceptable&quot;, \{}\) or \{}\)

[Source lines 53–66](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/policy.py#L53-L66)

> def evaluate\(results: list\[CheckResult\], policy: Policy, expected: set\[str\] &\#124; None = None,
>              accepted: set\[str\] &\#124; None = None\) -&gt; dict:
>     by\_name = \{r.check: r for r in results}
>     findings = \[\]
>     expected = EXPECTED\_CHECKS if expected is None else expected
> 
>     for name in sorted\(expected - set\(by\_name\)\):
>         findings.append\(\{&quot;rule\_id&quot;: &quot;DEFAULT-DENY&quot;, &quot;check&quot;: name, &quot;verdict&quot;: &quot;INSUFFICIENT\_EVIDENCE&quot;,
>                          &quot;reason&quot;: f&quot;Check &\#x27;\{name}&\#x27; did not report.&quot;, &quot;remedy&quot;: &quot;Investigate the engine.&quot;}\)
>     for r in results:
>         if r.status == &quot;not\_evaluable&quot;:
>             findings.append\(\{&quot;rule\_id&quot;: &quot;DEFAULT-DENY&quot;, &quot;check&quot;: r.check, &quot;verdict&quot;: &quot;INSUFFICIENT\_EVIDENCE&quot;,
>                              &quot;reason&quot;: f&quot;Check &\#x27;\{r.check}&\#x27; could not be evaluated. \{r.note}&quot;.strip\(\),
>                              &quot;remedy&quot;: &quot;Supply the missing data or metadata this check needs.&quot;}\)

[Source lines 68–87](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/policy.py#L68-L87)

>     for rule in policy.rules:
>         r = by\_name.get\(rule\[&quot;check&quot;\]\)
>         if r is None or r.status \!= &quot;ok&quot;:
>             continue  \# already covered by DEFAULT-DENY or skipped \(not applicable\)
>         fired, broken = True, False
>         for cond in rule\[&quot;when&quot;\]:
>             if cond\[&quot;metric&quot;\] not in r.metrics:
>                 broken = True
>                 break
>             v = r.metrics\[cond\[&quot;metric&quot;\]\]
>             if v is None:
>                 fired = False
>                 break
>             if not OPS\[cond\[&quot;op&quot;\]\]\(v, cond\[&quot;value&quot;\]\):
>                 fired = False
>                 break
>         if broken:
>             findings.append\(\{&quot;rule\_id&quot;: rule\[&quot;id&quot;\], &quot;check&quot;: rule\[&quot;check&quot;\], &quot;verdict&quot;: &quot;INSUFFICIENT\_EVIDENCE&quot;,
>                              &quot;reason&quot;: f&quot;Rule \{rule\[&\#x27;id&\#x27;\]} references a metric the check did not produce.&quot;,
>                              &quot;remedy&quot;: &quot;Fix the rule/engine mismatch.&quot;}\)

[Source lines 99–114](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/policy.py#L99-L114)

>     accepted = set\(accepted or set\(\)\)
>     allowed = set\(\(policy.acceptable or \{}\).keys\(\)\)
>     ignored\_acceptances = sorted\(accepted - allowed\)
>     for f in findings:
>         if f\[&quot;rule\_id&quot;\] in accepted and f\[&quot;rule\_id&quot;\] in allowed and f\[&quot;verdict&quot;\] == &quot;CONDITIONAL&quot;:
>             f\[&quot;accepted&quot;\] = True
>             f\[&quot;accepted\_as&quot;\] = policy.acceptable\[f\[&quot;rule\_id&quot;\]\]
> 
>     verdict = &quot;READY&quot;
>     counted = \[f for f in findings if not f.get\(&quot;accepted&quot;\)\]
>     for v in PRECEDENCE:
>         if any\(f\[&quot;verdict&quot;\] == v for f in counted\):
>             verdict = v
>             break
>     findings.sort\(key=lambda f: \(PRECEDENCE.index\(f\[&quot;verdict&quot;\]\), bool\(f.get\(&quot;accepted&quot;\)\)\)\)
>     return \{&quot;verdict&quot;: verdict, &quot;findings&quot;: findings, &quot;ignored\_acceptances&quot;: ignored\_acceptances}

Supplemental rules: None cited; official criterion above applies.

Impact: A reviewer can inspect which measured condition triggered a verdict and distinguish unavailable evidence from an actual negative finding. Constraining accepted limitations prevents an ordinary acceptance list from waiving Blocked findings.

Concrete change: Retain the policy/measurement separation, version hash and explicit unavailable states. Keep malformed-input validation separate and test None/type mismatches rather than assuming the generic evaluator covers every shape. Preserve the parallel report&\#x27;s distinct malformed-input findings.

Acceptance check: Omit an expected check, return not\_evaluable, remove a referenced metric and submit an unrecognized acceptance. Verify each has a visible and distinct result. Confirm a permitted Conditional acceptance works while Blocked cannot be waived. Do not infer success from source definitions alone.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-5: Working tool and clear setup. Judges can run the core workflow from the submitted repository.

Status: **not_tested**

README documents API, CLI and web setup. This source reviewer executed none of them. The parallel report&\#x27;s 12 narrow synthetic probes and six disclosure cases are not a full submitted suite, build, browser or hosted validation.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T1-6: Useful next steps. Suggested fixes are specific and match the size and importance of the problem.

Status: **observed**

Repairs are proposals and approval policy distinguishes unresolved evidence. Verify complete evidence identity before trusting a signed decision or repair simulation, and preserve the researcher&\#x27;s judgment of source correctness.

### Approval policy distinguishes unavailable results and explicit conditions

strength · P2 · Confidence: High for source decision controls and separately reported narrow rejection control; authentication, multi-process persistence and full API behavior remain untested.

Allowed decisions depend on the signed verdict. Blocked and Insufficient Evidence allow reject/request\_more but no approval; Conditional allows approve\_with\_conditions. Approval requires the relevant acknowledgments and nontrivial notes under the inspected policy, and release review requires a decision for every supplied analysis. The published Blocked-approval synthetic control was rejected. These are meaningful safeguards even though CFT-04/05 show that surrounding document binding is incomplete. Reviewer names are self-attested strings, not authenticated identity.

[Source lines 19–27](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/review.py#L19-L27)

> LABEL = \{&quot;Ready&quot;: &quot;READY&quot;, &quot;Conditional&quot;: &quot;CONDITIONAL&quot;, &quot;Blocked&quot;: &quot;BLOCKED&quot;,
>          &quot;Insufficient Evidence&quot;: &quot;INSUFFICIENT\_EVIDENCE&quot;}
> ALLOWED = \{
>     &quot;READY&quot;: \{&quot;approve&quot;, &quot;reject&quot;, &quot;request\_more&quot;},
>     &quot;CONDITIONAL&quot;: \{&quot;approve\_with\_conditions&quot;, &quot;reject&quot;, &quot;request\_more&quot;},
>     &quot;BLOCKED&quot;: \{&quot;reject&quot;, &quot;request\_more&quot;},
>     &quot;INSUFFICIENT\_EVIDENCE&quot;: \{&quot;reject&quot;, &quot;request\_more&quot;},
> }
> APPROVALS = \{&quot;approve&quot;, &quot;approve\_with\_conditions&quot;}

[Source lines 42–51](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/review.py#L42-L51)

> def \_check\_one\(verdict: str, decision: str, required: set\[str\], acknowledged: set\[str\], note: str, who: str\):
>     if decision not in ALLOWED\[verdict\]:
>         raise ReviewError\(f&quot;&\#x27;\{decision}&\#x27; is not allowed for a \{verdict.replace\(&\#x27;\_&\#x27;, &\#x27; &\#x27;\).title\(\)} result. &quot;
>                           f&quot;Allowed: \{&\#x27;, &\#x27;.join\(sorted\(ALLOWED\[verdict\]\)\)}.&quot;\)
>     if decision in APPROVALS and not required &lt;= acknowledged:
>         missing = &quot;, &quot;.join\(sorted\(required - acknowledged\)\)
>         raise ReviewError\(f&quot;\{who}: approving requires confirming you reviewed the evidence for \{missing}.&quot;\)
>     if \(decision \!= &quot;approve&quot; or required\) and len\(note.strip\(\)\) &lt; 10:
>         raise ReviewError\(f&quot;\{who}: write a short note \(why the findings are acceptable, what conditions apply, &quot;
>                           &quot;or what evidence is needed\).&quot;\)

[Source lines 102–122](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/review.py#L102-L122)

>     if not reviewer.strip\(\):
>         raise ReviewError\(&quot;Enter the reviewer&\#x27;s name.&quot;\)
>     finding\_ids = \{f\[&quot;id&quot;\] for f in doc.get\(&quot;findings&quot;, \[\]\)}
>     per = \[\]
>     for a in analyses:
>         d = decisions.get\(a\[&quot;id&quot;\]\)
>         if not d:
>             raise ReviewError\(f&quot;Choose a decision for \{a\[&\#x27;id&\#x27;\]}.&quot;\)
>         required = set\(a.get\(&quot;affected\_by&quot;, \[\]\)\) &amp; finding\_ids
>         \_check\_one\(LABEL\[a\[&quot;verdict&quot;\]\], d, required, set\(acknowledged\), note, a\[&quot;id&quot;\]\)
>         per.append\(\{&quot;analysis&quot;: a\[&quot;id&quot;\], &quot;verdict&quot;: a\[&quot;verdict&quot;\], &quot;decision&quot;: d}\)
>     payload = \{
>         &quot;review\_id&quot;: uuid.uuid4\(\).hex\[:12\], &quot;type&quot;: &quot;release&quot;,
>         &quot;subject&quot;: \{&quot;cert\_id&quot;: c\[&quot;cert\_id&quot;\], &quot;overall\_verdict&quot;: c\[&quot;payload&quot;\]\[&quot;verdict&quot;\],
>                     &quot;releases&quot;: \[r\[&quot;name&quot;\] for r in doc\[&quot;data&quot;\]\[&quot;releases&quot;\]\],
>                     &quot;policy\_version&quot;: c\[&quot;payload&quot;\]\[&quot;policy\_version&quot;\]},
>         &quot;reviewer&quot;: \{&quot;name&quot;: reviewer.strip\(\)\[:80\], &quot;role&quot;: role.strip\(\)\[:80\]},
>         &quot;decisions&quot;: per, &quot;acknowledged\_findings&quot;: sorted\(set\(acknowledged\) &amp; finding\_ids\),
>         &quot;note&quot;: note.strip\(\)\[:2000\],
>         &quot;created\_at&quot;: datetime.now\(timezone.utc\).isoformat\(timespec=&quot;seconds&quot;\),
>     }

[Source lines 47–67](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/ledger.py#L47-L67)

> def append\(event: str, subject: dict\) -&gt; dict:
>     &quot;&quot;&quot;Add one entry and return \{seq, hash}. Never raises: the ledger must not break a check.&quot;&quot;&quot;
>     try:
>         with \_lock:
>             p = path\(\)
>             p.parent.mkdir\(parents=True, exist\_ok=True\)
>             last = None
>             if p.exists\(\):
>                 lines = \[x for x in p.read\_text\(\).splitlines\(\) if x.strip\(\)\]
>                 last = json.loads\(lines\[-1\]\) if lines else None
>             entry = \{&quot;seq&quot;: \(last\[&quot;seq&quot;\] + 1\) if last else 1,
>                      &quot;ts&quot;: datetime.now\(timezone.utc\).isoformat\(timespec=&quot;seconds&quot;\),
>                      &quot;event&quot;: event, &quot;subject&quot;: subject,
>                      &quot;prev&quot;: last\[&quot;hash&quot;\] if last else GENESIS}
>             entry\[&quot;hash&quot;\] = \_hash\(entry\)
>             entry\[&quot;sig&quot;\] = base64.b64encode\(cert.\_load\_key\(\).sign\(bytes.fromhex\(entry\[&quot;hash&quot;\]\)\)\).decode\(\)
>             with p.open\(&quot;a&quot;\) as f:
>                 f.write\(json.dumps\(entry, sort\_keys=True\) + &quot;\\n&quot;\)
>             return \{&quot;seq&quot;: entry\[&quot;seq&quot;\], &quot;hash&quot;: entry\[&quot;hash&quot;\]}
>     except Exception as e:  \# pragma: no cover
>         return \{&quot;error&quot;: f&quot;ledger not written: \{e}&quot;}

[Source lines 1–8](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/ledger.py#L1-L8)

> &quot;&quot;&quot;Tamper-evident audit ledger: a hash-chained, signed record of every check and every human decision.
> 
> Each entry holds its sequence number, time, event, a short subject \(certificate id, verdicts, reviewer\),
> the previous entry&\#x27;s hash, its own hash, and an Ed25519 signature of that hash. Editing, deleting,
> inserting or reordering any past entry breaks the chain, and verify\(\) names the first entry affected.
> 
> Limitation: removing entries from the END leaves a valid shorter chain. Record the head hash somewhere
> else \(the review note, a ticket, an email\) to detect that, as Certificate Transparency logs do.

Supplemental rules: None cited; official criterion above applies.

Impact: The review handoff makes unresolved evidence a separate action rather than equating any recorded interaction with approval. It gives the researcher concrete conditions and a signed record to retain after fixing the evidence-binding boundary.

Concrete change: Preserve the decision matrix and original records. Bind the complete reviewed subject before applying those rules, and surface ledger-write errors distinctly from a successfully recorded decision. Keep the documented end-truncation limitation visible when presenting the hash-chained ledger.

Acceptance check: Exercise each verdict/decision pair with missing versus complete acknowledgments and notes. Retain the rejected Blocked-approval control. Then verify the resulting review subject matches the immutable evidence and that a logging failure is visible without claiming a complete ledger.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-7: Communication. Someone without specialist knowledge can understand the result and next step.

Status: **not_tested**

Plain summaries, limitations and structured next steps are implemented. Omitted-file disclosures should agree with per-analysis availability; no user-comprehension or accessibility claim is established.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## Excluded scope

- .gitignore: non-allowlisted file type
- data/demo/breast\_cohort.csv: file-size limit
- data/demo/breast\_cohort.dictionary.json: sensitive, data, sealed, or dependency path
- data/flatten\_synthea.py: sensitive, data, sealed, or dependency path
- data/flatten\_tcga.py: sensitive, data, sealed, or dependency path
- data/make\_demo\_cohort.py: sensitive, data, sealed, or dependency path
- data/make\_variants.py: sensitive, data, sealed, or dependency path
- docs/HIDDEN\_TEST.md: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- docs/RESULTS.md: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- examples/outputs/findings-practice-B.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- rehearsal/README.md: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- rehearsal/rehearsal-C.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- rehearsal/rehearsal-D.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- rehearsal/rehearsal-E.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- scripts/grade\_tower.py: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/.env.local.example: sensitive, data, sealed, or dependency path
- web/next.config.mjs: non-allowlisted file type
- web/package-lock.json: sensitive or generated filename
- web/public/samples/clean.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/leakage.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/no\_dictionary.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/phi.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/prompt\_injection.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/q2\_clinical.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/q3\_survival.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/risk\_score\_question.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/skewed\_subgroup.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/synthea\_large\_q1\_progression\_2yr.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/synthea\_large\_q2\_survival\_5yr.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/synthea\_small\_q1\_progression\_2yr.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/synthea\_small\_q2\_survival\_5yr.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/tcga\_q1\_er\_protein\_vs\_clinical.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/tcga\_q1b\_er\_protein\_profiled\_only.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/tcga\_q2\_survival\_5yr.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/tcga\_q3\_pfi\_2yr\_by\_race.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/tcga\_q5\_all\_samples.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/tcga\_q6\_patient\_risk\_score.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/tcga\_q7\_pam50\_subtype\_mix.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- web/public/samples/tower\_practice-B.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact

## Judge Follow-Up Sequence

1. Verify the official final commit and product declaration.
2. Start with the highest-priority synthetic acceptance checks above.
3. Follow one finding through evidence, affected versus unaffected analyses, proposed repair and human decision.
4. Verify the exported artifact against the organizer contract without reading sealed answers.
5. Record actual results separately from this static audit; revise only claims the new evidence supports.
