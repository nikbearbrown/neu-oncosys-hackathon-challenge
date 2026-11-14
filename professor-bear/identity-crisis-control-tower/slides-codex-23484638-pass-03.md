# Identity Crisis: UI State Follow-Through



Professor Bear | Independent Audit

Track 1: cohort-control-tower
Commit 380760dc3b7b
Static source review; no official score


<!-- Speaker notes:  -->

---

# Review Scope



Committed source, not an observed demo

65 text files collected; 3 entries excluded.
Selected implementation paths were inspected.
No submission code, tests, data fetches or sealed inputs were run.
The official freeze commit still needs confirmation.


<!-- Speaker notes:  -->

---

# The AI citation caption accurately describes an ID-membership check

Strength | IC-11 | T1-3 | P2

The checker identifies unknown finding/sample references and whether the verdict word appears. The UI describes its result narrowly as an ID existing in this result, rather than claiming that all prose is factually verified. The system prompt separately tells the model to use only supplied facts and avoid clinical advice.

Why it matters: This appropriately limits what an automated citation check proves. Existing IDs and a verdict word do not validate numbers, negation or the meaning of a generated sentence, so the narrow ...
Next check: With mocked responses, compare an unknown ID, a known ID with an unsupported numeric statement, and the wrong verdict embedded in a negation. Keep identity checks separate from semantic correctness and do not ...

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/ai_summary.py#L107-L118)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L675-L687)
- [Source 3](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/ai_summary.py#L28-L36)
- [Source 4](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tests/test_ai_summary.py#L32-L50)

<!-- Speaker notes: The checker identifies unknown finding/sample references and whether the verdict word appears. The UI describes its result narrowly as an ID existing in this result, rather than claiming that all prose is factually verified. The system prompt separately tells the model to use only supplied facts and avoid clinical advice.

Keep the scoped label and deterministic verdict as authoritative. Add evidence-version binding and targeted contradictory-number/negation cases before making any broader factual-validation claim.

Acceptance: With mocked responses, compare an unknown ID, a known ID with an unsupported numeric statement, and the wrong verdict embedded in a negation. Keep identity checks separate from semantic correctness and do not label all passing IDs as verified facts.

Confidence: High for checker and caption wording. The test file contains definitions, not this reviewer's observed test results, and no model was called. -->

---

# The browser enables permissive missing-check handling by default

Risk | IC-07 | T1-4 | P1

The sidebar sets st.session_state.allow_missing to True when the key is absent and passes that value into analyze and assess. With this option, an unregistered required check is unknown but nonmaterial. The callable assess and run_checks signatures default to False. Thus the strict API default and permissive browser default are different source facts.

Why it matters: If a required check is unavailable, a fresh browser session can exclude it from the deciding material set unless the user changes Settings. The UI does disclose pending checks and ...
Next check: In an authorized fresh-session test with a synthetic card requiring an unregistered check, inspect the initial toggle and resulting state. Compare the strict API, initial UI and explicit permissive opt-in. No ordinary approved ...

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L495-L501)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L537-L541)
- [Source 3](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L264-L274)
- [Source 4](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/__init__.py#L79-L105)
- [Source 5](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L133-L148)

<!-- Speaker notes: The sidebar sets st.session_state.allow_missing to True when the key is absent and passes that value into analyze and assess. With this option, an unregistered required check is unknown but nonmaterial. The callable assess and run_checks signatures default to False. Thus the strict API default and permissive browser default are different source facts.

Make strict handling the initial browser default, or give permissive runs a distinct incomplete/development state that cannot be confused with ordinary readiness. Keep the disclosure and test the browser entry point separately from the core API.

Acceptance: In an authorized fresh-session test with a synthetic card requiring an unregistered check, inspect the initial toggle and resulting state. Compare the strict API, initial UI and explicit permissive opt-in. No ordinary approved result should conceal the pending requirement.

Confidence: High for initialization and call flow. The browser was not executed by this reviewer; an API-only default probe does not answer this UI question. -->

---

# The analysis cache signature omits release-file identity

Risk | IC-08 | T1-3 | P1

inputs_sig enumerates card YAML and tower Python paths with modification times, but not release data. analyze is decorated with st.cache_data and receives the release path, card ID, missing-check option, that signature and optional custom-card JSON. Reading release bytes happens inside the cached body. Replacing data at the same path does not change ...

Why it matters: Under the documented cache contract, unchanged arguments and source can reuse an earlier result even when a release file changed in place. This is conditional on path reuse and a ...
Next check: On invented data, run a comparison, replace one value at the same release path without changing code/cards, and rerun. The cached result must either refresh to the new input digest or explicitly refuse ...

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L257-L274)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L277-L292)
- [Source 3](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L537-L541)

