# Identity Crisis: UI State Follow-Through - Concise Slides

Revision 4. Earlier artifacts remain unchanged. One finding per slide. Updated 2026-11-14T20:49:04.919373+00:00.

# Identity Crisis: UI State Follow-Through



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

# The AI citation caption accurately describes an ID-membership check

Strength - IC-11 - T1-3

The UI accurately describes its citation check as finding or sample IDs belonging to the result. The checker also looks for the verdict word. Neither check establishes the truth of every generated sentence.

Judge follow-up: Keep the narrow caption and deterministic verdict. Test unsupported numbers and negation separately from ID membership.

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/ai_summary.py#L107-L118)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L675-L687)
- [Source 3](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/ai_summary.py#L28-L36)
- [Source 4](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tests/test_ai_summary.py#L32-L50)

<!-- Speaker notes: The checker identifies unknown finding/sample references and whether the verdict word appears. The UI describes its result narrowly as an ID existing in this result, rather than claiming that all prose is factually verified. The system prompt separately tells the model to use only supplied facts and avoid clinical advice.

Keep the scoped label and deterministic verdict as authoritative. Add evidence-version binding and targeted contradictory-number/negation cases before making any broader factual-validation claim.

Acceptance: With mocked responses, compare an unknown ID, a known ID with an unsupported numeric statement, and the wrong verdict embedded in a negation. Keep identity checks separate from semantic correctness and do not label all passing IDs as verified facts.

Confidence: High for checker and caption wording. The test file contains definitions, not this reviewer's observed test results, and no model was called.

Later evidence qualification: This is a strength in honest labeling. Do not convert a limited guard into a false claim of full factual verification, and do not penalize the UI for a guarantee it does not make. -->

---

# The browser enables permissive missing-check handling by default

Risk - IC-07 - T1-4

The callable API defaults to strict missing-check handling. The browser instead initializes its permissive option to on. All eight inspected built-in cards have matching source declarations, so this concern applies when a required check is actually unavailable.

Judge follow-up: Compare fresh browser and API defaults with an explicitly unavailable invented check. A declaration alone does not prove runtime availability.

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L495-L501)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L537-L541)
- [Source 3](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L264-L274)
- [Source 4](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/__init__.py#L79-L105)
- [Source 5](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L133-L148)
- [Source 6](https://github.com/nikbearbrown/neu-oncosys-hackathon-challenge/blob/main/professor-bear/identity-crisis-control-tower/coverage-note-codex-23484638.md)

<!-- Speaker notes: The sidebar sets st.session_state.allow_missing to True when the key is absent and passes that value into analyze and assess. With this option, an unregistered required check is unknown but nonmaterial. The callable assess and run_checks signatures default to False. Thus the strict API default and permissive browser default are different source facts.

Make strict handling the initial browser default, or give permissive runs a distinct incomplete/development state that cannot be confused with ordinary readiness. Keep the disclosure and test the browser entry point separately from the core API.

Acceptance: In an authorized fresh-session test with a synthetic card requiring an unregistered check, inspect the initial toggle and resulting state. Compare the strict API, initial UI and explicit permissive opt-in. No ordinary approved result should conceal the pending requirement.

Confidence: High for initialization and call flow. The browser was not executed by this reviewer; an API-only default probe does not answer this UI question.

Later evidence qualification: The later coverage note found a declaration for every required name in eight built-in cards. No submission module was imported by this source reviewer. Do not treat the permissive initialization as proof that every ordinary card is incomplete. -->

---

# The analysis cache signature omits release-file identity

Risk - IC-08 - T1-3

The analysis cache receives release paths and a signature of code and card timestamps. It receives no release-content identity. Replacing data at the same path can therefore leave those cache arguments unchanged.

Judge follow-up: Test same-path replacement with an unchanged-input control. Immutable versioned release directories avoid this particular condition.

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L257-L274)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L277-L292)
- [Source 3](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L537-L541)
- [Source 4](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data)

