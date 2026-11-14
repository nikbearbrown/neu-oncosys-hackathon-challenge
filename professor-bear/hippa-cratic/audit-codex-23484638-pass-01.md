# Professor Bear Audit: HIPPA-cratic Cohort Studio

## Review Identity

This is an independent, provisional source-code audit for judge deliberation. It is not an official grade.

- Entry: `roh9031/HIPPA-cratic`
- Commit: `9f0ad46f32a1a76af25baf1aa621ab862f991c45`
- Organizer reference: `6e15a399a64ffbf80778db0b462ac239e70086b9`
- Product: `cohort-studio`; Track 1, Cohort Firewall
- Pass: 1; reviewed 2026-11-14T21:27:32.864901+00:00
- Runtime: **not executed**; official freeze/receipt: **not verified**

## Executive Assessment

This is a Cohort Studio, not a release-change Control Tower. Its source supports editable cohort operations, distinct row/sample/patient counts, checks for cross-sample links and inflating joins, carefully differentiated fixes, and a separately translated DuckDB verification path. The main concerns are reproducibility and evidence identity: a generated rebuild records steps without binding the selected release or hashes, a prior SQL success is keyed only to step text, and custom-data activation changes process-wide state. A separate generated-source boundary interpolates request text into a Python docstring. These are source-derived findings, not executed failures. The repository's submission tag matches the inspected main commit; no organizer freeze receipt or claimed test result was independently verified.

## Workflow Traced

The interface collects a request and editable filter/join/collapse steps, reads a sample manifest and selected source tables, runs the deterministic engine and reports rows, unique samples and patients after each operation. It identifies inflation, cross-sample attachments and some missingness/selection traps, proposes replacement step lists, and lets a person choose a fix. The optional AI supplies drafts, not counts. An independent SQL translation can compare final membership and per-step cardinalities. The final section exports unique sample IDs, a definition with fingerprints and a generated rebuild script. Changed-release files can overlay the original data; optional uploaded CSV or Supabase tables use a custom-data folder. The latter mode is additional functionality, not authority to load unapproved clinical inputs during this audit.

## Findings At A Glance

| ID | Type | Priority | Finding |
|---|---|---|---|
| HC-01 | gap | P1 | The rebuild script does not bind the exported cohort's data release |
| HC-02 | gap | P2 | Request text enters generated Python without serialization |
| HC-03 | gap | P1 | A SQL success can remain attached to unchanged steps after data changes |
| HC-04 | gap | P1 | Custom-data selection is process-wide rather than session-local |
| HC-05 | strength | P2 | Join checks distinguish duplicate rows from wrong-sample links |
| HC-06 | strength | P2 | A second execution path compares exact membership and step counts |
| HC-07 | strength | P2 | Fix advice explains when de-duplication leaves the real problem |

## Inspection Scope

The following files informed the implementation-level conclusions in this pass. Other collected files are not automatically treated as reviewed:

- `CLAUDE.md`
- `README.md`
- `app.py`
- `cohort_studio/data.py`
- `cohort_studio/custom.py`
- `cohort_studio/engine.py`
- `cohort_studio/export.py`
- `cohort_studio/advice.py`
- `cohort_studio/sqlcheck.py`
- `cohort_studio/versions.py`
- `cohort_studio/llm.py`
- `run_cohort.py`
- `tests/test_rebuild.py`

## Parallel Review Preservation

No earlier Markdown reports existed in this matching entry folder at the time this pass was prepared.

No earlier report for this matching entry existed when this supplement was prepared. The existing six entries are preserved. The README's 171 passing tests, 31 SQL trap cases, paired-team demonstration and provider evaluation are author-reported evidence only in this pass. No tests, provider calls, raw datasets or answer-bearing trap logs were accessed or run. The extra packet exclusions include docs/TRAP_LOG.md and tests/test_trap_requests.py. The local submission tag was read as a Git reference, not accepted as an organizer attestation.

This pass does not accept earlier agents' findings as established merely because they were reported. Any correction must identify the earlier claim and the new evidence explicitly.

## Detailed Criterion Review

# Judge review aid: hippa-cratic

Repository: https://github.com/roh9031/HIPPA-cratic
Commit: `9f0ad46f32a1a76af25baf1aa621ab862f991c45`
Track: 1
Reviewer: Professor Bear / Codex source review

**Not an official result. Source review does not establish runtime behavior.**

This is a Cohort Studio, not a release-change Control Tower. Its source supports editable cohort operations, distinct row/sample/patient counts, checks for cross-sample links and inflating joins, carefully differentiated fixes, and a separately translated DuckDB verification path. The main concerns are reproducibility and evidence identity: a generated rebuild records steps without binding the selected release or hashes, a prior SQL success is keyed only to step text, and custom-data activation changes process-wide state. A separate generated-source boundary interpolates request text into a Python docstring. These are source-derived findings, not executed failures. The repository&\#x27;s submission tag matches the inspected main commit; no organizer freeze receipt or claimed test result was independently verified.

## Coverage and limitations

Collection: complete_with_exclusions; 39 text files; 6 excluded entries; recursive tree truncated: False.
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

- P1 · T1-3 · The rebuild script does not bind the exported cohort&\#x27;s data release: Generate a rebuild entry point from the complete exported definition. Resolve required table mappings and release overlays explicitly, verify expected content fingerprints before calculation, and record the exact sample membership digest. Make missing or changed inputs an explicit failure unless the user intentionally creates a new version. For custom data, export the registry and a documented way to supply the referenced files without embedding sensitive records.
- P1 · T1-3 · A SQL success can remain attached to unchanged steps after data changes: Bind SQL verification and cohort versions to canonical steps plus resolved data/release identity and input hashes. Clear or mark prior checks historical when those inputs change, including custom-data activation. Keep the old result as history rather than relabelling it as a fresh verification.
- P1 · T1-4 · Custom-data selection is process-wide rather than session-local: Keep an immutable dataset context in each session and pass it explicitly to the engine, loader, SQL verifier and exporter. Avoid changing process environment and shared registries on a browser action. If the prototype supports only one local user, state and enforce that limit rather than implying multi-user isolation.
- P2 · T1-1 · Join checks distinguish duplicate rows from wrong-sample links: Retain these separate checks and the left-join caveat. Keep counts and sample examples attached to the precise step, and demonstrate that a chosen fix removes the relevant problem rather than just its visible duplicates.
- P2 · T1-2 · A second execution path compares exact membership and step counts: Preserve the query and exact-set comparison, and bind its result to the input identity as in HC-03. Assert matching step counts before pairing them and keep independently designed expected cohort cases separate from compiler agreement.
- P2 · T1-4 · Request text enters generated Python without serialization: Serialize the request as a Python literal or JSON data and keep it outside source delimiters. Generate source through fixed templates with data encoded separately, then parse the result before offering it. Apply the same boundary discipline to all user-controlled fields included in executable exports.
- P2 · T1-6 · Fix advice explains when de-duplication leaves the real problem: Keep the causal explanation of each fix and the explicit judgment boundary. Ensure diagnostic exports preserve unresolved status and the user&\#x27;s override in a machine-readable companion, rather than relying only on a transient checkbox.