<!-- Speaker notes: inputs_sig enumerates card YAML and tower Python paths with modification times, but not release data. analyze is decorated with st.cache_data and receives the release path, card ID, missing-check option, that signature and optional custom-card JSON. Reading release bytes happens inside the cached body. Replacing data at the same path does not change the explicitly supplied data identity.

Pass a content-bound release manifest or immutable release-version identity into every cached analysis and board call. Show which version the result represents and invalidate all derived views together. A code/card timestamp signature should remain a separate policy-version input.

Acceptance: On invented data, run a comparison, replace one value at the same release path without changing code/cards, and rerun. The cached result must either refresh to the new input digest or explicitly refuse the changed immutable release. Retain an unchanged-input cache-hit control.

Confidence: High for the inspected cache arguments and official cache contract; stale-result behavior has not been reproduced here. -->

---

# Sign-off invalidation does not compare the evidence digests

Risk | IC-09 | T1-6 | P1

signed stores findings and readiness digests in the receipt. The live UI's separate signature contains current repair/issue decisions, verdict, sign-off choice, note and reviewer fields, but no findings/readiness digest, input-file digest or complete card policy. It clears signed state only when that narrower signature changes, and the overview reports Signed whenever the ...

Why it matters: A changed policy or refreshed evidence can retain the same verdict and decision IDs while differing from the evidence a reviewer signed. The saved old receipt still identifies its old ...
Next check: Sign an invented result, then change a card's material policy or evidence while keeping verdict and decision IDs the same. After recomputation, the current result must be Pending or explicitly show that the ...

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L47-L63)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L575-L588)
- [Source 3](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L690-L713)
- [Source 4](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L1141-L1153)

<!-- Speaker notes: signed stores findings and readiness digests in the receipt. The live UI's separate signature contains current repair/issue decisions, verdict, sign-off choice, note and reviewer fields, but no findings/readiness digest, input-file digest or complete card policy. It clears signed state only when that narrower signature changes, and the overview reports Signed whenever the retained signed object exists.

Build the live invalidation identity from the same canonical evidence/policy digests used in the receipt, alongside reviewer decisions. Preserve the old receipt as history and require a new decision for a changed evidence version. Exclude only documented nondeterministic display fields from canonicalization.

Acceptance: Sign an invented result, then change a card's material policy or evidence while keeping verdict and decision IDs the same. After recomputation, the current result must be Pending or explicitly show that the retained signature covers an older version. The original receipt must remain unchanged.

Confidence: High for the missing fields in the invalidation signature and the Signed display predicate; no session-level reproduction was executed here. -->

---

# The optional summary cache is keyed only by release label and card ID

Risk | IC-10 | T1-7 | P2

ai_box retrieves generated text under ai|release_label|card_id and reuses it until the user requests another summary. That key excludes current findings, readiness, card policy and missing-check setting. The analysis path can recompute when those settings or card timestamps change, while the stored summary remains under the same key.

Why it matters: Optional prose can describe an older result beside a newly recomputed verdict or reason. The UI's accurate citation-ID captions do not establish that cached prose belongs to the current evidence ...
Next check: Mock model output for one invented context, then change the missing-check policy or a card's reasons with the same release label and card ID. The old summary must disappear or carry an explicit ...

- [Source 1](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L655-L674)
- [Source 2](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L675-L687)
- [Source 3](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L537-L541)
- [Source 4](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/ai_summary.py#L50-L66)
- [Source 5](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/ai_summary.py#L121-L131)

<!-- Speaker notes: ai_box retrieves generated text under ai|release_label|card_id and reuses it until the user requests another summary. That key excludes current findings, readiness, card policy and missing-check setting. The analysis path can recompute when those settings or card timestamps change, while the stored summary remains under the same key.

Bind the summary to a canonical digest of the exact context sent to the model. Invalidate or visibly mark old prose when context changes, retain its prior version if useful, and keep deterministic results available without a model.

Acceptance: Mock model output for one invented context, then change the missing-check policy or a card's reasons with the same release label and card ID. The old summary must disappear or carry an explicit old-version label until regenerated. No network call is required.

Confidence: High for session key construction and reuse. Actual model behavior and UI refresh were not tested. -->

---

# Before A Judging Decision



Resolve evidence gaps before interpreting readiness

Confirm the final commit and intended product.
Run the named synthetic follow-up checks in an authorized environment.
Observe a fresh-machine workflow and exported result.
Keep untested claims, proposed scores and clinical claims out of the conclusion.


<!-- Speaker notes:  -->

---
