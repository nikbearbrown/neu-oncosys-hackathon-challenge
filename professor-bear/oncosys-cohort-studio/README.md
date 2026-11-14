# Cohort Studio

Pinned source: `54aeacb6f6f355a1dcaa42d7abf2ce174315ad69`. Updated 2026-11-14T19:40:03+00:00.

- [Detailed report](REPORT.md) — strengths, issues, concrete changes, acceptance checks and exact rubric.
- [Issue-by-issue deck](slides.html) — download and open in a browser; GitHub displays source.
- [Editable slide data](slides.json).
- [Actual static checks](evidence/static-checks.json).

The initial pass was static; current runtime evidence is linked below. No hosted deployment was verified. No official score. Work through the issues one at a time, then update this evidence at a stated commit.

## Runtime update

299 passed, 0 skipped, 0 failed, 0 errors. [Detailed tests and independent reproductions](TESTS.md). No official score.

[PDF deck](slides.pdf) — view directly on GitHub. The HTML version includes presenter notes and keyboard navigation.

## Companion source audit

A separate reviewer supplied [a detailed source audit](audit-codex-23484638-pass-01.md) and [an issue deck](slides-codex-23484638-pass-01.html) ([Markdown version](slides-codex-23484638-pass-01.md)), committed 2026-11-14T15:08:02-05:00. The companion adds reconstruction after a hash mismatch. It distinguishes a permissive warning policy from strict reproducibility. The main report separately tests request serialization and unknown checksum states; these are different issues. The companion's “not run” statements describe that reviewer's pass, not all testing in this folder. [Cross-review status](../REVIEW-STATUS.md) explains the relationship.
