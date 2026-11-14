# SNS Cohort Control Tower - Concise Slides

Revision 2. Earlier artifacts remain unchanged. One finding per slide. Updated 2026-11-14T20:20:41.956710+00:00.

# SNS Cohort Control Tower



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

# A failed candidate analysis has an explicit uncertainty route

Strength - SN-05 - T1-4

The candidate-analysis error branch returns Insufficient Evidence before the ordinary Ready path. This explicit uncertainty route should remain while movement precedence changes.

Judge follow-up: Add baseline-error and nonfinite-output controls without weakening the existing candidate-error guard.

- [Source 1](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/impact.py#L187-L199)

<!-- Speaker notes: Before the no-finding branch, verdict_for checks the candidate analysis error field and returns Insufficient Evidence with its reason. This prevents a known candidate execution failure from automatically taking the ordinary Ready route.

Preserve this error-first behavior and extend typed execution states to baseline failure, nonfinite results and missing expected analyses. Avoid interpreting a missing error key as proof that numerical outputs are valid.

Acceptance: Supply an explicit candidate error with no affecting findings and verify Insufficient Evidence. Add baseline-error, nonfinite-output and valid-result controls and document the intended policy for each.

Confidence: High for the inspected branch; runtime tests were not executed by this reviewer. -->

---

# Release provenance includes named content hashes

Strength - SN-06 - T1-3

The export names recognized files and their content SHA-256 values. These fingerprints support reproducibility and cache reuse when bytes match.

Judge follow-up: Include skipped inputs too. Bind derived cohorts and approval records to the same manifest.

- [Source 1](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/release.py#L88-L106)
- [Source 2](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/findings.py#L458-L470)

<!-- Speaker notes: load_release computes a content digest and can reuse a parsed layer only when its prior digest matches. The findings document emits each release's file names, SHA-256 values and hash_of=content. This distinguishes content identity from a directory label or mutable filename.

Keep content fingerprints and add a complete discovered-file inventory, including unsupported or skipped files. Bind review decisions and derived cohorts to the same evidence manifest.

Acceptance: Change one synthetic file byte and confirm its digest and run identity change. Verify a renamed identical file is handled according to the documented identity policy and that unsupported files remain visible.

Confidence: High for source construction; cache correctness and served artifact hashes were not verified in a running app. -->

---

# Before, after and simulated repair results are inspectable

Strength - SN-07 - T1-7

Before, after and simulated repair results expose a proposal's numerical effect. Returning to the baseline number only demonstrates recovery under an assumed trusted baseline.

Judge follow-up: Keep simulations visible and require independent evidence before approving a reversal.

- [Source 1](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/findings.py#L427-L450)
- [Source 2](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/impact.py#L237-L254)

<!-- Speaker notes: Each analysis entry includes baseline, candidate and simulated repaired output, inputs, used features, affecting findings and a repair_restores_before equality field. The assessment layer builds a temporary repaired release and removes that temporary directory in finally. These are simulations relative to the assumed baseline, not independent truth checks.

Label the third result as a baseline-recovery simulation and state the trust assumption beside it. Require independent evidence and human authorization before using simulated recovery as an approved repair.

Acceptance: Demonstrate a legitimate documented correction in B and a separate erroneous alteration. Both may differ from A, but only evidence and a reviewer decision should authorize reversal; equality with A must not substitute for that evidence.

Confidence: High for exported comparison fields and temporary simulation structure; numerical correctness and baseline truth remain untested. -->

---

# Cohort repair parsing does not consult approval decisions

Risk - SN-01 - T1-4

Cohort repair parsing consumes proposed repairs without consulting decisions. A rejected exclusion can therefore affect the derived cohort even while original files remain untouched.

Judge follow-up: Require evidence-bound approval for approved exports. Label unapproved simulations separately.

- [Source 1](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L45-L69)
- [Source 2](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L123-L137)
- [Source 3](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L148-L160)

<!-- Speaker notes: parse_repairs iterates every repair proposal and derives excluded, flagged, restored and relabeled sets without reading decisions. run_cohort calls that parser and applies its mapping during require_file steps. The parser does not distinguish an approved proposal from an explicitly rejected or undecided one.

For approved exports, accept only explicit approved decisions bound to the exact findings digest. Retain a separately labeled simulation mode for proposals and make its non-approved status travel with every output file.

Acceptance: Provide a rejected exclusion, an undecided proposal and an approved repair. Only the approved action may affect an approved cohort; a preview may simulate others but must remain unmistakably unapproved.

Confidence: High for parser and caller control flow; the parallel TESTS.md reports a rejected-exclusion helper reproduction, not a complete UI run. -->

---

# Flagging an absent sample can also restore it

Risk - SN-02 - T1-6

Flagging a sample absent from B can restore it from A. The caller explicitly adds that flagged sample back to the working cohort.

Judge follow-up: Keep investigation and restoration separate. An absent sample needs an approved restore action.

- [Source 1](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L89-L113)
- [Source 2](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L148-L160)

<!-- Speaker notes: _apply_file_repairs adds a flagged sample back when it is absent from B but present in A, recording flag_for_review_restored. The require_file caller then explicitly re-adds flagged samples after its intersection. The source therefore assigns a membership-changing behavior to a review flag.

Keep flagging and restoration as separate operations. An absent sample should remain absent unless an explicit restore proposal is approved with evidence explaining why the earlier membership is authoritative.

Acceptance: Use a synthetic sample deliberately absent from B. Flagging alone must not restore it; a separately authorized restore should be traceable and must not overwrite the original releases.

Confidence: High for the two membership-addition branches; the retained parallel review reports the helper effect with invented records. -->

---

# No detected finding bypasses movement and adequacy checks

Risk - SN-03 - T1-2

With no affecting finding, the verdict helper returns Ready before checking result movement or group size. The exported verification note promises more than this branch enforces.

Judge follow-up: Test unexplained movement and undersized groups alongside a valid unchanged positive control.

- [Source 1](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/impact.py#L187-L210)
- [Source 2](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/findings.py#L427-L450)

<!-- Speaker notes: verdict_for first handles an error in the new-release result, then returns Ready immediately when affected_by is empty. Minimum group size, sign changes and relative movement are tested only afterward. Exported analysis notes say unaffected analyses were rerun to confirm no movement, but this branch does not require that confirmation.

Assess result validity, required evidence and unexplained movement before the no-finding Ready return. Export both compatibility and adequacy states if they answer different questions.

Acceptance: Compare no-finding cases with an unchanged adequate result, an undersized result and a sign change. Keep the valid stable positive control, and ensure absence of a finding alone cannot override the latter evidence problems.

Confidence: High for precedence; the parallel review reports helper probes with a detected-sign-change positive control. -->

---

# Wide-table recognition depends on having more than ten samples

Risk - SN-04 - T1-1

Wide-table recognition requires more than ten TCGA sample columns. Smaller valid wide inputs can fall through and disappear from the recognized release layers.

Judge follow-up: Parse or explicitly reject equivalent 1-, 10- and 11-sample matrices. Retain unsupported files in the inventory.

- [Source 1](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/release.py#L60-L85)
- [Source 2](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/release.py#L88-L106)

<!-- Speaker notes: load_layer recognizes a TCGA-wide layout only with more than ten TCGA-named columns and the stated proportion. A smaller wide table falls through to long-format ID detection and may return None. load_release retains only non-None layers, without an explicit unsupported-file result in that loop.

Use declared schema or robust header semantics independent of sample count. Record every discovered but unsupported file and prevent omission from being mistaken for absence or a clean comparison.

Acceptance: Load otherwise equivalent invented wide matrices with 1, 10 and 11 samples. Each must be parsed consistently or explicitly rejected, and the release inventory must retain the file and reason.

Confidence: High for the hard boundary; the parallel TESTS.md reports 1/10/11-sample probes and the 11-sample positive control. -->

---

# Judging Limits



The official rubric and human judges determine the result.

Confirm the final submission commit.
Separate source conclusions from observed runs and policy recommendations.
Different test counts do not establish a cross-team ranking.


<!-- Speaker notes:  -->

---
