# Professor Bear Audit: OncoSys Cohort Studio

## Review Identity

This is an independent, provisional source-code audit for judge deliberation. It is not an official grade.

- Entry: `tammy357/oncosys-cohort-studio`
- Commit: `54aeacb6f6f355a1dcaa42d7abf2ce174315ad69`
- Organizer reference: `6e15a399a64ffbf80778db0b462ac239e70086b9`
- Product: `cohort-studio`; Track 1, Cohort Firewall
- Pass: 1; reviewed 2026-11-14T20:05:56.895189+00:00
- Runtime: **not executed**; official freeze/receipt: **not verified**

## Executive Assessment

Cohort Studio implements the distinct Studio workflow: editable operations, counts of rows versus samples versus patients, inflation-aware fixes, unique cohort IDs and a standalone reconstruction script. The most important concerns are an unknown-checksum state being described as verified, unsafe interpolation of request text into generated Python, and reconstruction continuing after input-hash mismatch. The final concern is an explicit trust-policy question, not a claim that Studio must obey every Control Tower contract.

## Workflow Traced

A text request is drafted into a specification, or an existing specification is accepted. The engine validates and applies steps, records counts, removals, failures and row inflation, then optionally constructs a fixed copy with a change log. A rule-based evaluator assigns a verdict and writes cohort, ledger, exclusions, audit, selection and reconstruction artifacts. The API defaults to automatic drafting and inflation fixes; those defaults should be distinguished from an explicitly human-approved cohort.

## Findings At A Glance

| ID | Type | Priority | Finding |
|---|---|---|---|
| CS-01 | gap | P1 | An unknown checksum can be described as a matching checksum |
| CS-02 | gap | P1 | Request text is inserted into a generated Python docstring |
| CS-03 | question | P2 | Reconstruction warns about changed inputs but still writes a cohort |
| CS-04 | strength | P2 | Step ledgers distinguish rows, samples and patients |
| CS-05 | strength | P2 | The export path has unique cohort IDs and inspectable operations |
| CS-06 | strength | P2 | Inflation fixes are explicit copied transformations with a log |

## Inspection Scope

The following files informed the implementation-level conclusions in this pass. Other collected files are not automatically treated as reviewed:

- `cohort_studio/data.py`
- `cohort_studio/api.py`
- `cohort_studio/engine.py`
- `cohort_studio/ops.py`
- `cohort_studio/verdict.py`
- `cohort_studio/exports.py`
- `cohort_studio/llm.py`
- `cohort_studio/hosted.py`

## Parallel Review Preservation

Existing reports were read and retained. This is a separately versioned supplement; prior conclusions are not silently replaced.

The existing REPORT.md and updated TESTS.md were read and retained. The parallel agent reports 279 passed and 20 skipped submitted tests and targeted checksum/code-generation probes. Those are attributed observations, not runs by this reviewer. CS-01 and CS-02 corroborate its checksum and generated-script findings. CS-03 follows the script's mismatch behavior further. Earlier concerns about auto-fixes, blocked exports and disclosed hosted drafting remain in the original report and are not relabeled as new discoveries.

This pass does not accept earlier agents' findings as established merely because they were reported. Any correction must identify the earlier claim and the new evidence explicitly.

## Detailed Criterion Review

# Judge review aid: oncosys-cohort-studio

Repository: https://github.com/tammy357/oncosys-cohort-studio
Commit: `54aeacb6f6f355a1dcaa42d7abf2ce174315ad69`
Track: 1
Reviewer: Professor Bear / Codex source review

**Not an official result. Source review does not establish runtime behavior.**

Cohort Studio implements the distinct Studio workflow: editable operations, counts of rows versus samples versus patients, inflation-aware fixes, unique cohort IDs and a standalone reconstruction script. The most important concerns are an unknown-checksum state being described as verified, unsafe interpolation of request text into generated Python, and reconstruction continuing after input-hash mismatch. The final concern is an explicit trust-policy question, not a claim that Studio must obey every Control Tower contract.

## Coverage and limitations

Collection: complete_with_exclusions; 124 text files; 188 excluded entries; recursive tree truncated: False.
Runtime: not tested by this toolkit. Git blob identity and evidence line/quote consistency were checked.

Challenge reference: https://github.com/disleveK/oncosys-hackathon-challenge/tree/6e15a399a64ffbf80778db0b462ac239e70086b9

Product: cohort-studio

Product review route: Inspect editable filters and joins, distinct patient/sample counts at every step, rerunnable export, and cohort\_samples.csv with unique sample\_id values. Test join inflation without assuming every row is a patient.

- Pinned local checkout, not a verified official final-submission receipt; branch names and later changes are outside this pass.
- Static source analysis only. No submission code, tests, installers, workflows, notebook, server, hosted endpoint or model was executed.
- No sealed envelopes, answer keys or raw clinical datasets were accessed. Numerical correctness, performance, accessibility and fresh-machine setup remain untested.
- Source-derived control-flow consequences are labeled as such. Proposed acceptance checks are not observed test results.
- The collected text budget is 160 files, 200 KB/file and 4 MB/entry. Complete\_with\_exclusions is not an exhaustive audit; exclusions and focused follow-ups are recorded.
- No official score, cross-team ranking, clinical validity or regulatory/accessibility certification is asserted.

## Priorities

