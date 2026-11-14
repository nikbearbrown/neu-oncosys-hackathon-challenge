# Identity Crisis: Source And Runtime Reconciliation

Added November 14, 2026, 21:04 UTC. This is a companion interpretation note, not a new official score or an additional set of failures. Earlier reports and decks remain intact.

- Submission: `AravindKumar2504/identity-crisis-control-tower` at `380760dc3b7b61097756f2b85c0f462feadc802c`.
- Organizer reference: `6e15a399a64ffbf80778db0b462ac239e70086b9`; official final-submission receipt remains unverified.
- Separate runtime evidence: review-repository commit [`a544f20ded69561df4c5252b0cce7b12f6d0de88`](https://github.com/nikbearbrown/neu-oncosys-hackathon-challenge/commit/a544f20ded69561df4c5252b0cce7b12f6d0de88).
- This source reviewer read the published observations, reproduction programs and corresponding pinned submission paths. This reviewer did not execute the submission, its tests, the AppTest probe or a model service. The runtime observations below belong to the separate reviewer and retain that environment's limitations.

## What Changed In The Evidence

| Companion concern | New observation | Correct interpretation |
|---|---|---|
| IC-07: strict API versus permissive browser default | A fresh Chromium session observed the missing-check option enabled. A separate import control loaded 14 registrations without errors; all required names in eight built-in cards were present. | The entry-point difference is now browser-observed. The failure consequence remains conditional on a required check being unavailable. Do not claim the current built-ins are all missing implementations. |
| IC-08: cached analysis omits data identity | The browser displayed 114 eligible samples. A temporary same-path protein-file change altered its hash; Show results still showed 114. Changing a cache argument revealed 113. | A targeted local freshness failure is reproduced. It is not proof that the hosted app has stale data or that an immutable release directory changes under normal use. |
| IC-09: signed receipt versus current evidence | A deterministic AppTest approved-review path retained a signed receipt after intended-use text changed. Revised context was rendered, but the receipt retained the old context and digest. A separate browser path with Request more evidence and page navigation withdrew sign-off. | The failure is interaction-path dependent. Do not claim that all context changes retain sign-off. The old digest was not forged; its continuing applicability was the concern. |
| IC-10: optional AI summary cache | No new model-call or summary-cache reproduction is recorded in this update. | This remains a source-derived concern, not a newly observed AI error. |

Sources: [browser observations](evidence/browser-qa.json), [registration coverage](evidence/identity-check-coverage.json), [approved-review state trace](evidence/identity-state-probe.json), and the separate reviewer's [current report](REPORT.md) and [test record](TESTS.md).

## Source Follow-Through And Controls

### Cache Freshness

The analysis cache accepts a release path, card identity, missing-check policy and a signature. The signature contains card and code modification times, not release-file content identity. The browser observation therefore matches a specific source path rather than merely a guessed explanation. Both the analysis and board cache should be bound to an immutable release version or content manifest. See [app.py:257-274](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L257-L274) and [app.py:277-295](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L277-L295).

Retain the passing cache-invalidation control. A fresh count after changing a cache argument helps isolate freshness from an invariant cohort definition. The probe changed invented fixture data in a disposable copy and restored it; it did not inspect or alter the original clinical dataset. See the [browser reproduction program](../review-tools/identity-browser-qa.py).

**Acceptance check:** unchanged input gives the same version-bound result; same-path changed content either refreshes all counts/evidence/exports together or is rejected because a supposedly immutable release changed. A different release path should not inherit an earlier result.

### Receipt Applicability

The signed document includes readiness and findings digests. The live invalidation signature covers reviewer, role, verdict and decision fields, but not the complete current evidence or question-policy document. The two mechanisms serve different purposes. See [app.py:580-588](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L580-L588) and [tower/review.py:47-63](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L47-L63).

The deterministic probe selects pages through the submission's own headless-test route, not a general browser navigation guarantee. That route is explicitly supported in [app.py:1251-1256](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L1251-L1256), and the submitted screen tests use it at [tests/test_screen.py:22-33](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tests/test_screen.py#L22-L33). The [published probe](../review-tools/identity-state-probe.py) signs an approved review, changes intended-use text, reruns and checks both the review state and overview. The separate Chromium Request more evidence route and reviewer-change control must remain visible as counterevidence to an overbroad claim.

**Acceptance check:** cover approve, reject and request-more-evidence decisions, with and without page navigation. Independently vary intended use, relevant data and check policy while preserving the verdict label and item IDs. Either mark the old receipt historical or require a new review when its canonical inputs differ. Reviewer-only and decision-only changes should continue to withdraw the old sign-off. Preserve historical receipts rather than rewriting their digests.

### Check Availability

The new runtime control is stronger than the earlier [declaration-only note](coverage-note-codex-23484638.md): it records successful module imports in isolated Python 3.14.6, zero load errors and zero missing required registrations for the eight built-in cards. It does not prove that every implementation is scientifically correct or that another installation imports identically. A future custom card or import failure still needs explicit unavailable-check handling. The browser initialization is visible at [app.py:495-501](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L495-L501).

**Acceptance check:** use an intentionally unknown required check as a controlled custom-card case. Record strict and permissive results in both entry points; the output should make unavailable required evidence explicit. Keep the ordinary eight-card registration control as a separate check.

## Strengths And Remaining Limits

The separate browser review also observed disabled sign-off without reviewer/decision information, a required reason for rejecting a repair, passing organizer schema validation, and exports retaining the requested-evidence decision and reviewer identity. These are useful controls to preserve, not reasons to erase the narrower freshness and applicability findings. Schema validity is not scientific correctness or authenticated reviewer identity.

The 11 browser assertions are reviewer-proposed safeguards, not official rubric points or 11 independent product defects. The earlier submitted-suite count and these targeted probes must not be summed into an accuracy estimate or compared mechanically with another team's suite. No hosted deployment, full accessibility audit, clinical validity, unseen-input performance or final freeze receipt is established.

For the judge: read issues 2, 6 and 7 in the [current main report](REPORT.md) together with this note. The earlier [UI-state source supplement](audit-codex-23484638-pass-03.md) and [concise deck](slides-codex-23484638-pass-04.pdf) retain their historical source-only scope. This later note adds separately attributed runtime support and the interaction-path qualification; it does not turn the old static pass into an executed one.
