# Tripwire / Driftwire

Pinned source: `45df43640836025b40e89fc190f913ad694a6011`. Updated 2026-11-14T19:40:03+00:00.

- [Detailed report](REPORT.md) — strengths, issues, concrete changes, acceptance checks and exact rubric.
- [Issue-by-issue deck](slides.html) — download and open in a browser; GitHub displays source.
- [Editable slide data](slides.json).
- [Actual static checks](evidence/static-checks.json).

The initial pass was static; current runtime evidence is linked below. No hosted deployment was verified. No official score. Work through the issues one at a time, then update this evidence at a stated commit.

## Runtime update

404 passed, 1 skipped, 0 failed, 0 errors. [Detailed tests and independent reproductions](TESTS.md). No official score.

[PDF deck](slides.pdf) — view directly on GitHub. The HTML version includes presenter notes and keyboard navigation.

## Companion source audit

A separate reviewer supplied [a detailed source audit](audit-codex-23484638-pass-01.md) and [an issue deck](slides-codex-23484638-pass-01.html) ([Markdown version](slides-codex-23484638-pass-01.md)), committed 2026-11-14T15:03:44-05:00. The companion predates the corrected four-sample full API case. The latest runtime evidence confirms Ready release compatibility alongside Insufficient Evidence question adequacy; it does not claim that the separate question checker ignores size. The companion's “not run” statements describe that reviewer's pass, not all testing in this folder. [Cross-review status](../REVIEW-STATUS.md) explains the relationship.


The companion also has a [concise revised deck](slides-codex-23484638-pass-02.html), [full slide notes](slides-codex-23484638-pass-02.md) and a [cross-review reading guide](../review-guide-codex-23484638.md). These preserve the source review; current runtime observations remain in TESTS.md.

[Source/runtime reconciliation](runtime-reconciliation-codex-23484638.md) explains why the zero-open counter is a communication issue and does not establish repair approval.
