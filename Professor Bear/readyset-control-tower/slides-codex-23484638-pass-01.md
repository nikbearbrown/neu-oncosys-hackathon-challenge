# ReadySet Control Tower



Professor Bear | Independent Audit

Track 1: cohort-control-tower
Commit 4dd07736e99f
Static source review; no official score


<!-- Speaker notes:  -->

---

# Review Scope



Committed source, not an observed demo

87 text files collected; 21 entries excluded.
Selected implementation paths were inspected.
No submission code, tests, data fetches or sealed inputs were run.
The official freeze commit still needs confirmation.


<!-- Speaker notes:  -->

---

# Changes are mapped to the selected analysis before rerunning

Strength | RS-04 | T1-2 | P2

Each finding is mapped through the analysis's touched_by function with used samples and per-file samples from both releases. Analyses without a mapped finding receive a not_rerun explanation; affected analyses are calculated before and after.

Why it matters: This directly supports the Control Tower requirement to distinguish affected from unaffected analyses rather than rerunning everything or treating equal row counts as sufficient.
Next check: Change a protein value outside A1's cohort and then a value inside it. Demonstrate different affected-analysis decisions and preserve an unchanged A2 result with an evidence-backed reason.

- [Source 1](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L138-L151)
- [Source 2](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L153-L171)

<!-- Speaker notes: Each finding is mapped through the analysis's touched_by function with used samples and per-file samples from both releases. Analyses without a mapped finding receive a not_rerun explanation; affected analyses are calculated before and after.

Retain the explicit impact explanation and selective rerun path. Add the independent input-validity gate described above without removing this separation.

Acceptance: Change a protein value outside A1's cohort and then a value inside it. Demonstrate different affected-analysis decisions and preserve an unchanged A2 result with an evidence-backed reason.

Confidence: High for implementation structure; numerical equivalence to organizer analyses has not been executed here. -->

---

# The export retains evidence rules and isolated per-finding effects

Strength | RS-05 | T1-3 | P2

The engine computes an analysis on the trusted inputs and again with only one finding's changes applied, then stores before, after, size, measure and relative movement. The export includes rules, effects, file summaries and witness data in x_readyset.

Why it matters: Reviewers can inspect why a finding matters and distinguish an isolated effect from the net effect of several changes. This is stronger evidence design than an unexplained severity label.
Next check: Use two synthetic changes with opposing effects. Show each isolated effect, the combined result and an unavailable-effect case; confirm the displayed claims distinguish these quantities.

- [Source 1](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L342-L365)
- [Source 2](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L249-L255)

<!-- Speaker notes: The engine computes an analysis on the trusted inputs and again with only one finding's changes applied, then stores before, after, size, measure and relative movement. The export includes rules, effects, file summaries and witness data in x_readyset.

Keep the counterfactual calculation and expose its exact assumptions. State when effects cannot be computed and avoid implying that isolated effects add linearly.

Acceptance: Use two synthetic changes with opposing effects. Show each isolated effect, the combined result and an unavailable-effect case; confirm the displayed claims distinguish these quantities.

Confidence: High for the code and exported fields; the calculations have not been independently rerun. -->

---

# Repair urgency is tied to both measured effect and uncertainty

Strength | RS-06 | T1-6 | P2

The priority function distinguishes changes outside the question, unavailable reruns, large isolated effects, identity swaps/copies and smaller effects. Findings require human review and carry limitations, and repairs refer back to the finding they address.

Why it matters: The review handoff names a useful next action instead of merely enumerating anomalies. Uncertainty about whether a changed release is correct is not replaced with automatic source-data editing in this ...
Next check: Show one unrelated finding, one noncomputable result and one small effect. Check that their repair urgency differs and that the exported findings and original input hashes are preserved through review.

- [Source 1](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L186-L200)
- [Source 2](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L369-L391)

<!-- Speaker notes: The priority function distinguishes changes outside the question, unavailable reruns, large isolated effects, identity swaps/copies and smaller effects. Findings require human review and carry limitations, and repairs refer back to the finding they address.

Retain these explanations and require a live reviewer to demonstrate approval, rejection and unresolved evidence before sign-off. Treat the half-percent convention as a configurable research rule, not a validated universal threshold.

