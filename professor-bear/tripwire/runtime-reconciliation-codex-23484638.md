# Tripwire: Review Activity Is Not Evidence Resolution

Added November 14, 2026, 21:12 UTC. This is a source/runtime reconciliation of existing finding TW-02, not a new score, ranking or additional independent defect.

Submission: `Adhithyan245/tripwire` at `45df43640836025b40e89fc190f913ad694a6011`. The separate browser evidence was published in review commit [`d585525`](https://github.com/nikbearbrown/neu-oncosys-hackathon-challenge/commit/d585525). The official final-submission receipt remains unverified. This reviewer read the browser observations and reproduction program and followed the corresponding pinned source paths; this reviewer did not execute the submission or browser harness.

## What The Browser Adds

The separate reviewer recorded 13 targeted local checks: 12 met the proposed expectations and one did not. These counts are neither official rubric points nor a representative success rate. See the [observations](evidence/browser-qa.json), [test record](TESTS.md#local-browser-workflow) and [reproduction program](../review-tools/tripwire-browser-qa.py).

The tested workflow used invented 120-primary-tumor/four-normal releases and a cross-group protein-profile swap, with RNA absent. It did not open practice or sealed envelopes or call a model provider. Its observations were:

- The interface showed Conditional release compatibility, affected A1 versus unchanged A2, and separate question-level Blocked and Insufficient Evidence states.
- Expanded evidence included the affected analysis and the limitation of the inferred swap.
- A missing review reason and missing reviewer role were rejected.
- Recording Request more evidence produced `Review (0 open)` and zero awaiting human review.
- The downloaded document still recorded `request_more_evidence` and `original_preserved=true`; the organizer format check passed.
- A failed replacement comparison cleared the old results and export controls. No page script errors or document-level horizontal overflow were observed at the tested 390-pixel viewport.

The last point is an important positive control: this test did not show stale prior results after a failed replacement. The viewport result is not a full responsive or accessibility certification. The failed zero-open expectation concerns the meaning of the review counter, not evidence of an applied repair or a falsely rewritten decision.

## Why The Counter Behaves This Way

The helper's documented question is which flagged findings still have an *undecided repair*. It forms a set from every recorded repair decision, without distinguishing approve, reject and request_more_evidence, then removes a finding from open when all linked repairs have decisions. See [tripwire/review.py:37-46](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L37-L46).

That is a defensible activity count if labelled as such. The dashboard, however, uses the same result for an awaiting-human-review indicator and its open-review tab. This is where a user can confuse a recorded request with resolution. See [app/dashboard.py:367-389](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/app/dashboard.py#L367-L389). Judges should evaluate that communication boundary against the intended workflow, not infer a hidden approval transition.

The source explicitly states that recording decisions does not apply repairs. `apply_decisions` validates reason and role, deep-copies the document and records the requested decision. See [tripwire/review.py:14-34](https://github.com/Adhithyan245/tripwire/blob/45df43640836025b40e89fc190f913ad694a6011/tripwire/review.py#L14-L34). The browser export corroborates this preservation for the tested request. Do not turn the zero-open observation into a claim that Tripwire authorized a repair, approved research use or mutated source evidence.

## What Still Needs A Separate Check

The companion's flagged-finding-with-no-repair case remains a helper-level observation. The actual browser run used a linked repair and does not establish that every imported no-repair finding is hidden by the UI. The source's `all(...)` over an empty list explains that helper path, but its reachability through each importer or future check remains a separate question.

Nor does this test overturn the separate question-readiness guard: the earlier four-sample full-API control returned Ready for compatibility and Insufficient Evidence for the selected question, with a 40-sample Ready question control. That distinction remains in the [main report](REPORT.md). No claim is made that the question engine ignores sample size.

## Concrete Acceptance Checks

1. Show separate counts for decisions still to record and concerns awaiting evidence. Preserve the exact exported decision and never map a request for evidence to approval.
2. Start with a linked flagged repair, request more evidence and verify the evidence obligation remains visible with its reason. Then record reject and approve as separate controls; do not assume they resolve the same obligation in the same way.
3. Import an authorized invented finding with no linked repair. Require an explicit finding-level disposition or a clearly labelled unsupported state rather than relying on a vacuous all-decided result.
4. Retain the passing blank-reason, blank-role and failed-replacement controls. Verify source files and the earlier evidence document remain unchanged.

These are proposed safeguards, not extra organizer requirements or observed fixes. Preserve the submitted distinction between compatibility and question adequacy, and retain the useful evidence/export workflow while improving the unresolved-evidence labels. Read this with the [detailed source audit](audit-codex-23484638-pass-01.md), [concise source deck](slides-codex-23484638-pass-02.html), current [main report](REPORT.md) and [test record](TESTS.md).
