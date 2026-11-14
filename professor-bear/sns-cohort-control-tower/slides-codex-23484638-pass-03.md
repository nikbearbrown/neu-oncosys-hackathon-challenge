# SNS Control Tower: Reconstruction Follow-Through



Professor Bear | Independent Audit

Track 1: cohort-control-tower
Commit c1e8b79a2987
Static source review; no official score


<!-- Speaker notes:  -->

---

# Review Scope



Committed source, not an observed demo

56 text files collected; 82 entries excluded.
Selected implementation paths were inspected.
No submission code, tests, data fetches or sealed inputs were run.
The official freeze commit still needs confirmation.


<!-- Speaker notes:  -->

---

# A missing required filter input silently leaves the cohort unchanged

Risk | SN-08 | T1-1 | P1

Built-in A1 requires a usable ER status and A2 requires a nonempty subtype call. The require_value branch filters working only if a clinical table exists and contains the requested column. There is no else error or unavailable state. With an existing recognized table lacking that column, the step can be logged with ...

Why it matters: Membership can include samples whose required eligibility cannot be evaluated. An unchanged count does not tell the researcher that the promised filter was skipped. This is a source-derived path for ...
Next check: Use a valid invented clinical table with sample IDs but omit the ER column, then the subtype column. The corresponding built-in cohort must identify an unavailable eligibility test and must not present an ...

- [Source 1](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L9-L20)
- [Source 2](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L166-L176)
- [Source 3](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L198-L202)
- [Source 4](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L163-L189)

<!-- Speaker notes: Built-in A1 requires a usable ER status and A2 requires a nonempty subtype call. The require_value branch filters working only if a clinical table exists and contains the requested column. There is no else error or unavailable state. With an existing recognized table lacking that column, the step can be logged with unchanged counts and the CLI proceeds to write the cohort.

Validate every required table and field before applying cohort steps. On missing evidence, stop the approved export or emit a visibly incomplete diagnostic result with an explicit skipped/error step and reason. Do not treat a missing prerequisite as a successful no-op.

Acceptance: Use a valid invented clinical table with sample IDs but omit the ER column, then the subtype column. The corresponding built-in cohort must identify an unavailable eligibility test and must not present an ordinary filtered success. Retain a valid-field control.

Confidence: High for the conditional branch and export caller. Full CLI and UI outcomes remain untested in this source pass. -->

---

# The main cohort and reconstruction use different clinical inputs

Risk | SN-09 | T1-5 | P1

run_cohort falls back to clinical data from release A when none is loaded from B. The generated script looks only for B/clinical.tsv and skips require_value when that clinical object is None. Although it declares RELEASE_A, the generated clinical-loading and filter path does not reproduce the main engine's fallback.

Why it matters: For A1 with a recognized protein layer in B, no clinical table in B and a usable clinical table in A, the main export can filter with A while reconstruction ...
Next check: Create invented A labels that exclude at least one B protein sample, omit B clinical data and run the A1 export and reconstruction in an authorized isolated environment. Both must either refuse the ...

- [Source 1](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L140-L142)
- [Source 2](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L166-L176)
- [Source 3](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L77-L81)
- [Source 4](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L116-L128)
- [Source 5](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L191-L193)

<!-- Speaker notes: run_cohort falls back to clinical data from release A when none is loaded from B. The generated script looks only for B/clinical.tsv and skips require_value when that clinical object is None. Although it declares RELEASE_A, the generated clinical-loading and filter path does not reproduce the main engine's fallback.

Share one versioned transformation implementation or serialize the exact resolved input map into the reconstruction. Make any cross-release fallback explicit and hash-bound, or reject missing B prerequisites consistently in both paths. Compare exact membership, not just row count.

Acceptance: Create invented A labels that exclude at least one B protein sample, omit B clinical data and run the A1 export and reconstruction in an authorized isolated environment. Both must either refuse the same missing evidence or produce identical sorted sample IDs with the same declared input provenance.

Confidence: High for divergent source policies. The proposed parity fixture has not been executed. -->

---

# The A2 reconstruction embeds a JSON boolean as a Python name

Risk | SN-10 | T1-5 | P1

The generator writes SPEC = followed by json.dumps(spec). The built-in A2 spec contains not_empty=True, which JSON serializes as lowercase true. In Python source, that token is a name rather than the True literal, and the generated script shown here defines no name true. The ordinary A2 specification therefore contains an unresolved name ...

Why it matters: The standalone reconstruction can fail before rebuilding membership even when the main cohort export succeeded. Syntax parsing alone will not catch this particular defect because a bare name is valid ...
Next check: Export the built-in A2 specification and run its reconstruction on an authorized synthetic fixture. Verify no unresolved true/false/null names occur and exact membership matches the main engine. Keep a normal A1 control and ...

- [Source 1](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L17-L29)
- [Source 2](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L16-L20)
- [Source 3](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L125-L132)

<!-- Speaker notes: The generator writes SPEC = followed by json.dumps(spec). The built-in A2 spec contains not_empty=True, which JSON serializes as lowercase true. In Python source, that token is a name rather than the True literal, and the generated script shown here defines no name true. The ordinary A2 specification therefore contains an unresolved name in the reconstructed Python assignment.

Embed a safely quoted JSON string and call json.loads at runtime, or use repr for a supported Python-literal structure. Apply the same serialization rule to applied repairs and test booleans, null values, quotes and non-ASCII descriptions as data.

Acceptance: Export the built-in A2 specification and run its reconstruction on an authorized synthetic fixture. Verify no unresolved true/false/null names occur and exact membership matches the main engine. Keep a normal A1 control and separate syntax checks from execution checks.

Confidence: High for the generator and built-in A2 literal. No generated code was executed or represented as a passed/failed runtime test by this reviewer. -->

---

# Before A Judging Decision



Resolve evidence gaps before interpreting readiness

Confirm the final commit and intended product.
Run the named synthetic follow-up checks in an authorized environment.
Observe a fresh-machine workflow and exported result.
Keep untested claims, proposed scores and clinical claims out of the conclusion.


<!-- Speaker notes:  -->

---