- P1 · T1-3 · An unknown checksum can be described as a matching checksum: Preserve distinct missing, unverified, mismatched and verified states. Require True for a matching-checksum claim and mark unavailable expected metadata as unknown with a concrete recovery instruction.
- P1 · T1-4 · Request text is inserted into a generated Python docstring: Serialize request text safely as a string literal or external JSON metadata and keep executable code structurally separate. Apply the same rule to every user-controlled value and test the resulting artifact without executing arbitrary text.
- P2 · T1-1 · Step ledgers distinguish rows, samples and patients: Retain all three count dimensions and the exact join rule. Explain intentional one-to-many data separately from accidental inflation and keep counts before and after any fix visible.
- P2 · T1-2 · Inflation fixes are explicit copied transformations with a log: Retain copied specifications, first results and fix logs. Show the semantic change and ask for explicit confirmation before representing the fixed cohort as approved for a research use that depends on join meaning.
- P2 · T1-5 · The export path has unique cohort IDs and inspectable operations: Keep the complete export bundle and bind it to a manifest of input and output hashes. Add exact membership parity checks between the app result and an independently reviewed reconstruction.
- P2 · T1-6 · Reconstruction warns about changed inputs but still writes a cohort: Decide and document the contract. A strict reproduction mode should stop on hash mismatch and compare membership or an output digest; an exploratory mode can continue but must produce a clearly labeled new run with changed-input provenance.

## T1-1: Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support.

Status: **observed**

Step counts and join-inflation evidence fit the Studio product. Detection accuracy and real-cohort inclusion were not independently measured.

### Step ledgers distinguish rows, samples and patients

strength · P2 · Confidence: High for the inspected count and inflation construction; no join fixture was run in this pass.

Each applied step records incoming and outgoing row, distinct-sample and distinct-patient counts. The engine identifies growth in rows per sample, records duplicate counts and examples, and the verdict distinguishes unresolved inflation from inflation later resolved by a step or logged fix.