Acceptance: Show one unrelated finding, one noncomputable result and one small effect. Check that their repair urgency differs and that the exported findings and original input hashes are preserved through review.

Confidence: High for the priority and export construction; human-review UI behavior is not tested. -->

---

# Required files absent from both releases do not make the verdict insufficient

Risk | RS-01 | T1-1 | P1

The file loop records an absent file and immediately continues when both paths are missing. The insufficient flag remains false. An analysis with no mapped finding is not rerun, and the final fallback verdict is Ready. MeanByGroup.used also turns missing inputs into an empty set. Together these paths permit an empty or ...

Why it matters: A judge or researcher could interpret Ready as usable inputs even though the selected analysis cannot be calculated. This affects data-problem detection and the distinction between missing evidence and an ...
Next check: Using authorized synthetic fixtures, compare two empty folders, two folders both missing protein for A1, and two valid unchanged releases. The first two should be Insufficient Evidence with named inputs; the third may ...

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

Risk | RS-02 | T1-4 | P1

The comparison skips a file immediately when its content hash matches. The later unreadable-table handler only covers compare_file on changed content. Thus identical malformed or empty contents do not traverse that handler. Existing empty-input tests mutate only the new release, so their successful definitions do not establish coverage of identical bad inputs.

Why it matters: Equality of two byte streams is not evidence that either is a valid analysis input. A missing baseline-validity gate can conceal shared corruption or an empty analytical cohort.
Next check: Create identical zero-byte clinical files, identical invalid tables and identical valid files with no eligible ER group. None should receive an unqualified Ready verdict. Include a valid identical positive control and verify that ...

- [Source 1](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L114-L136)
- [Source 2](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/tests/test_empty_inputs.py#L22-L37)

<!-- Speaker notes: The comparison skips a file immediately when its content hash matches. The later unreadable-table handler only covers compare_file on changed content. Thus identical malformed or empty contents do not traverse that handler. Existing empty-input tests mutate only the new release, so their successful definitions do not establish coverage of identical bad inputs.

Validate the baseline and candidate against the selected question before using the equality shortcut, or reuse a validity receipt bound to the exact content hash and question. Keep file equality and analysis readiness as separate states.

Acceptance: Create identical zero-byte clinical files, identical invalid tables and identical valid files with no eligible ER group. None should receive an unqualified Ready verdict. Include a valid identical positive control and verify that a cached validity receipt is invalidated by input or question changes.

Confidence: High that the shortcut precedes changed-file parsing; actual end-to-end outcomes require the stated follow-up. -->

---

# Ambiguous file variants are resolved by filesystem modification time

Risk | RS-03 | T1-3 | P2

path_of accepts compressed TSV, uncompressed TSV, CSV, XLSX and TXT candidates and chooses the one with the newest modification time. The choice is not made from an explicit release manifest or an ambiguity error.

Why it matters: Copying or unzipping the same directory can change timestamps and therefore which physical file is analyzed. A recorded hash helps identify what was read, but does not make this selection ...
Next check: Provide different compressed and uncompressed versions of one synthetic table, change only their timestamps, and confirm the tool either refuses ambiguity or selects the same explicitly configured file. Export the selected physical path.

- [Source 1](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/release.py#L33-L40)
- [Source 2](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L229-L234)

<!-- Speaker notes: path_of accepts compressed TSV, uncompressed TSV, CSV, XLSX and TXT candidates and chooses the one with the newest modification time. The choice is not made from an explicit release manifest or an ambiguity error.

Reject multiple variants by default or require an explicit file map. Include the resolved relative path and the selection rule alongside the content hash in the evidence receipt.

Acceptance: Provide different compressed and uncompressed versions of one synthetic table, change only their timestamps, and confirm the tool either refuses ambiguity or selects the same explicitly configured file. Export the selected physical path.

Confidence: High; the selection rule is explicit. Cross-machine behavior was not exercised. -->

---

# Before A Judging Decision



Resolve evidence gaps before interpreting readiness

Confirm the final commit and intended product.
Run the named synthetic follow-up checks in an authorized environment.
Observe a fresh-machine workflow and exported result.
Keep untested claims, proposed scores and clinical claims out of the conclusion.


<!-- Speaker notes:  -->

---
