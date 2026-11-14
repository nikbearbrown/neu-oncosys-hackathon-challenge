# Cross-review status

Updated 2026-11-14T20:23:17+00:00.

Each submission has a main REPORT.md, an evolving TESTS.md and HTML/PDF decks. Files named audit-codex-23484638-pass-01 are independent source-only supplements; their accompanying deck and structured review preserve that pass. They use the same pinned submission commits. No numeric scores are awarded here.

A source finding, a helper reproduction, a full engine execution and a browser observation support different claims. Later runtime evidence supersedes an earlier “not tested in this pass” statement only for the exact path tested. It does not make every source finding true or certify an application. Avoid adding the same issue twice when considering the official rubric.

## readyset-control-tower

The companion is a source audit. The main report adds 107 submitted tests, synthetic regressions, a production build and browser checks, plus the later public unchanged-input control and 38 passing authored public-data mutation cases.

[Main report](readyset-control-tower/REPORT.md) · [Current tests](readyset-control-tower/TESTS.md) · [Companion audit](readyset-control-tower/audit-codex-23484638-pass-01.md)

## tripwire

The companion predates the corrected four-sample full API case. The latest runtime evidence confirms Ready release compatibility alongside Insufficient Evidence question adequacy; it does not claim that the separate question checker ignores size.

[Main report](tripwire/REPORT.md) · [Current tests](tripwire/TESTS.md) · [Companion audit](tripwire/audit-codex-23484638-pass-01.md)

## identity-crisis-control-tower

The companion source findings and later runtime probes agree. Current suite counts are 96 passed and three skipped; development bypass is non-default and the default unknown-check path fails closed.

[Main report](identity-crisis-control-tower/REPORT.md) · [Current tests](identity-crisis-control-tower/TESTS.md) · [Companion audit](identity-crisis-control-tower/audit-codex-23484638-pass-01.md)

## busy-beavers

The companion adds duplicate-ID ordering and rounded-hash concerns. These are linked separately; targeted runtime corroboration now appears in main-report issues 6–7 and TESTS.md. Conditional versus Blocked remains a question-policy judgment, not a universal clinical threshold.

[Main report](busy-beavers/REPORT.md) · [Current tests](busy-beavers/TESTS.md) · [Companion audit](busy-beavers/audit-codex-23484638-pass-01.md)

## oncosys-cohort-studio

The companion adds reconstruction after a hash mismatch. It distinguishes a permissive warning policy from strict reproducibility. The main report separately tests request serialization and unknown checksum states. New issue 6 reproduces the warning-and-continue policy using a changed synthetic manifest; these are different issues.

[Main report](oncosys-cohort-studio/REPORT.md) · [Current tests](oncosys-cohort-studio/TESTS.md) · [Companion audit](oncosys-cohort-studio/audit-codex-23484638-pass-01.md)

## sns-cohort-control-tower

The companion is a source review with attributed helper probes. Later main-report evidence adds the full small-matrix engine reproduction, the generated A2-script failure and a synthetic browser smoke test.

[Main report](sns-cohort-control-tower/REPORT.md) · [Current tests](sns-cohort-control-tower/TESTS.md) · [Companion audit](sns-cohort-control-tower/audit-codex-23484638-pass-01.md)

## Common interpretation limits

- Ready can mean unchanged analysis compatibility or fitness for a selected question. Read the product contract before judging that label.
- A permissive diagnostic export is not automatically an approved clinical artifact. Check its labels, metadata and authority boundary.
- Targeted synthetic probes are deliberately selected cases, not representative failure rates. Submitted test counts differ in scope and are not a leaderboard.
- The public baseline is not a sealed challenge. No unseen judging input was opened.
- Clinical meaning, sampling independence, deployment security and full accessibility still require qualified human review.