<!-- Speaker notes: inputs_sig enumerates card YAML and tower Python paths with modification times, but not release data. analyze is decorated with st.cache_data and receives the release path, card ID, missing-check option, that signature and optional custom-card JSON. Reading release bytes happens inside the cached body. Replacing data at the same path does not change the explicitly supplied data identity.

Pass a content-bound release manifest or immutable release-version identity into every cached analysis and board call. Show which version the result represents and invalidate all derived views together. A code/card timestamp signature should remain a separate policy-version input.

Acceptance: On invented data, run a comparison, replace one value at the same release path without changing code/cards, and rerun. The cached result must either refresh to the new input digest or explicitly refuse the changed immutable release. Retain an unchanged-input cache-hit control.

Confidence: High for the inspected cache arguments and official cache contract; stale-result behavior has not been reproduced here.

Later evidence qualification: This is a source inference under Streamlit's documented cache contract. It requires same-path input reuse and a retained cache. No stale result was observed by this reviewer. -->

---

# Sign-off invalidation does not compare the evidence digests

Risk - IC-09 - T1-6

The saved receipt contains evidence digests. The live invalidation signature checks decisions, verdict and reviewer fields instead. A changed policy or recomputed evidence can preserve those fields while changing what the reviewer signed.

Judge follow-up: Keep the old receipt as history and bind current approval to the current evidence digest. A targeted session test remains necessary.

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L47-L63)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L575-L588)
- [Source 3](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L690-L713)
- [Source 4](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L1141-L1153)

<!-- Speaker notes: signed stores findings and readiness digests in the receipt. The live UI's separate signature contains current repair/issue decisions, verdict, sign-off choice, note and reviewer fields, but no findings/readiness digest, input-file digest or complete card policy. It clears signed state only when that narrower signature changes, and the overview reports Signed whenever the retained signed object exists.

Build the live invalidation identity from the same canonical evidence/policy digests used in the receipt, alongside reviewer decisions. Preserve the old receipt as history and require a new decision for a changed evidence version. Exclude only documented nondeterministic display fields from canonicalization.

Acceptance: Sign an invented result, then change a card's material policy or evidence while keeping verdict and decision IDs the same. After recomputation, the current result must be Pending or explicitly show that the retained signature covers an older version. The original receipt must remain unchanged.

Confidence: High for the missing fields in the invalidation signature and the Signed display predicate; no session-level reproduction was executed here.

Later evidence qualification: The source report distinguishes authentic old receipt contents from the UI's claim of current applicability. It does not allege forged digests or an observed live bypass. -->

---

# The optional summary cache is keyed only by release label and card ID

Risk - IC-10 - T1-7

Optional AI prose is retained under a release label and card ID. The key excludes the current evidence and missing-check policy. Recomputed results can therefore appear beside prose written for an older context.

Judge follow-up: Mock the model, change context under the same labels, and require regeneration or an explicit old-version label.

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L655-L674)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L675-L687)
- [Source 3](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L537-L541)
- [Source 4](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/ai_summary.py#L50-L66)
- [Source 5](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/ai_summary.py#L121-L131)

<!-- Speaker notes: ai_box retrieves generated text under ai|release_label|card_id and reuses it until the user requests another summary. That key excludes current findings, readiness, card policy and missing-check setting. The analysis path can recompute when those settings or card timestamps change, while the stored summary remains under the same key.

Bind the summary to a canonical digest of the exact context sent to the model. Invalidate or visibly mark old prose when context changes, retain its prior version if useful, and keep deterministic results available without a model.

Acceptance: Mock model output for one invented context, then change the missing-check policy or a card's reasons with the same release label and card ID. The old summary must disappear or carry an explicit old-version label until regenerated. No network call is required.

Confidence: High for session key construction and reuse. Actual model behavior and UI refresh were not tested.

Later evidence qualification: No provider request or stale output was observed. The proposed check needs only invented context and a mocked model, not a network call. -->

---

# Judging Limits



The official rubric and human judges determine the result.

Confirm the final submission commit.
Separate source conclusions from observed runs and policy recommendations.
Different test counts do not establish a cross-team ranking.


<!-- Speaker notes:  -->

---
