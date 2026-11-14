# Identity Crisis Control Tower: independent review

Reviewed commit: `380760dc3b7b61097756f2b85c0f462feadc802c`. Updated: **2026-11-14T20:56:16+00:00**. Track 1: Cohort Firewall.

**Status: source review plus isolated runtime checks; no verified hosted demo.** No official score is assigned. Runtime observations are labelled per issue; remaining source findings still require reproduction. Exact branches and limitations are stated. No student code or files were changed.

This submission goes beyond change detection: research-question cards, baseline checks, measured effects, uncertainty estimates and fingerprinted review receipts are visible in source. The main first-pass concerns are a sign-off path that permits a missing validator, different missing-check defaults in the API and browser, and silent loss of optional robustness evidence.

## What it does well

### Question-specific materiality and traceable reasons

Material issues determine the verdict in Blocked, unknown, warning order. The output records fields, sample references, rules and file hashes. [tower/readiness.py:108](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L108)

### Explicit empty-measurement handling

A1 refuses missing or repeated ERALPHA rows and groups with no measured values instead of returning a fabricated zero. [tower/analyses.py:28](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/analyses.py#L28)

### Fingerprint-bound human review

Sign-off records the reviewer, time, decision and digests of both findings and readiness. The UI withdraws sign-off when specified reviewer/decision fields change; that signature does not cover all evidence changes (see issue 7). [tower/review.py:47](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L47)

## Issue-by-issue findings

### 1. Missing validator does not stop review-file publication

**Priority: high. Evidence: source and isolated runtime reproduction.**

**Runtime update:** A synthetic sign-off passed to save with a nonexistent validator wrote readiness.signed.json. The returned message explicitly said the findings were not checked. This is a fail-open save policy, not a hidden claim that validation ran. See [test evidence](TESTS.md).

validate returns None when the organizer validator is absent. save rejects only ok is False, then writes the signed readiness and review files for None as well. The UI subsequently records the sign-off. This differs from the stated requirement that sign-off counts only after validation passes.

**Evidence:** [tower/review.py:103](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L103); [tower/review.py:118](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L118); [app.py:1141](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L1141).

**Concrete change:** Require ok is True before a validated sign-off. Allow a separately labelled draft export if validation is unavailable.

**Acceptance check:** Run with an absent validator and confirm no validated sign-off is persisted; then use passing and failing validators as controls.

### 2. The browser defaults to permissive handling of unavailable checks

**Priority: high. Evidence: source and isolated runtime reproduction.**

**Runtime update:** With a synthetic unknown required check, default assess returned Insufficient Evidence. Setting allow_missing=True returned Ready. The test card omitted analyses to isolate this check. The API default therefore fails closed. A fresh-browser check separately observed the option enabled. An actual import control loaded all 14 registrations without errors and covered every required check in the eight built-in cards. See [second-round evidence](evidence/synthetic-probes-round2.json).

allow_missing=True marks unknown checks nonmaterial. assess starts at Ready and excludes these pending checks from the deciding set. The callable API defaults strict, but the fresh browser initializes this option to true. The option is disclosed in Settings. The risk is conditional on a required check becoming unavailable; it is not proof that built-in cards currently omit checks.

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

**Priority: methodological note; no repeated-patient defect observed in the public A1 cohort. Evidence: source, aggregate public-input audit and synthetic repeated-specimen probe.**

**Runtime qualification:** All 698 eligible public Release A samples had distinct 12-character patient barcode prefixes; 529 positive and 169 negative measurements were present. No repeated-patient issue was found in this selected cohort. An invented six-patient-per-group fixture, copied into ten specimens per patient, narrowed the sample-resampling interval from width 4.00 to 1.25 while adding no independent patients. That demonstrates the conditional assumption, not a defect in the event cohort. [Aggregate counts and synthetic result](evidence/independence-audit.json).

The percentile bootstrap redraws observations within each ER group. The method, seed and repetitions are documented, which is good. If distinct sample IDs represent repeated specimens from a patient, independent observation resampling can overstate precision. This is a conditional statistical limitation, not an observed failure on the event dataset.

**Evidence:** [tower/robustness.py:43](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/robustness.py#L43).

**Concrete change:** State the sampling unit and verify one independent patient per unit, or use patient-cluster resampling when the question requires it.

**Acceptance check:** A statistician reviews the interval and a repeated-patient synthetic example; document the supported independence assumption.

### 6. Same-path data replacement can leave the cohort display stale

**Priority: high. Evidence: actual local browser reproduction on invented data.**

The app displayed 114 eligible samples. One eligible sample was then removed from the temporary release's protein file without changing its path. Its byte hash changed. Clicking Show results still displayed 114; changing the missing-check option (a cache argument) refreshed the result to 113. The file was restored afterwards. This is not a report about the original or hosted dataset.

The cache identity includes paths, question/card context and code/card modification times, but not release-file identity. **Evidence:** [app.py:257](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L257), [app.py:263](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L263), [app.py:535](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L535); [browser observations](evidence/browser-qa.json).

**Concrete change:** Include an immutable release version or content-bound manifest in analysis and board cache keys, and show which version the result represents.

**Acceptance check:** Replace a release at the same path, refresh, and verify counts, evidence and exports update together. Retain the unchanged-input cache-hit control.

### 7. A signed review can outlive its question's evidence context

**Priority: high. Evidence: deterministic Streamlit AppTest reproduction; browser behavior depends on the interaction path.**

An approved synthetic review was signed using the actual UI test runner and organizer schema validator. Changing only the question's intended-use text, while keeping its ID, title, verdict, reviewer and decisions unchanged, retained the original signed receipt. The app rendered the revised context; the receipt still held the old context and digest. No exception or warning appeared in that deterministic run. This does not mean the stored digest was forged: the problem is continuing to present an older receipt as applicable.

A separate Chromium route using Request more evidence and navigating between pages did withdraw sign-off after the context change. Changing the reviewer also withdrew it. These are positive controls and delimit the claim: not every interaction preserves a stale receipt. The deterministic approved-review path is the reproduced failure.

**Evidence:** [app.py:580](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L580), [tower/review.py:47](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L47); [exact state trace](evidence/identity-state-probe.json), [reproduction](../review-tools/identity-state-probe.py).

**Concrete change:** Compare the current canonical evidence and question-policy digests with the signed receipt's inputs before showing it as current. Preserve old receipts as history and require a new decision for changed evidence.

**Acceptance check:** Change intended use, relevant data, or check policy while preserving the verdict label; the old receipt must be marked historical or withdrawn. Reviewer-only and decision-only changes remain passing controls.

## Exact official rubric: evidence, not scores

The maximum points below reproduce the official track weights. They are not points awarded. Supplemental dashboard and data-quality rules do not add scoring criteria.

| Criterion | Maximum | Evidence and question for judges |
|---|---:|---|
| Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support. | 20 | Detailed baseline and change checks exist; 96 submitted tests passed and three practice-envelope tests remain skipped; author scorecards are not independent accuracy estimates. |
| Reasoning for the research question. Changes its result appropriately when the research question or intended use changes. | 20 | Cards make intended use explicit; missing-check bypass needs stronger output qualification. |
| Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion. | 15 | File digests and lineage are strong; cache freshness and receipt applicability require fixes. |
| Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review. | 15 | Review receipts are explicit, but missing validation must not count as validated sign-off. |
| Working tool and clear setup. Judges can run the core workflow from the submitted repository. | 15 | Fresh-machine instructions and test modules exist; submitted Streamlit AppTest checks and a synthetic Chromium workflow ran locally; no hosted deployment was verified. |
| Useful next steps. Suggested fixes are specific and match the size and importance of the problem. | 10 | Next steps include evidence needed; preserve that distinction when proposing restored values. |
| Communication. Someone without specialist knowledge can understand the result and next step. | 5 | Glossary and staged views are described; denominators and incomplete results need plain-language labels. |

## Runtime update

96 passed, 3 skipped, 0 failed, 0 errors. Eleven local browser checks: nine met, two did not meet reviewer-proposed safeguards. A separate deterministic sign-off probe reproduced issue 7. Earlier independent safeguards remain recorded by round. [Commands, limitations and concrete observations](TESTS.md). These counts are not scores.

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

A separate reviewer supplied [a detailed source audit](audit-codex-23484638-pass-01.md) and [an issue deck](slides-codex-23484638-pass-01.html) ([Markdown version](slides-codex-23484638-pass-01.md)), committed 2026-11-14T15:04:09-05:00. The companion source findings and later runtime probes agree. Current suite counts are 96 passed and three skipped; the API unknown-check default fails closed, while the browser starts permissive. The companion's “not run” statements describe that reviewer's pass, not all testing in this folder. [Cross-review status](../REVIEW-STATUS.md) explains the relationship.


The companion also has a [concise revised deck](slides-codex-23484638-pass-02.html), [full slide notes](slides-codex-23484638-pass-02.md) and a [cross-review reading guide](../review-guide-codex-23484638.md). These preserve the source review; current runtime observations remain in TESTS.md.

## Later UI-Scoped Qualification

The earlier nondefault-bypass wording describes `assess` and `run_checks`, whose callable defaults are strict. It does not describe the fresh browser default: [app.py:495-501](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L495-L501) initializes `allow_missing=True` and the analysis caller passes it through. The UI discloses the option and pending-check meaning. This is a conditional policy concern when a required check is unavailable, not evidence that every current built-in card lacks checks.

The [UI-state follow-through](audit-codex-23484638-pass-03.md) also narrows the broad input-change sign-off claim: stored receipt digests and the live invalidation signature are separate controls. Its cache and signature concerns now have the scoped reproductions in issues 6–7; optional-summary caching remains source-derived. The [coverage qualification](coverage-note-codex-23484638.md) records declarations for every required check in all eight inspected built-in cards, and the later runtime coverage control confirms successful imports in the recorded test environment. Earlier tests and their API-level observations remain valid within their stated scope.