[Source lines 314–338](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/engine.py#L314-L338)

> def run\(spec, store\):
>     problems = validate\(spec, store\)
>     frame = store.manifest.copy\(\)
>     start\_ids = list\(frame\[&quot;sample\_id&quot;\].unique\(\)\)
>     filtered\_vars = set\(\)
>     all\_links = \{}
>     results = \[\]
>     failed = False
>     for i, step in enumerate\(spec.get\(&quot;steps&quot;, \[\]\)\):
>         r = StepResult\(index=i, label=describe\_step\(step, store\), op=step.get\(&quot;op&quot;, &quot;?&quot;\)\)
>         r.rows\_in, r.samples\_in, r.patients\_in = len\(frame\), frame\[&quot;sample\_id&quot;\].nunique\(\), frame\[&quot;patient\_id&quot;\].nunique\(\)
>         step\_problems = \[m for \(j, m\) in problems if j == i\]
>         if failed or step\_problems:
>             r.skipped = True
>             r.error = &quot;; &quot;.join\(step\_problems\) if step\_problems else &quot;Not run because an earlier step failed.&quot;
>             failed = True
>             results.append\(r\)
>             continue
>         try:
>             new = apply\_step\(frame, step, store\)
>         except Exception as exc:  \# show the error in the ledger instead of crashing the app
>             r.error, r.skipped, failed = str\(exc\), True, True
>             results.append\(r\)
>             continue
>         r.rows\_out, r.samples\_out, r.patients\_out = len\(new\), new\[&quot;sample\_id&quot;\].nunique\(\), new\[&quot;patient\_id&quot;\].nunique\(\)

[Source lines 355–363](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/engine.py#L355-L363)

>         ratio\_in = r.rows\_in / r.samples\_in if r.samples\_in else 1
>         if r.samples\_out and r.rows\_per\_sample &gt; ratio\_in + 1e-9:
>             r.inflated = True
>             extra = r.rows\_out - r.samples\_out
>             r.inflation\_note = \(f&quot;Rows grew to \{r.rows\_out:,} but there are only \{r.samples\_out:,} distinct samples &quot;
>                                 f&quot;\(\{r.patients\_out:,} patients\): \{extra:,} extra rows would count samples more than once.&quot;\)
>             r.duplicate\_examples = \_duplicate\_examples\(new, step\)
>             counts = new\[&quot;sample\_id&quot;\].value\_counts\(\)
>             r.duplicate\_counts = \{sid: int\(n\) for sid, n in sorted\(counts\[counts &gt; 1\].items\(\)\)}

[Source lines 165–182](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/verdict.py#L165-L182)

>     \# 4. Join inflation
>     inflated = \[s for s in result.steps if s.inflated\]
>     if result.unresolved\_inflation:
>         worst = max\(inflated, key=lambda s: s.rows\_out - s.samples\_out\) if inflated else None
>         where = f&quot; It starts at step \{worst.index + 1} \(\{worst.label}\).&quot; if worst else &quot;&quot;
>         checks.append\(Check\(&quot;No sample is counted twice&quot;, &quot;fail&quot;,
>                             f&quot;The final table has \{result.final\_rows:,} rows for \{result.final\_samples:,} samples.\{where}&quot;,
>                             &quot;Apply the suggested fix before exporting.&quot;\)\)
>     elif inflated:
>         checks.append\(Check\(&quot;No sample is counted twice&quot;, &quot;pass&quot;,
>                             &quot;A join inflated the rows, and a later step brought it back to one row per sample: &quot;
>                             + &quot;; &quot;.join\(f&quot;step \{s.index + 1}&quot; for s in inflated\) + &quot;.&quot;\)\)
>     elif spec.get\(&quot;fix\_log&quot;\):
>         fixed = &quot;; &quot;.join\(f&quot;step \{f\[&\#x27;step&\#x27;\]} had \{f\[&\#x27;rows&\#x27;\]:,} rows for \{f\[&\#x27;samples&\#x27;\]:,} samples and was fixed &quot;
>                           f&quot;\(\{f\[&\#x27;fix&\#x27;\].rstrip\(&\#x27;.&\#x27;\)}\)&quot; for f in spec\[&quot;fix\_log&quot;\]\)
>         checks.append\(Check\(&quot;No sample is counted twice&quot;, &quot;pass&quot;, f&quot;Inflation found and fixed: \{fixed}.&quot;\)\)
>     else:
>         checks.append\(Check\(&quot;No sample is counted twice&quot;, &quot;pass&quot;, &quot;Every step kept one row per sample.&quot;\)\)

Supplemental rules: None cited; official criterion above applies.

Impact: This directly addresses a central Studio failure mode: join multiplicity can increase rows without adding independent samples or patients. The source makes the distinction inspectable instead of presenting one misleading cohort size.

Concrete change: Retain all three count dimensions and the exact join rule. Explain intentional one-to-many data separately from accidental inflation and keep counts before and after any fix visible.

Acceptance check: Join one invented sample to two slide records. Verify rows increase, distinct samples do not, the ledger names the inflating step, and a later exists-style fix retains the intended sample exactly once.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-2: Reasoning for the research question. Changes its result appropriately when the research question or intended use changes.

Status: **observed**

Editable steps and copied, logged fixes expose construction logic. Automatic transformation must remain distinct from human approval of the research meaning.

### Inflation fixes are explicit copied transformations with a log

strength · P2 · Confidence: High for clone/log and API return structure; researcher acceptance and end-to-end presentation remain untested.

suggest\_fix chooses exists-style matching for slide/normal joins, sample-level keys for patient-key joins, or a deduplication step. apply\_fixes clones the specification and records the old step, row/sample/patient counts, examples and proposed fix. The API retains the first result and list of fixes when it reruns a fixed specification.

[Source lines 392–403](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/engine.py#L392-L403)

> def suggest\_fix\(step\):
>     &quot;&quot;&quot;A minimal change that stops a step counting samples twice, with a plain-words reason.&quot;&quot;&quot;
>     fixed = dict\(step\)
>     if step\[&quot;op&quot;\] == &quot;join&quot; and step\[&quot;table&quot;\] in \(&quot;slides&quot;, &quot;normals&quot;\):
>         fixed\[&quot;mode&quot;\] = &quot;exists&quot;
>         what = &quot;slide&quot; if step\[&quot;table&quot;\] == &quot;slides&quot; else &quot;normal-tissue sample&quot;
>         return fixed, f&quot;Keep each sample once if it has at least one matching \{what}, instead of one row per \{what}.&quot;
>     if step\[&quot;op&quot;\] == &quot;join&quot; and step.get\(&quot;key&quot;\) == &quot;patient\_id&quot;:
>         fixed\[&quot;key&quot;\] = &quot;sample\_id&quot;
>         return fixed, \(&quot;Match each sample to its own record by sample barcode. Joining on the patient barcode &quot;
>                        &quot;also matches the patient&\#x27;s other samples \(for example a normal-tissue sample\).&quot;\)
>     return None, &quot;Add a &\#x27;keep one row per sample&\#x27; step after this one.&quot;

[Source lines 406–424](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/engine.py#L406-L424)

> def apply\_fixes\(spec, result, only=None\):
>     &quot;&quot;&quot;Return a copy of the spec with every inflating step fixed \(or just step \`only\`\), plus what changed.&quot;&quot;&quot;
>     new = clone\(spec\)
>     changes = \[\]
>     inserts = \[\]
>     for r in result.steps:
>         if not r.inflated or \(only is not None and r.index \!= only\):
>             continue
>         step = new\[&quot;steps&quot;\]\[r.index\]
>         fixed, why = suggest\_fix\(step\)
>         if fixed is not None:
>             new\[&quot;steps&quot;\]\[r.index\] = fixed
>         else:
>             inserts.append\(r.index + 1\)
>         changes.append\(f&quot;Step \{r.index + 1}: \{why}&quot;\)
>         new.setdefault\(&quot;fix\_log&quot;, \[\]\).append\(\{
>             &quot;step&quot;: r.index + 1, &quot;was&quot;: r.label, &quot;rows&quot;: r.rows\_out, &quot;samples&quot;: r.samples\_out,
>             &quot;patients&quot;: r.patients\_out, &quot;examples&quot;: r.duplicate\_examples\[:5\], &quot;fix&quot;: why,
>             &quot;inserted\_step&quot;: fixed is None, &quot;rows\_per\_sample&quot;: r.duplicate\_counts}\)

[Source lines 116–139](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/api.py#L116-L139)

> def \_run\(spec, store, fix\):
>     first = engine.run\(spec, store\)
>     if fix and any\(s.inflated for s in first.steps\):
>         spec, changes = engine.apply\_fixes\(spec, first\)
>         return spec, engine.run\(spec, store\), first, changes
>     return spec, first, first, \[\]
> 
> 
> def build\_cohort\(query, out\_dir=&quot;output&quot;, store=None, data\_dir=None, ai=&quot;auto&quot;, fix=True, accept\_unparsed=False,
>                  team=&quot;Cohort Studio team&quot;, write=True, log=None, drafter=None, \*\*ai\_options\):
>     &quot;&quot;&quot;Draft \(if needed\), run, fix inflation, evaluate and export one cohort. ai: &quot;auto&quot;, &quot;own&quot; or &quot;off&quot; \(see
>     llm.draft\_spec\); ai\_options: provider, api\_key, model, base\_url or client for your own model. drafter: a
>     function request -&gt; \(spec, route\) used instead of llm.draft\_spec \(the hosted MCP server drafts on the server\).&quot;&quot;&quot;
>     store = store or DataStore\(data\_dir\)
>     kind, q = as\_query\(query\)
>     if kind == &quot;spec&quot;:
>         spec, route = q, \{&quot;used&quot;: &quot;definition&quot;, &quot;label&quot;: &quot;cohort definition, run as written&quot;, &quot;tried&quot;: \[\]}
>     elif drafter is not None:
>         spec, route = drafter\(q\)
>     else:
>         spec, route = draft\_spec\(q, store, ai=ai, log=log, \*\*ai\_options\)
>     if accept\_unparsed:
>         spec\[&quot;unparsed\_confirmed&quot;\] = True
>     spec, result, first, fixes = \_run\(spec, store, fix\)

[Source lines 151–153](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/api.py#L151-L153)

>     v = verdict.evaluate\(result, store\)
>     out = exports.write\_all\(result, v, store, out\_dir, team=team\) if write else None
>     return CohortRun\(spec.get\(&quot;request&quot;, q if kind == &quot;text&quot; else &quot;&quot;\), spec, result, first, fixes, v, route, out\)

Supplemental rules: None cited; official criterion above applies.

Impact: This makes the before-versus-after transformation inspectable and preserves evidence of why a cohort changed. Automatic API fixing is not equivalent to human approval, even when the change is logged and originals are not edited.

Concrete change: Retain copied specifications, first results and fix logs. Show the semantic change and ask for explicit confirmation before representing the fixed cohort as approved for a research use that depends on join meaning.

Acceptance check: Compare fix=False and fix=True on an inflated synthetic join. Confirm the original specification is unchanged, the first result and exact policy change remain available, and the approved versus preview state is explicit.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-3: Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion.

Status: **observed**

Exported specifications and input hashes aid provenance, but unknown checksum state must not be called verified.

### An unknown checksum can be described as a matching checksum

gap · P1 · Confidence: High for the tri-state control flow; the parallel TESTS.md reports a matching helper-level unknown-to-pass reproduction.

Raw-file status starts verified=None and becomes True or False only when an expected digest exists. available accepts a present file unless verification is explicitly False. The frozen-file verdict looks only for False and otherwise says every raw file used matches sources.csv. A missing expected digest is therefore not distinguished from a verified match in that check.

[Source lines 64–86](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/data.py#L64-L86)

>     def \_check\_files\(self\):
>         expected = \{}
>         sources = self.data\_dir / &quot;sources.csv&quot;
>         if sources.exists\(\):
>             with open\(sources\) as f:
>                 expected = \{row\[&quot;file&quot;\]: row\[&quot;sha256&quot;\] for row in csv.DictReader\(f\)}
>         status = \{}
>         for name in \[&quot;sample\_manifest.csv&quot;, &quot;slide\_manifest.csv&quot;\]:
>             path = self.data\_dir / name
>             status\[name\] = \{&quot;present&quot;: path.exists\(\), &quot;verified&quot;: None, &quot;sha256&quot;: sha256\(path\) if path.exists\(\) else None,
>                             &quot;note&quot;: &quot;committed manifest&quot;}
>         for table, name in RAW\_FILES.items\(\):
>             path = self.data\_dir / &quot;raw&quot; / name
>             entry = \{&quot;present&quot;: path.exists\(\), &quot;verified&quot;: None, &quot;sha256&quot;: None, &quot;note&quot;: &quot;&quot;}
>             if path.exists\(\):
>                 entry\[&quot;sha256&quot;\] = sha256\(path\)
>                 if name in expected:
>                     entry\[&quot;verified&quot;\] = entry\[&quot;sha256&quot;\] == expected\[name\]
>                     entry\[&quot;note&quot;\] = &quot;matches the frozen checksum&quot; if entry\[&quot;verified&quot;\] else \\
>                         &quot;DOES NOT match the frozen checksum: tell the organizers and don&\#x27;t use it for judged results&quot;
>             else:
>                 entry\[&quot;note&quot;\] = &quot;not downloaded yet: run python data/tcga-brca/fetch.py&quot;
>             status\[name\] = entry

[Source lines 89–93](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/data.py#L89-L93)

>     def available\(self, table\):
>         if table in \(&quot;manifest&quot;, &quot;slides&quot;, &quot;normals&quot;\):
>             return True
>         entry = self.file\_status.get\(RAW\_FILES.get\(table, &quot;&quot;\), \{}\)
>         return bool\(entry.get\(&quot;present&quot;\)\) and entry.get\(&quot;verified&quot;\) is not False

[Source lines 143–160](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/verdict.py#L143-L160)

>     \# 3. Frozen files
>     used = \{&quot;sample\_manifest.csv&quot;}
>     for s in steps:
>         if s.get\(&quot;op&quot;\) == &quot;join&quot;:
>             used.add\(SOURCE\_FILES\[s\[&quot;table&quot;\]\]\)
>         if s.get\(&quot;op&quot;\) == &quot;mutation&quot;:
>             used.add\(SOURCE\_FILES\[&quot;mutation&quot;\]\)
>         if s.get\(&quot;op&quot;\) == &quot;where&quot;:
>             used &\#124;= \{SOURCE\_FILES\[n\] for n in condition\_sources\(s.get\(&quot;condition&quot;\) or \{}\)}
>     bad = \[f for f in used if store.file\_status.get\(f, \{}\).get\(&quot;verified&quot;\) is False\]
>     if bad:
>         checks.append\(Check\(&quot;Files match the event&\#x27;s frozen checksums&quot;, &quot;unknown&quot;,
>                             f&quot;\{&\#x27;, &\#x27;.join\(bad\)} changed since the frozen release.&quot;,
>                             &quot;Tell the organizers; don&\#x27;t use these results for judging.&quot;\)\)
>     else:
>         checks.append\(Check\(&quot;Files match the event&\#x27;s frozen checksums&quot;, &quot;pass&quot;,
>                             &quot;Every raw file used matches sources.csv \(manifests are the committed versions\).&quot;,
>                             fields=sorted\(used\)\)\)

Supplemental rules: None cited; official criterion above applies.

Impact: A hash of current bytes establishes identity of those bytes, not agreement with the organizer&\#x27;s frozen release. The claim can overstate provenance when expected checksum metadata is absent. This does not establish that ordinary bundled metadata is missing.

Concrete change: Preserve distinct missing, unverified, mismatched and verified states. Require True for a matching-checksum claim and mark unavailable expected metadata as unknown with a concrete recovery instruction.

Acceptance check: Use a present synthetic raw file with no expected digest, then a matching digest and a mismatched digest. Only the matching case may claim verification; the unknown case must name the missing reference metadata.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-4: Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review.

Status: **observed**

Generated-script text boundaries need fixing. Hosted drafting is disclosed in the repository and was not called; no undisclosed transmission or actual leak is claimed.

### Request text is inserted into a generated Python docstring

gap · P1 · Confidence: High for literal interpolation; the parallel reviewer reports syntax and statement-boundary probes, which were not rerun here.

reproduce\_script places spec.request verbatim between triple-quoted Python docstring delimiters. Most operation arguments later use repr formatting, but this leading prose field is not encoded as a Python literal. Quotes and newlines in request text can therefore break script syntax or terminate the docstring and become code in the exported file.

[Source lines 154–171](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L154-L171)

> def reproduce\_script\(result, store\):
>     &quot;&quot;&quot;A standalone script that rebuilds the cohort with the same operations the app used.&quot;&quot;&quot;
>     spec = result.spec
>     lines = \[
>         &\#x27;&quot;&quot;&quot;Reproduce a Cohort Studio cohort from the frozen TCGA-BRCA release.&\#x27;,
>         &quot;&quot;,
>         f&quot;Request : \{spec.get\(&\#x27;request&\#x27;, &\#x27;&\#x27;\)}&quot;,
>         f&quot;Created : \{datetime.date.today\(\).isoformat\(\)} by Cohort Studio&quot;,
>         f&quot;Expected: \{len\(result.cohort\_ids\)} samples&quot;,
>         &quot;&quot;,
>         &quot;Usage \(from the repository root, after python data/tcga-brca/fetch.py\):&quot;,
>         &quot;    python reproduce\_cohort.py \[data/tcga-brca\] \[cohort\_samples.csv\]&quot;,
>         &\#x27;&quot;&quot;&quot;&\#x27;,
>         &quot;import hashlib&quot;,
>         &quot;import sys&quot;,
>         &quot;&quot;,
>         &quot;\# ---- the exact operations Cohort Studio uses \(copied from cohort\_studio/ops.py\) ----&quot;,
>         inspect.getsource\(ops\).split\(&\#x27;&quot;&quot;&quot;&\#x27;, 2\)\[2\].strip\(\),

[Source lines 237–255](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L237-L255)

>             lines.append\(f&quot;df = join\_table\(df, right, \{PREFIX\[t\]\!r}, \{s\[&\#x27;key&\#x27;\]\!r}, \{s.get\(&\#x27;mode&\#x27;, &\#x27;rows&\#x27;\)\!r}\)&quot;\)
>         elif op == &quot;filter&quot;:
>             col = store.resolve\_field\(s\[&quot;table&quot;\], s\[&quot;field&quot;\]\)
>             if col is None:   \# the file isn&\#x27;t downloaded or has no such column; the verdict already says so
>                 lines.append\(f&quot;raise SystemExit\(\{\(&\#x27;This release has no column for &\#x27; + repr\(s\[&\#x27;field&\#x27;\]\) + &\#x27; in &\#x27; + s\[&\#x27;table&\#x27;\] + &\#x27;; run data/tcga-brca/fetch.py first.&\#x27;\)\!r}\)&quot;\)
>             else:
>                 lines.append\(f&quot;df = filter\_column\(df, \{PREFIX\[s\[&\#x27;table&\#x27;\]\] + &\#x27;.&\#x27; + col\!r}, \{s\[&\#x27;cmp&\#x27;\]\!r}, \{s.get\(&\#x27;value&\#x27;\)\!r}\)&quot;\)
>         elif op == &quot;mutation&quot;:
>             if &quot;mutation&quot; not in loaded:
>                 lines.append\(&quot;mutation = load\_mutation\(DATA\)&quot;\)
>                 loaded.add\(&quot;mutation&quot;\)
>             lines.append\(f&quot;df = filter\_mutation\(df, mutation, \{s\[&\#x27;gene&\#x27;\]\!r}, \{bool\(s.get\(&\#x27;mutated&\#x27;, True\)\)\!r}\)&quot;\)
>         elif op == &quot;dedupe&quot;:
>             lines.append\(&quot;df = one\_row\_per\_sample\(df\)&quot;\)
>         elif op == &quot;where&quot;:
>             names = sorted\(condition\_sources\(s\[&quot;condition&quot;\]\)\)
>             sources = &quot;, &quot;.join\(f&quot;\{n\!r}: load\_\{n}\(DATA\)&quot; for n in names\)
>             tree = resolve\_condition\(s\[&quot;condition&quot;\], store\)
>             lines.append\(f&quot;df = filter\_where\(df, \{tree\!r}, \{\{\{sources}}}, \{s.get\(&\#x27;apply\_to&\#x27;, &\#x27;sample&\#x27;\)\!r}\)&quot;\)

Supplemental rules: None cited; official criterion above applies.

Impact: A reproduction artifact should preserve a user&\#x27;s description as data, not reinterpret it as executable syntax. The dangerous transition occurs if someone later runs the generated script; this review did not execute generated code or establish a deployed attack.

Concrete change: Serialize request text safely as a string literal or external JSON metadata and keep executable code structurally separate. Apply the same rule to every user-controlled value and test the resulting artifact without executing arbitrary text.

Acceptance check: Generate scripts from ordinary text, multiline text and text containing triple quotes. Parse the generated syntax in an authorized environment and verify the original request remains a literal value with no extra executable statements.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-5: Working tool and clear setup. Judges can run the core workflow from the submitted repository.

Status: **observed**

The code exports unique IDs and reconstruction artifacts. The parallel review reports 279 passed and 20 skipped tests; this source pass did not execute them.

### The export path has unique cohort IDs and inspectable operations

strength · P2 · Confidence: High for the export construction; fresh-machine reconstruction and output parity were not executed by this reviewer.

cohort\_sample\_ids collects IDs into a set and returns them sorted. cohort\_frame writes a sample\_id column from those IDs. write\_all emits the specification, ledger, exclusions, audit trail, sample selections, verdict and reconstruction script alongside cohort\_samples.csv. The script serializes most operation arguments with repr.

[Source lines 323–328](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/ops.py#L323-L328)

> def cohort\_sample\_ids\(df, extra\_columns=\(\)\):
>     ids = set\(df\[&quot;sample\_id&quot;\].dropna\(\)\)
>     for col in extra\_columns:
>         if col in df.columns:
>             ids &\#124;= set\(df\[col\].dropna\(\)\)
>     return sorted\(ids\)

[Source lines 105–106](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L105-L106)

> def cohort\_frame\(result\):
>     return pd.DataFrame\(\{&quot;sample\_id&quot;: result.cohort\_ids}\)

[Source lines 336–349](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L336-L349)

> def write\_all\(result, verdict, store, out\_dir, team=&quot;Cohort Studio team&quot;\):
>     out = pathlib.Path\(out\_dir\)
>     out.mkdir\(parents=True, exist\_ok=True\)
>     cohort\_frame\(result\).to\_csv\(out / &quot;cohort\_samples.csv&quot;, index=False\)
>     \(out / &quot;cohort\_spec.json&quot;\).write\_text\(json.dumps\(result.spec, indent=2\)\)
>     ledger\_frame\(result\).to\_csv\(out / &quot;ledger.csv&quot;, index=False\)
>     exclusions\_frame\(result\).to\_csv\(out / &quot;exclusions.csv&quot;, index=False\)
>     audit\_trail\_frame\(result\).to\_csv\(out / &quot;audit\_trail.csv&quot;, index=False\)
>     selection\_frame\(result\).to\_csv\(out / &quot;sample\_selection.csv&quot;, index=False\)
>     coverage\_frame\(result, store\).to\_csv\(out / &quot;coverage.csv&quot;, index=False\)
>     \(out / &quot;verdict.json&quot;\).write\_text\(json.dumps\(verdict.to\_dict\(\), indent=2\)\)
>     \(out / &quot;reproduce\_cohort.py&quot;\).write\_text\(reproduce\_script\(result, store\)\)
>     \(out / &quot;findings.json&quot;\).write\_text\(json.dumps\(findings\_document\(result, verdict, store, team\), indent=2\)\)
>     return out

[Source lines 237–255](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L237-L255)

>             lines.append\(f&quot;df = join\_table\(df, right, \{PREFIX\[t\]\!r}, \{s\[&\#x27;key&\#x27;\]\!r}, \{s.get\(&\#x27;mode&\#x27;, &\#x27;rows&\#x27;\)\!r}\)&quot;\)
>         elif op == &quot;filter&quot;:
>             col = store.resolve\_field\(s\[&quot;table&quot;\], s\[&quot;field&quot;\]\)
>             if col is None:   \# the file isn&\#x27;t downloaded or has no such column; the verdict already says so
>                 lines.append\(f&quot;raise SystemExit\(\{\(&\#x27;This release has no column for &\#x27; + repr\(s\[&\#x27;field&\#x27;\]\) + &\#x27; in &\#x27; + s\[&\#x27;table&\#x27;\] + &\#x27;; run data/tcga-brca/fetch.py first.&\#x27;\)\!r}\)&quot;\)
>             else:
>                 lines.append\(f&quot;df = filter\_column\(df, \{PREFIX\[s\[&\#x27;table&\#x27;\]\] + &\#x27;.&\#x27; + col\!r}, \{s\[&\#x27;cmp&\#x27;\]\!r}, \{s.get\(&\#x27;value&\#x27;\)\!r}\)&quot;\)
>         elif op == &quot;mutation&quot;:
>             if &quot;mutation&quot; not in loaded:
>                 lines.append\(&quot;mutation = load\_mutation\(DATA\)&quot;\)
>                 loaded.add\(&quot;mutation&quot;\)
>             lines.append\(f&quot;df = filter\_mutation\(df, mutation, \{s\[&\#x27;gene&\#x27;\]\!r}, \{bool\(s.get\(&\#x27;mutated&\#x27;, True\)\)\!r}\)&quot;\)
>         elif op == &quot;dedupe&quot;:
>             lines.append\(&quot;df = one\_row\_per\_sample\(df\)&quot;\)
>         elif op == &quot;where&quot;:
>             names = sorted\(condition\_sources\(s\[&quot;condition&quot;\]\)\)
>             sources = &quot;, &quot;.join\(f&quot;\{n\!r}: load\_\{n}\(DATA\)&quot; for n in names\)
>             tree = resolve\_condition\(s\[&quot;condition&quot;\], store\)
>             lines.append\(f&quot;df = filter\_where\(df, \{tree\!r}, \{\{\{sources}}}, \{s.get\(&\#x27;apply\_to&\#x27;, &\#x27;sample&\#x27;\)\!r}\)&quot;\)

Supplemental rules: None cited; official criterion above applies.

Impact: The artifact set fits the Studio handoff and makes cohort construction more inspectable than a screenshot alone. Unique IDs do not by themselves prove correct inclusion, and the request-docstring issue remains a separate safety defect.

Concrete change: Keep the complete export bundle and bind it to a manifest of input and output hashes. Add exact membership parity checks between the app result and an independently reviewed reconstruction.

Acceptance check: For an authorized synthetic specification, compare the app&\#x27;s sorted unique IDs, CSV and reconstructed IDs exactly. Verify the ledger and specification explain each exclusion and that all bundle files share one run identity.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-6: Useful next steps. Suggested fixes are specific and match the size and importance of the problem.

Status: **observed**

Before/after fix evidence is useful. Strict reproduction and exploratory reruns should have distinguishable provenance and success criteria.

### Reconstruction warns about changed inputs but still writes a cohort

question · P2 · Confidence: High for the warning-and-continue path; whether strict refusal is required is a product-policy question for judges, not an invented organizer rule.

The generated script compares current file hashes with EXPECTED and prints a warning when they differ, then continues to load and transform the data. It writes cohort\_samples.csv and prints the expected count rather than asserting the original membership. This is an intentional-looking permissive path, not a demonstrated numeric failure.

[Source lines 203–214](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L203-L214)

>     for name, rel in used.items\(\):
>         digest = store.file\_status.get\(name, \{}\).get\(&quot;sha256&quot;\)
>         if digest:
>             lines.append\(f&quot;    \{rel\!r}: \{digest\!r},&quot;\)
>     lines += \[
>         &quot;}&quot;,
>         &quot;for rel, digest in EXPECTED.items\(\):&quot;,
>         &quot;    if \_sha256\(DATA / rel\) \!= digest:&quot;,
>         &quot;        print\(f&\#x27;WARNING: \{rel} differs from the file this cohort was built from&\#x27;\)&quot;,
>         &quot;&quot;,
>         &quot;df = load\_manifest\(DATA\)&quot;,
>         &quot;print\(f&\#x27;Start: \{len\(df\)} rows, \{df.sample\_id.nunique\(\)} samples&\#x27;\)&quot;,

[Source lines 267–275](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L267-L275)

>         lines.append\(f&quot;print\(f&\#x27;Step \{i}: \{\{len\(df\)}} rows, \{\{df.sample\_id.nunique\(\)}} samples, \{\{df.patient\_id.nunique\(\)}} patients&\#x27;\)&quot;\)
>     lines += \[
>         &quot;&quot;,
>         f&quot;ids = cohort\_sample\_ids\(df, \{extra\_cohort\_columns\(spec\)\!r}\)&quot;,
>         &quot;pd.DataFrame\(\{&\#x27;sample\_id&\#x27;: ids}\).to\_csv\(OUT, index=False\)&quot;,
>         f&quot;print\(f&\#x27;Wrote \{\{len\(ids\)}} samples to \{\{OUT}} \(expected \{len\(result.cohort\_ids\)}\)&\#x27;\)&quot;,
>         &quot;&quot;,
>     \]
>     return &quot;\\n&quot;.join\(lines\)

Supplemental rules: None cited; official criterion above applies.

Impact: A usable exploratory rerun on new data is different from a faithful reconstruction of the reviewed cohort. Without a distinct mode or failure state, a reader may mistake a warning-bearing new cohort for a verified reproduction.

Concrete change: Decide and document the contract. A strict reproduction mode should stop on hash mismatch and compare membership or an output digest; an exploratory mode can continue but must produce a clearly labeled new run with changed-input provenance.

Acceptance check: Change one synthetic input after export. Confirm strict reconstruction refuses to certify the old cohort, while any permitted exploratory run has a new identity and cannot silently replace the original reproduction result.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-7: Communication. Someone without specialist knowledge can understand the result and next step.

Status: **not_tested**

Rows, distinct samples, patients, proposed fixes and approval states must remain plain-language distinctions. Accessibility and unguided usability are untested.

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
- evals/expected/any\_slide\_cnv.csv: non-allowlisted file type
- evals/expected/basal\_er\_neg.csv: non-allowlisted file type
- evals/expected/basal\_over60.csv: non-allowlisted file type
- evals/expected/brief\_demo.csv: non-allowlisted file type
- evals/expected/cdh1\_lobular\_frozen\_opp.csv: non-allowlisted file type
- evals/expected/died\_dx.csv: non-allowlisted file type
- evals/expected/earliest\_pt\_met.csv: non-allowlisted file type
- evals/expected/early\_under40.csv: non-allowlisted file type
- evals/expected/er\_pos\_by\_patient.csv: non-allowlisted file type
- evals/expected/er\_pos\_her2\_neg.csv: non-allowlisted file type
- evals/expected/er\_pos\_nature2012.csv: non-allowlisted file type
- evals/expected/every\_sample\_dx.csv: non-allowlisted file type
- evals/expected/frozen\_slide.csv: non-allowlisted file type
- evals/expected/her2\_enriched.csv: non-allowlisted file type
- evals/expected/her2\_ihc.csv: non-allowlisted file type
- evals/expected/her2\_low.csv: non-allowlisted file type
- evals/expected/latest\_any.csv: non-allowlisted file type
- evals/expected/lobular\_50plus.csv: non-allowlisted file type
- evals/expected/lobular\_anyslide\_no\_mets.csv: non-allowlisted file type
- evals/expected/luminal\_a\_or\_b\_protein.csv: non-allowlisted file type
- evals/expected/male.csv: non-allowlisted file type
- evals/expected/matched\_normal.csv: non-allowlisted file type
- evals/expected/met\_protein.csv: non-allowlisted file type
- evals/expected/normal\_rna.csv: non-allowlisted file type
- evals/expected/opp\_all\_rna.csv: non-allowlisted file type
- evals/expected/os\_5yr\_or\_death.csv: non-allowlisted file type
- evals/expected/p\_brief\_demo.csv: non-allowlisted file type
- evals/expected/p\_died\_dx.csv: non-allowlisted file type
- evals/expected/p\_earliest\_pt\_met.csv: non-allowlisted file type
- evals/expected/p\_er\_pos\_her2\_neg.csv: non-allowlisted file type
- evals/expected/p\_her2\_ihc.csv: non-allowlisted file type
- evals/expected/p\_lobular\_50plus.csv: non-allowlisted file type
- evals/expected/p\_matched\_normal.csv: non-allowlisted file type
- evals/expected/p\_opp\_all\_rna.csv: non-allowlisted file type
- evals/expected/p\_tn\_pairs.csv: non-allowlisted file type
- evals/expected/p\_tnbc\_rna.csv: non-allowlisted file type
- evals/expected/pam50\_called\_dx.csv: non-allowlisted file type
- evals/expected/pik3ca\_wt\_er\_pos.csv: non-allowlisted file type
- evals/expected/postmeno\_ductal\_rna.csv: non-allowlisted file type
- evals/expected/pr\_neg\_cnv.csv: non-allowlisted file type
- evals/expected/pt\_met\_protein.csv: non-allowlisted file type
- evals/expected/stage2\_surv\_by\_patient.csv: non-allowlisted file type
- evals/expected/stage34\_os.csv: non-allowlisted file type
- evals/expected/tn\_pairs.csv: non-allowlisted file type
- evals/expected/tnbc\_rna.csv: non-allowlisted file type
- evals/expected/tp53\_pfi.csv: non-allowlisted file type
- frontend/static/tour/build-ask-dark.jpg: non-allowlisted file type
- frontend/static/tour/build-ask-dark.mp4: file-size limit
- frontend/static/tour/build-ask.jpg: non-allowlisted file type
- frontend/static/tour/build-ask.mp3: non-allowlisted file type
- frontend/static/tour/build-ask.mp4: file-size limit
- frontend/static/tour/build-fix-dark.jpg: non-allowlisted file type
- frontend/static/tour/build-fix-dark.mp4: file-size limit
- frontend/static/tour/build-fix.jpg: non-allowlisted file type
- frontend/static/tour/build-fix.mp3: non-allowlisted file type
- frontend/static/tour/build-fix.mp4: file-size limit
- frontend/static/tour/build-take-dark.jpg: non-allowlisted file type
- frontend/static/tour/build-take-dark.mp4: file-size limit
- frontend/static/tour/build-take.jpg: non-allowlisted file type
- frontend/static/tour/build-take.mp3: non-allowlisted file type
- frontend/static/tour/build-take.mp4: file-size limit
- frontend/static/tour/build-verdict-dark.jpg: non-allowlisted file type
- frontend/static/tour/build-verdict-dark.mp4: file-size limit
- frontend/static/tour/build-verdict.jpg: non-allowlisted file type
- frontend/static/tour/build-verdict.mp3: non-allowlisted file type
- frontend/static/tour/build-verdict.mp4: file-size limit
- frontend/static/tour/canvas-add-dark.jpg: non-allowlisted file type
- frontend/static/tour/canvas-add-dark.mp4: file-size limit
- frontend/static/tour/canvas-add.jpg: non-allowlisted file type
- frontend/static/tour/canvas-add.mp3: non-allowlisted file type
- frontend/static/tour/canvas-add.mp4: file-size limit
- frontend/static/tour/canvas-code-dark.jpg: non-allowlisted file type
- frontend/static/tour/canvas-code-dark.mp4: file-size limit
- frontend/static/tour/canvas-code.jpg: non-allowlisted file type
- frontend/static/tour/canvas-code.mp3: non-allowlisted file type
- frontend/static/tour/canvas-code.mp4: file-size limit
- frontend/static/tour/canvas-fix-dark.jpg: non-allowlisted file type
- frontend/static/tour/canvas-fix-dark.mp4: file-size limit
- frontend/static/tour/canvas-fix.jpg: non-allowlisted file type
- frontend/static/tour/canvas-fix.mp3: non-allowlisted file type
- frontend/static/tour/canvas-fix.mp4: file-size limit
- frontend/static/tour/canvas-lanes-dark.jpg: non-allowlisted file type
- frontend/static/tour/canvas-lanes-dark.mp4: file-size limit
- frontend/static/tour/canvas-lanes.jpg: non-allowlisted file type
- frontend/static/tour/canvas-lanes.mp3: non-allowlisted file type
- frontend/static/tour/canvas-lanes.mp4: file-size limit
- frontend/static/tour/canvas-read-dark.jpg: non-allowlisted file type
- frontend/static/tour/canvas-read-dark.mp4: file-size limit
- frontend/static/tour/canvas-read.jpg: non-allowlisted file type
- frontend/static/tour/canvas-read.mp3: non-allowlisted file type
- frontend/static/tour/canvas-read.mp4: file-size limit
- frontend/static/tour/compare-outcomes-dark.jpg: non-allowlisted file type
- frontend/static/tour/compare-outcomes-dark.mp4: file-size limit
- frontend/static/tour/compare-outcomes.jpg: non-allowlisted file type
- frontend/static/tour/compare-outcomes.mp3: non-allowlisted file type
- frontend/static/tour/compare-outcomes.mp4: file-size limit
- frontend/static/tour/compare-overlap-dark.jpg: non-allowlisted file type
- frontend/static/tour/compare-overlap-dark.mp4: file-size limit
- frontend/static/tour/compare-overlap.jpg: non-allowlisted file type
- frontend/static/tour/compare-overlap.mp3: non-allowlisted file type
- frontend/static/tour/compare-overlap.mp4: file-size limit
- frontend/static/tour/compare-pick-dark.jpg: non-allowlisted file type
- frontend/static/tour/compare-pick-dark.mp4: file-size limit
- frontend/static/tour/compare-pick.jpg: non-allowlisted file type
- frontend/static/tour/compare-pick.mp3: non-allowlisted file type
- frontend/static/tour/compare-pick.mp4: file-size limit
- kickoff/Cancer\_AI\_Lab\_Kickoff.pdf: file-size limit
- products/multimodal-case-room/practice\_cases.csv: non-allowlisted file type
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
