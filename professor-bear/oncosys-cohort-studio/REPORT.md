# Cohort Studio: independent first-pass review

Reviewed commit: `54aeacb6f6f355a1dcaa42d7abf2ce174315ad69`. Updated: **2026-11-14T20:04:21+00:00**. Track 1: Cohort Firewall.

**Status: source review plus isolated runtime checks; no verified hosted demo.** No official score is assigned. Runtime observations are labelled per issue; remaining source findings still require reproduction. Exact branches and limitations are stated. No student code or files were changed.

This is a cohort-construction product, not a release-difference tower. Its strongest source features are explicit steps, row/sample/patient counts, join-inflation detection, composition shifts and reproducible exports. The first-pass review focuses on provenance truthfulness, safe generation of reproduction scripts and explicit approval of automated changes.

## What it does well

### Cohort accounting distinguishes rows, samples and patients

Join inflation and repeated-patient checks are separate, with recorded selection rules and a per-sample selection export. [cohort_studio/verdict.py:165](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/verdict.py#L165)

### Unknown evidence has a distinct verdict

The central decision order distinguishes failed, unknown and warning checks rather than folding unknown into Ready. [cohort_studio/verdict.py:314](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/verdict.py#L314)

### Reproduction script pins input hashes

The generated script records expected source hashes and copies the actual operation implementation. This is stronger than a narrative-only recipe. [cohort_studio/exports.py:185](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L185)

## Issue-by-issue findings

### 1. Unknown checksum verification is counted as a pass

**Priority: high. Evidence: source and isolated runtime reproduction.**

**Runtime update:** Removed sources.csv from an invented test fixture. clinical.tsv had verified=null, but the frozen-checksum check returned pass and claimed every raw file matched sources.csv. The overall verdict was Blocked because the synthetic cohort was small; the false checksum pass is independently wrong even when another check blocks release. See [test evidence](TESTS.md).

When sources.csv or an expected entry is missing, file_status retains verified=None. The verdict rejects only verified is False; otherwise it claims every used raw file matches the frozen checksums. Missing verification and successful verification are not equivalent. Committed manifests are separately marked unverified.

**Evidence:** [cohort_studio/data.py:64](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/data.py#L64); [cohort_studio/verdict.py:152](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/verdict.py#L152).

**Concrete change:** Use a three-state check: verified True, mismatch False, and unavailable/unknown. State exactly which raw files and manifests were verified.

**Acceptance check:** Remove only the expected checksum entry from a synthetic fixture. The provenance check must become unknown without inventing a mismatch or pass.

### 2. Request text is inserted into generated Python source

**Priority: high. Evidence: source and isolated runtime reproduction.**

**Runtime update:** A normal generated reproduction script parsed successfully. A request containing triple quotes produced invalid Python; a second harmless delimiter example placed a review_marker assignment in the generated program AST. These generated examples were parsed only and never executed. See [test evidence](TESTS.md).

The reproduction script inserts the raw request inside a triple-quoted module docstring. A request containing triple quotes can terminate that string, damage the script or introduce Python source. This is a source-identified code-generation hazard; no malicious generated file was executed.

**Evidence:** [cohort_studio/exports.py:158](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L158).

**Concrete change:** Serialize request text as a Python string literal with repr or a JSON value, rather than interpolating it into source delimiters.

**Acceptance check:** Use quotes, backslashes, newlines and a harmless marker as request text. Parse the output with ast.parse and verify the request remains data only.

### 3. Automatic fixes are enabled by default in the API

**Priority: medium. Evidence: source inspection; runtime reproduction pending.**

build_cohort defaults fix=True, applies inflation fixes and exports the resulting cohort. The first result and fix log are retained, which is useful. CLI/MCP consumers can nevertheless receive a changed analysis without an explicit per-change acceptance step. This is an authority and communication improvement, not a claim that all inflation fixes are wrong.

**Evidence:** [cohort_studio/api.py:116](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/api.py#L116); [cohort_studio/api.py:124](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/api.py#L124).

**Concrete change:** Separate draft, preview and accepted execution states; make the automation policy explicit and preserve the exact before/after operation.

**Acceptance check:** An inflating join produces a proposed correction and two distinct versions; the user can inspect and accept or reject it before an approved export.

### 4. Blocked outputs are exported beside ordinary cohorts

**Priority: medium. Evidence: source and isolated runtime reproduction.**

**Runtime update:** The actual write_all function exported cohort_samples.csv for a Blocked synthetic join-inflation example. verdict.json was also present and retained Blocked. Diagnostic exports are useful; the concern is preserving the restriction when a CSV is separated from its accompanying evidence. See [second-round evidence](evidence/synthetic-probes-round2.json).

write_all writes cohort_samples.csv regardless of the verdict; the verdict is in a separate JSON. Exporting blocked cohorts can be useful for diagnosis, but the CSV alone loses the restriction. The report must not imply that a generated file is approved for use.

**Evidence:** [cohort_studio/api.py:151](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/api.py#L151); [cohort_studio/exports.py:336](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L336).

**Concrete change:** Bundle a manifest binding files to verdict, limitations, review state and hashes; label blocked outputs as diagnostic and avoid an approved-download affordance.

**Acceptance check:** Produce a blocked cohort, move its CSV alone and inspect the export contract. Ensure downstream tools can detect missing approval metadata.

### 5. Automatic drafting can use a hosted service by default

**Priority: medium. Evidence: source inspection; runtime reproduction pending.**

ai=auto tries an own model, then the hosted service, then rules. The README explains this and --rules provides a local-only route; it is not hidden in documentation. A scientist may still reasonably assume a local CLI will not transmit their typed question.

**Evidence:** [cohort_studio/llm.py:69](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/llm.py#L69); [cohort_studio/api.py:124](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/api.py#L124).

**Concrete change:** Give a first-use routing notice or explicit opt-in; persist local-only settings and list what request/context is sent.

**Acceptance check:** Mock both providers and verify ai=off makes no outbound request; an auto request displays provider selection before transmission.

## Exact official rubric: evidence, not scores

The maximum points below reproduce the official track weights. They are not points awarded. Supplemental dashboard and data-quality rules do not add scoring criteria.

| Criterion | Maximum | Evidence and question for judges |
|---|---:|---|
| Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support. | 20 | Join inflation and composition checks fit the product; quantify false alarms with synthetic controls. |
| Reasoning for the research question. Changes its result appropriately when the research question or intended use changes. | 20 | Cohort steps encode the question; review automatic fix semantics and missing request meaning. |
| Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion. | 15 | Reproduction hashes are strong; issue 1 overstates verification and issue 2 endangers generated code. |
| Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review. | 15 | Review messages exist; distinguish automated preview from approved cohort and outbound routing. |
| Working tool and clear setup. Judges can run the core workflow from the submitted repository. | 15 | CLI, Streamlit, frontend and MCP interfaces exist; submitted interface tests ran locally; no hosted deployment was verified. |
| Useful next steps. Suggested fixes are specific and match the size and importance of the problem. | 10 | Fixes and per-step losses are concrete; retain user choice and blocked-export context. |
| Communication. Someone without specialist knowledge can understand the result and next step. | 5 | Show rows versus independent patients clearly; give provenance states distinct labels. |

## Runtime update

299 passed, 0 skipped, 0 failed, 0 errors. Independent safeguards: 1 met, 3 unmet. [Commands, limitations and concrete observations](TESTS.md). These counts are not scores.

## Initial static pass (historical scope)

- Pinned and read source at `54aeacb6f6f355a1dcaa42d7abf2ce174315ad69`; original checkout was clean when inspected.
- Parsed **65/65** selected Python source files with `ast.parse`; **0** syntax failures. Parsing does not execute or validate behavior.
- Counted **209** `test_` function definitions in the inspected source set. This is a source count, not collected tests or passed tests.
- Validated every cited source path and starting line against the pinned commit.
- Rendered deck QA is recorded separately in `evidence/deck-qa.json` after rendering.
- The initial pass was static only. Later isolated runtime checks are reported above and in TESTS.md; this historical scope is not the current verification status.

[Machine-readable static checks](evidence/static-checks.json). No raw TCGA records, answer keys or credentials are included.

## Follow-up and review limits

Work through the issues above in order. Use the supplied reproductions for confirmed issues; reproduce the remaining source-only concerns in isolation with positive controls. Retain the recorded commit when comparing results. Changes after this review require a new commit-specific update; they do not retroactively change the evidence.

A statistician should review adequacy thresholds, interval assumptions and claims of bias or representativeness. A domain expert should review clinical meaning. Neither source inspection nor passing software tests establishes clinical validity.
