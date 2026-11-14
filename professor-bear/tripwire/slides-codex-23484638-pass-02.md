# Tripwire / Driftwire - Concise Slides

Revision 2. Earlier artifacts remain unchanged. One finding per slide. Updated 2026-11-14T20:20:41.919442+00:00.

# Tripwire / Driftwire



Professor Bear - Independent Audit

Track 1: cohort-control-tower
Commit 45df43640836
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

# Missing inputs and empty cohorts are not silently passed

Strength - TW-04 - T1-1

The builder explicitly rejects missing required files, missing fields and empty eligible cohorts as Insufficient Evidence. This limits the scope of the adequacy concern.

Judge follow-up: Retain separate missing-file, dropped-target and empty-cohort controls.

- [Source 1](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/findings.py#L153-L173)
- [Source 2](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/analyses.py#L26-L34)

<!-- Speaker notes: Before analytical execution, the builder checks required files in both releases, required fields and nonempty eligible cohorts. Each failure appends an explicit Insufficient Evidence analysis result and continues. This is separate from the undersized-but-nonempty adequacy issue above.

Retain these guards and expose their reasons in every consumer. Extend explicit checks to finite measurement counts and clarify where group-level adequacy belongs.

Acceptance: Independently omit a required file, drop ERALPHA, remove all eligible samples and supply valid inputs. Verify the first three name the missing evidence and the valid control reaches analysis execution.

Confidence: High for the inspected preflight branches; runtime behavior was not exercised here. -->

---

# Unaffected analyses have a transparent verification route

Strength - TW-05 - T1-2

Dependency mapping uses file, field and cohort membership. Optional verification reruns cross-check analyses that the map calls unaffected, and the export states why each rerun occurred.

Judge follow-up: Compare verification on and off. Separate required recomputation from the cost of cross-checking.

- [Source 1](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/impact.py#L47-L66)
- [Source 2](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/impact.py#L69-L82)
- [Source 3](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/config.py#L19-L21)
- [Source 4](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/findings.py#L174-L190)

<!-- Speaker notes: The impact map evaluates relevant files, fields and the union of eligible samples from both releases. verify_unaffected defaults to true, so the builder can rerun supposedly unaffected analyses and compare actual slices. Exported rerun_reason distinguishes affected execution from verification rather than disguising verification as required work.

Keep the explicit reason and expose the verification toggle and its cost. Add an input-slice digest and regression controls when analyses or cohort policies change.

Acceptance: Change an unused field, then an A1 field in an eligible sample. Compare runs with verification enabled and disabled; show which executions were necessary, which were cross-checks, and how unexplained movement is surfaced.

Confidence: High for dependency and rerun structure; performance and detection coverage remain unmeasured. -->

---

# Repair decisions require a reason and reviewer role

Strength - TW-06 - T1-6

Repair decisions require a supported action, a reason and a reviewer role. The helper copies the document and preserves source data. It records a current snapshot.

Judge follow-up: Keep validation and preserve earlier events if the product promises review history.

- [Source 1](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L14-L34)

<!-- Speaker notes: apply_decisions rejects unknown repair IDs, unsupported decisions, blank reasons and blank reviewer roles. It deep-copies the document and records original_preserved without applying the repair to source data. The resulting decisions field is a current snapshot, not an immutable history.

Preserve reason and role validation. For repeated reviews, add timestamped evidence-bound events and derive the current snapshot separately; do not present a role string as authenticated identity.

Acceptance: Attempt an unknown repair and blank reason/role, then record an authorized decision. Verify invalid requests fail, the original document remains unchanged, and later revisions preserve a distinguishable history if history is claimed.

Confidence: High for helper validation and copying; authentication, persistence and UI behavior remain untested. -->

---

# Local compatibility can be Ready before adequacy is checked

Risk - TW-01 - T1-2

The compatibility helper can return Ready before checking sample adequacy. A later parallel full-API probe found release compatibility Ready while question readiness correctly said Insufficient Evidence.

Judge follow-up: Ask users to distinguish compatibility from adequacy. Preserve both results and their different meanings.

- [Source 1](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/verdicts.py#L24-L45)
- [Source 2](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/findings.py#L153-L173)
- [Source 3](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/analyses.py#L119-L127)
- [Source 4](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/config.py#L5-L10)

<!-- Speaker notes: release_verdict handles the unaffected branch before movement.insufficient. With an unmoved result and unchanged input slice it returns Ready even if the movement object reports insufficient samples. The builder rejects missing files, missing fields and empty cohorts first, and question readiness is separate. This is a local compatibility-field issue, not evidence that all small-cohort end-to-end results are Ready.

Either check adequacy before compatibility returns or export compatibility and adequacy as distinct, explicitly labeled dimensions. Preserve the outer guards and question checks rather than conflating their meanings.

Acceptance: Trace an unchanged nonempty cohort below the configured minimum through the helper, A1/A2 fields, selected question and overall output. Require a visible adequacy warning wherever compatibility is Ready, and retain a sufficiently sized unchanged control.

Confidence: High for branch ordering; end-to-end generalization is explicitly limited by the retained counterexample.

Update: parallel review commit 1191871 reports a corrected full-API four-sample probe with release compatibility Ready and question readiness Insufficient Evidence. The earlier malformed fixture was Blocked. These observations distinguish compatibility from adequacy. -->

---

# Recorded review activity is not the same as resolved evidence

Risk - TW-02 - T1-4

The open-review helper counts request_more_evidence as decided. A flagged finding with no linked repair also drops out of the open list.

Judge follow-up: Keep requests for evidence unresolved. Require a finding-level disposition when no repair exists.

- [Source 1](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L10-L17)
- [Source 2](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L21-L34)
- [Source 3](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L37-L46)

<!-- Speaker notes: review_status considers any repair ID appearing in decisions to be decided, regardless of whether its decision is request_more_evidence. A flagged finding with no linked repair also disappears from open because all over an empty list is true. apply_decisions explicitly permits request_more_evidence. These are helper semantics; a user-interface approval bypass was not established here.

Represent reviewed, awaiting evidence, rejected, approved and unresolved finding states separately. Require an explicit finding-level disposition when no repair exists and keep evidence requests open until their stated conditions are satisfied.

Acceptance: Use synthetic documents with a flagged finding and no repair, then a linked repair with request_more_evidence, reject and approve. Verify each exported state communicates its distinct meaning and that requesting evidence never appears as authorization to proceed.

Confidence: High for the inspected list construction; parallel helper reproductions are attributed in the retained TESTS.md. -->

---

# Display precision participates in analytical decisions

Risk - TW-03 - T1-3

A1 rounds its numerical results before classifying movement. Input-slice evidence can still reveal a change, but it cannot restore precision lost from the effect calculation.

Judge follow-up: Probe near-zero effects. Display precision should not change the analytical classification.

- [Source 1](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/analyses.py#L91-L110)
- [Source 2](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/analyses.py#L119-L127)

<!-- Speaker notes: A1 rounds means and the group difference to three decimals before a1_compare computes relative movement and direction. Its input slice retains repr of the numeric value, so a slice change can still be visible even when the displayed analytical difference is quantized. The concern is classification fidelity, not a claim that every small input change is wholly undetected.

Keep full-precision analytical fields and format display text separately. Define absolute as well as relative tolerances near zero, and document whether baseline adequacy is assumed or assessed.

Acceptance: Compare full-precision near-zero effects on either side of a tolerance and a zero-crossing boundary. Changing display precision must not change classification, and input-slice evidence must remain visible even when the final aggregate is unchanged.

Confidence: High for precision flow; no numerical fixture or organizer parity test was executed by this reviewer. -->

---

# Judging Limits



The official rubric and human judges determine the result.

Confirm the final submission commit.
Separate source conclusions from observed runs and policy recommendations.
Different test counts do not establish a cross-team ranking.


<!-- Speaker notes:  -->

---
