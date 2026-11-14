# Independent synthetic safeguards

`synthetic-probes.py` contains small, invented cases for the five named pinned submissions. It imports submission code: inspect it and run only inside an isolated disposable environment with no credentials, outbound network or access to original data. It is not a general safe runner for arbitrary repositories. The recorded run used the exact commits in each report.

Expected outcomes are reviewer-proposed safeguards, not an organizer answer key. A false `safeguard_met` identifies a behavior to review; it is not an official score. Helper-level probes and controlled fault injection are identified in the reports. Generated Python delimiter cases are parsed, never executed.

Usage inside the isolation described in each TESTS.md: `python synthetic-probes.py /disposable/path/to/submission`. It writes observations to stdout and uses temporary invented fixtures. It does not edit the submission.

## Second synthetic round and public inputs

[synthetic-probes-round2.py](synthetic-probes-round2.py) uses the same isolated invocation and fixed commits. It includes explicit positive controls and mock storage providers where stated. Proposed safeguard outcomes are not official requirements or scores. [Public frozen-release verification](PUBLIC-RELEASE.md) documents the separate submitted-suite round.

The [third probe round](synthetic-probes-round3.py) adds full SNS engine cases, A1/A2 generated-script execution, rounding and mocked provider controls. The [public baseline runner](public-baseline.py) records aggregate unchanged-input outcomes only. These scripts import submission code and require the same inspected sandbox; they are not safe generic executors.

[Supplement probes](supplement-probes.py) corroborate selected findings from the independent source audit. Generated reconstruction code was inspected and executed only with invented data in the restricted environment.

[SNS reconstruction probes](sns-reconstruction-probes.py) compare exact synthetic cohort membership between the actual CLI and its generated scripts, including a complete-input control, a missing eligibility column, cross-release fallback and a CSV clinical file.

[Studio browser checks](studio-browser-qa.py) require the documented isolated synthetic local server and recorded visual dependencies. They check visible results, exports and basic controls; they are not a general deployment test.

[Sampling-unit audit](independence-audit.py) reports aggregate A1 sample/patient-prefix counts and an invented repeated-specimen control. It publishes no participant identifiers and qualifies a conditional statistical limitation.

[Busy Beavers browser checks](busy-browser-qa.py) and [synthetic server setup](busy-browser-server.py) reproduce an invented sample swap through the actual local interface. They require the documented isolated environment and are not general safe executors.

Identity Crisis follow-through: [browser checks](identity-browser-qa.py), [fixture setup](identity-browser-setup.py), [deterministic state probe](identity-state-probe.py), and [runtime registration control](identity-check-coverage.py). These require the same isolated environment and do not open sealed inputs.
