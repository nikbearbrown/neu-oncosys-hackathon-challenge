# Professor Bear Audit: ReadySet Control Tower

## Supplement To Existing Parallel Review

Read the retained [existing report](REPORT.md) first. This pass independently corroborates its required-input and identical-invalid-input concerns (Issue 1) and timestamp-based file selection (Issue 5); these are not claimed as newly discovered issues. It adds criterion-level exact excerpts and explicit acceptance checks. The existing report also records another agent's isolated runtime and browser results. Those results were not rerun by this reviewer and remain separately attributed; this supplement's own checks are static only. No existing report, test record or deck was replaced.

## Review Identity

This is an independent, provisional source-code audit for judge deliberation. It is not an official grade.

- Entry: `a7ussein/readyset-control-tower`
- Commit: `4dd07736e99f96dd46cb6199c32bea32465bd20e`
- Organizer reference: `6e15a399a64ffbf80778db0b462ac239e70086b9`
- Product: `cohort-control-tower`; Track 1, Cohort Firewall
- Pass: 1; reviewed 2026-11-14T19:46:55.628262+00:00
- Runtime: **not executed**; official freeze/receipt: **not verified**

## Executive Assessment

A focused, standard-library comparison engine with unusually explicit evidence, question-specific impact mapping and per-finding counterfactual effects. The principal first-pass concern is that absence or unreadability shared by both releases can bypass the changed-file path and still lead to Ready. Input selection by modification time also weakens reproducibility. These are static source findings, not results of an executed demo.

## Workflow Traced

The selected analyses define the research question. The engine locates each expected file, hashes available contents, compares changed files, maps changes to files/fields/samples used by each analysis, reruns affected analyses, estimates each finding's isolated effect, and exports v0.2 findings with repairs, rules and witness values. The hosted site is a precomputed demonstration according to the README; it is not evidence that a newly supplied release was processed live.

## Findings At A Glance

| ID | Type | Priority | Finding |
|---|---|---|---|
| RS-01 | gap | P1 | Required files absent from both releases do not make the verdict insufficient |
| RS-02 | gap | P1 | Identical content is skipped before readability or analytical validity is established |
| RS-03 | gap | P2 | Ambiguous file variants are resolved by filesystem modification time |
| RS-04 | strength | P2 | Changes are mapped to the selected analysis before rerunning |
| RS-05 | strength | P2 | The export retains evidence rules and isolated per-finding effects |
| RS-06 | strength | P2 | Repair urgency is tied to both measured effect and uncertainty |

## Inspection Scope

The following files informed the implementation-level conclusions in this pass. Other collected files are not automatically treated as reviewed:

- `control_tower/compare.py`
- `control_tower/analyses.py`
- `control_tower/release.py`
- `tests/test_empty_inputs.py`
- `README.md`

## Parallel Review Preservation

No earlier Markdown reports existed in this matching entry folder at the time this pass was prepared.

This pass does not accept earlier agents' findings as established merely because they were reported. Any correction must identify the earlier claim and the new evidence explicitly.

## Detailed Criterion Review

# Judge review aid: readyset-control-tower

Repository: https://github.com/a7ussein/readyset-control-tower
Commit: `4dd07736e99f96dd46cb6199c32bea32465bd20e`
Track: 1
Reviewer: Professor Bear / Codex source review

**Not an official result. Source review does not establish runtime behavior.**

A focused, standard-library comparison engine with unusually explicit evidence, question-specific impact mapping and per-finding counterfactual effects. The principal first-pass concern is that absence or unreadability shared by both releases can bypass the changed-file path and still lead to Ready. Input selection by modification time also weakens reproducibility. These are static source findings, not results of an executed demo.

## Coverage and limitations

Collection: complete_with_exclusions; 87 text files; 21 excluded entries; recursive tree truncated: False.
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

