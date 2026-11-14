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

Updated 2026-11-14T20:11:00+00:00. Download HTML decks to open them locally; GitHub renders the PDFs directly. Each deck presents one issue at a time. No official numerical scores are assigned.

Submitted-suite results: ReadySet **107 passed**; Tripwire **404 passed / 1 skipped**; Identity Crisis **96 passed / 3 skipped**; Busy Beavers **65 passed**; Cohort Studio **299 passed**. No submitted SNS test suite was found; its independent synthetic checks are documented. These suites cover different assertions and are not a ranking.

The latest three public-data runs used [six checksum-verified frozen files](review-tools/PUBLIC-RELEASE.md). No sealed judging inputs were opened. The tests do not establish clinical validity, unseen-input performance, production security or full accessibility. Each TESTS.md records the independent reproductions and remaining limits.

Latest additions: SNS small-matrix behavior reproduced through the full engine; A2 generated-script NameError reproduced with an A1 passing control; Cohort Studio automatic fixes and local-only routing checked; Tripwire rounding and consent controls checked. All six now have at least a public-release test or unchanged-input control, with the distinct scope documented.
