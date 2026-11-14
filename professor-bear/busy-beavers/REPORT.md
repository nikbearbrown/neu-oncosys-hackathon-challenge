# Busy Beavers Cohort Firewall: independent first-pass review

Reviewed commit: `bfb369f231bf97a1d3aa21abade3ba4b1406a355`. Updated: **2026-11-14T20:11:00+00:00**. Track 1: Cohort Firewall.

**Status: source review plus isolated runtime checks; no verified hosted demo.** No official score is assigned. Runtime observations are labelled per issue; remaining source findings still require reproduction. Exact branches and limitations are stated. No student code or files were changed.

The architecture distinguishes detector output, validated API exports, labelled mocks and dashboard presentation. The most consequential first-pass findings concern the verdict logic, required-input preflight, and the route that turns proposed exclusions into a downloadable modified dataset.

## What it does well

### Mock and missing-engine states are explicit

The adapter distinguishes missing configuration and engine errors instead of silently substituting a demo as a successful real run. [backend/services/detector_adapter.py:124](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/backend/services/detector_adapter.py#L124)

### Original releases and validated findings are preserved

Fixes are recorded separately and a derivative ZIP is built without overwriting release B or the original validated findings. [backend/services/fixes.py:1](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/backend/services/fixes.py#L1)

### Deterministic evidence and analysis dependencies

Events produce evidence pointers, limitations, proposed repairs and per-analysis impact reasons. [detection/engine.py:238](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L238)

## Issue-by-issue findings

### 1. The detector cannot return Blocked

**Priority: high. Evidence: source and isolated runtime reproduction.**

**Runtime update:** The real analyze_releases engine returned Conditional for a synthetic 40-sample example whose A1 difference changed from +2.0 to −8.0. Both groups retained 20 samples. The change was detected and rerun, but the verdict never became Blocked. See [test evidence](TESTS.md).

The final decision is Insufficient Evidence on rerun failure, Conditional for any finding affecting an analysis, and Ready otherwise. No branch returns Blocked, even if a rerun succeeds but its conclusion changes substantially. The track offers four verdicts; the absence needs a deliberate question-specific policy, not an implicit collapse.

**Evidence:** [detection/engine.py:270](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L270).

**Concrete change:** Add explicit blocking conditions tied to the research question, measured effects and unresolved integrity failures.

**Acceptance check:** Use a synthetic change that reverses the relevant conclusion; explain why its result is Blocked or document a defensible narrower meaning for Conditional.

### 2. The unchanged-file shortcut lacks required-input validation

**Priority: high. Evidence: source and isolated runtime reproduction.**

**Runtime update:** The real analyze_releases engine returned Ready for two empty directories and again for two directories with identical zero-byte clinical.tsv and protein_rppa.tsv.gz. Both analyses were marked not_rerun with an identical-input explanation. The inspected reference-analysis Python module was present; it was not a missing-dependency failure. See [test evidence](TESTS.md).

changed_stems examines the union of files found. Two absent required files produce no changed stem. compare then says analysis inputs are byte-identical without loading them. The engine can reach Ready when no rerun failed and no affecting finding exists. The reproduced shortcut does not establish baseline fitness.

**Evidence:** [cfw/compare.py:34](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/compare.py#L34); [cfw/compare.py:48](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/compare.py#L48); [detection/engine.py:288](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L288).

**Concrete change:** Check required-file presence, decodability and required columns before any equality shortcut.

**Acceptance check:** Two empty folders and identical corrupt files must never return Ready; a valid unchanged release remains a control.

### 3. Easy export applies exclusion proposals without per-repair approval

**Priority: high. Evidence: source and isolated runtime reproduction.**

**Runtime update:** The actual build_dataset easy route removed one synthetic record even though the supplied decision explicitly rejected its exclusion. Storage lookup was mocked; dataset construction and ZIP contents were real. The original four-row file was unchanged. This tests export semantics, not a deployed authorization bypass. See [second-round evidence](evidence/synthetic-probes-round2.json).

The easy mode calls _suggested_removals, whose own description says no person is involved, and builds a derivative from every exclude proposal. Clicking download is a user action, but it is not an evidence-bound decision on each proposed repair. Original files remain safe; the concern is the status of the derivative.

**Evidence:** [backend/services/fixes.py:229](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/backend/services/fixes.py#L229); [backend/services/fixes.py:272](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/backend/services/fixes.py#L272).

**Concrete change:** Treat this as a clearly labelled unapproved preview, or require recorded review decisions before an approved repaired-data export.

**Acceptance check:** Reject or leave a repair undecided and verify an approved export cannot silently apply it. Preview exports retain explicit unapproved status.

### 4. Evidence and repair targets are truncated to 500

**Priority: medium. Evidence: source and isolated runtime reproduction.**

**Runtime update:** A synthetic 620-sample change produced a summary naming 620 affected samples but only 500 evidence entries and 500 unique repair targets. The truncation affects the machine-consumed repair set as well as display evidence. See [second-round evidence](evidence/synthetic-probes-round2.json).

Both evidence and repair targets are sliced to MAX_EVIDENCE=500. A large finding can describe more affected records than the exported repair covers. The easy export later consumes those targets. A presentation limit must not silently become the scope of a repair.

**Evidence:** [detection/engine.py:26](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L26); [detection/engine.py:257](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L257); [backend/services/fixes.py:229](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/backend/services/fixes.py#L229).

**Concrete change:** Keep a bounded display sample plus total count, truncation marker and complete separately addressable target set; prevent partial repairs from appearing complete.

**Acceptance check:** Create 501 synthetic affected targets. Verify all intended targets are represented or the export explicitly refuses/labels a partial operation.

### 5. Free-text model context includes sample identifiers and evidence notes

**Priority: medium. Evidence: source and isolated runtime reproduction.**

**Runtime update:** build_context retained a synthetic sample identifier and its synthetic evidence note. Known-ID validation rejected an invented citation and accepted a real fixture citation. No provider transport was called. This verifies payload construction and citation-ID checks, not a privacy breach or semantic factual correctness. [Exact observations](evidence/synthetic-probes-round3.json).

build_context includes up to 40 sample identifiers and ten evidence notes per finding, and a configured OpenAI route sends the context with the question. This is source evidence of payload construction, not an observed transmission or privacy breach. A local model route also exists.

**Evidence:** [detection/qa.py:48](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/qa.py#L48); [detection/qa.py:84](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/qa.py#L84); [frontend/app.py:1073](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/frontend/app.py#L1073).

**Concrete change:** Show the active provider and exact outbound categories before the first free-text request; minimize identifiers and offer a local-only mode.

**Acceptance check:** Use a mocked transport and synthetic markers to verify the payload and consent path. Do not test with real records or credentials.

## Interpretation boundary

A proposed fix can justify Conditional when a reviewer has the evidence needed to approve it. A sign change is not a universal clinical blocking threshold. Issue 1 concerns the absence of any output-level severity policy: the engine uses whether a finding affects an analysis, not how the result changed, to choose Conditional. Judges should ask the team to explain and demonstrate its policy rather than award or deduct points solely for one chosen threshold. No clinical cutoff is proposed here.

## Exact official rubric: evidence, not scores

The maximum points below reproduce the official track weights. They are not points awarded. Supplemental dashboard and data-quality rules do not add scoring criteria.

| Criterion | Maximum | Evidence and question for judges |
|---|---:|---|
| Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support. | 20 | Real detector code exists beyond the infrastructure docs; inspect input preflight and >500-record behavior. |
| Reasoning for the research question. Changes its result appropriately when the research question or intended use changes. | 20 | A1/A2 dependencies are explicit; the final policy lacks a Blocked branch. |
| Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion. | 15 | Validated exports and preserved originals help; truncated target sets need explicit coverage. |
| Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review. | 15 | Easy export needs review semantics; optional model routing needs clear outbound-data context. |
| Working tool and clear setup. Judges can run the core workflow from the submitted repository. | 15 | API, dashboard and infrastructure tests exist; isolated engine and backend tests ran; no hosted deployment was verified. |
| Useful next steps. Suggested fixes are specific and match the size and importance of the problem. | 10 | Repair ZIPs are practical, but proposals must not imply approved corrections. |
| Communication. Someone without specialist knowledge can understand the result and next step. | 5 | README demo placeholder and upstream clone instructions should be reconciled with the submitted repository. |

## Runtime update

65 passed, 0 skipped, 0 failed, 0 errors. Independent safeguards: 0 met, 3 unmet. [Commands, limitations and concrete observations](TESTS.md). These counts are not scores.

## Initial static pass (historical scope)

- Pinned and read source at `bfb369f231bf97a1d3aa21abade3ba4b1406a355`; original checkout was clean when inspected.
- Parsed **45/45** selected Python source files with `ast.parse`; **0** syntax failures. Parsing does not execute or validate behavior.
- Counted **45** `test_` function definitions in the inspected source set. This is a source count, not collected tests or passed tests.
- Validated every cited source path and starting line against the pinned commit.
- Rendered deck QA is recorded separately in `evidence/deck-qa.json` after rendering.
- The initial pass was static only. Later isolated runtime checks are reported above and in TESTS.md; this historical scope is not the current verification status.

[Machine-readable static checks](evidence/static-checks.json). No raw TCGA records, answer keys or credentials are included.

## Follow-up and review limits

Work through the issues above in order. Use the supplied reproductions for confirmed issues; reproduce the remaining source-only concerns in isolation with positive controls. Retain the recorded commit when comparing results. Changes after this review require a new commit-specific update; they do not retroactively change the evidence.

A statistician should review adequacy thresholds, interval assumptions and claims of bias or representativeness. A domain expert should review clinical meaning. Neither source inspection nor passing software tests establishes clinical validity.

Latest unchanged-public-input control: verified frozen Release A versus itself returned Ready and zero findings. [Scope and aggregate evidence](TESTS.md#frozen-public-baseline-control). This does not invalidate the synthetic missing-input or small-matrix findings.

## Companion source audit

A separate reviewer supplied [a detailed source audit](audit-codex-23484638-pass-01.md) and [an issue deck](slides-codex-23484638-pass-01.html) ([Markdown version](slides-codex-23484638-pass-01.md)), committed 2026-11-14T14:59:17-05:00. The companion adds duplicate-ID ordering and rounded-hash concerns. These are linked separately; targeted runtime corroboration is being recorded. Conditional versus Blocked remains a question-policy judgment, not a universal clinical threshold. The companion's “not run” statements describe that reviewer's pass, not all testing in this folder. [Cross-review status](../REVIEW-STATUS.md) explains the relationship.
