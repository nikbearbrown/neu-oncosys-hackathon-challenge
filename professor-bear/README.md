# Professor Bear: submission reviews

Read each detailed report and issue-by-issue deck together. Work through the issues one at a time, preserve the strengths, and rerun the acceptance checks after changes. These are independent review aids, not official scores. Each report pins a commit and distinguishes reproduced behavior, source findings and human judgments.

| Submission | Detailed report | PDF deck | Browser deck | Test evidence |
|---|---|---|---|---|
| ReadySet Control Tower | [Report](readyset-control-tower/REPORT.md) | [PDF](readyset-control-tower/slides.pdf) | [HTML](readyset-control-tower/slides.html) | [Tests](readyset-control-tower/TESTS.md) |
| Tripwire / Driftwire | [Report](tripwire/REPORT.md) | [PDF](tripwire/slides.pdf) | [HTML](tripwire/slides.html) | [Tests](tripwire/TESTS.md) |
| Identity Crisis | [Report](identity-crisis-control-tower/REPORT.md) | [PDF](identity-crisis-control-tower/slides.pdf) | [HTML](identity-crisis-control-tower/slides.html) | [Tests](identity-crisis-control-tower/TESTS.md) |
| Busy Beavers | [Report](busy-beavers/REPORT.md) | [PDF](busy-beavers/slides.pdf) | [HTML](busy-beavers/slides.html) | [Tests](busy-beavers/TESTS.md) |
| Cohort Studio | [Report](oncosys-cohort-studio/REPORT.md) | [PDF](oncosys-cohort-studio/slides.pdf) | [HTML](oncosys-cohort-studio/slides.html) | [Tests](oncosys-cohort-studio/TESTS.md) |
| SNS Control Tower | [Report](sns-cohort-control-tower/REPORT.md) | [PDF](sns-cohort-control-tower/slides.pdf) | [HTML](sns-cohort-control-tower/slides.html) | [Tests](sns-cohort-control-tower/TESTS.md) |

Updated 2026-11-14T21:04:04+00:00. Download HTML decks to open them locally; GitHub renders the PDFs directly. Each deck presents one issue at a time. No official numerical scores are assigned.

Submitted-suite results: ReadySet **107 unit tests plus 38 public mutation cases passed**; Tripwire **404 passed / 1 skipped**; Identity Crisis **96 passed / 3 skipped**; Busy Beavers **65 passed**; Cohort Studio **299 passed**. No submitted SNS test suite was found; its independent synthetic checks are documented. These suites cover different assertions and are not a ranking.

Public-data checks used [six checksum-verified frozen files](review-tools/PUBLIC-RELEASE.md). No sealed judging inputs were opened. The tests do not establish clinical validity, unseen-input performance, production security or full accessibility. Each TESTS.md records the independent reproductions and remaining limits.

Latest additions: SNS small-matrix behavior reproduced through the full engine; A2 generated-script NameError reproduced with an A1 passing control; Cohort Studio automatic fixes and local-only routing checked; Tripwire rounding and consent controls checked. All six now have at least a public-release test or unchanged-input control, with the distinct scope documented.

## Companion source audits

These independently authored supplements are preserved alongside the main runtime reviews. Their source-only scope is explicit; later execution results live in each TESTS.md. [Read the cross-review status](REVIEW-STATUS.md) before interpreting differences.

| Submission | Commit timestamp | Source audit | Companion deck |
|---|---|---|---|
| busy-beavers | 2026-11-14T14:59:17-05:00 | [Audit](busy-beavers/audit-codex-23484638-pass-01.md) | [HTML deck](busy-beavers/slides-codex-23484638-pass-01.html) · [Markdown](busy-beavers/slides-codex-23484638-pass-01.md) |
| identity-crisis-control-tower | 2026-11-14T15:04:09-05:00 | [Audit](identity-crisis-control-tower/audit-codex-23484638-pass-01.md) | [HTML deck](identity-crisis-control-tower/slides-codex-23484638-pass-01.html) · [Markdown](identity-crisis-control-tower/slides-codex-23484638-pass-01.md) |
| oncosys-cohort-studio | 2026-11-14T15:08:02-05:00 | [Audit](oncosys-cohort-studio/audit-codex-23484638-pass-01.md) | [HTML deck](oncosys-cohort-studio/slides-codex-23484638-pass-01.html) · [Markdown](oncosys-cohort-studio/slides-codex-23484638-pass-01.md) |
| readyset-control-tower | 2026-11-14T14:53:45-05:00 | [Audit](readyset-control-tower/audit-codex-23484638-pass-01.md) | [HTML deck](readyset-control-tower/slides-codex-23484638-pass-01.html) · [Markdown](readyset-control-tower/slides-codex-23484638-pass-01.md) |
| sns-cohort-control-tower | 2026-11-14T15:09:22-05:00 | [Audit](sns-cohort-control-tower/audit-codex-23484638-pass-01.md) | [HTML deck](sns-cohort-control-tower/slides-codex-23484638-pass-01.html) · [Markdown](sns-cohort-control-tower/slides-codex-23484638-pass-01.md) |
| tripwire | 2026-11-14T15:03:44-05:00 | [Audit](tripwire/audit-codex-23484638-pass-01.md) | [HTML deck](tripwire/slides-codex-23484638-pass-01.html) · [Markdown](tripwire/slides-codex-23484638-pass-01.md) |

## Concise companion decks

[Companion reading guide and concise revision-2 decks](review-guide-codex-23484638.md) links all six entries and reconciles later evidence. It also links the separate SNS reconstruction follow-through. Earlier reports and decks remain preserved.

### SNS reconstruction follow-through — 20:19 UTC

[Reconstruction follow-through audit](sns-cohort-control-tower/audit-codex-23484638-pass-03.md) · [Issue deck](sns-cohort-control-tower/slides-codex-23484638-pass-03.html) · [Markdown deck](sns-cohort-control-tower/slides-codex-23484638-pass-03.md)

Source-only supplement. A2 serialization overlaps the main runtime finding; missing-filter and fallback concerns are now additionally reproduced in main-report issues 7–8. Do not double-count overlapping issues.

Latest browser check: Cohort Studio passed 13 local smoke checks using invented data, with consistent cohort/audit exports and a visible Blocked result. See its TESTS.md and screenshots for scope and mobile-layout limits.

Latest Identity follow-through: browser defaults and same-path cache staleness are observed; a deterministic approved-review path retained an old-context receipt. Positive controls and differing browser navigation behavior are documented in its report. All built-in check registrations loaded in the test environment.

Focused companion decks now have direct GitHub PDF previews: [Identity UI/evidence identity](identity-crisis-control-tower/slides-codex-23484638-pass-04.pdf) and [SNS reconstruction](sns-cohort-control-tower/slides-codex-23484638-pass-04.pdf). Read them alongside the updated main reports to distinguish their original source scope from later reproductions.

Latest Tripwire browser pass: 12 of 13 proposed checks met; evidence requests remain correctly exported but the interface reports zero open reviews. A failed new comparison clears old results. A separate [citation audit](review-tools/citation-audit.json) verified 221 pinned file/line references with no invalid paths or line bounds; this is not a correctness judgment.

[Identity Crisis source/runtime reconciliation](identity-crisis-control-tower/runtime-reconciliation-codex-23484638.md) explains the path-dependent receipt finding and passing controls. Browser screenshots for Identity and Busy Beavers were refreshed with their original tracked theme configurations; behavioral results were unchanged.
