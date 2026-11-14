# SNS Cohort Control Tower

Pinned source: `c1e8b79a2987cee6087d847867f9895deaa109a4`. Updated 2026-11-14T19:40:03+00:00.

- [Detailed report](REPORT.md) — strengths, issues, concrete changes, acceptance checks and exact rubric.
- [Issue-by-issue deck](slides.html) — download and open in a browser; GitHub displays source.
- [Editable slide data](slides.json).
- [Actual static checks](evidence/static-checks.json).

First pass: no runtime tests or live-site verification. No official score. Work through the issues one at a time, then update this evidence at a stated commit.

## Runtime update

No submitted test suite identified in the inspected source; none claimed executed. [Detailed tests and independent reproductions](TESTS.md). No official score.

[PDF deck](slides.pdf) — view directly on GitHub. The HTML version includes presenter notes and keyboard navigation.

## Companion source audit

A separate reviewer supplied [a detailed source audit](audit-codex-23484638-pass-01.md) and [an issue deck](slides-codex-23484638-pass-01.html) ([Markdown version](slides-codex-23484638-pass-01.md)), committed 2026-11-14T15:09:22-05:00. The companion is a source review with attributed helper probes. Later main-report evidence adds the full small-matrix engine reproduction, the generated A2-script failure and a synthetic browser smoke test. The companion's “not run” statements describe that reviewer's pass, not all testing in this folder. [Cross-review status](../REVIEW-STATUS.md) explains the relationship.


## Additional reconstruction audit — 20:19 UTC

[Reconstruction follow-through audit](audit-codex-23484638-pass-03.md) · [Issue deck](slides-codex-23484638-pass-03.html) · [Markdown deck](slides-codex-23484638-pass-03.md)

This separate source-only pass covers missing filter prerequisites, inconsistent cross-release fallback and A2 JSON serialization. The A2 serialization issue overlaps main-report issue 6, already reproduced at runtime; count it once. The two other findings are now reproduced through the actual CLI and generated scripts in main-report issues 7–8 and TESTS.md.


The companion also has a [concise revised deck](slides-codex-23484638-pass-02.html), [full slide notes](slides-codex-23484638-pass-02.md) and a [cross-review reading guide](../review-guide-codex-23484638.md). These preserve the source review; current runtime observations remain in TESTS.md.

Latest concise follow-through: [PDF](slides-codex-23484638-pass-04.pdf) · [HTML](slides-codex-23484638-pass-04.html) · [full notes](slides-codex-23484638-pass-04.md). This companion preserves its stated source-review scope; current runtime evidence is in [TESTS.md](TESTS.md).
