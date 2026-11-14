# Identity Crisis Control Tower - Concise Slides

Revision 2. Earlier artifacts remain unchanged. One finding per slide. Updated 2026-11-14T20:20:41.929034+00:00.

# Identity Crisis Control Tower



Professor Bear - Independent Audit

Track 1: cohort-control-tower
Commit 380760dc3b7b
Static source review; no official score


<!-- Speaker notes:  -->

---

# Review Scope



Pinned source with separately attributed test evidence

The source reviewer did not run submission code.
Read the retained REPORT.md and TESTS.md for parallel runtime observations.
No official score, clinical validity or comparative accuracy rate is asserted.


<!-- Speaker notes:  -->

---

# Question cards make materiality and intended use inspectable

Strength - IC-04 - T1-2

Question cards state the intended research use, cohort, required fields and acceptable limitations. Material issues retain rules, sample references and file hashes.

Judge follow-up: Use the same release with different research questions and explain every change in the result.

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/cards/er-alpha-by-er.yaml#L1-L22)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L133-L158)
- [Source 3](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L175-L205)

<!-- Speaker notes: The A1 card states its descriptive research use, eligible group, target field, acceptable limitations, unacceptable identity problems and excluded clinical uses. Assessment selects material issues in its declared verdict order and attaches fields, rules, source references, row counts and file hashes to lineage.

Retain explicit cards and version their policies with each export. Demonstrate how changing intended use changes a result while the underlying release remains fixed.

Acceptance: Use the same synthetic release with descriptive and training-oriented cards. Explain each difference using declared dependencies and limits, and verify exported lineage identifies the fields and policy behind the decision.

Confidence: High for the inspected card and lineage construction; cross-card numerical behavior remains untested here. -->

---

# Unknown checks and empty measurements have explicit failure routes

Strength - IC-05 - T1-1

Default required-check failures become material unknowns. A1 refuses empty measurement groups and ambiguous target rows. The missing-check bypass is explicitly nondefault.

Judge follow-up: Keep the default safeguards and label development-bypass output as incomplete.

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/__init__.py#L79-L105)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/analyses.py#L28-L45)

<!-- Speaker notes: By default, an unregistered required check becomes material unknown, and a crashed check becomes material unknown with a limitation. A1 refuses duplicated relevant clinical IDs, missing or repeated ERALPHA rows, and a group with no measured values. allow_missing=True is a documented nondefault development option that changes the missing-check materiality.

Keep fail-explicit defaults and label development-bypass outputs as incomplete and non-approvable. Do not let consumers treat the nondefault bypass as equivalent to a complete checked run.

Acceptance: Omit a required registered check, induce a check error and create a zero-measurement group. Verify each names the uncertainty; compare the development option and confirm its output cannot be confused with fully assessed readiness.

Confidence: High for source defaults and guards; no runtime checks were performed in this source pass. -->

---

# Review receipts bind the human decision to evidence fingerprints

Strength - IC-06 - T1-6

The review receipt records the tool verdict separately from the human decision and binds the decision to evidence digests. A digest does not authenticate the named reviewer.

Judge follow-up: Change the evidence after sign-off. Keep the original receipt tied to its original inputs.

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L47-L63)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L66-L80)

<!-- Speaker notes: signed copies the readiness document, records repair and issue decisions, and includes reviewer, role, timestamp and digests of findings and readiness at sign-off. The Markdown record presents the tool verdict separately from the reviewer's decision. A digest detects content changes; it does not authenticate the named person.

Keep separate tool and reviewer decisions, retain evidence digests and add authenticated identity only if the deployment claims it. Preserve earlier receipts when a reviewer revises a decision.

Acceptance: Sign a synthetic record, change one evidence field and compare its digest. Confirm the old receipt remains tied to the old evidence, the tool verdict is not rewritten as the human decision, and missing validation is visibly non-approved.

Confidence: High for receipt construction; authentication, tamper-resistant storage and UI invalidation were not verified at runtime. -->

---

# Unavailable validation still permits signed review artifacts

Risk - IC-01 - T1-4

When the organizer validator is absent, the save helper still writes signed review artifacts. Its message discloses that validation did not run.

Judge follow-up: Separate unvalidated drafts from validated sign-off. Test absent, passing and rejecting validators.

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L103-L115)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L118-L134)
- [Source 3](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L1136-L1159)

<!-- Speaker notes: validate returns None when the organizer validator is absent. save rejects only False and then writes readiness.signed.json and findings.reviewed.json for the None case too. The UI records the signed state after save returns normally. The returned message does disclose that findings were not checked: this is permissive policy, not a hidden assertion that validation ran.

Require an explicit True result for validated sign-off. If review without the validator is useful, emit a separately named, non-approved draft carrying validation_status=unavailable and do not activate the normal signed success state.

Acceptance: With a missing validator, no validated signed artifact or success state should be created. Repeat with passing and rejecting validators, and inspect both files and UI state rather than the message alone.

Confidence: High for helper and UI control flow; the retained parallel TESTS.md independently reports the helper-level missing-validator write. -->

---

# Optional calculation failure loses its evidence state

Risk - IC-02 - T1-3

Failures in optional robustness or error-budget calculations become empty objects. The output loses the distinction between failure, inapplicability and missing context.

Judge follow-up: Expose an execution state and reason. Gate only the claims that depend on the failed calculation.

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L108-L131)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L133-L148)

<!-- Speaker notes: The conclusion calculation and error-budget calculation catch broad exceptions and replace their outputs with empty dictionaries. A conclusion issue is appended only when the robustness object is nonempty. The source therefore does not distinguish a calculation that failed from one that was inapplicable or absent in these fields.

Export separate applicable, attempted, succeeded, unavailable and failed states with bounded error details. Gate only claims that actually depend on that calculation, and keep unrelated checks usable.

Acceptance: Inject a controlled robustness error and a separate error-budget error in an authorized synthetic run. The output must identify each missing calculation and affected claim, while a non-applicable question remains explicitly not applicable.

Confidence: High for exception handling; the parallel review reports a controlled robustness fault, not an ordinary-data failure rate. -->

---

# Eligible group size and measured denominator need separate labels

Risk - IC-03 - T1-7

A1 means skip missing measurements, while group size includes eligible entries with missing values. This follows the reference convention but needs clearer denominators.

Judge follow-up: Show eligible, measured and missing counts beside each estimate.

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/analyses.py#L35-L51)

<!-- Speaker notes: A1 rejects a group with zero observed values, then computes means using Series.mean while reporting n_positive and n_negative using Series.size. With some missing values, size includes entries that do not contribute to the mean. This may preserve a reference-compatible eligible count, but it is not the measured denominator.

Preserve eligible counts if the organizer requires them and add measured and missing counts beside each estimate. Use measured counts where an evidence-adequacy rule specifically concerns observed values.

Acceptance: Keep at least one measured value per ER group and blank several other values. Show eligible, measured and missing counts separately and identify which denominator drives each limit and interval.

Confidence: High for the count-versus-mean distinction; no missing-value fixture was executed by this reviewer. -->

---

# Judging Limits



The official rubric and human judges determine the result.

Confirm the final submission commit.
Separate source conclusions from observed runs and policy recommendations.
Different test counts do not establish a cross-team ranking.


<!-- Speaker notes:  -->

---
