# Identity Crisis Control Tower: independent first-pass review

Reviewed commit: `380760dc3b7b61097756f2b85c0f462feadc802c`. Updated: **2026-11-14T20:04:21+00:00**. Track 1: Cohort Firewall.

**Status: source review plus isolated runtime checks; no verified hosted demo.** No official score is assigned. Runtime observations are labelled per issue; remaining source findings still require reproduction. Exact branches and limitations are stated. No student code or files were changed.

This submission goes beyond change detection: research-question cards, baseline checks, measured effects, uncertainty estimates and fingerprinted review receipts are visible in source. The main first-pass concerns are a sign-off path that permits a missing validator, an explicit development bypass for missing checks, and silent loss of optional robustness evidence.

## What it does well

### Question-specific materiality and traceable reasons

Material issues determine the verdict in Blocked, unknown, warning order. The output records fields, sample references, rules and file hashes. [tower/readiness.py:108](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L108)

### Explicit empty-measurement handling

A1 refuses missing or repeated ERALPHA rows and groups with no measured values instead of returning a fabricated zero. [tower/analyses.py:28](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/analyses.py#L28)

### Fingerprint-bound human review

Sign-off records the reviewer, time, decision and digests of both findings and readiness. UI code withdraws sign-off when its inputs change. [tower/review.py:47](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L47)

## Issue-by-issue findings

### 1. Missing validator does not stop review-file publication

**Priority: high. Evidence: source and isolated runtime reproduction.**

**Runtime update:** A synthetic sign-off passed to save with a nonexistent validator wrote readiness.signed.json. The returned message explicitly said the findings were not checked. This is a fail-open save policy, not a hidden claim that validation ran. See [test evidence](TESTS.md).

validate returns None when the organizer validator is absent. save rejects only ok is False, then writes the signed readiness and review files for None as well. The UI subsequently records the sign-off. This differs from the stated requirement that sign-off counts only after validation passes.

**Evidence:** [tower/review.py:103](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L103); [tower/review.py:118](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L118); [app.py:1141](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L1141).

**Concrete change:** Require ok is True before a validated sign-off. Allow a separately labelled draft export if validation is unavailable.

**Acceptance check:** Run with an absent validator and confirm no validated sign-off is persisted; then use passing and failing validators as controls.

### 2. Development bypass can allow Ready with pending required checks

**Priority: high. Evidence: source and isolated runtime reproduction.**

**Runtime update:** With a synthetic unknown required check, default assess returned Insufficient Evidence. Setting the explicit development-only allow_missing=True option returned Ready. The test card omitted analyses to isolate this check. The default path therefore fails closed; the recommendation concerns labelling and approval of development output. See [second-round evidence](evidence/synthetic-probes-round2.json).

allow_missing=True marks unknown checks nonmaterial. assess starts at Ready and excludes these pending checks from the deciding set. The bypass is explicitly documented and is not the default; the risk is presenting its output as normal readiness.

**Evidence:** [tower/checks/__init__.py:79](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/__init__.py#L79); [tower/readiness.py:133](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L133).

**Concrete change:** Keep the bypass useful for development but force an incomplete/development status and prohibit approval while required checks remain pending.

**Acceptance check:** A card with an unavailable required check stays Insufficient Evidence even under a development run, or produces a clearly separate non-approvable draft result.

### 3. Robustness failures disappear into empty objects

**Priority: medium. Evidence: source and isolated runtime reproduction.**

**Runtime update:** Injected a ValueError into the robustness calculation only. assess returned a document with no explicit occurrence of the failure or reason. This is controlled fault injection, not evidence that the ordinary calculation always crashes. See [test evidence](TESTS.md).

Exceptions from the conclusion/uncertainty calculation and error-budget calculation are replaced by empty dictionaries. These calculations may be optional, so failing them need not invalidate every use; silently omitting them does not show whether they ran.

**Evidence:** [tower/readiness.py:113](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L113); [tower/readiness.py:122](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L122).

**Concrete change:** Record not-run, error type and affected claim as explicit evidence states. Gate only the claims that require the missing calculation.

**Acceptance check:** Inject a controlled calculation failure and verify the report shows the missing result and its consequence rather than merely omitting the panel.

### 4. Reported group size includes unmeasured values

**Priority: medium. Evidence: source and isolated runtime reproduction.**

**Runtime update:** With 20 eligible positive samples and one missing measurement, run_a1 reported n_positive=20, actual measured count=19, and a mean of 2.001. This matches the documented reference convention; add the measured denominator rather than silently changing reference-compatible fields. See [second-round evidence](evidence/synthetic-probes-round2.json).

A1 computes means with missing values skipped but reports n_positive and n_negative using Series.size. The robustness code explicitly acknowledges this reference-compatible convention. The count can therefore exceed the actual denominator of the mean and bootstrap.

**Evidence:** [tower/analyses.py:40](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/analyses.py#L40); [tower/robustness.py:25](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/robustness.py#L25).

**Concrete change:** Preserve reference-compatible eligible counts but add measured counts and missing counts for each group beside the estimates.

**Acceptance check:** Leave at least one measured value per group and blank several others; display eligible, measured and missing denominators separately.

### 5. Bootstrap independence needs a stated unit

**Priority: medium. Evidence: source inspection; runtime reproduction pending.**

The percentile bootstrap redraws observations within each ER group. The method, seed and repetitions are documented, which is good. If distinct sample IDs represent repeated specimens from a patient, independent observation resampling can overstate precision. This is a conditional statistical limitation, not an observed failure on the event dataset.

**Evidence:** [tower/robustness.py:43](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/robustness.py#L43).

**Concrete change:** State the sampling unit and verify one independent patient per unit, or use patient-cluster resampling when the question requires it.

**Acceptance check:** A statistician reviews the interval and a repeated-patient synthetic example; document the supported independence assumption.

## Exact official rubric: evidence, not scores

The maximum points below reproduce the official track weights. They are not points awarded. Supplemental dashboard and data-quality rules do not add scoring criteria.

| Criterion | Maximum | Evidence and question for judges |
|---|---:|---|
| Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support. | 20 | Detailed baseline and change checks exist; 96 submitted tests passed and three practice-envelope tests remain skipped; author scorecards are not independent accuracy estimates. |
| Reasoning for the research question. Changes its result appropriately when the research question or intended use changes. | 20 | Cards make intended use explicit; missing-check bypass needs stronger output qualification. |
| Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion. | 15 | File digests, issue lineage and range-method metadata are strong; surface missing computations. |
| Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review. | 15 | Review receipts are explicit, but missing validation must not count as validated sign-off. |
| Working tool and clear setup. Judges can run the core workflow from the submitted repository. | 15 | Fresh-machine instructions and test modules exist; submitted Streamlit AppTest checks ran locally; no hosted deployment was verified. |
| Useful next steps. Suggested fixes are specific and match the size and importance of the problem. | 10 | Next steps include evidence needed; preserve that distinction when proposing restored values. |
| Communication. Someone without specialist knowledge can understand the result and next step. | 5 | Glossary and staged views are described; denominators and incomplete results need plain-language labels. |

## Runtime update

96 passed, 3 skipped, 0 failed, 0 errors. Independent safeguards: 0 met, 2 unmet. [Commands, limitations and concrete observations](TESTS.md). These counts are not scores.

## Initial static pass (historical scope)

- Pinned and read source at `380760dc3b7b61097756f2b85c0f462feadc802c`; original checkout was clean when inspected.
- Parsed **36/36** selected Python source files with `ast.parse`; **0** syntax failures. Parsing does not execute or validate behavior.
- Counted **99** `test_` function definitions in the inspected source set. This is a source count, not collected tests or passed tests.
- Validated every cited source path and starting line against the pinned commit.
- Rendered deck QA is recorded separately in `evidence/deck-qa.json` after rendering.
- The initial pass was static only. Later isolated runtime checks are reported above and in TESTS.md; this historical scope is not the current verification status.

[Machine-readable static checks](evidence/static-checks.json). No raw TCGA records, answer keys or credentials are included.

## Follow-up and review limits

Work through the issues above in order. Use the supplied reproductions for confirmed issues; reproduce the remaining source-only concerns in isolation with positive controls. Retain the recorded commit when comparing results. Changes after this review require a new commit-specific update; they do not retroactively change the evidence.

A statistician should review adequacy thresholds, interval assumptions and claims of bias or representativeness. A domain expert should review clinical meaning. Neither source inspection nor passing software tests establishes clinical validity.

## Companion source audit

A separate reviewer supplied [a detailed source audit](audit-codex-23484638-pass-01.md) and [an issue deck](slides-codex-23484638-pass-01.html) ([Markdown version](slides-codex-23484638-pass-01.md)), committed 2026-11-14T15:04:09-05:00. The companion source findings and later runtime probes agree. Current suite counts are 96 passed and three skipped; development bypass is non-default and the default unknown-check path fails closed. The companion's “not run” statements describe that reviewer's pass, not all testing in this folder. [Cross-review status](../REVIEW-STATUS.md) explains the relationship.
