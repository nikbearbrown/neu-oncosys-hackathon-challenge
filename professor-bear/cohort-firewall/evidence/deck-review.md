# Deck rendering review

Purpose: projection with a presenter; REPORT.md and presenter notes carry the full evidence and qualifications. The 11-slide HTML deck follows the existing Professor Bear Lato/red/white style. All 11 slides were rendered individually and inspected in the contact sheet. No overlaps, clipped bodies or crowded comparisons were visible. The PDF contains 11 nonempty 16:9 pages.

## Headline sequence

1. Cohort Firewall needs stronger evidence boundaries — claim.
2. Keep the explicit rules and approval safeguards — action.
3. Newly eligible samples can miss an analysis rerun — claim.
4. Duplicate clinical IDs disappear before comparison — claim.
5. Release approval can omit signed-result evidence — claim.
6. Question approval can record an unbound question — claim.
7. Malformed inputs escape the safe fallback — claim.
8. The sample export overstates complete cases — claim.
9. The optional wording guard accepts contradictions — claim.
10. The tests establish mechanisms, not event accuracy — scope claim.
11. Repair evidence first, then verify the complete flow — action.

The sequence preserves the strengths, demonstrates seven specific boundary failures and ends with a scoped repair/verification sequence. It does not imply official submission status or full event-data accuracy.

## Per-slide assessment

| Slide | Assessment |
|---|---|
| 1 | Clear overview; pinned short SHA and no-score qualification visible. |
| 2 | Two tested controls support the retained safeguards; notes separate source facts from tests. |
| 3 | Baseline/new-release count makes the dependency error concrete. |
| 4 | Row count and zero-findings comparison communicates the identity gap. |
| 5 | Required versus stripped acknowledgment comparison supports the integrity claim; detailed limits remain in notes/report. |
| 6 | Question A/B comparison clearly isolates the missing question binding. |
| 7 | Input shapes and exception classes show failure without implying a Ready verdict. |
| 8 | Missing predictor versus two yes exports supports the answerability contradiction. |
| 9 | Guard-level scope is visible; no claim of actual generated model output. |
| 10 | Counts describe probe/case scope, not an accuracy or pass percentage. |
| 11 | Repair ordering is legible and matches the report. |

## Measurements and limits

Playwright found no JavaScript page errors, no slide overflow and no descendants outside slide bounds at the tested desktop viewport. Every headline was one line at that viewport. One representative narrow viewport check had document width equal to viewport width (390 px). PDF inspection found 11 pages and no empty pages.

The design uses the reference deck's small evidence links/status labels. Those are reading aids, not projected body content; the primary comparison text carries the claims. No full screen-reader, contrast automation, keyboard focus-order or real-room viewing test was performed. Geometry and contact-sheet inspection do not establish accessibility compliance. The reduced-motion setting was enabled during screenshots, and the deck retains the reference reduced-motion CSS.

The deck-review skill's coherence/staging principles (Tier A), sentence-claim headline guidance (Tier B), and consistency/legibility guidance (Tier C) informed this review; the size thresholds are design heuristics rather than clinical or official rubric requirements.
