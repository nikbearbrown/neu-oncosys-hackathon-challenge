# Tripwire / Driftwire: independent first-pass review

Reviewed commit: `45df43640836025b40e89fc190f913ad694a6011`. Updated: **2026-11-14T19:40:03+00:00**. Track 1: Cohort Firewall.

**Status: source review, not a verified live demo.** No official score is assigned. Source findings below are hypotheses about reachable runtime behavior unless labelled otherwise; exact branches and limitations are stated. No student code or files were changed.

The code separates release-change compatibility from model-training readiness, includes question-specific dependencies, and reruns nominally unaffected analyses as a cross-check. The first priorities are verdict precedence and completeness of the human-review state. No claim about its real-data detection rate is independently verified in this first pass.

## What it does well

### Question readiness treats missing checks explicitly

Unavailable and skipped checks map to Insufficient Evidence, and required checks absent from a result are added as unavailable. [tripwire/verdicts.py:50](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/verdicts.py#L50)

### Independent check of supposedly unaffected analyses

The build path reruns analyses when verify_unaffected is enabled and compares the actual slices. Required files, missing fields and empty cohorts have explicit insufficient-evidence paths. [tripwire/findings.py:140](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/findings.py#L140)

### Repair decisions validate reason and role

The helper rejects unknown repairs, unknown decisions, blank reasons and blank roles. It copies the input instead of changing source data. [tripwire/review.py:14](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L14)

## Issue-by-issue findings

### 1. Insufficient samples are checked after the unaffected branch

**Priority: high. Evidence: source inspection; runtime reproduction pending.**

release_verdict returns Ready for an unaffected, unmoved result before it tests movement.insufficient. Thus the helper can report compatibility as Ready even when its movement object says the sample evidence is insufficient. The outer build guards empty cohorts, but an undersized nonempty cohort is a separate case. This is a source-identified path; an end-to-end reproduction is still needed.

**Evidence:** [tripwire/verdicts.py:24](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/verdicts.py#L24); [tripwire/analyses.py:122](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/analyses.py#L122).

**Concrete change:** Evaluate insufficiency before the unaffected return, or return separate compatibility and adequacy results with an explicit trusted-baseline requirement.

**Acceptance check:** Use an unchanged nonempty cohort below the configured per-group minimum. Confirm the result names insufficient evidence; retain a sufficiently large unchanged control.

### 2. A flagged finding without a repair appears fully decided

**Priority: high. Evidence: source inspection; runtime reproduction pending.**

review_status defines open findings using all(...) over associated repairs. For a flagged finding with no associated repair, all([]) is true, so it is excluded from the open list. This matters for imported findings and future checks even if the current builder normally emits a repair for each finding.

**Evidence:** [tripwire/review.py:37](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L37).

**Concrete change:** Require an explicit finding-level disposition when no repair exists, and distinguish request_more_evidence from approval to proceed.

**Acceptance check:** A synthetic needs_human_review finding with no repair must remain open. A request for evidence should remain visibly unresolved until the required evidence is recorded.

### 3. Analysis rounding precedes effect classification

**Priority: medium. Evidence: source inspection; runtime reproduction pending.**

A1 returns means and differences rounded to three decimals before movement is computed. Small changes and near-zero effects can be hidden or disproportionately changed by display precision. This is not evidence that the published practice result is wrong.

**Evidence:** [tripwire/analyses.py:98](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/analyses.py#L98); [tripwire/analyses.py:122](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/analyses.py#L122).

**Concrete change:** Keep full-precision calculation fields and format separate display values. Justify absolute and relative tolerances per question.

**Acceptance check:** Probe near-zero values and changes on each side of the tolerance at full precision; ensure changing display precision cannot change the verdict.

### 4. New review calls replace prior decisions

**Priority: medium. Evidence: source inspection; runtime reproduction pending.**

apply_decisions creates a new decisions list from the supplied mapping and replaces the previous list. The helper records neither decision time nor a stable reviewer identity. This is suitable for a current-state document, but is not an immutable approval history.

**Evidence:** [tripwire/review.py:14](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L14).

**Concrete change:** Document snapshot semantics; for repeated review, append timestamped events bound to the evidence digest and derive current decisions separately.

**Acceptance check:** Approve, revise, and request evidence on the same repair. Export the complete history without changing the original evidence.

### 5. The no-AI statement is broader than the repository

**Priority: low. Evidence: source inspection; runtime reproduction pending.**

The README says there are no AI features or AI-service calls, while the optional intake prototype implements consent-gated OpenAI mapping suggestions. The consent gate is a positive control; its presence makes the blanket claim inaccurate. No network call was made in this review.

**Evidence:** [README.md:1](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/README.md#L1); [intake_prototype/ai_suggest.py:48](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/intake_prototype/ai_suggest.py#L48).

**Concrete change:** Scope the claim to the deterministic core and explain the optional intake route, transmitted metadata, and opt-in control.

**Acceptance check:** Documentation and UI agree about which route sends information; a no-consent test verifies no request occurs.

## Exact official rubric: evidence, not scores

The maximum points below reproduce the official track weights. They are not points awarded. Supplemental dashboard and data-quality rules do not add scoring criteria.

| Criterion | Maximum | Evidence and question for judges |
|---|---:|---|
| Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support. | 20 | Change detectors and mutation tests are present; accuracy and false alarms need an independent synthetic run. |
| Reasoning for the research question. Changes its result appropriately when the research question or intended use changes. | 20 | Distinct description/training cards are a strength; inspect the adequacy precedence in issue 1. |
| Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion. | 15 | Hashes, field dependencies and documented thresholds aid traceability; preserve raw precision. |
| Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review. | 15 | Reason/role validation helps; issue 2 can hide an unresolved review obligation. |
| Working tool and clear setup. Judges can run the core workflow from the submitted repository. | 15 | CLI, API, Streamlit and static site are present; no application execution in this first pass. |
| Useful next steps. Suggested fixes are specific and match the size and importance of the problem. | 10 | Repairs remain proposals; add history and evidence-needed states. |
| Communication. Someone without specialist knowledge can understand the result and next step. | 5 | Explain the Ready scope and reconcile the optional AI documentation. |

## Checks actually performed

- Pinned and read source at `45df43640836025b40e89fc190f913ad694a6011`; original checkout was clean when inspected.
- Parsed **91/91** selected Python source files with `ast.parse`; **0** syntax failures. Parsing does not execute or validate behavior.
- Counted **276** `test_` function definitions in the inspected source set. This is a source count, not collected tests or passed tests.
- Validated every cited source path and starting line against the pinned commit.
- Rendered deck QA is recorded separately in `evidence/deck-qa.json` after rendering.
- No application builds, dependency installs, submitted runtime tests, live deployment checks, real-data evaluation, sealed-envelope runs or model-provider calls in this first pass.

[Machine-readable static checks](evidence/static-checks.json). No raw TCGA records, answer keys or credentials are included.

## Next investigation

Work through the issues above in order. Reproduce them in an isolated copy with invented inputs, including positive controls. Retain the recorded commit when comparing results. Changes after this review require a new commit-specific update; they do not retroactively change the evidence.

A statistician should review adequacy thresholds, interval assumptions and claims of bias or representativeness. A domain expert should review clinical meaning. Neither source inspection nor passing software tests establishes clinical validity.
