# Tests and evidence: busy-beavers

Updated 2026-11-14T20:44:14+00:00. The fixed source commit remains the one in [REPORT.md](REPORT.md).

## Submitted tests

**65 passed, 0 skipped, 0 failed, 0 errors.** Reported final test duration: 3.18 seconds.

Raw TCGA data and sealed envelopes were absent. Data-dependent checks were skipped by the submitted suite where reported.

The first isolated attempts exposed missing environment dependencies (pandas/pytz and child-process dependency paths), not submission failures. Those were corrected in the disposable environment. Cohort Studio initially also lacked copied manifest/media files; those prerequisites were restored from its pinned Git commit and the complete suite was rerun. Final counts above describe the final command, not a sum of retries. Dependencies differ from Tripwire’s exact pinned Python 3.11/3.13 environment; this was Python 3.14.6 on macOS ARM64. No student code was modified to make tests pass.

## Independent safeguards

**3 probes: 0 met the proposed safeguard; 3 did not.** These are deliberately targeted cases and positive controls, not a representative detection-rate estimate. Read the observed values in [synthetic-probes.json](evidence/synthetic-probes.json). The [reproduction source](../review-tools/synthetic-probes.py) is shared across submissions. Assertions and scope are explained in [the runner notes](../review-tools/README.md).

| Safeguard | Expected | Observed | Met? |
|---|---|---|---|
| Empty release directories are not Ready | false | true | No |
| Identical zero-byte required inputs are not Ready | false | true | No |
| Sign-changing target shift is Blocked | "Blocked" | "Conditional" | No |

## Isolation and limits

Git blobs were copied into a disposable directory, without hooks, secrets or sealed files. macOS sandbox rules denied reads under /Users and /Volumes, denied writes outside that disposable directory, and blocked external network access. Test subprocesses inherited those restrictions. Environment variables were cleared and only required non-secret paths and offline flags were supplied. Published binary Python wheels were installed only into the disposable directory; no submission installer or package lifecycle script was run.

No hosted application, real provider call, clinical validity, production authorization, screen-reader usability or real-world accuracy was verified. Passing tests demonstrates the assertions in those tests, not all rubric requirements. The issue decks distinguish source findings from independently reproduced behavior. No official score is assigned.

[Final submitted-test log](evidence/submitted-tests.log) · [Recorded command](evidence/submitted-test-command.json)

[Recorded dependency versions and isolation probes](../review-tools/environment.json). The final profile explicitly permits loopback only; external probes returned PermissionError.

## Second independent synthetic round

The following are targeted recommendations and controls, not additional official judging requirements. Read [exact observations](evidence/synthetic-probes-round2.json) and [reproduction source](../review-tools/synthetic-probes-round2.py).

| Check | Expected | Observed | Proposed safeguard met? |
|---|---|---|---|
| All 620 affected repair targets retained | 620 | 500 | No |
| Easy export respects explicit rejection | true | false | No |
| Original file preserved | true | true | Yes |

For Tripwire, release compatibility and question adequacy are distinct outputs. For Identity Crisis, the bypass is explicitly non-default. For export checks, a diagnostic export can be legitimate when its restrictions remain clear. See REPORT.md for these interpretation limits.

## Third independent round

[Exact observations](evidence/synthetic-probes-round3.json) · [Inspected reproduction script](../review-tools/synthetic-probes-round3.py). Provider transports were mocked; no model API was called. SNS generated scripts used invented fixtures, inspected imports and the same sandbox.

| Check | Proposed safeguard met? |
|---|---|
| Context omits sample identifiers by default | No |
| Known-id check rejects invented citation | Yes |
| Known-id check accepts existing citation | Yes |

## Frozen public baseline control

The verified public Release A compared with itself returned Ready and zero findings. [Aggregate result](evidence/public-baseline.json) · [reproduction](../review-tools/public-baseline.py) · [input hashes](../review-tools/PUBLIC-RELEASE.md). ReadySet and Busy Beavers used their identical-file shortcut (analyses not rerun); SNS reran its reference analyses. This is an unchanged-input control, not an independent clinical-data audit or a sealed-input test. No record-level output is published.

## Companion-audit reproductions

[Exact observations](evidence/supplement-probes.json) · [source](../review-tools/supplement-probes.py). These independently execute the supplemental source concerns on invented fixtures. Busy Beavers has three proposed safeguards met and three unmet, plus a full-engine quantization observation. Cohort Studio has a passing unchanged control and a failed proposed strict-hash safeguard: it explicitly warns and continues. These are not official scoring requirements.

## Local browser workflow — synthetic sample swap

**13 checks passed; zero failed.** Actual Streamlit frontend and FastAPI detector, using two invented 40-sample releases in the same restricted disposable environment. A cross-group protein-profile swap produced one finding and Conditional; A1 reran, A2 remained unchanged. The browser exposed evidence and the limitation that matching profiles do not establish which release is correct. Filtering, reset, findings JSON export, pending researcher review and theme switching worked. No fixes were applied.

[Exact checks and observations](evidence/browser-qa.json) · [desktop viewport](evidence/results-synthetic.png) · [review state](evidence/next-steps-synthetic.png) · [mobile viewport](evidence/mobile-synthetic.png) · [browser script](../review-tools/busy-browser-qa.py) · [synthetic server setup](../review-tools/busy-browser-server.py).

No page script errors or document-level horizontal overflow were observed at 390 px. The mobile navigation occupies substantial vertical space; that remains a usability consideration. Screenshots are viewport observations, not a full responsive/accessibility audit. No hosted service or model provider was called. A first screenshot/check was refined to verify the expanded evidence panel itself; counts describe the final run, not retries. Streamlit's extracted-package development-mode heuristic required an explicit false setting in the test command; this was environment setup, not an application failure. Both temporary servers were stopped after testing.
