# HIPPA-cratic Cohort Studio



Professor Bear | Independent Audit

Track 1: cohort-studio
Commit 9f0ad46f32a1
Static source review; no official score


<!-- Speaker notes:  -->

---

# Review Scope



Pinned source with explicit limits

39 text files collected; 6 entries excluded.
Selected implementation paths were inspected.
No submission code, tests, data fetches or sealed inputs were run.
The official freeze commit still needs confirmation.


<!-- Speaker notes:  -->

---

# Join checks distinguish duplicate rows from wrong-sample links

Strength | HC-05 | T1-1 | P2

The engine checks duplicate rows and wrong-sample links separately. Its proposed fixes respect different join semantics.

A left join does not silently become a semi-join.
Keep the identity and row-inflation controls distinct.

- [Source 1](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/engine.py#L440-L465)
- [Source 2](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/engine.py#L468-L483)
- [Source 3](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/engine.py#L508-L530)

<!-- Speaker notes: The engine records row/sample/patient counts at each step and checks both increases in repeated sample rows and patient-key joins attaching another sample's record. Semi/anti joins also warn when membership is obtained only through a different sample, unless an explicit constrained allow_cross_sample policy applies. The inflation fix offers a semi-join only for inner joins; it avoids silently dropping unmatched samples from a left join. These are distinct checks rather than a generic row-count warning.

Retain these separate checks and the left-join caveat. Keep counts and sample examples attached to the precise step, and demonstrate that a chosen fix removes the relevant problem rather than just its visible duplicates.

Acceptance: With invented patients having tumor/normal specimens and multiple slides, compare inner, left, semi and anti joins on sample versus patient IDs. Show row inflation, wrong-sample membership and an explicit patient-level existence policy separately. Confirm a valid sample-key control remains quiet.

Confidence: High for the source paths; numerical results and the author's demonstration were not rerun. -->

---

# A second execution path compares exact membership and step counts

Strength | HC-06 | T1-2 | P2

DuckDB separately executes translated steps and compares exact sample IDs plus counts at each step.

The UI explains that agreement does not validate the research question.
Retain this control and bind it to the current inputs.

- [Source 1](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/sqlcheck.py#L24-L45)
- [Source 2](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/sqlcheck.py#L218-L234)
- [Source 3](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L430-L444)

<!-- Speaker notes: The SQL verifier builds DuckDB views from resolved source files and translates the cohort steps into SQL rather than reusing the pandas output. verify compares final sample-ID sets and row/sample/patient counts at every paired step, returning differences and the query. The app explicitly says this checks execution of the steps, not whether those steps express the research question. Shared file resolution and policy assumptions still limit the independence of the check.

Preserve the query and exact-set comparison, and bind its result to the input identity as in HC-03. Assert matching step counts before pairing them and keep independently designed expected cohort cases separate from compiler agreement.

Acceptance: Inject an invented translation/execution discrepancy that preserves the total number of samples but changes one ID; verify the set mismatch is reported. Exercise an intermediate duplicate-row difference with the same final cohort. Confirm an agreed result still requires human review of intended meaning.

Confidence: High for the separate SQL construction and comparisons; no DuckDB or student test was executed. -->

---

# Fix advice explains when de-duplication leaves the real problem

Strength | HC-07 | T1-6 | P2

Fix advice explains why removing duplicate rows may leave the wrong record attached.

Human-review and unresolved-export controls are visible in source.
Keep the reasoning and export limitations with the result.

- [Source 1](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/advice.py#L50-L55)
- [Source 2](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/advice.py#L70-L84)
- [Source 3](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L380-L388)
- [Source 4](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L451-L466)
- [Source 5](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/engine.py#L550-L562)

<!-- Speaker notes: Advice classifies a proposed fix by the actual step change. For a cross-sample problem it recommends matching sample_id; an inflation-only collapse is explicitly not enough. For a left join it distinguishes collapse from a semi-join that would change membership. Judgment calls such as excluding redacted records or selecting one patient specimen receive no automatic recommendation. The app also displays human-review/quality limits and requires an explicit override before exporting unresolved problems.

Keep the causal explanation of each fix and the explicit judgment boundary. Ensure diagnostic exports preserve unresolved status and the user's override in a machine-readable companion, rather than relying only on a transient checkbox.

Acceptance: Show a cross-sample join, choose a collapse and demonstrate that its unresolved warning persists; then choose a sample-key repair. For an unresolved diagnostic export, inspect the standalone CSV and companion definition to confirm their status cannot be mistaken for approval.

Confidence: High for inspected recommendation rules and controls; user comprehension and override persistence were not tested. -->

---

# The rebuild script does not bind the exported cohort's data release

Risk | HC-01 | T1-3 | P1

The definition records input fingerprints. The rebuild script uses current environment defaults instead.

A fresh process can select a different release.
Check exact membership with recorded inputs and a clean environment.

- [Source 1](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/export.py#L21-L33)
- [Source 2](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/export.py#L36-L55)
- [Source 3](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/data.py#L82-L101)
- [Source 4](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/tests/test_rebuild.py#L32-L47)

<!-- Speaker notes: cohort_definition records data_dir, release and input_sha256, but rebuild_script accepts only steps and request and emits run(STEPS) without the recorded location, release or expected hashes. That call resolves data through the new process's environment and defaults. A colleague running the script in a fresh shell can therefore use the original release rather than the changed release used for export, or lack the custom table registry entirely. The existing rebuild tests inherit the current environment and exercise two fixed default-data examples; their definitions do not establish changed-release or custom-data reconstruction. This is a source-derived reproduction gap, not an observed membership mismatch.

Generate a rebuild entry point from the complete exported definition. Resolve required table mappings and release overlays explicitly, verify expected content fingerprints before calculation, and record the exact sample membership digest. Make missing or changed inputs an explicit failure unless the user intentionally creates a new version. For custom data, export the registry and a documented way to supply the referenced files without embedding sensitive records.

Acceptance: Using invented data, export from a changed release and from a custom-data folder. Start a clean process with release/data environment variables absent and different defaults present. The script must either select the recorded inputs and reproduce exact sample IDs or fail with a precise missing/version-mismatch reason. Keep an unchanged default-data positive control and compare IDs, not just row counts.

Confidence: High for the missing binding in the complete generated script; the resulting runtime membership depends on the data and execution environment and was not exercised. -->

---

# A SQL success can remain attached to unchanged steps after data changes

Risk | HC-03 | T1-3 | P1

The SQL success record identifies step text, but omits the data release. Switching data can leave an old Match visible.

Version history also keys on steps alone.
Bind verification and history to steps plus input fingerprints.

- [Source 1](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L95-L103)
- [Source 2](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L408-L425)
- [Source 3](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L430-L449)
- [Source 4](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/versions.py#L33-L49)

<!-- Speaker notes: run_sql_check saves its result in session state with only ss.steps_text. The display accepts that result whenever the step text still matches. Release selection changes a process environment variable, clears Streamlit data caches and reruns, but does not clear this session-state verification record. The engine recomputes its current result, while the old SQL result can still be presented as Match for the same steps. The session's version history similarly uses only serialized steps as its key and returns the prior record immediately when those steps are unchanged. No current dataset fingerprint participates in either identity check.

Bind SQL verification and cohort versions to canonical steps plus resolved data/release identity and input hashes. Clear or mark prior checks historical when those inputs change, including custom-data activation. Keep the old result as history rather than relabelling it as a fresh verification.

Acceptance: Verify an invented release A, switch to release B with the same steps but different eligible membership, and confirm the old Match is withdrawn until a new SQL run completes. Inspect the stored version IDs and membership. Repeat a same-path content change and an unchanged-input control. Preserve the existing per-step/final-membership comparison.

Confidence: High for the inspected session-state and key logic; no live Streamlit session was run. -->

---

# Custom-data selection is process-wide rather than session-local

Risk | HC-04 | T1-4 | P1

Custom-data activation changes a shared table registry and process environment. Other sessions use those same globals.

This is a conditional multi-user risk, not an observed disclosure.
Test two invented datasets in separate browser sessions.

- [Source 1](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/custom.py#L163-L181)
- [Source 2](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L162-L173)
- [Source 3](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/data.py#L82-L93)
- [Source 4](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/data.py#L222-L225)

<!-- Speaker notes: custom.activate clears and replaces the module-global data.TABLES and sets ONCOSYS_DATA in os.environ; deactivate restores those same global objects. The UI stores the original setting in one browser's session state but calls these global mutators. The engine and loaders resolve their inputs from those globals unless a location is explicitly supplied. In a server process hosting multiple sessions, selecting custom data in one session can therefore change the inputs or available tables used by another. This is a conditional concurrency/isolation risk, not an observed disclosure or a claim that a single-user local demonstration is broken.

Keep an immutable dataset context in each session and pass it explicitly to the engine, loader, SQL verifier and exporter. Avoid changing process environment and shared registries on a browser action. If the prototype supports only one local user, state and enforce that limit rather than implying multi-user isolation.

Acceptance: Use two independent local browser sessions and two invented datasets with unmistakably different schemas/IDs. Alternate activation, engine execution, SQL verification and export; each session must retain its own context. Test returning one session to TCGA mode without changing the other. No real participant data is needed.

Confidence: High that the mutation is process-global; actual cross-session effects require the stated controlled test. -->

---

# Request text enters generated Python without serialization

Risk | HC-02 | T1-4 | P2

The generator places the request directly inside a Python docstring. Closing quotes can break that boundary.

The app downloads this source; it does not execute it.
Serialize request text and parse generated source before export.

- [Source 1](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/export.py#L36-L53)
- [Source 2](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L458-L466)

<!-- Speaker notes: rebuild_script inserts the raw request into an opening triple-quoted Python docstring. A request containing the closing delimiter can terminate that string, producing invalid syntax or additional source text in the downloaded script. The app passes its editable request directly into this generator. The inspected route downloads source; it does not itself execute the generated script, so this is not evidence of automatic server execution or a demonstrated compromise.

Serialize the request as a Python literal or JSON data and keep it outside source delimiters. Generate source through fixed templates with data encoded separately, then parse the result before offering it. Apply the same boundary discipline to all user-controlled fields included in executable exports.

Acceptance: Prepare harmless requests containing triple quotes, backslashes, newlines and Unicode. Without executing the submission or generated program, an authorized follow-up can parse each generated source file and verify it contains only the intended fixed statements and the exact request value. Run ordinary reconstruction controls separately in an approved environment.

Confidence: High for direct unescaped interpolation; no generated-source execution or exploit was attempted. -->

---

# Before A Judging Decision



Resolve evidence gaps before interpreting readiness

Confirm the final commit and intended product.
Run the named synthetic follow-up checks in an authorized environment.
Observe a fresh-machine workflow and exported result.
Keep untested claims, proposed scores and clinical claims out of the conclusion.


<!-- Speaker notes:  -->

---