- P1 · T1-1 · Required files absent from both releases do not make the verdict insufficient: Preflight the mandatory inputs for every selected analysis in each release independently of the diff. Record unavailable inputs as evidence and produce Insufficient Evidence before selective rerun logic. Preserve the intentional optional-RNA exception only for questions that genuinely do not need RNA.
- P1 · T1-4 · Identical content is skipped before readability or analytical validity is established: Validate the baseline and candidate against the selected question before using the equality shortcut, or reuse a validity receipt bound to the exact content hash and question. Keep file equality and analysis readiness as separate states.
- P2 · T1-2 · Changes are mapped to the selected analysis before rerunning: Retain the explicit impact explanation and selective rerun path. Add the independent input-validity gate described above without removing this separation.
- P2 · T1-3 · Ambiguous file variants are resolved by filesystem modification time: Reject multiple variants by default or require an explicit file map. Include the resolved relative path and the selection rule alongside the content hash in the evidence receipt.
- P2 · T1-3 · The export retains evidence rules and isolated per-finding effects: Keep the counterfactual calculation and expose its exact assumptions. State when effects cannot be computed and avoid implying that isolated effects add linearly.
- P2 · T1-6 · Repair urgency is tied to both measured effect and uncertainty: Retain these explanations and require a live reviewer to demonstrate approval, rejection and unresolved evidence before sign-off. Treat the half-percent convention as a configurable research rule, not a validated universal threshold.

## T1-1: Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support.

Status: **observed**

Changed-file detection and evidence construction are implemented, but shared missing inputs need an independent readiness gate. No sensitivity, specificity or unseen-input result was measured in this audit.

### Required files absent from both releases do not make the verdict insufficient

gap · P1 · Confidence: High for the inspected control flow; runtime and CLI-level handling remain untested.

The file loop records an absent file and immediately continues when both paths are missing. The insufficient flag remains false. An analysis with no mapped finding is not rerun, and the final fallback verdict is Ready. MeanByGroup.used also turns missing inputs into an empty set. Together these paths permit an empty or equally incomplete pair of release folders to look unchanged rather than unassessable. This is a source-derived control-flow conclusion, not an executed reproduction.

[Source lines 75–82](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L75-L82)

>     insufficient = False
> 
>     describe = \_describer\(folder\_a, folder\_b\)
>     for file in FILES:
>         pa, pb = release.path\_of\(folder\_a, file\), release.path\_of\(folder\_b, file\)
>         if not pa and not pb:
>             files\_info.append\(\{&quot;file&quot;: file, &quot;status&quot;: &quot;absent&quot;, &quot;opened&quot;: False}\)
>             continue

[Source lines 153–162](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L153-L162)

>     \# Rerun only the analyses a finding touches.
>     analyses, status\_of, blocked = \[\], \{}, False
>     for a in chosen:
>         because = \[i for i, f in enumerate\(raw\) if a.id in f\[&quot;affects&quot;\]\]
>         if not because:
>             status\_of\[a.id\] = &quot;not\_rerun&quot;
>             analyses.append\(\{&quot;id&quot;: a.id, &quot;status&quot;: &quot;not\_rerun&quot;,
>                              &quot;note&quot;: f&quot;Not rerun: no finding touches a file, column, row or sample that \{a.id} &quot;
>                                      f&quot;\(\{a.title}\) reads.&quot;}\)
>             continue

[Source lines 220–227](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L220-L227)

>     if insufficient:
>         verdict = &quot;Insufficient Evidence&quot;
>     elif blocked:
>         verdict = &quot;Blocked&quot;
>     elif any\(f\[&quot;affects\_analyses&quot;\] for f in findings\):
>         verdict = &quot;Conditional&quot;
>     else:
>         verdict = &quot;Ready&quot;                \# nothing changed, or nothing that changed is read by the question&\#x27;s analyses

