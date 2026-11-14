# ReadySet Control Tower - Concise Slides

Revision 2. Earlier artifacts remain unchanged. One finding per slide. Updated 2026-11-14T20:20:41.906504+00:00.

# ReadySet Control Tower



Professor Bear - Independent Audit

Track 1: cohort-control-tower
Commit 4dd07736e99f
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

# Changes are mapped to the selected analysis before rerunning

Strength - RS-04 - T1-2

The comparison connects changes to fields and samples used by each analysis. This supports a reasoned distinction between affected and unaffected results.

Judge follow-up: Change an unused field and a required target field. Explain the different rerun decisions.

- [Source 1](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L138-L151)
- [Source 2](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L153-L171)

<!-- Speaker notes: Each finding is mapped through the analysis's touched_by function with used samples and per-file samples from both releases. Analyses without a mapped finding receive a not_rerun explanation; affected analyses are calculated before and after.

Retain the explicit impact explanation and selective rerun path. Add the independent input-validity gate described above without removing this separation.

Acceptance: Change a protein value outside A1's cohort and then a value inside it. Demonstrate different affected-analysis decisions and preserve an unchanged A2 result with an evidence-backed reason.

Confidence: High for implementation structure; numerical equivalence to organizer analyses has not been executed here. -->

---

# The export retains evidence rules and isolated per-finding effects

Strength - RS-05 - T1-3

Per-event counterfactual calculations help a reviewer separate one finding's effect from the total release change. A counterfactual remains a model of an intervention.

Judge follow-up: Compare the event-level witness with the full release result. Keep the assumptions visible.

- [Source 1](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L342-L365)
- [Source 2](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L249-L255)

<!-- Speaker notes: The engine computes an analysis on the trusted inputs and again with only one finding's changes applied, then stores before, after, size, measure and relative movement. The export includes rules, effects, file summaries and witness data in x_readyset.

Keep the counterfactual calculation and expose its exact assumptions. State when effects cannot be computed and avoid implying that isolated effects add linearly.

Acceptance: Use two synthetic changes with opposing effects. Show each isolated effect, the combined result and an unavailable-effect case; confirm the displayed claims distinguish these quantities.

Confidence: High for the code and exported fields; the calculations have not been independently rerun. -->

---

# Repair urgency is tied to both measured effect and uncertainty

Strength - RS-06 - T1-6

Repair priorities and review flags make the handoff concrete. They preserve a place for human judgment instead of treating a proposed correction as established truth.

Judge follow-up: Follow one proposal through evidence, priority and a recorded decision. Preserve the original inputs.

- [Source 1](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L186-L200)
- [Source 2](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L369-L391)

<!-- Speaker notes: The priority function distinguishes changes outside the question, unavailable reruns, large isolated effects, identity swaps/copies and smaller effects. Findings require human review and carry limitations, and repairs refer back to the finding they address.

Retain these explanations and require a live reviewer to demonstrate approval, rejection and unresolved evidence before sign-off. Treat the half-percent convention as a configurable research rule, not a validated universal threshold.

Acceptance: Show one unrelated finding, one noncomputable result and one small effect. Check that their repair urgency differs and that the exported findings and original input hashes are preserved through review.

Confidence: High for the priority and export construction; human-review UI behavior is not tested. -->

---

# Required files absent from both releases do not make the verdict insufficient

Risk - RS-01 - T1-1

When both releases lack a required file, the comparison records absence and continues. That shortcut can leave missing evidence outside the analysis verdict.

Judge follow-up: Check two releases missing the same required file. Show the missing evidence before interpreting compatibility.

- [Source 1](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L75-L82)
- [Source 2](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L153-L162)
- [Source 3](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L220-L227)
- [Source 4](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/analyses.py#L107-L113)

<!-- Speaker notes: The file loop records an absent file and immediately continues when both paths are missing. The insufficient flag remains false. An analysis with no mapped finding is not rerun, and the final fallback verdict is Ready. MeanByGroup.used also turns missing inputs into an empty set. Together these paths permit an empty or equally incomplete pair of release folders to look unchanged rather than unassessable. This is a source-derived control-flow conclusion, not an executed reproduction.

Preflight the mandatory inputs for every selected analysis in each release independently of the diff. Record unavailable inputs as evidence and produce Insufficient Evidence before selective rerun logic. Preserve the intentional optional-RNA exception only for questions that genuinely do not need RNA.

Acceptance: Using authorized synthetic fixtures, compare two empty folders, two folders both missing protein for A1, and two valid unchanged releases. The first two should be Insufficient Evidence with named inputs; the third may be Ready. Repeat with A2-only and optional RNA absent.

Confidence: High for the inspected control flow; runtime and CLI-level handling remain untested. -->

---

# Identical content is skipped before readability or analytical validity is established

Risk - RS-02 - T1-4

Byte-identical inputs can skip parsing and analysis. Equality alone cannot establish that a file is readable or has the required fields.

Judge follow-up: Compare identical invalid files and identical valid files. Keep compatibility separate from baseline fitness.

- [Source 1](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L114-L136)
- [Source 2](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/tests/test_empty_inputs.py#L22-L37)

<!-- Speaker notes: The comparison skips a file immediately when its content hash matches. The later unreadable-table handler only covers compare_file on changed content. Thus identical malformed or empty contents do not traverse that handler. Existing empty-input tests mutate only the new release, so their successful definitions do not establish coverage of identical bad inputs.

Validate the baseline and candidate against the selected question before using the equality shortcut, or reuse a validity receipt bound to the exact content hash and question. Keep file equality and analysis readiness as separate states.

Acceptance: Create identical zero-byte clinical files, identical invalid tables and identical valid files with no eligible ER group. None should receive an unqualified Ready verdict. Include a valid identical positive control and verify that a cached validity receipt is invalidated by input or question changes.

Confidence: High that the shortcut precedes changed-file parsing; actual end-to-end outcomes require the stated follow-up. -->

---

# Ambiguous file variants are resolved by filesystem modification time

Risk - RS-03 - T1-3

File alias selection uses modification time. Two candidate filenames can therefore resolve differently after copying or restoring a directory.

Judge follow-up: Change timestamps without changing file contents. Resolution should follow a documented, deterministic rule.

- [Source 1](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/release.py#L33-L40)
- [Source 2](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L229-L234)

<!-- Speaker notes: path_of accepts compressed TSV, uncompressed TSV, CSV, XLSX and TXT candidates and chooses the one with the newest modification time. The choice is not made from an explicit release manifest or an ambiguity error.

Reject multiple variants by default or require an explicit file map. Include the resolved relative path and the selection rule alongside the content hash in the evidence receipt.

Acceptance: Provide different compressed and uncompressed versions of one synthetic table, change only their timestamps, and confirm the tool either refuses ambiguity or selects the same explicitly configured file. Export the selected physical path.

Confidence: High; the selection rule is explicit. Cross-machine behavior was not exercised. -->

---

# Judging Limits



The official rubric and human judges determine the result.

Confirm the final submission commit.
Separate source conclusions from observed runs and policy recommendations.
Different test counts do not establish a cross-team ranking.


<!-- Speaker notes:  -->

---
