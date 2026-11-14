# SNS Control Tower: Reconstruction Follow-Through - Concise Slides

Revision 4. Earlier artifacts remain unchanged. One finding per slide. Updated 2026-11-14T20:49:04.935751+00:00.

# SNS Control Tower: Reconstruction Follow-Through



Professor Bear - Independent Audit

Track 1: cohort-control-tower
Commit c1e8b79a2987
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

# A missing required filter input silently leaves the cohort unchanged

Risk - SN-08 - T1-1

A required clinical filter has no error branch when its field is absent. The parallel invented-data CLI case corroborates the consequence: forty rows exported without an eligibility error.

Judge follow-up: Require an explicit unavailable-filter state. Keep a valid-field control and distinguish diagnostic output from an approved cohort.

- [Source 1](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L9-L20)
- [Source 2](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L166-L176)
- [Source 3](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L198-L202)
- [Source 4](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L163-L189)
- [Source 5](https://github.com/nikbearbrown/neu-oncosys-hackathon-challenge/blob/12b33dbb498402b7e8bf0a45a83a91521b31977b/professor-bear/sns-cohort-control-tower/evidence/reconstruction-parity.json)

<!-- Speaker notes: Built-in A1 requires a usable ER status and A2 requires a nonempty subtype call. The require_value branch filters working only if a clinical table exists and contains the requested column. There is no else error or unavailable state. With an existing recognized table lacking that column, the step can be logged with unchanged counts and the CLI proceeds to write the cohort.

Validate every required table and field before applying cohort steps. On missing evidence, stop the approved export or emit a visibly incomplete diagnostic result with an explicit skipped/error step and reason. Do not treat a missing prerequisite as a successful no-op.

Acceptance: Use a valid invented clinical table with sample IDs but omit the ER column, then the subtype column. The corresponding built-in cohort must identify an unavailable eligibility test and must not present an ordinary filtered success. Retain a valid-field control.

Confidence: High for the conditional branch and export caller. Full CLI and UI outcomes remain untested in this source pass.

Later evidence qualification: This source reviewer did not run the fixture. The separately published missing-required-column case reports CLI exit zero, forty exported rows and forty reconstructed rows. This is a targeted case, not a detection-rate estimate. -->

---

# The main cohort and reconstruction use different clinical inputs

Risk - SN-09 - T1-5

The main cohort accepts a clinical-file fallback that reconstruction does not repeat. Parallel missing-B-clinical and clinical-CSV cases exported thirty-nine members but reconstructed forty. The normal control matched.

Judge follow-up: Share a versioned transformation and exact input map. Verify sorted membership parity, not just successful file creation.

- [Source 1](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L140-L142)
- [Source 2](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L166-L176)
- [Source 3](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L77-L81)
- [Source 4](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L116-L128)
- [Source 5](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L191-L193)
- [Source 6](https://github.com/nikbearbrown/neu-oncosys-hackathon-challenge/blob/12b33dbb498402b7e8bf0a45a83a91521b31977b/professor-bear/sns-cohort-control-tower/evidence/reconstruction-parity.json)

<!-- Speaker notes: run_cohort falls back to clinical data from release A when none is loaded from B. The generated script looks only for B/clinical.tsv and skips require_value when that clinical object is None. Although it declares RELEASE_A, the generated clinical-loading and filter path does not reproduce the main engine's fallback.

Share one versioned transformation implementation or serialize the exact resolved input map into the reconstruction. Make any cross-release fallback explicit and hash-bound, or reject missing B prerequisites consistently in both paths. Compare exact membership, not just row count.

Acceptance: Create invented A labels that exclude at least one B protein sample, omit B clinical data and run the A1 export and reconstruction in an authorized isolated environment. Both must either refuse the same missing evidence or produce identical sorted sample IDs with the same declared input provenance.

Confidence: High for divergent source policies. The proposed parity fixture has not been executed.

Later evidence qualification: The separate parallel observations report one additional reconstructed member in each fallback case and equality for the normal case. They corroborate the source path under those conditions, not every normal full-release run. -->

---

# The A2 reconstruction embeds a JSON boolean as a Python name

Risk - SN-10 - T1-5

The A2 generator writes JSON directly into Python source. Its lowercase true token becomes an unresolved Python name. The parallel review reproduced a NameError with an A1 reconstruction passing as a control.

Judge follow-up: Encode a quoted JSON string or supported Python literals. Check exact reconstruction membership after the serialization fix.

- [Source 1](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L17-L29)
- [Source 2](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L16-L20)
- [Source 3](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/cohort.py#L125-L132)
- [Source 4](https://github.com/nikbearbrown/neu-oncosys-hackathon-challenge/blob/07721d9/professor-bear/sns-cohort-control-tower/evidence/synthetic-probes-round3.json)

<!-- Speaker notes: The generator writes SPEC = followed by json.dumps(spec). The built-in A2 spec contains not_empty=True, which JSON serializes as lowercase true. In Python source, that token is a name rather than the True literal, and the generated script shown here defines no name true. The ordinary A2 specification therefore contains an unresolved name in the reconstructed Python assignment.

Embed a safely quoted JSON string and call json.loads at runtime, or use repr for a supported Python-literal structure. Apply the same serialization rule to applied repairs and test booleans, null values, quotes and non-ASCII descriptions as data.

Acceptance: Export the built-in A2 specification and run its reconstruction on an authorized synthetic fixture. Verify no unresolved true/false/null names occur and exact membership matches the main engine. Keep a normal A1 control and separate syntax checks from execution checks.

Confidence: High for the generator and built-in A2 literal. No generated code was executed or represented as a passed/failed runtime test by this reviewer.

Later evidence qualification: This overlaps the main report's issue 6 and is not a second scoring event. The source reviewer did not execute the generated script. Syntax parsing alone cannot catch a valid but unresolved bare name. -->

---

# Judging Limits



The official rubric and human judges determine the result.

Confirm the final submission commit.
Separate source conclusions from observed runs and policy recommendations.
Different test counts do not establish a cross-team ranking.


<!-- Speaker notes:  -->

---