## T1-1: Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support.

Status: **observed**

Source supports per-step inflation, cross-sample and some missingness/selection checks. Author-reported test counts are not independently observed accuracy, and answer-bearing trap material was excluded.

### Join checks distinguish duplicate rows from wrong-sample links

strength · P2 · Confidence: High for the source paths; numerical results and the author&\#x27;s demonstration were not rerun.

The engine records row/sample/patient counts at each step and checks both increases in repeated sample rows and patient-key joins attaching another sample&\#x27;s record. Semi/anti joins also warn when membership is obtained only through a different sample, unless an explicit constrained allow\_cross\_sample policy applies. The inflation fix offers a semi-join only for inner joins; it avoids silently dropping unmatched samples from a left join. These are distinct checks rather than a generic row-count warning.

[Source lines 440–465](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/engine.py#L440-L465)

>     if how in \(&quot;semi&quot;, &quot;anti&quot;\):
>         hit = df\[on\].isin\(right\[on\]\)
>         out = df\[hit\] if how == &quot;semi&quot; else df\[~hit\]
>         if on == &quot;patient\_id&quot; and not allow\_cross\_sample and &quot;sample\_id&quot; in right.columns:
>             by\_sample = df\[&quot;sample\_id&quot;\].isin\(right\[&quot;sample\_id&quot;\]\)
>             only\_via\_patient = df\[hit &amp; ~by\_sample\]
>             if len\(only\_via\_patient\):
>                 if how == &quot;semi&quot;:
>                     message = \(
>                         f&quot;\{only\_via\_patient\[&\#x27;sample\_id&\#x27;\].nunique\(\)} samples were kept only because a \*different\* &quot;
>                         f&quot;sample of the same patient has a matching \{table} record \(e.g. a normal-tissue slide\). &quot;
>                         &quot;Records should link to a sample only when the sample barcode matches.&quot;
>                     \)
>                 else:
>                     message = \(
>                         f&quot;\{only\_via\_patient\[&\#x27;sample\_id&\#x27;\].nunique\(\)} samples were excluded only because a \*different\* &quot;
>                         f&quot;sample of the same patient has a matching \{table} record. &quot;
>                         &quot;Records should link to a sample only when the sample barcode matches.&quot;
>                     \)
>                 warns.append\(Warning\_\(
>                     &quot;cross\_sample&quot;, &quot;problem&quot;,
>                     message,
>                     examples=only\_via\_patient\[\[&quot;sample\_id&quot;, &quot;patient\_id&quot;\]\].head\(10\).to\_dict\(&quot;records&quot;\),
>                     fixes=\[\{&quot;label&quot;: &quot;Match on sample\_id instead of patient\_id&quot;,
>                             &quot;steps&quot;: \_with\_step\(steps, i, on=&quot;sample\_id&quot;\)}\],
>                 \)\)

[Source lines 468–483](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/engine.py#L468-L483)

>     right = \_prepare\_right\(df, right, table, on\)
>     out = df.merge\(right, on=on, how=how\)
>     if on == &quot;patient\_id&quot; and not allow\_cross\_sample:
>         other = f&quot;sample\_id\_\_\{table}&quot;
>         if other in out.columns:
>             bad = out\[out\[other\].notna\(\) &amp; \(out\[other\] \!= out\[&quot;sample\_id&quot;\]\)\]
>             if len\(bad\):
>                 warns.append\(Warning\_\(
>                     &quot;cross\_sample&quot;, &quot;problem&quot;,
>                     f&quot;\{len\(bad\)} joined rows attach a \{table} record from a \*different sample\* of the same &quot;
>                     f&quot;patient \(for example a normal-tissue record on a tumor sample\). &quot;
>                     f&quot;Join on sample\_id so each record belongs to the sample it describes.&quot;,
>                     examples=bad\[\[&quot;sample\_id&quot;, other\]\].head\(10\).to\_dict\(&quot;records&quot;\),
>                     fixes=\[\{&quot;label&quot;: &quot;Join on sample\_id instead of patient\_id&quot;,
>                             &quot;steps&quot;: \_with\_step\(steps, i, on=&quot;sample\_id&quot;\)}\],
>                 \)\)

[Source lines 508–530](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/engine.py#L508-L530)

> def \_inflation\_check\(before, after, step, i, steps\) -&gt; list\[Warning\_\]:
>     extra\_before = len\(before\) - before\[&quot;sample\_id&quot;\].nunique\(\)
>     extra\_after = len\(after\) - after\[&quot;sample\_id&quot;\].nunique\(\)
>     if extra\_after &lt;= extra\_before:
>         return \[\]
>     vc = after\[&quot;sample\_id&quot;\].value\_counts\(\)
>     dup = vc\[vc &gt; 1\]
>     fixes = \[\]
>     if step\[&quot;op&quot;\] == &quot;join&quot;:
>         \# A semi-join only keeps samples that have a match. That&\#x27;s the same cohort as an inner join, but for a
>         \# left join it would silently drop samples with no match, so only offer it for inner joins.
>         if step.get\(&quot;how&quot;, &quot;inner&quot;\) == &quot;inner&quot;:
>             fixes.append\(\{&quot;label&quot;: &quot;Keep each sample once if it has a match \(semi-join\)&quot;,
>                           &quot;steps&quot;: \_with\_step\(steps, i, how=&quot;semi&quot;\)}\)
>         fixes.append\(\{&quot;label&quot;: &quot;Keep the joined columns, then collapse to one row per sample&quot;,
>                       &quot;steps&quot;: \_insert\_after\(steps, i, \{&quot;op&quot;: &quot;collapse&quot;, &quot;level&quot;: &quot;sample&quot;}\)}\)
>     return \[Warning\_\(
>         &quot;inflation&quot;, &quot;problem&quot;,
>         f&quot;Rows grew faster than samples: \{len\(after\):,} rows but only \{after\[&\#x27;sample\_id&\#x27;\].nunique\(\):,} distinct &quot;
>         f&quot;samples. \{len\(dup\):,} samples now appear more than once \(up to \{int\(dup.max\(\)\)}x\), so counting rows &quot;
>         f&quot;here overstates the cohort by \{extra\_after:,}.&quot;,
>         examples=\[\{&quot;sample\_id&quot;: s, &quot;rows&quot;: int\(n\)} for s, n in dup.head\(10\).items\(\)\],
>         fixes=fixes,

Supplemental rules: None cited; official criterion above applies.

Impact: This directly supports the Cohort Studio task: a superficially correct unique sample count cannot by itself establish that the joined records belong to those samples. Separate findings and fixes help a researcher understand the actual identity error.

Concrete change: Retain these separate checks and the left-join caveat. Keep counts and sample examples attached to the precise step, and demonstrate that a chosen fix removes the relevant problem rather than just its visible duplicates.

Acceptance check: With invented patients having tumor/normal specimens and multiple slides, compare inner, left, semi and anti joins on sample versus patient IDs. Show row inflation, wrong-sample membership and an explicit patient-level existence policy separately. Confirm a valid sample-key control remains quiet.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-2: Reasoning for the research question. Changes its result appropriately when the research question or intended use changes.

Status: **observed**

Editable steps, explicit join policies and SQL comparison support question-aware reasoning. Agreement between two executions does not prove the steps match a natural-language request.

### A second execution path compares exact membership and step counts

strength · P2 · Confidence: High for the separate SQL construction and comparisons; no DuckDB or student test was executed.

The SQL verifier builds DuckDB views from resolved source files and translates the cohort steps into SQL rather than reusing the pandas output. verify compares final sample-ID sets and row/sample/patient counts at every paired step, returning differences and the query. The app explicitly says this checks execution of the steps, not whether those steps express the research question. Shared file resolution and policy assumptions still limit the independence of the check.

[Source lines 24–45](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/sqlcheck.py#L24-L45)

>     if data.is\_custom\(ddir\):                  \# the user&\#x27;s own tables \(custom.py\): one plain view per CSV
>         con = duckdb.connect\(\)
>         con.sql\(f&quot;CREATE VIEW samples AS SELECT \* FROM read\_csv\(\{\_lit\(data.file\_path\(data.BASE\_FILE, ddir\).as\_posix\(\)\)}\)&quot;\)
>         for name, meta in data.TABLES.items\(\):
>             if name \!= &quot;samples&quot;:
>                 con.sql\(f&quot;CREATE VIEW \{\_q\(name\)} AS SELECT \* FROM read\_csv\(&quot;
>                         f&quot;\{\_lit\(data.file\_path\(meta\[&\#x27;file&\#x27;\], ddir\).as\_posix\(\)\)}\)&quot;\)
>         return con
> 
>     \# Only \*which\* file to read comes from data.py \(so a chosen release is used, see data.file\_path\); the
>     \# reading itself is DuckDB&\#x27;s, independent of the engine&\#x27;s loaders.
>     f = \{rel: data.file\_path\(rel, ddir\).as\_posix\(\) for rel in
>          \(&quot;sample\_manifest.csv&quot;, &quot;slide\_manifest.csv&quot;, &quot;raw/survival.tsv&quot;, &quot;raw/clinical.tsv&quot;,
>           &quot;raw/mutation\_gene\_level.tsv.gz&quot;\)}
>     con = duckdb.connect\(\)
>     con.sql\(f&quot;CREATE VIEW samples  AS SELECT \* FROM read\_csv\(\{\_lit\(f\[&\#x27;sample\_manifest.csv&\#x27;\]\)}\)&quot;\)
>     con.sql\(f&quot;CREATE VIEW slides   AS SELECT \* FROM read\_csv\(\{\_lit\(f\[&\#x27;slide\_manifest.csv&\#x27;\]\)}\)&quot;\)
>     con.sql\(f&quot;CREATE VIEW survival AS SELECT sample AS sample\_id, \_PATIENT AS patient\_id, \* &quot;
>             f&quot;FROM read\_csv\(\{\_lit\(f\[&\#x27;raw/survival.tsv&\#x27;\]\)}, delim=&\#x27;\\t&\#x27;\)&quot;\)
>     \# clinical.tsv&\#x27;s own patient\_id is a 4-char suffix; the real key is the sample barcode.
>     con.sql\(f&quot;CREATE VIEW clinical AS SELECT sampleID AS sample\_id, left\(sampleID, 12\) AS patient\_id, &quot;
>             f&quot;\* EXCLUDE \(patient\_id\) FROM read\_csv\(\{\_lit\(f\[&\#x27;raw/clinical.tsv&\#x27;\]\)}, delim=&\#x27;\\t&\#x27;, all\_varchar=true\)&quot;\)

[Source lines 218–234](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/sqlcheck.py#L218-L234)

> def verify\(steps: list\[dict\], engine\_df, results, ddir: str &\#124; None = None\) -&gt; dict:
>     &quot;&quot;&quot;Run the SQL version and compare it with the engine, step by step and sample by sample.&quot;&quot;&quot;
>     con = connect\(ddir\)
>     try:
>         con.sql\(&quot;SET threads TO 1&quot;\)  \# keeps row\_number\(\) OVER \(\) in file order, for patient-level collapse
>         sql = steps\_to\_sql\(steps, con\)
>         ids = \{r\[0\] for r in con.sql\(sql\).fetchall\(\)}
>         counts = con.sql\(\_counts\_sql\(steps, con\)\).fetchall\(\)
>     finally:
>         con.close\(\)
>     eng\_ids = set\(engine\_df\[&quot;sample\_id&quot;\]\)
>     by\_step = \[\{&quot;step&quot;: r.index, &quot;engine rows&quot;: r.rows, &quot;SQL rows&quot;: c\[1\], &quot;engine samples&quot;: r.samples,
>                 &quot;SQL samples&quot;: c\[2\], &quot;match&quot;: &quot;✅&quot; if \(r.rows, r.samples, r.patients\) == tuple\(c\[1:\]\) else &quot;❌&quot;}
>                for r, c in zip\(results, counts\)\]
>     return \{&quot;sql&quot;: sql, &quot;by\_step&quot;: by\_step, &quot;sql\_samples&quot;: len\(ids\), &quot;engine\_samples&quot;: len\(eng\_ids\),
>             &quot;only\_engine&quot;: sorted\(eng\_ids - ids\), &quot;only\_sql&quot;: sorted\(ids - eng\_ids\),
>             &quot;match&quot;: ids == eng\_ids and all\(b\[&quot;match&quot;\] == &quot;✅&quot; for b in by\_step\)}

[Source lines 430–444](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L430-L444)

>             if v\[&quot;match&quot;\]:
>                 st.success\(f&quot;✅ \*\*Match.\*\* Engine: \*\*\{v\[&\#x27;engine\_samples&\#x27;\]:,}\*\* samples · independent SQL: &quot;
>                            f&quot;\*\*\{v\[&\#x27;sql\_samples&\#x27;\]:,}\*\* samples. Same sample IDs, and the same rows, samples and &quot;
>                            f&quot;patients after every step.&quot;\)
>                 if problems:
>                     st.warning\(&quot;Both agree on the numbers, \*\*including the problems flagged above\*\*. &quot;
>                                &quot;Apply a fix first, then verify again.&quot;\)
>             else:
>                 st.error\(f&quot;❌ \*\*Mismatch.\*\* Engine: \{v\[&\#x27;engine\_samples&\#x27;\]:,} samples · SQL: \{v\[&\#x27;sql\_samples&\#x27;\]:,}. &quot;
>                          f&quot;Don&\#x27;t use this cohort until someone finds out why.&quot;\)
>                 if v\[&quot;only\_engine&quot;\] or v\[&quot;only\_sql&quot;\]:
>                     st.write\(&quot;Only in the engine:&quot;, v\[&quot;only\_engine&quot;\]\[:20\], &quot;Only in SQL:&quot;, v\[&quot;only\_sql&quot;\]\[:20\]\)
>             st.dataframe\(pd.DataFrame\(v\[&quot;by\_step&quot;\]\), hide\_index=True\)
>             st.caption\(&quot;This checks that the steps were \*carried out\* correctly. It can&\#x27;t tell you whether the &quot;
>                        &quot;steps match your research question: that&\#x27;s the human review below.&quot;\)

Supplemental rules: None cited; official criterion above applies.

Impact: A matching final count can conceal swapped membership or intermediate inflation. Exact membership plus per-step comparisons gives a much more useful execution cross-check, while the explicit semantic limitation leaves the research decision with a person.

Concrete change: Preserve the query and exact-set comparison, and bind its result to the input identity as in HC-03. Assert matching step counts before pairing them and keep independently designed expected cohort cases separate from compiler agreement.

Acceptance check: Inject an invented translation/execution discrepancy that preserves the total number of samples but changes one ID; verify the set mismatch is reported. Exercise an intermediate duplicate-row difference with the same final cohort. Confirm an agreed result still requires human review of intended meaning.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-3: Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion.

Status: **observed**

Definitions contain input fingerprints and exact SQL membership comparison is implemented. The rebuild and live verification identities do not consistently bind those inputs; HC-01 and HC-03 are priority follow-ups.

### The rebuild script does not bind the exported cohort&\#x27;s data release

gap · P1 · Confidence: High for the missing binding in the complete generated script; the resulting runtime membership depends on the data and execution environment and was not exercised.

cohort\_definition records data\_dir, release and input\_sha256, but rebuild\_script accepts only steps and request and emits run\(STEPS\) without the recorded location, release or expected hashes. That call resolves data through the new process&\#x27;s environment and defaults. A colleague running the script in a fresh shell can therefore use the original release rather than the changed release used for export, or lack the custom table registry entirely. The existing rebuild tests inherit the current environment and exercise two fixed default-data examples; their definitions do not establish changed-release or custom-data reconstruction. This is a source-derived reproduction gap, not an observed membership mismatch.

[Source lines 21–33](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/export.py#L21-L33)

> def cohort\_definition\(steps, request: str, results\) -&gt; dict:
>     return \{
>         &quot;tool&quot;: TOOL,
>         &quot;version&quot;: VERSION,
>         &quot;created&quot;: dt.datetime.now\(dt.timezone.utc\).isoformat\(timespec=&quot;seconds&quot;\),
>         &quot;request&quot;: request,
>         &quot;data\_dir&quot;: str\(data.data\_dir\(\)\),
>         &quot;release&quot;: str\(data.release\_dir\(\)\) if data.release\_dir\(\) else None,   \# changed raw files, if any
>         &quot;input\_sha256&quot;: data.file\_fingerprints\(\),
>         &quot;steps&quot;: steps,
>         &quot;funnel&quot;: \[\{&quot;step&quot;: r.index, &quot;label&quot;: r.label, &quot;rows&quot;: r.rows, &quot;samples&quot;: r.samples,
>                     &quot;patients&quot;: r.patients} for r in results\],
>     }

[Source lines 36–55](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/export.py#L36-L55)

> def rebuild\_script\(steps, request: str\) -&gt; str:
>     steps\_json = json.dumps\(steps, indent=2\)
>     return f&\#x27;&\#x27;&\#x27;&quot;&quot;&quot;Rebuild a cohort exported by \{TOOL} \{VERSION}.
> 
> Request: \{request or &quot;\(none given\)&quot;}
> 
> Save this file in the cohort-studio repo root and run:
>     python rebuild\_cohort.py
> It writes cohort\_samples.csv and prints the step-by-step funnel.
> &quot;&quot;&quot;
> import json, sys, pathlib
> sys.path.insert\(0, str\(pathlib.Path\(\_\_file\_\_\).resolve\(\).parent\)\)
> from cohort\_studio.engine import run, unresolved\_problems
> from cohort\_studio.export import cohort\_samples
> 
> STEPS = json.loads\(r&quot;&quot;&quot;
> \{steps\_json}
> &quot;&quot;&quot;\)
> 
> df, results = run\(STEPS\)

[Source lines 82–101](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/data.py#L82-L101)

> def location\(ddir: str &\#124; Path &\#124; None = None\) -&gt; Path:
>     &quot;&quot;&quot;The folder data is read from: a data folder, or a release folder of changed raw files.&quot;&quot;&quot;
>     if ddir:
>         return Path\(ddir\).expanduser\(\).resolve\(\)
>     base = \_configured\_base\(\)
>     rel = os.environ.get\(&quot;ONCOSYS\_RELEASE&quot;, &quot;&quot;\).strip\(\)
>     if rel:
>         r = Path\(rel\).expanduser\(\)
>         if not r.exists\(\):
>             r = \_split\(base\)\[0\] / &quot;releases&quot; / rel
>         return r.resolve\(\)
>     return base
> 
> 
> def data\_dir\(ddir: str &\#124; Path &\#124; None = None\) -&gt; Path:
>     return \_split\(location\(ddir\)\)\[0\]
> 
> 
> def release\_dir\(ddir: str &\#124; Path &\#124; None = None\) -&gt; Path &\#124; None:
>     return \_split\(location\(ddir\)\)\[1\]

[Source lines 32–47](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/tests/test_rebuild.py#L32-L47)

> @pytest.mark.parametrize\(&quot;name,steps,n&quot;, \[\(&quot;demo&quot;, \_fixed\_demo\(\), 731\), \(&quot;survival\_trap&quot;, \_fixed\_survival\_trap\(\), 807\)\]\)
> def test\_rebuild\_script\_reproduces\_export\(tmp\_path, name, steps, n\):
>     df, \_ = run\(steps\)
>     expected = cohort\_samples\(df\)
> 
>     script = tmp\_path / &quot;rebuild\_cohort.py&quot;
>     script.write\_text\(rebuild\_script\(steps, f&quot;test \{name}&quot;\), encoding=&quot;utf-8&quot;\)
>     env = \{\*\*os.environ, &quot;PYTHONPATH&quot;: str\(ROOT\), &quot;PYTHONIOENCODING&quot;: &quot;utf-8&quot;}
>     proc = subprocess.run\(\[sys.executable, str\(script\)\], cwd=tmp\_path, env=env,
>                           capture\_output=True, text=True, encoding=&quot;utf-8&quot;, timeout=120\)
>     assert proc.returncode == 0, proc.stderr\[-2000:\]
> 
>     rebuilt = pd.read\_csv\(tmp\_path / &quot;cohort\_samples.csv&quot;\)
>     assert len\(rebuilt\) == n
>     assert list\(rebuilt\[&quot;sample\_id&quot;\]\) == list\(expected\[&quot;sample\_id&quot;\]\)
>     assert rebuilt.equals\(expected.reset\_index\(drop=True\)\)

Supplemental rules: None cited; official criterion above applies.

Impact: The organizer product requires a script or notebook that reproduces the exported cohort exactly. The separate JSON definition is useful provenance, but it does not make a standalone script consume the same bytes. An apparently successful rerun can construct a different cohort without first establishing input equivalence.

Concrete change: Generate a rebuild entry point from the complete exported definition. Resolve required table mappings and release overlays explicitly, verify expected content fingerprints before calculation, and record the exact sample membership digest. Make missing or changed inputs an explicit failure unless the user intentionally creates a new version. For custom data, export the registry and a documented way to supply the referenced files without embedding sensitive records.

Acceptance check: Using invented data, export from a changed release and from a custom-data folder. Start a clean process with release/data environment variables absent and different defaults present. The script must either select the recorded inputs and reproduce exact sample IDs or fail with a precise missing/version-mismatch reason. Keep an unchanged default-data positive control and compare IDs, not just row counts.

### A SQL success can remain attached to unchanged steps after data changes

gap · P1 · Confidence: High for the inspected session-state and key logic; no live Streamlit session was run.

run\_sql\_check saves its result in session state with only ss.steps\_text. The display accepts that result whenever the step text still matches. Release selection changes a process environment variable, clears Streamlit data caches and reruns, but does not clear this session-state verification record. The engine recomputes its current result, while the old SQL result can still be presented as Match for the same steps. The session&\#x27;s version history similarly uses only serialized steps as its key and returns the prior record immediately when those steps are unchanged. No current dataset fingerprint participates in either identity check.

[Source lines 95–103](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L95-L103)

>         wanted = None if pick == options\[0\] else pick
>         if wanted \!= \(None if not current else \(current.name if current.name in releases else str\(current\)\)\):
>             if wanted:
>                 os.environ\[&quot;ONCOSYS\_RELEASE&quot;\] = wanted
>             else:
>                 os.environ.pop\(&quot;ONCOSYS\_RELEASE&quot;, None\)
>             st.cache\_data.clear\(\)
>             st.rerun\(\)
>     status = data.check\_data\(str\(data.location\(\)\)\)

[Source lines 408–425](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L408-L425)

> def run\_sql\_check\(\):
>     try:
>         from cohort\_studio.sqlcheck import verify
>         ss.sql\_check = \(ss.steps\_text, verify\(steps, df, results\)\)
>     except ImportError:
>         ss.sql\_check = \(ss.steps\_text, \{&quot;error&quot;: &quot;DuckDB isn&\#x27;t installed: run \`pip install -r requirements.txt\`.&quot;}\)
>     except Exception as e:  \# show what DuckDB said rather than crash the page
>         ss.sql\_check = \(ss.steps\_text, \{&quot;error&quot;: f&quot;The SQL version couldn&\#x27;t run: \{e}&quot;}\)
> 
> 
> with st.container\(border=True\):
>     v1, v2 = st.columns\(\[3, 1\]\)
>     v1.markdown\(&quot;\*\*Independent check.\*\* Rebuild this cohort a second way: the same steps written as one &quot;
>                 &quot;DuckDB SQL query over the raw files, without the app&\#x27;s engine. Both should give the same samples.&quot;\)
>     v2.button\(&quot;🔎 Verify with SQL&quot;, on\_click=run\_sql\_check, width=&quot;stretch&quot;,
>               disabled=any\(r.error for r in results\)\)
>     chk = ss.get\(&quot;sql\_check&quot;\)
>     if chk and chk\[0\] == ss.steps\_text:

[Source lines 430–449](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L430-L449)

>             if v\[&quot;match&quot;\]:
>                 st.success\(f&quot;✅ \*\*Match.\*\* Engine: \*\*\{v\[&\#x27;engine\_samples&\#x27;\]:,}\*\* samples · independent SQL: &quot;
>                            f&quot;\*\*\{v\[&\#x27;sql\_samples&\#x27;\]:,}\*\* samples. Same sample IDs, and the same rows, samples and &quot;
>                            f&quot;patients after every step.&quot;\)
>                 if problems:
>                     st.warning\(&quot;Both agree on the numbers, \*\*including the problems flagged above\*\*. &quot;
>                                &quot;Apply a fix first, then verify again.&quot;\)
>             else:
>                 st.error\(f&quot;❌ \*\*Mismatch.\*\* Engine: \{v\[&\#x27;engine\_samples&\#x27;\]:,} samples · SQL: \{v\[&\#x27;sql\_samples&\#x27;\]:,}. &quot;
>                          f&quot;Don&\#x27;t use this cohort until someone finds out why.&quot;\)
>                 if v\[&quot;only\_engine&quot;\] or v\[&quot;only\_sql&quot;\]:
>                     st.write\(&quot;Only in the engine:&quot;, v\[&quot;only\_engine&quot;\]\[:20\], &quot;Only in SQL:&quot;, v\[&quot;only\_sql&quot;\]\[:20\]\)
>             st.dataframe\(pd.DataFrame\(v\[&quot;by\_step&quot;\]\), hide\_index=True\)
>             st.caption\(&quot;This checks that the steps were \*carried out\* correctly. It can&\#x27;t tell you whether the &quot;
>                        &quot;steps match your research question: that&\#x27;s the human review below.&quot;\)
>             with st.expander\(&quot;Show the SQL \(copy it, or download and run \`python scripts/sql.py -f cohort.sql\`\)&quot;\):
>                 st.code\(v\[&quot;sql&quot;\], language=&quot;sql&quot;\)
>                 st.download\_button\(&quot;cohort.sql&quot;, v\[&quot;sql&quot;\], &quot;cohort.sql&quot;, &quot;text/plain&quot;\)
>     elif chk:
>         st.caption\(&quot;The steps changed since the last check. Click \*\*Verify with SQL\*\* again.&quot;\)

[Source lines 33–49](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/versions.py#L33-L49)

> def record\(steps: list\[dict\], df: pd.DataFrame\) -&gt; list\[dict\]:
>     &quot;&quot;&quot;Remember this cohort if the steps changed. Returns every version, newest first.&quot;&quot;&quot;
>     ss = st.session\_state
>     history: list\[dict\] = ss.get\(&quot;versions&quot;, \[\]\)
>     key = json.dumps\(steps, sort\_keys=True\)
>     if history and history\[0\]\[&quot;key&quot;\] == key:
>         return history
> 
>     samples = sorted\(df\[&quot;sample\_id&quot;\].astype\(str\).unique\(\)\)
>     n = ss.get\(&quot;version\_counter&quot;, 0\) + 1
>     ss.version\_counter = n
>     version = \{&quot;key&quot;: key, &quot;n&quot;: n, &quot;steps&quot;: steps, &quot;samples&quot;: samples,
>                &quot;rows&quot;: len\(df\), &quot;patients&quot;: df\[&quot;patient\_id&quot;\].nunique\(\),
>                &quot;label&quot;: \_label\(n, steps, len\(samples\), len\(df\)\)}
>     \# An earlier identical cohort is dropped, so the list reads as the distinct cohorts tried.
>     history = \[version\] + \[h for h in history if h\[&quot;key&quot;\] \!= key\]
>     ss.versions = history\[:MAX\_VERSIONS\]

Supplemental rules: None cited; official criterion above applies.

Impact: An independent computation is valuable only for the inputs it actually checked. A stored green success can mislead a user after a release switch, even if the engine itself loads the new path correctly. Historical membership comparison can likewise describe an earlier dataset while the current table has changed.

Concrete change: Bind SQL verification and cohort versions to canonical steps plus resolved data/release identity and input hashes. Clear or mark prior checks historical when those inputs change, including custom-data activation. Keep the old result as history rather than relabelling it as a fresh verification.

Acceptance check: Verify an invented release A, switch to release B with the same steps but different eligible membership, and confirm the old Match is withdrawn until a new SQL run completes. Inspect the stored version IDs and membership. Repeat a same-path content change and an unchanged-input control. Preserve the existing per-step/final-membership comparison.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-4: Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review.

Status: **observed**

Human-review notices, error states and an unresolved-export acknowledgment are visible in source. Generated-source serialization and process-global dataset selection need controlled checks. No privacy incident, clinical validity or production suitability is established.

### Request text enters generated Python without serialization

gap · P2 · Confidence: High for direct unescaped interpolation; no generated-source execution or exploit was attempted.

rebuild\_script inserts the raw request into an opening triple-quoted Python docstring. A request containing the closing delimiter can terminate that string, producing invalid syntax or additional source text in the downloaded script. The app passes its editable request directly into this generator. The inspected route downloads source; it does not itself execute the generated script, so this is not evidence of automatic server execution or a demonstrated compromise.

[Source lines 36–53](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/export.py#L36-L53)

> def rebuild\_script\(steps, request: str\) -&gt; str:
>     steps\_json = json.dumps\(steps, indent=2\)
>     return f&\#x27;&\#x27;&\#x27;&quot;&quot;&quot;Rebuild a cohort exported by \{TOOL} \{VERSION}.
> 
> Request: \{request or &quot;\(none given\)&quot;}
> 
> Save this file in the cohort-studio repo root and run:
>     python rebuild\_cohort.py
> It writes cohort\_samples.csv and prints the step-by-step funnel.
> &quot;&quot;&quot;
> import json, sys, pathlib
> sys.path.insert\(0, str\(pathlib.Path\(\_\_file\_\_\).resolve\(\).parent\)\)
> from cohort\_studio.engine import run, unresolved\_problems
> from cohort\_studio.export import cohort\_samples
> 
> STEPS = json.loads\(r&quot;&quot;&quot;
> \{steps\_json}
> &quot;&quot;&quot;\)

[Source lines 458–466](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L458-L466)

> out = export.cohort\_samples\(df\)
> defn = export.cohort\_definition\(steps, ss.request, results\)
> e1, e2, e3 = st.columns\(3\)
> e1.download\_button\(&quot;cohort\_samples.csv&quot;, out.to\_csv\(index=False\), &quot;cohort\_samples.csv&quot;, &quot;text/csv&quot;,
>                    disabled=not ok, width=&quot;stretch&quot;\)
> e2.download\_button\(&quot;cohort.json \(definition + funnel\)&quot;, json.dumps\(defn, indent=2\), &quot;cohort.json&quot;,
>                    &quot;application/json&quot;, disabled=not ok, width=&quot;stretch&quot;\)
> e3.download\_button\(&quot;rebuild\_cohort.py&quot;, export.rebuild\_script\(steps, ss.request\), &quot;rebuild\_cohort.py&quot;,
>                    &quot;text/x-python&quot;, disabled=not ok, width=&quot;stretch&quot;\)

Supplemental rules: None cited; official criterion above applies.

Impact: Ordinary quoted research text should remain data. A malformed generated script undermines the required rerunnable export; executing a manually edited or untrusted generated program adds a separate trust risk. The review should not exaggerate this into an observed exploit.

Concrete change: Serialize the request as a Python literal or JSON data and keep it outside source delimiters. Generate source through fixed templates with data encoded separately, then parse the result before offering it. Apply the same boundary discipline to all user-controlled fields included in executable exports.

Acceptance check: Prepare harmless requests containing triple quotes, backslashes, newlines and Unicode. Without executing the submission or generated program, an authorized follow-up can parse each generated source file and verify it contains only the intended fixed statements and the exact request value. Run ordinary reconstruction controls separately in an approved environment.

### Custom-data selection is process-wide rather than session-local

gap · P1 · Confidence: High that the mutation is process-global; actual cross-session effects require the stated controlled test.

custom.activate clears and replaces the module-global data.TABLES and sets ONCOSYS\_DATA in os.environ; deactivate restores those same global objects. The UI stores the original setting in one browser&\#x27;s session state but calls these global mutators. The engine and loaders resolve their inputs from those globals unless a location is explicitly supplied. In a server process hosting multiple sessions, selecting custom data in one session can therefore change the inputs or available tables used by another. This is a conditional concurrency/isolation risk, not an observed disclosure or a claim that a single-user local demonstration is broken.

[Source lines 163–181](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/custom.py#L163-L181)

> def activate\(folder: str &\#124; Path\) -&gt; None:
>     &quot;&quot;&quot;Use the custom data folder for everything from now on \(this process\).&quot;&quot;&quot;
>     import json
>     folder = Path\(folder\)
>     meta = json.loads\(\(folder / &quot;tables.json&quot;\).read\_text\(encoding=&quot;utf-8&quot;\)\)
>     data.TABLES.clear\(\)
>     data.TABLES.update\(meta\)
>     os.environ\[&quot;ONCOSYS\_DATA&quot;\] = str\(folder\)
>     os.environ.pop\(&quot;ONCOSYS\_RELEASE&quot;, None\)
> 
> 
> def deactivate\(original\_data: str &\#124; None\) -&gt; None:
>     &quot;&quot;&quot;Back to TCGA-BRCA.&quot;&quot;&quot;
>     data.TABLES.clear\(\)
>     data.TABLES.update\(copy.deepcopy\(TCGA\_TABLES\)\)
>     if original\_data:
>         os.environ\[&quot;ONCOSYS\_DATA&quot;\] = original\_data
>     else:
>         os.environ.pop\(&quot;ONCOSYS\_DATA&quot;, None\)

[Source lines 162–173](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L162-L173)

>             if st.button\(&quot;Use this data&quot;, type=&quot;primary&quot;, width=&quot;stretch&quot;\):
>                 try:
>                     folder = custom.build\(tables, base, keys\)
>                     if not CUSTOM:
>                         ss.byod\_original\_data = os.environ.get\(&quot;ONCOSYS\_DATA&quot;\)
>                     custom.activate\(folder\)
>                     forget\_session\_history\(\)
>                     st.cache\_data.clear\(\)
>                     ss.request = &quot;&quot;
>                     ss.ai\_notes = None
>                     set\_steps\(\[\]\)
>                     st.rerun\(\)

[Source lines 82–93](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/data.py#L82-L93)

> def location\(ddir: str &\#124; Path &\#124; None = None\) -&gt; Path:
>     &quot;&quot;&quot;The folder data is read from: a data folder, or a release folder of changed raw files.&quot;&quot;&quot;
>     if ddir:
>         return Path\(ddir\).expanduser\(\).resolve\(\)
>     base = \_configured\_base\(\)
>     rel = os.environ.get\(&quot;ONCOSYS\_RELEASE&quot;, &quot;&quot;\).strip\(\)
>     if rel:
>         r = Path\(rel\).expanduser\(\)
>         if not r.exists\(\):
>             r = \_split\(base\)\[0\] / &quot;releases&quot; / rel
>         return r.resolve\(\)
>     return base

[Source lines 222–225](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/data.py#L222-L225)

> def load\(name: str, ddir: str &\#124; None = None\) -&gt; pd.DataFrame:
>     &quot;&quot;&quot;Return a copy so callers can&\#x27;t mutate the cache. The cache key is the resolved location, so
>     switching release \(ONCOSYS\_RELEASE\) never serves the old files.&quot;&quot;&quot;
>     return \_load\(name, str\(location\(ddir\)\)\).copy\(\)

Supplemental rules: None cited; official criterion above applies.

Impact: The uploaded tables may belong to one researcher while all browser sessions share the process. A session boundary in the interface does not isolate a module dictionary or environment variable. Correct counts and provenance can be lost if another session changes those settings between operations.

Concrete change: Keep an immutable dataset context in each session and pass it explicitly to the engine, loader, SQL verifier and exporter. Avoid changing process environment and shared registries on a browser action. If the prototype supports only one local user, state and enforce that limit rather than implying multi-user isolation.

Acceptance check: Use two independent local browser sessions and two invented datasets with unmistakably different schemas/IDs. Alternate activation, engine execution, SQL verification and export; each session must retain its own context. Test returning one session to TCGA mode without changing the other. No real participant data is needed.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-5: Working tool and clear setup. Judges can run the core workflow from the submitted repository.

Status: **not_tested**

README documents CLI/app setup, release overlays and a submission tag matching this pin. No install, app, test, SQL query, hosted deployment or provider call was run by this reviewer; fresh-machine and changed-release reconstruction remain untested.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T1-6: Useful next steps. Suggested fixes are specific and match the size and importance of the problem.

Status: **observed**

Fix recommendations discriminate identity correction from row de-duplication and disclose tradeoffs. Confirm chosen fixes and diagnostic export limitations survive in durable records.

### Fix advice explains when de-duplication leaves the real problem

strength · P2 · Confidence: High for inspected recommendation rules and controls; user comprehension and override persistence were not tested.

Advice classifies a proposed fix by the actual step change. For a cross-sample problem it recommends matching sample\_id; an inflation-only collapse is explicitly not enough. For a left join it distinguishes collapse from a semi-join that would change membership. Judgment calls such as excluding redacted records or selecting one patient specimen receive no automatic recommendation. The app also displays human-review/quality limits and requires an explicit override before exporting unresolved problems.

[Source lines 50–55](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/advice.py#L50-L55)

> def advise\(result, steps: list\[dict\]\) -&gt; dict\[tuple\[int, int\], tuple\[bool, str\]\]:
>     &quot;&quot;&quot;\{\(warning index, fix index\): \(is recommended, what to know about it\)}.
> 
>     Only problems with a demonstrably right answer get a recommendation. Judgement calls
>     \(exclude redacted records, collapse to one patient per row\) deliberately get none.
>     &quot;&quot;&quot;

[Source lines 70–84](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/advice.py#L70-L84)

>             effect = \_effect\(fix, index, steps\)
>             if &quot;cross\_sample&quot; in kinds:
>                 \# The wrong record is attached to the sample. Nothing else fixes that.
>                 if effect == &quot;on:sample\_id&quot;:
>                     out\[\(w\_i, f\_i\)\] = \(True, WHY\[&quot;sample\_id&quot;\]\)
>                 elif w.kind == &quot;inflation&quot;:
>                     out\[\(w\_i, f\_i\)\] = \(False, WHY\[&quot;still\_cross&quot;\]\)
>             elif w.kind == &quot;inflation&quot; and step.get\(&quot;op&quot;\) == &quot;join&quot;:
>                 how = step.get\(&quot;how&quot;, &quot;inner&quot;\)
>                 if how == &quot;inner&quot; and effect == &quot;how:semi&quot;:
>                     out\[\(w\_i, f\_i\)\] = \(True, WHY\[&quot;semi&quot;\]\)
>                 elif how == &quot;left&quot; and effect == &quot;collapse&quot;:
>                     out\[\(w\_i, f\_i\)\] = \(True, WHY\[&quot;collapse\_left&quot;\]\)
>                 elif how == &quot;inner&quot; and effect == &quot;collapse&quot;:
>                     out\[\(w\_i, f\_i\)\] = \(False, WHY\[&quot;arbitrary\_row&quot;\]\)

[Source lines 380–388](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L380-L388)

> if CUSTOM:
>     st.warning\(&quot;\*\*Human review required.\*\* A person should confirm the steps match the research question &quot;
>                &quot;before this cohort is used. \*\*Limitation:\*\* your tables are used as uploaded: values aren&\#x27;t &quot;
>                &quot;quality-checked, and samples and patients are linked only through the ID columns you chose.&quot;\)
> else:
>     st.warning\(&quot;\*\*Human review required.\*\* A person should confirm the steps match the research question before &quot;
>                &quot;this cohort is used. \*\*Limitation:\*\* layer membership \(\`has\_\*\`\) comes from the sample manifest. &quot;
>                &quot;This tool doesn&\#x27;t check the quality of values inside each layer. It joins the clinical, survival, &quot;
>                &quot;slide and gene-level mutation tables; RNA, protein and copy-number values can&\#x27;t be filtered on.&quot;\)

[Source lines 451–466](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L451-L466)

> if problems:
>     st.error\(&quot;Not ready to export:\\n\\n&quot; + &quot;\\n&quot;.join\(f&quot;- \{p}&quot; for p in problems\)\)
>     ok = st.checkbox\(&quot;I understand: export anyway. cohort\_samples.csv will still contain each sample only once.&quot;\)
> else:
>     st.success\(&quot;No unresolved problems: one row per sample, and every joined record belongs to its own sample.&quot;\)
>     ok = True
> 
> out = export.cohort\_samples\(df\)
> defn = export.cohort\_definition\(steps, ss.request, results\)
> e1, e2, e3 = st.columns\(3\)
> e1.download\_button\(&quot;cohort\_samples.csv&quot;, out.to\_csv\(index=False\), &quot;cohort\_samples.csv&quot;, &quot;text/csv&quot;,
>                    disabled=not ok, width=&quot;stretch&quot;\)
> e2.download\_button\(&quot;cohort.json \(definition + funnel\)&quot;, json.dumps\(defn, indent=2\), &quot;cohort.json&quot;,
>                    &quot;application/json&quot;, disabled=not ok, width=&quot;stretch&quot;\)
> e3.download\_button\(&quot;rebuild\_cohort.py&quot;, export.rebuild\_script\(steps, ss.request\), &quot;rebuild\_cohort.py&quot;,
>                    &quot;text/x-python&quot;, disabled=not ok, width=&quot;stretch&quot;\)

[Source lines 550–562](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/engine.py#L550-L562)

> def unresolved\_problems\(results: list\[StepResult\]\) -&gt; list\[str\]:
>     &quot;&quot;&quot;Problems still visible in the final cohort \(an inflation fixed by a later collapse doesn&\#x27;t count\).&quot;&quot;&quot;
>     out = \[\]
>     final = results\[-1\]
>     if final.error or any\(r.error for r in results\):
>         out.append\(&quot;A step failed to run.&quot;\)
>     if final.rows \!= final.samples:
>         out.append\(f&quot;The final table has \{final.rows - final.samples:,} duplicate sample rows.&quot;\)
>     for r in results:
>         for w in r.warnings:
>             if w.kind == &quot;cross\_sample&quot;:
>                 out.append\(f&quot;Step \{r.index}: records linked through a different sample of the same patient.&quot;\)
>     return out

Supplemental rules: None cited; official criterion above applies.

Impact: The interface gives a specific next step with an explanation of what that step does and does not solve. This is more useful than treating every warning as equivalent or equating a unique CSV with a correct research cohort.

Concrete change: Keep the causal explanation of each fix and the explicit judgment boundary. Ensure diagnostic exports preserve unresolved status and the user&\#x27;s override in a machine-readable companion, rather than relying only on a transient checkbox.

Acceptance check: Show a cross-sample join, choose a collapse and demonstrate that its unresolved warning persists; then choose a sample-key repair. For an unresolved diagnostic export, inspect the standalone CSV and companion definition to confirm their status cannot be mistaken for approval.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-7: Communication. Someone without specialist knowledge can understand the result and next step.

Status: **not_tested**

Step counts and visible review/quality limitations address the intended non-coding researcher. No unguided use, keyboard, screen-reader, responsive-layout or time-pressure task was observed in this pass.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## Excluded scope

- .gitignore: non-allowlisted file type
- docs/TRAP\_LOG.md: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- examples/byod\_synthetic/labs.csv: non-allowlisted file type
- examples/byod\_synthetic/samples.csv: non-allowlisted file type
- examples/byod\_synthetic/visits.csv: non-allowlisted file type
- tests/test\_trap\_requests.py: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact

## Judge Follow-Up Sequence

1. Verify the official final commit and product declaration.
2. Start with the highest-priority synthetic acceptance checks above.
3. Follow one finding through evidence, affected versus unaffected analyses, proposed repair and human decision.
4. Verify the exported artifact against the organizer contract without reading sealed answers.
5. Record actual results separately from this static audit; revise only claims the new evidence supports.
