# Identity Crisis Control Tower

Pinned source: `380760dc3b7b61097756f2b85c0f462feadc802c`. Updated 2026-11-14T19:40:03+00:00.

- [Detailed report](REPORT.md) — strengths, issues, concrete changes, acceptance checks and exact rubric.
- [Issue-by-issue deck](slides.html) — download and open in a browser; GitHub displays source.
- [Editable slide data](slides.json).
- [Actual static checks](evidence/static-checks.json).

The initial pass was static; current runtime evidence is linked below. No hosted deployment was verified. No official score. Work through the issues one at a time, then update this evidence at a stated commit.

## Runtime update

96 passed, 3 skipped, 0 failed, 0 errors. [Detailed tests and independent reproductions](TESTS.md). No official score.

[PDF deck](slides.pdf) — view directly on GitHub. The HTML version includes presenter notes and keyboard navigation.

## Companion source audit

A separate reviewer supplied [a detailed source audit](audit-codex-23484638-pass-01.md) and [an issue deck](slides-codex-23484638-pass-01.html) ([Markdown version](slides-codex-23484638-pass-01.md)), committed 2026-11-14T15:04:09-05:00. The companion source findings and later runtime probes agree. Current suite counts are 96 passed and three skipped; development bypass is non-default and the default unknown-check path fails closed. The companion's “not run” statements describe that reviewer's pass, not all testing in this folder. [Cross-review status](../REVIEW-STATUS.md) explains the relationship.


The companion also has a [concise revised deck](slides-codex-23484638-pass-02.html), [full slide notes](slides-codex-23484638-pass-02.md) and a [cross-review reading guide](../review-guide-codex-23484638.md). These preserve the source review; current runtime observations remain in TESTS.md.
