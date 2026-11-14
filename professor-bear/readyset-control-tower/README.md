# ReadySet Control Tower review

Pinned submission: `a7ussein/readyset-control-tower@4dd07736e99f96dd46cb6199c32bea32465bd20e`.

- [Detailed report](REPORT.md): findings, strengths, exact source links and proposed fixes.
- [Issue-by-issue slide deck](slides.html): download and open in a browser; use arrow keys, Next, or the issue selector. GitHub displays HTML source rather than running it.
- [Editable deck content](slides.json): slide text, evidence links and notes.
- [Tests and limits](TESTS.md): exact results and reproducibility notes.
- [Synthetic regression probes](reproductions/checks.py).

All reproduced inputs are invented. This is independent feedback for judges and
students, not an official score. Read the report before interpreting failed
probes: they test recommended guards and include scoped limitations.

[PDF deck](slides.pdf) — view directly on GitHub. The HTML version includes presenter notes and keyboard navigation.

## Companion source audit

A separate reviewer supplied [a detailed source audit](audit-codex-23484638-pass-01.md) and [an issue deck](slides-codex-23484638-pass-01.html) ([Markdown version](slides-codex-23484638-pass-01.md)), committed 2026-11-14T14:53:45-05:00. The companion is a source audit. The main report adds 107 submitted tests, synthetic regressions, a production build and browser checks, plus the later public unchanged-input control. The companion's “not run” statements describe that reviewer's pass, not all testing in this folder. [Cross-review status](../REVIEW-STATUS.md) explains the relationship.