[Source lines 107–113](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/analyses.py#L107-L113)

>     def used\(self, folder\):
>         &quot;&quot;&quot;The samples this analysis reads in this release.&quot;&quot;&quot;
>         try:
>             clinical, samples, \_ = self.inputs\(folder\)
>         except \(CannotRun, release.Unreadable, OSError, EOFError, UnicodeDecodeError\):
>             return set\(\)
>         return set\(self.\_used\(clinical, samples\)\)

Supplemental rules: None cited; official criterion above applies.

Impact: A judge or researcher could interpret Ready as usable inputs even though the selected analysis cannot be calculated. This affects data-problem detection and the distinction between missing evidence and an unchanged valid result.

Concrete change: Preflight the mandatory inputs for every selected analysis in each release independently of the diff. Record unavailable inputs as evidence and produce Insufficient Evidence before selective rerun logic. Preserve the intentional optional-RNA exception only for questions that genuinely do not need RNA.

Acceptance check: Using authorized synthetic fixtures, compare two empty folders, two folders both missing protein for A1, and two valid unchanged releases. The first two should be Insufficient Evidence with named inputs; the third may be Ready. Repeat with A2-only and optional RNA absent.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-2: Reasoning for the research question. Changes its result appropriately when the research question or intended use changes.

Status: **observed**

The selected analysis changes the impact map and isolated-effect calculation. Confirm numeric results and an A1/A2 question switch in a live authorized run.

### Changes are mapped to the selected analysis before rerunning

strength · P2 · Confidence: High for implementation structure; numerical equivalence to organizer analyses has not been executed here.

Each finding is mapped through the analysis&\#x27;s touched\_by function with used samples and per-file samples from both releases. Analyses without a mapped finding receive a not\_rerun explanation; affected analyses are calculated before and after.

[Source lines 138–151](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L138-L151)

>     \# Which analyses does each finding touch?
>     used = \{a.id: a.used\(folder\_a\) &\#124; a.used\(folder\_b\) for a in chosen}
>     in\_file = \{a.id: a.file\_samples\(folder\_a\) &\#124; a.file\_samples\(folder\_b\) for a in chosen}
>     for f in raw:
>         f\[&quot;affects&quot;\] = \[a.id for a in chosen
>                         if any\(a.touched\_by\(ch, used\[a.id\], in\_file\[a.id\]\) for ch in f\[&quot;changes&quot;\]\)\]
>     \# Severity must not depend on which analyses the question names, so &quot;is read by an analysis&quot; is asked of every
>     \# registered analysis as well as the ones in the question.
>     others = \[a for a in REGISTRY if a not in chosen\]
>     used\_o = \{a.id: a.used\(folder\_a\) &\#124; a.used\(folder\_b\) for a in others}
>     in\_file\_o = \{a.id: a.file\_samples\(folder\_a\) &\#124; a.file\_samples\(folder\_b\) for a in others}
>     for f in raw:
>         f\[&quot;read\_by\_any&quot;\] = bool\(f\[&quot;affects&quot;\]\) or any\(
>             a.touched\_by\(ch, used\_o\[a.id\], in\_file\_o\[a.id\]\) for a in others for ch in f\[&quot;changes&quot;\]\)

[Source lines 153–171](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L153-L171)

>     \# Rerun only the analyses a finding touches.
>     analyses, status\_of, blocked = \[\], \{}, False
>     for a in chosen:
>         because = \[i for i, f in enumerate\(raw\) if a.id in f\[&quot;affects&quot;\]\]
>         if not because:
>             status\_of\[a.id\] = &quot;not\_rerun&quot;
>             analyses.append\(\{&quot;id&quot;: a.id, &quot;status&quot;: &quot;not\_rerun&quot;,
>                              &quot;note&quot;: f&quot;Not rerun: no finding touches a file, column, row or sample that \{a.id} &quot;
>                                      f&quot;\(\{a.title}\) reads.&quot;}\)
>             continue
>         entry = \{&quot;id&quot;: a.id}
>         try:
>             before = a.run\(folder\_a\)
>             entry\[&quot;before&quot;\] = \_clean\(before\)
>         except \(CannotRun, release.Unreadable, OSError, EOFError, UnicodeDecodeError\) as e:
>             before = None
>             entry\[&quot;note&quot;\] = f&quot;Could not be run on \{rel\_a}: \{e}.&quot;
>         try:
>             after = a.run\(folder\_b\)

Supplemental rules: None cited; official criterion above applies.

Impact: This directly supports the Control Tower requirement to distinguish affected from unaffected analyses rather than rerunning everything or treating equal row counts as sufficient.

Concrete change: Retain the explicit impact explanation and selective rerun path. Add the independent input-validity gate described above without removing this separation.

Acceptance check: Change a protein value outside A1&\#x27;s cohort and then a value inside it. Demonstrate different affected-analysis decisions and preserve an unchanged A2 result with an evidence-backed reason.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-3: Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion.

Status: **observed**

Rules, effects, witnesses and hashes give a useful audit trail. Resolve ambiguous physical file selection and bind validity to the chosen input hashes.

### Ambiguous file variants are resolved by filesystem modification time

gap · P2 · Confidence: High; the selection rule is explicit. Cross-machine behavior was not exercised.

path\_of accepts compressed TSV, uncompressed TSV, CSV, XLSX and TXT candidates and chooses the one with the newest modification time. The choice is not made from an explicit release manifest or an ambiguity error.

[Source lines 33–40](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/release.py#L33-L40)

> def path\_of\(folder, name\):
>     &quot;&quot;&quot;Where a release&\#x27;s file is in a folder. A packed file may have been unpacked by whoever edited it, so
>     \`x.tsv\` stands in for \`x.tsv.gz\`; when both are there, the one changed most recently is the one meant.&quot;&quot;&quot;
>     stem = name\[:-3\] if name.endswith\(&quot;.gz&quot;\) else name
>     stem = stem\[:-4\] if stem.endswith\(&quot;.tsv&quot;\) else stem
>     names = \[name, stem + &quot;.tsv&quot;\] + \[stem + ext for ext in \(&quot;.csv&quot;, &quot;.xlsx&quot;, &quot;.txt&quot;\)\]
>     found = \[p for p in dict.fromkeys\(os.path.join\(folder, n\) for n in names\) if os.path.isfile\(p\)\]
>     return max\(found, key=os.path.getmtime\) if found else None

[Source lines 229–234](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L229-L234)

>     return \{
>         &quot;format\_version&quot;: &quot;0.2&quot;,
>         &quot;producer&quot;: dict\(PRODUCER\),
>         &quot;data&quot;: \{&quot;dataset&quot;: &quot;TCGA-BRCA \(event frozen release\)&quot;,
>                  &quot;releases&quot;: \[\{&quot;name&quot;: rel\_a, &quot;files&quot;: hashes\[rel\_a\]}, \{&quot;name&quot;: rel\_b, &quot;files&quot;: hashes\[rel\_b\]}\]},
>         &quot;question&quot;: f&quot;Did anything change between release \{rel\_a} and release \{rel\_b} that affects analysis &quot;

Supplemental rules: None cited; official criterion above applies.

Impact: Copying or unzipping the same directory can change timestamps and therefore which physical file is analyzed. A recorded hash helps identify what was read, but does not make this selection rule reproducible before the run.

Concrete change: Reject multiple variants by default or require an explicit file map. Include the resolved relative path and the selection rule alongside the content hash in the evidence receipt.

Acceptance check: Provide different compressed and uncompressed versions of one synthetic table, change only their timestamps, and confirm the tool either refuses ambiguity or selects the same explicitly configured file. Export the selected physical path.

### The export retains evidence rules and isolated per-finding effects

strength · P2 · Confidence: High for the code and exported fields; the calculations have not been independently rerun.

The engine computes an analysis on the trusted inputs and again with only one finding&\#x27;s changes applied, then stores before, after, size, measure and relative movement. The export includes rules, effects, file summaries and witness data in x\_readyset.

[Source lines 342–365](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L342-L365)

> def \_effects\(raw, findings, chosen, folder\_a, folder\_b\):
>     &quot;&quot;&quot;What each finding does to each analysis on its own: the analysis recomputed on the trusted release with only
>     that finding&\#x27;s changes applied.&quot;&quot;&quot;
>     inputs = \{}
>     for a in chosen:
>         try:
>             inputs\[a.id\] = \(a.inputs\(folder\_a\), a.inputs\(folder\_b\)\)
>         except \(CannotRun, release.Unreadable, OSError, EOFError, UnicodeDecodeError\):
>             inputs\[a.id\] = None
>     wrap = lambda v: v if isinstance\(v, tuple\) else \(v,\)
>     effects = \{}
>     for f, raw\_f in zip\(findings, raw\):
>         for a in chosen:
>             if a.id not in raw\_f\[&quot;affects&quot;\] or not inputs\[a.id\]:
>                 continue
>             before\_in, after\_in = inputs\[a.id\]
>             try:
>                 before = \_clean\(a.compute\(\*wrap\(before\_in\)\)\)
>                 alone = \_clean\(a.compute\(\*wrap\(a.with\_only\(before\_in, after\_in, raw\_f\[&quot;changes&quot;\]\)\)\)\)
>             except \(CannotRun, ValueError, KeyError, TypeError\):
>                 continue
>             size, measure, by = \_size\(before, alone\)
>             effects.setdefault\(f\[&quot;id&quot;\], \{}\)\[a.id\] = \{&quot;before&quot;: before, &quot;after&quot;: alone, &quot;size&quot;: size,
>                                                      &quot;measure&quot;: measure, &quot;moved\_by&quot;: by}

[Source lines 249–255](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L249-L255)

>             &quot;notes&quot;: notes,
>             &quot;rules&quot;: rules,
>             &quot;effects&quot;: effects,
>             &quot;repair\_priority&quot;: priority,
>             &quot;files&quot;: files\_info,
>             &quot;witness&quot;: witness,
>             &quot;scope&quot;: SCOPE},

Supplemental rules: None cited; official criterion above applies.

Impact: Reviewers can inspect why a finding matters and distinguish an isolated effect from the net effect of several changes. This is stronger evidence design than an unexplained severity label.

Concrete change: Keep the counterfactual calculation and expose its exact assumptions. State when effects cannot be computed and avoid implying that isolated effects add linearly.

Acceptance check: Use two synthetic changes with opposing effects. Show each isolated effect, the combined result and an unavailable-effect case; confirm the displayed claims distinguish these quantities.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-4: Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review.

Status: **observed**

Limitations and mandatory human-review fields are present. Identical-invalid and equally-incomplete inputs are the priority fail-closed checks.

### Identical content is skipped before readability or analytical validity is established

gap · P1 · Confidence: High that the shortcut precedes changed-file parsing; actual end-to-end outcomes require the stated follow-up.

The comparison skips a file immediately when its content hash matches. The later unreadable-table handler only covers compare\_file on changed content. Thus identical malformed or empty contents do not traverse that handler. Existing empty-input tests mutate only the new release, so their successful definitions do not establish coverage of identical bad inputs.

[Source lines 114–136](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L114-L136)

>         try:
>             ha, hb = release.content\_hash\(pa\), release.content\_hash\(pb\)
>         except release.Unreadable as e:
>             files\_info.append\(\{&quot;file&quot;: file, &quot;status&quot;: &quot;unreadable&quot;, &quot;opened&quot;: False}\)
>             insufficient = True
>             raw.append\(\_unreadable\(file, rel\_b, str\(e\)\)\)
>             continue
>         hashes\[rel\_a\].append\(\{&quot;file&quot;: file, &quot;sha256&quot;: ha, &quot;hash\_of&quot;: &quot;content&quot;}\)
>         hashes\[rel\_b\].append\(\{&quot;file&quot;: file, &quot;sha256&quot;: hb, &quot;hash\_of&quot;: &quot;content&quot;}\)
>         if ha == hb:
>             files\_info.append\(\{&quot;file&quot;: file, &quot;status&quot;: &quot;unchanged&quot;, &quot;opened&quot;: False}\)
>             continue
>         try:
>             found = compare\_file\(file, pa, pb, rel\_a, rel\_b, describe\)
>             raw += found
>             info = \{&quot;file&quot;: file, &quot;status&quot;: &quot;changed&quot;, &quot;opened&quot;: True}
>             if not found:
>                 info\[&quot;note&quot;\] = SAME\_VALUES
>             files\_info.append\(info\)
>         except release.Unreadable as e:
>             files\_info.append\(\{&quot;file&quot;: file, &quot;status&quot;: &quot;unreadable&quot;, &quot;opened&quot;: True}\)
>             insufficient = True
>             raw.append\(\_unreadable\(file, rel\_b, str\(e\)\)\)

[Source lines 22–37](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/tests/test_empty_inputs.py#L22-L37)

> class EmptyInputs\(unittest.TestCase\):
>     def changed\(self, file, change\):
>         d = tempfile.mkdtemp\(\)
>         a = TinyRelease\(\)
>         folder\_a, folder\_b = a.write\(os.path.join\(d, &quot;A&quot;\)\), a.copy\(\).write\(os.path.join\(d, &quot;B&quot;\)\)
>         path = os.path.join\(folder\_b, file\)
>         write\(path, change\(read\(path\)\)\)
>         return compare\(folder\_a, folder\_b\)
> 
>     def test\_a\_file\_with\_nothing\_in\_it\_is\_reported\_and\_the\_verdict\_is\_insufficient\_evidence\(self\):
>         for file, empty in \(\(PROTEIN, &quot;&quot;\), \(PROTEIN, &quot;\\n\\n&quot;\), \(CLINICAL, &quot;&quot;\), \(MUTATION, &quot;&quot;\)\):
>             doc = self.changed\(file, lambda text: empty\)
>             self.assertEqual\(doc\[&quot;verdict&quot;\], &quot;Insufficient Evidence&quot;, \(file, empty\)\)
>             self.assertEqual\(len\(doc\[&quot;findings&quot;\]\), 1\)
>             self.assertIn\(f&quot;\{file} could not be read&quot;, doc\[&quot;findings&quot;\]\[0\]\[&quot;summary&quot;\]\)
>             self.assertIn\(&quot;is empty&quot;, doc\[&quot;findings&quot;\]\[0\]\[&quot;summary&quot;\]\)

Supplemental rules: None cited; official criterion above applies.

Impact: Equality of two byte streams is not evidence that either is a valid analysis input. A missing baseline-validity gate can conceal shared corruption or an empty analytical cohort.

Concrete change: Validate the baseline and candidate against the selected question before using the equality shortcut, or reuse a validity receipt bound to the exact content hash and question. Keep file equality and analysis readiness as separate states.

Acceptance check: Create identical zero-byte clinical files, identical invalid tables and identical valid files with no eligible ER group. None should receive an unqualified Ready verdict. Include a valid identical positive control and verify that a cached validity receipt is invalidated by input or question changes.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-5: Working tool and clear setup. Judges can run the core workflow from the submitted repository.

Status: **not_tested**

Setup instructions and empty-input test definitions were inspected; no installer, submission test, server, hosted demo or organizer validator was run. A fresh-machine demonstration is still needed.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T1-6: Useful next steps. Suggested fixes are specific and match the size and importance of the problem.

Status: **observed**

The source implements differentiated repair priorities. A reviewer should verify that proposals, decisions and the original analysis remain distinct in the live workflow.

### Repair urgency is tied to both measured effect and uncertainty

strength · P2 · Confidence: High for the priority and export construction; human-review UI behavior is not tested.

The priority function distinguishes changes outside the question, unavailable reruns, large isolated effects, identity swaps/copies and smaller effects. Findings require human review and carry limitations, and repairs refer back to the finding they address.

[Source lines 186–200](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L186-L200)

>     \# Number the findings, set severity, attach repairs.
>     findings, repairs = \[\], \[\]
>     for i, f in enumerate\(raw, 1\):
>         fid = f&quot;F\{i}&quot;
>         moved = \[a for a in f\[&quot;affects&quot;\] if status\_of\[a\] in \(&quot;changed&quot;, &quot;blocked&quot;\)\]
>         findings.append\(\{
>             &quot;id&quot;: fid, &quot;kind&quot;: f\[&quot;kind&quot;\], &quot;summary&quot;: f\[&quot;summary&quot;\], &quot;severity&quot;: &quot;low&quot;,       \# set below, from its effect
>             &quot;confidence&quot;: f\[&quot;confidence&quot;\], &quot;evidence&quot;: f\[&quot;evidence&quot;\],
>             &quot;affects\_analyses&quot;: f\[&quot;affects&quot;\],
>             &quot;not\_affected\_analyses&quot;: \[a.id for a in chosen if a.id not in f\[&quot;affects&quot;\]\],
>             &quot;limitation&quot;: f\[&quot;limitation&quot;\], &quot;needs\_human\_review&quot;: True}\)
>         for r in \(f.get\(&quot;repair&quot;\), f.get\(&quot;extra\_repair&quot;\)\):
>             if r:
>                 repairs.append\(\{&quot;id&quot;: f&quot;R\{len\(repairs\) + 1}&quot;, &quot;action&quot;: r\[&quot;action&quot;\], &quot;targets&quot;: r\[&quot;targets&quot;\],
>                                 &quot;justification&quot;: r\[&quot;justification&quot;\], &quot;addresses&quot;: \[fid\]}\)

[Source lines 369–391](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L369-L391)

> def \_priority\(findings, repairs, effects\):
>     &quot;&quot;&quot;How urgently each suggested fix is needed, sized by its finding&\#x27;s own effect.&quot;&quot;&quot;
>     priority = \{}
>     for r in repairs:
>         fid = r\[&quot;addresses&quot;\]\[0\]
>         f = next\(x for x in findings if x\[&quot;id&quot;\] == fid\)
>         sizes = \[e\[&quot;size&quot;\] for e in effects.get\(fid, \{}\).values\(\)\]
>         if not f\[&quot;affects\_analyses&quot;\]:
>             priority\[r\[&quot;id&quot;\]\] = \{&quot;level&quot;: &quot;for the record&quot;, &quot;why&quot;: &quot;Nothing in the question reads what this finding touches.&quot;}
>         elif not sizes:
>             priority\[r\[&quot;id&quot;\]\] = \{&quot;level&quot;: &quot;before use&quot;, &quot;why&quot;: &quot;An analysis you rely on cannot be rerun until this is resolved.&quot;}
>         elif &quot;large&quot; in sizes:
>             priority\[r\[&quot;id&quot;\]\] = \{&quot;level&quot;: &quot;before use&quot;, &quot;why&quot;: &quot;On its own this finding clearly moves a result you rely on.&quot;}
>         elif f\[&quot;kind&quot;\] in \(&quot;sample\_swap&quot;, &quot;duplicate&quot;\):
>             priority\[r\[&quot;id&quot;\]\] = \{&quot;level&quot;: &quot;before use&quot;, &quot;why&quot;: &quot;These samples carry another sample&\#x27;s data. The effect on this &quot;
>                                  &quot;result is small or none, but anything else computed from them is wrong too.&quot;}
>         elif &quot;small&quot; in sizes:
>             priority\[r\[&quot;id&quot;\]\] = \{&quot;level&quot;: &quot;small effect&quot;, &quot;why&quot;: &quot;On its own this finding moves no headline number of a result by &quot;
>                                  &quot;half a percent or more. Confirm it with the data provider; if you use the release &quot;
>                                  &quot;anyway, say so in your methods.&quot;}
>         else:
>             priority\[r\[&quot;id&quot;\]\] = \{&quot;level&quot;: &quot;no effect on the result&quot;, &quot;why&quot;: &quot;It touches samples a result reads, but on its own &quot;
>                                  &quot;the result is the same. Fix it when convenient.&quot;}

Supplemental rules: None cited; official criterion above applies.

Impact: The review handoff names a useful next action instead of merely enumerating anomalies. Uncertainty about whether a changed release is correct is not replaced with automatic source-data editing in this inspected path.

Concrete change: Retain these explanations and require a live reviewer to demonstrate approval, rejection and unresolved evidence before sign-off. Treat the half-percent convention as a configurable research rule, not a validated universal threshold.

Acceptance check: Show one unrelated finding, one noncomputable result and one small effect. Check that their repair urgency differs and that the exported findings and original input hashes are preserved through review.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-7: Communication. Someone without specialist knowledge can understand the result and next step.

Status: **not_tested**

README wording explains precomputed hosted comparison versus local live comparison. Unguided usability, keyboard access and comprehension remain untested.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## Excluded scope

- .gitignore: non-allowlisted file type
- run.bat: non-allowlisted file type
- run.command: non-allowlisted file type
- web/dist/assets/index-BCGbygox.js: file-size limit
- web/dist/assets/red-hat-display-latin-ext-wght-normal-Do32GAgg.woff2: non-allowlisted file type
- web/dist/assets/red-hat-display-latin-wght-normal-BX-N26TK.woff2: non-allowlisted file type
- web/dist/assets/red-hat-mono-latin-ext-wght-normal-BQQ6IFDA.woff2: non-allowlisted file type
- web/dist/assets/red-hat-mono-latin-wght-normal-Dwfc5A3M.woff2: non-allowlisted file type
- web/dist/assets/red-hat-text-latin-ext-wght-normal-BYbCslLJ.woff2: non-allowlisted file type
- web/dist/assets/red-hat-text-latin-wght-normal-ZHr5wXre.woff2: non-allowlisted file type
- web/dist/brand/icon-180.png: non-allowlisted file type
- web/dist/brand/icon-32.png: non-allowlisted file type
- web/dist/brand/icon-512.png: non-allowlisted file type
- web/dist/brand/mark-dark.png: non-allowlisted file type
- web/dist/brand/mark-light.png: non-allowlisted file type
- web/package-lock.json: sensitive or generated filename
- web/public/brand/icon-180.png: non-allowlisted file type
- web/public/brand/icon-32.png: non-allowlisted file type
- web/public/brand/icon-512.png: non-allowlisted file type
- web/public/brand/mark-dark.png: non-allowlisted file type
- web/public/brand/mark-light.png: non-allowlisted file type

## Judge Follow-Up Sequence

1. Verify the official final commit and product declaration.
2. Start with the highest-priority synthetic acceptance checks above.
3. Follow one finding through evidence, affected versus unaffected analyses, proposed repair and human decision.
4. Verify the exported artifact against the organizer contract without reading sealed answers.
5. Record actual results separately from this static audit; revise only claims the new evidence supports.
