# Tests and evidence: identity-crisis-control-tower

Updated 2026-11-14T20:56:16+00:00. The fixed source commit remains the one in [REPORT.md](REPORT.md).

## Submitted tests

**96 passed, 3 skipped, 0 failed, 0 errors.** Recorded command duration: 18.91 seconds.

The six checksum-verified public Release A files were available for this final run. Sealed envelopes were absent. The earlier synthetic/committed-manifest run had 81 passed and 18 skipped; its log remains below. [Public input provenance and limits](../review-tools/PUBLIC-RELEASE.md).

The first isolated attempts exposed missing environment dependencies (pandas/pytz and child-process dependency paths), not submission failures. Those were corrected in the disposable environment. Cohort Studio initially also lacked copied manifest/media files; those prerequisites were restored from its pinned Git commit and the complete suite was rerun. Final counts above describe the final command, not a sum of retries. Dependencies differ from Tripwire’s exact pinned Python 3.11/3.13 environment; this was Python 3.14.6 on macOS ARM64. No student code was modified to make tests pass.

## Independent safeguards

**2 probes: 0 met the proposed safeguard; 2 did not.** These are deliberately targeted cases and positive controls, not a representative detection-rate estimate. Read the observed values in [synthetic-probes.json](evidence/synthetic-probes.json). The [reproduction source](../review-tools/synthetic-probes.py) is shared across submissions. Assertions and scope are explained in [the runner notes](../review-tools/README.md).

| Safeguard | Expected | Observed | Met? |
|---|---|---|---|
| Missing validator prevents validated sign-off artifacts | false | true | No |
| Robustness exception has explicit error state | true | false | No |

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
| Default unknown-required-check fails closed | "Insufficient Evidence" | "Insufficient Evidence" | Yes |
| Development bypass cannot report ordinary Ready | "Insufficient Evidence" | "Ready" | No |
| Count beside mean equals measured count | 19 | 20 | No |

For Tripwire, release compatibility and question adequacy are distinct outputs. For Identity Crisis, the bypass is explicitly non-default. For export checks, a diagnostic export can be legitimate when its restrictions remain clear. See REPORT.md for these interpretation limits.

## Sampling-unit qualification — 2026-11-14T20:35:36+00:00

[Aggregate-only audit](evidence/independence-audit.json) · [Probe source](../review-tools/independence-audit.py). The checksum-verified public A1 selection contained 698 eligible samples and 698 distinct 12-character patient barcode prefixes; none had multiple eligible samples. All 698 values were measured (529 positive and 169 negative). This is an identifier-based check, not external verification of identity. It does not identify the repeated-patient problem in this actual cohort.

A separate invented six-patient-per-group fixture repeated each value into ten specimens. The unchanged submitted resampling function produced a narrower interval (width 1.25 instead of 4.00) despite no additional independent patients. This supports documenting its sampling-unit assumption for future inputs; it is not an extra official failure or evidence of an invalid current interval. No raw patient record or identifier was published.

## Browser workflow and evidence identity

**11 final browser checks: 9 met, 2 did not meet the proposed safeguard.** Actual local Chromium/Streamlit, invented 120-primary-tumor plus four-normal fixtures, no external model calls. The fresh browser starts permissive for unavailable checks; a same-path removal left 114 displayed until a cache-argument change revealed 113. Reviewer identity, repair rejection reasons, schema validation and exports worked in the tested workflow. [Exact results](evidence/browser-qa.json) · [overview](evidence/overview-synthetic.png) · [review controls](evidence/signed-synthetic.png) · [browser script](../review-tools/identity-browser-qa.py) · [fixture setup](../review-tools/identity-browser-setup.py).

The browser route with Request more evidence and page navigation withdrew the receipt after a question-context change. A separate deterministic AppTest approved-review route did not: revised intended use was rendered while the old signed context/digest remained current, without warnings. [State trace](evidence/identity-state-probe.json) · [runner](../review-tools/identity-state-probe.py). These paths are reported separately; they do not support a claim that all context changes either always withdraw or always retain sign-off. The unchanged live signature explains the failing path.

An availability control imported all **14 check registrations**, with **zero load errors** and **zero missing required registrations across eight built-in cards**. [Runtime coverage](evidence/identity-check-coverage.json) · [runner](../review-tools/identity-check-coverage.py). Availability is not proof that every check is correct. The browser-default concern applies to a future/custom/unavailable required check, not a demonstrated omission in these built-ins.

Harness corrections used the actual switch role, keyboard activation and observed navigation links; only the completed run is counted. The first AppTest attempt used an inaccessible working directory and did not reach the app; the corrected command ran in the disposable copy. Question text and fixture bytes were restored in finally blocks. A stub refuses envelope access; no sealed input exists in this test copy. The actual organizer validator and reference-analysis source were supplied. No student source changes, hosted tests, clinical validation or full accessibility audit.
