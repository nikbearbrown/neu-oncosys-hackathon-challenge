# Tripwire / Driftwire: independent review

Reviewed commit: `45df43640836025b40e89fc190f913ad694a6011`. Updated: **2026-11-14T21:04:04+00:00**. Track 1: Cohort Firewall.

**Status: source review plus isolated runtime checks; no verified hosted demo.** No official score is assigned. Runtime observations are labelled per issue; remaining source findings still require reproduction. Exact branches and limitations are stated. No student code or files were changed.

The code separates release-change compatibility from model-training readiness, includes question-specific dependencies, and reruns nominally unaffected analyses as a cross-check. The first priorities are verdict precedence and completeness of the human-review state. No claim about its real-data detection rate is independently verified in this first pass.

## What it does well

### Question readiness treats missing checks explicitly

Unavailable and skipped checks map to Insufficient Evidence, and required checks absent from a result are added as unavailable. [tripwire/verdicts.py:50](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/verdicts.py#L50)

### Independent check of supposedly unaffected analyses

The build path reruns analyses when verify_unaffected is enabled and compares the actual slices. Required files, missing fields and empty cohorts have explicit insufficient-evidence paths. [tripwire/findings.py:140](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/findings.py#L140)

### Repair decisions validate reason and role

The helper rejects unknown repairs, unknown decisions, blank reasons and blank roles. It copies the input instead of changing source data. [tripwire/review.py:14](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L14)

### Local browser workflow observed

Thirteen synthetic checks completed: **12 met, one did not meet the proposed safeguard**. The real interface distinguished release compatibility from question adequacy, expanded finding evidence, rejected missing review reasons and roles, validated the export, preserved the evidence-request decision, and cleared the previous result/export when a replacement comparison failed. The remaining review-counter issue is described below. [Browser evidence](TESTS.md#local-browser-workflow).

## Issue-by-issue findings

### 1. Insufficient samples are checked after the unaffected branch

**Priority: high. Evidence: source and isolated runtime reproduction.**

**Runtime update:** A corrected, well-formed four-sample release passed through the full check API: release verdict and A1/A2 were Ready, while the ER-protein question correctly returned Insufficient Evidence. A 40-sample control returned Ready for that question. This confirms the separate meanings of compatibility and question adequacy; it does not invalidate the question-readiness checks. See [second-round evidence](evidence/synthetic-probes-round2.json).

release_verdict returns Ready for an unaffected, unmoved result before it tests movement.insufficient. Thus the helper can report compatibility as Ready even when its movement object says the sample evidence is insufficient. The outer build guards empty cohorts, but an undersized nonempty cohort is a separate case. A later end-to-end synthetic reproduction below confirms the headline can remain Ready while question-specific adequacy is Insufficient Evidence. The README explicitly defines release Ready as unchanged dependency inputs; therefore this is chiefly a scope/communication and precedence concern, not evidence that its separate question-readiness engine ignores sample size.

**Evidence:** [tripwire/verdicts.py:24](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/verdicts.py#L24); [tripwire/analyses.py:122](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/analyses.py#L122).

**Concrete change:** Evaluate insufficiency before the unaffected return, or return separate compatibility and adequacy results with an explicit trusted-baseline requirement.

**Acceptance check:** Use an unchanged nonempty cohort below the configured per-group minimum. Confirm the result names insufficient evidence; retain a sufficiently large unchanged control.

### 2. Review counts can hide unresolved evidence requests

**Priority: high. Evidence: source and isolated runtime reproduction.**

**Runtime update:** Direct review_status calls returned an empty open list for a flagged finding without repairs and for a repair marked request_more_evidence. The no-repair case is a helper-level reproduction. A later actual local browser test recorded Request more evidence and observed Review (0 open) plus zero awaiting human review; the exported decision correctly remained request_more_evidence and no repair was applied. The counter tracks decisions recorded rather than concerns resolved. See [test evidence](TESTS.md).

review_status defines open findings using all(...) over associated repairs. For a flagged finding with no associated repair, all([]) is true, so it is excluded from the open list. This matters for imported findings and future checks even if the current builder normally emits a repair for each finding.

**Evidence:** [tripwire/review.py:37](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L37).

**Concrete change:** Require an explicit finding-level disposition when no repair exists, and distinguish request_more_evidence from approval to proceed.

**Acceptance check:** A synthetic needs_human_review finding with no repair must remain open. A request for evidence should remain visibly unresolved until the required evidence is recorded.

### 3. Analysis rounding precedes effect classification

**Priority: medium. Evidence: source and isolated runtime reproduction.**

**Runtime update:** A synthetic increase of 0.0004 in every positive-group measurement left the rounded mean and difference unchanged. a1_compare reported moved=False and 0.0% relative change. The full check API still returned Conditional because its input-level detector caught the change; this is an effect-precision limitation, not a demonstrated overall Ready bypass. [Exact observations](evidence/synthetic-probes-round3.json).

A1 returns means and differences rounded to three decimals before movement is computed. Small changes and near-zero effects can be hidden or disproportionately changed by display precision. This is not evidence that the published practice result is wrong.

**Evidence:** [tripwire/analyses.py:98](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/analyses.py#L98); [tripwire/analyses.py:122](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/analyses.py#L122).

**Concrete change:** Keep full-precision calculation fields and format separate display values. Justify absolute and relative tolerances per question.

**Acceptance check:** Probe near-zero values and changes on each side of the tolerance at full precision; ensure changing display precision cannot change the verdict.

### 4. New review calls replace prior decisions

**Priority: medium. Evidence: source and isolated runtime reproduction.**

**Runtime update:** Two apply_decisions calls (approve, then reject) retained one latest decision rather than two events. The original first-returned object was unchanged. This verifies snapshot semantics, not an immutable history. See [second-round evidence](evidence/synthetic-probes-round2.json).

apply_decisions creates a new decisions list from the supplied mapping and replaces the previous list. The helper records neither decision time nor a stable reviewer identity. This is suitable for a current-state document, but is not an immutable approval history.

**Evidence:** [tripwire/review.py:14](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L14).

**Concrete change:** Document snapshot semantics; for repeated review, append timestamped events bound to the evidence digest and derive current decisions separately.

**Acceptance check:** Approve, revise, and request evidence on the same repair. Export the complete history without changing the original evidence.

### 5. The no-AI statement is broader than the repository

**Priority: low. Evidence: source and isolated runtime reproduction.**

**Runtime update:** With consent=False, suggest_mappings raised ValueError before the mocked transport was called. Zero provider calls occurred. This confirms the consent guard; the remaining issue is the README blanket claim. [Exact observations](evidence/synthetic-probes-round3.json).

The README says there are no AI features or AI-service calls, while the optional intake prototype implements consent-gated OpenAI mapping suggestions. The consent gate is a positive control; its presence makes the blanket claim inaccurate. No network call was made in this review.

**Evidence:** [README.md:343](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/README.md#L343); [intake_prototype/ai_suggest.py:48](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/intake_prototype/ai_suggest.py#L48).

**Concrete change:** Scope the claim to the deterministic core and explain the optional intake route, transmitted metadata, and opt-in control.

**Acceptance check:** Documentation and UI agree about which route sends information; a no-consent test verifies no request occurs.

## Interpretation boundary

The organizer’s Control Tower product protects analyses across releases; it is not a requirement to revalidate every unchanged measurement against clinical truth. Tripwire’s README explicitly defines release Ready as “Nothing this result depends on changed” ([README.md:189](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/README.md#L189)). Its question-readiness cards are a separate, stronger check. Judges should assess whether users can distinguish those meanings, and should not treat an unchanged baseline as proof of fitness or a disagreement over labels as a failed detector. Proposed safeguards in this review are review recommendations, not additional official scoring rules.

## Exact official rubric: evidence, not scores

The maximum points below reproduce the official track weights. They are not points awarded. Supplemental dashboard and data-quality rules do not add scoring criteria.

| Criterion | Maximum | Evidence and question for judges |
|---|---:|---|
| Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support. | 20 | Change detectors and mutation tests are present; accuracy and false alarms need an independent synthetic run. |
| Reasoning for the research question. Changes its result appropriately when the research question or intended use changes. | 20 | Distinct description/training cards are a strength; inspect the adequacy precedence in issue 1. |
| Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion. | 15 | Hashes, field dependencies and documented thresholds aid traceability; preserve raw precision. |
| Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review. | 15 | Reason/role validation helps; issue 2 can hide an unresolved review obligation. |
| Working tool and clear setup. Judges can run the core workflow from the submitted repository. | 15 | CLI, API, Streamlit and static site are present; 404 submitted tests passed in isolation with the frozen public release; the hosted application was not verified. |
| Useful next steps. Suggested fixes are specific and match the size and importance of the problem. | 10 | Repairs remain proposals; add history and evidence-needed states. |
| Communication. Someone without specialist knowledge can understand the result and next step. | 5 | Explain the Ready scope and reconcile the optional AI documentation. |

## Runtime update

404 passed, 1 skipped, 0 failed, 0 errors. Independent safeguards: 4 met, 3 unmet. [Commands, limitations and concrete observations](TESTS.md). These counts are not scores.

## Initial static pass (historical scope)

- Pinned and read source at `45df43640836025b40e89fc190f913ad694a6011`; original checkout was clean when inspected.
- Parsed **91/91** selected Python source files with `ast.parse`; **0** syntax failures. Parsing does not execute or validate behavior.
- Counted **276** `test_` function definitions in the inspected source set. This is a source count, not collected tests or passed tests.
- Validated every cited source path and starting line against the pinned commit.
- Rendered deck QA is recorded separately in `evidence/deck-qa.json` after rendering.
- The initial pass was static only. Later isolated runtime checks are reported above and in TESTS.md; this historical scope is not the current verification status.

[Machine-readable static checks](evidence/static-checks.json). No raw TCGA records, answer keys or credentials are included.

## Follow-up and review limits

Work through the issues above in order. Use the supplied reproductions for confirmed issues; reproduce the remaining source-only concerns in isolation with positive controls. Retain the recorded commit when comparing results. Changes after this review require a new commit-specific update; they do not retroactively change the evidence.

A statistician should review adequacy thresholds, interval assumptions and claims of bias or representativeness. A domain expert should review clinical meaning. Neither source inspection nor passing software tests establishes clinical validity.

## Companion source audit

A separate reviewer supplied [a detailed source audit](audit-codex-23484638-pass-01.md) and [an issue deck](slides-codex-23484638-pass-01.html) ([Markdown version](slides-codex-23484638-pass-01.md)), committed 2026-11-14T15:03:44-05:00. The companion predates the corrected four-sample full API case. The latest runtime evidence confirms Ready release compatibility alongside Insufficient Evidence question adequacy; it does not claim that the separate question checker ignores size. The companion's “not run” statements describe that reviewer's pass, not all testing in this folder. [Cross-review status](../REVIEW-STATUS.md) explains the relationship.


The companion also has a [concise revised deck](slides-codex-23484638-pass-02.html), [full slide notes](slides-codex-23484638-pass-02.md) and a [cross-review reading guide](../review-guide-codex-23484638.md). These preserve the source review; current runtime observations remain in TESTS.md.
