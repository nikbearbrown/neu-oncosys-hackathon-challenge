# Busy Beavers Cohort Firewall

Pinned source: `bfb369f231bf97a1d3aa21abade3ba4b1406a355`. Updated 2026-11-14T19:40:03+00:00.

- [Detailed report](REPORT.md) — strengths, issues, concrete changes, acceptance checks and exact rubric.
- [Issue-by-issue deck](slides.html) — download and open in a browser; GitHub displays source.
- [Editable slide data](slides.json).
- [Actual static checks](evidence/static-checks.json).

The initial pass was static; current runtime evidence is linked below. No hosted deployment was verified. No official score. Work through the issues one at a time, then update this evidence at a stated commit.

## Runtime update

65 passed, 0 skipped, 0 failed, 0 errors. [Detailed tests and independent reproductions](TESTS.md). No official score.

[PDF deck](slides.pdf) — view directly on GitHub. The HTML version includes presenter notes and keyboard navigation.

## Companion source audit

A separate reviewer supplied [a detailed source audit](audit-codex-23484638-pass-01.md) and [an issue deck](slides-codex-23484638-pass-01.html) ([Markdown version](slides-codex-23484638-pass-01.md)), committed 2026-11-14T14:59:17-05:00. The companion adds duplicate-ID ordering and rounded-hash concerns. These are linked separately; targeted runtime corroboration now appears in main-report issues 6–7 and TESTS.md. Conditional versus Blocked remains a question-policy judgment, not a universal clinical threshold. The companion's “not run” statements describe that reviewer's pass, not all testing in this folder. [Cross-review status](../REVIEW-STATUS.md) explains the relationship.
