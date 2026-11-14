# Tests and evidence: tripwire

Updated 2026-11-14T21:04:04+00:00. The fixed source commit remains the one in [REPORT.md](REPORT.md).

## Submitted tests

**404 passed, 1 skipped, 0 failed, 0 errors.** Recorded command duration: 11.9 seconds.

The six checksum-verified public Release A files were available for this final run. Sealed envelopes were absent. The earlier synthetic/committed-manifest run had 399 passed and 6 skipped; its log remains below. [Public input provenance and limits](../review-tools/PUBLIC-RELEASE.md).

The first isolated attempts exposed missing environment dependencies (pandas/pytz and child-process dependency paths), not submission failures. Those were corrected in the disposable environment. Cohort Studio initially also lacked copied manifest/media files; those prerequisites were restored from its pinned Git commit and the complete suite was rerun. Final counts above describe the final command, not a sum of retries. Dependencies differ from Tripwire’s exact pinned Python 3.11/3.13 environment; this was Python 3.14.6 on macOS ARM64. No student code was modified to make tests pass.

## Independent safeguards

**7 probes: 4 met the proposed safeguard; 3 did not.** These are deliberately targeted cases and positive controls, not a representative detection-rate estimate. Read the observed values in [synthetic-probes.json](evidence/synthetic-probes.json). The [reproduction source](../review-tools/synthetic-probes.py) is shared across submissions. Assertions and scope are explained in [the runner notes](../review-tools/README.md).

| Safeguard | Expected | Observed | Met? |
|---|---|---|---|
| Insufficient unchanged movement is not Ready | "Insufficient Evidence" | "Ready" | No |
| Affected insufficient movement is rejected | "Insufficient Evidence" | "Insufficient Evidence" | Yes |
| Unexplained movement blocks | "Blocked" | "Blocked" | Yes |
| Flagged finding without repair stays open | ["F1"] | [] | No |
| Request-more-evidence stays unresolved | ["F1"] | [] | No |
| End-to-end unchanged tiny release is not Ready | false | false | Yes |
| Empty readiness checks do not pass | "Insufficient Evidence" | "Insufficient Evidence" | Yes |

## Isolation and limits

Git blobs were copied into a disposable directory, without hooks, secrets or sealed files. macOS sandbox rules denied reads under /Users and /Volumes, denied writes outside that disposable directory, and blocked external network access. Test subprocesses inherited those restrictions. Environment variables were cleared and only required non-secret paths and offline flags were supplied. Published binary Python wheels were installed only into the disposable directory; no submission installer or package lifecycle script was run.

No hosted application, real provider call, clinical validity, production authorization, screen-reader usability or real-world accuracy was verified. Passing tests demonstrates the assertions in those tests, not all rubric requirements. The issue decks distinguish source findings from independently reproduced behavior. No official score is assigned.

[Earlier synthetic-run log](evidence/submitted-tests.log) · [Earlier command](evidence/submitted-test-command.json)

[Recorded dependency versions and isolation probes](../review-tools/environment.json). The final profile explicitly permits loopback only; external probes returned PermissionError.

[Final public-release test log, identifiers redacted](evidence/public-release-tests.log) · [Final command](evidence/public-release-command.json)

## Second independent synthetic round

The following are targeted recommendations and controls, not additional official judging requirements. Read [exact observations](evidence/synthetic-probes-round2.json) and [reproduction source](../review-tools/synthetic-probes-round2.py).

| Check | Expected | Observed | Proposed safeguard met? |
|---|---|---|---|
| Full API unchanged 4-sample release is correctly scoped | "Insufficient Evidence" | "Ready" | No |
| Full API unchanged 40-sample release is correctly scoped | "Ready" | "Ready" | Yes |
| Revision retains both review events | 2 | 1 | No |
| Revision leaves prior object unchanged | "approve" | "approve" | Yes |

For Tripwire, release compatibility and question adequacy are distinct outputs. Identity Crisis’s Python API defaults strict, while its browser checkbox defaults to allowing missing validators; see its updated report. For export checks, a diagnostic export can be legitimate when its restrictions remain clear. See REPORT.md for these interpretation limits.

## Third independent round

[Exact observations](evidence/synthetic-probes-round3.json) · [Inspected reproduction script](../review-tools/synthetic-probes-round3.py). Provider transports were mocked; no model API was called. SNS generated scripts used invented fixtures, inspected imports and the same sandbox.

| Check | Proposed safeguard met? |
|---|---|
| Display precision does not erase calculated change | No |
| No consent means no provider call | Yes |

## Local browser workflow

**13 final checks: 12 met, one did not meet the reviewer-proposed safeguard.** Actual Streamlit app, original tracked dark-theme configuration, invented 120-primary-tumor/four-normal releases and a cross-group protein swap. No practice or sealed envelope was opened. [Results](evidence/browser-qa.json) · [overview](evidence/overview-synthetic.png) · [zero-open review counter](evidence/request-evidence-synthetic.png) · [mobile viewport](evidence/mobile-synthetic.png) · [runner](../review-tools/tripwire-browser-qa.py).

The interface showed Conditional compatibility and separate question-level Blocked/Insufficient Evidence results. Evidence expansion, reason/role requirements, organizer schema validation and JSON export worked. Request more evidence became Review (0 open), while the JSON correctly retained the request and original_preserved=true; no repair was applied. This is a distinction between decisions recorded and concerns resolved, not evidence of an unauthorized repair.

A failed replacement comparison removed the previous result and download controls, a useful positive control. No page script errors or document-level horizontal overflow were observed at 390px. These do not establish full accessibility or hosted behavior. The radio was exercised by keyboard because its styled input is covered by its label. An early screenshot omitted the tracked theme configuration; that harness omission was corrected, the completed workflow rerun, and only the final captures/counts are reported. Temporary server shutdown is recorded in the review completion notes.
