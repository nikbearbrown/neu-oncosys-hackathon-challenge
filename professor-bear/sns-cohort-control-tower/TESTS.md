# Tests and evidence: sns-cohort-control-tower

Updated 2026-11-14T19:51:28+00:00. The fixed source commit remains the one in [REPORT.md](REPORT.md).

## Submitted tests

**No submitted test suite identified in the inspected source; none claimed executed.** 

Raw TCGA data and sealed envelopes were absent. Data-dependent checks were skipped by the submitted suite where reported.

The first isolated attempts exposed missing environment dependencies (pandas/pytz and child-process dependency paths), not submission failures. Those were corrected in the disposable environment. Cohort Studio initially also lacked copied manifest/media files; those prerequisites were restored from its pinned Git commit and the complete suite was rerun. Final counts above describe the final command, not a sum of retries. Dependencies differ from Tripwire’s exact pinned Python 3.11/3.13 environment; this was Python 3.14.6 on macOS ARM64. No student code was modified to make tests pass.

## Independent safeguards

**8 probes: 2 met the proposed safeguard; 6 did not.** These are deliberately targeted cases and positive controls, not a representative detection-rate estimate. Read the observed values in [synthetic-probes.json](evidence/synthetic-probes.json). The [reproduction source](../review-tools/synthetic-probes.py) is shared across submissions. Assertions and scope are explained in [the runner notes](../review-tools/README.md).

| Safeguard | Expected | Observed | Met? |
|---|---|---|---|
| No detected finding does not override undersized group | "Insufficient Evidence" | "Ready" | No |
| Unexplained sign change is blocked | "Blocked" | "Ready" | No |
| Detected sign change is blocked | "Blocked" | "Blocked" | Yes |
| Valid 1-sample wide matrix is recognized | true | false | No |
| Valid 10-sample wide matrix is recognized | true | false | No |
| Valid 11-sample wide matrix is recognized | true | true | Yes |
| Rejected exclusion is not applied | true | false | No |
| Flag-for-review does not restore absent record | false | true | No |

## Isolation and limits

Git blobs were copied into a disposable directory, without hooks, secrets or sealed files. macOS sandbox rules denied reads under /Users and /Volumes, denied writes outside that disposable directory, and blocked external network access. Test subprocesses inherited those restrictions. Environment variables were cleared and only required non-secret paths and offline flags were supplied. Published binary Python wheels were installed only into the disposable directory; no submission installer or package lifecycle script was run.

No hosted application, real provider call, clinical validity, production authorization, screen-reader usability or real-world accuracy was verified. Passing tests demonstrates the assertions in those tests, not all rubric requirements. The issue decks distinguish source findings from independently reproduced behavior. No official score is assigned.

[Recorded dependency versions and isolation probes](../review-tools/environment.json). The final profile explicitly permits loopback only; external probes returned PermissionError.
