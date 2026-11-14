# Tests and evidence: oncosys-cohort-studio

Updated 2026-11-14T19:51:28+00:00. The fixed source commit remains the one in [REPORT.md](REPORT.md).

## Submitted tests

**299 passed, 0 skipped, 0 failed, 0 errors.** Recorded command duration: 52.64 seconds.

The complete submitted suite was run. Its 20 skips require raw TCGA release files. The suite used the repository’s committed public sample/slide manifests and tutorial media in the disposable copy; these were not republished. No raw TCGA tables or slides were loaded.

The first isolated attempts exposed missing environment dependencies (pandas/pytz and child-process dependency paths), not submission failures. Those were corrected in the disposable environment. Cohort Studio initially also lacked copied manifest/media files; those prerequisites were restored from its pinned Git commit and the complete suite was rerun. Final counts above describe the final command, not a sum of retries. Dependencies differ from Tripwire’s exact pinned Python 3.11/3.13 environment; this was Python 3.14.6 on macOS ARM64. No student code was modified to make tests pass.

## Independent safeguards

**4 probes: 1 met the proposed safeguard; 3 did not.** These are deliberately targeted cases and positive controls, not a representative detection-rate estimate. Read the observed values in [synthetic-probes.json](evidence/synthetic-probes.json). The [reproduction source](../review-tools/synthetic-probes.py) is shared across submissions. Assertions and scope are explained in [the runner notes](../review-tools/README.md).

| Safeguard | Expected | Observed | Met? |
|---|---|---|---|
| Absent expected checksum is unknown | "unknown" | "pass" | No |
| Ordinary generated reproduction script parses | true | true | Yes |
| Quoted request still produces valid Python | true | false | No |
| Request text cannot become executable statement | false | true | No |

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
| Blocked export is clearly separated from usable cohort file | false | true | No |
| Blocked result retains verdict metadata | true | true | Yes |

For Tripwire, release compatibility and question adequacy are distinct outputs. For Identity Crisis, the bypass is explicitly non-default. For export checks, a diagnostic export can be legitimate when its restrictions remain clear. See REPORT.md for these interpretation limits.

## Third independent round

[Exact observations](evidence/synthetic-probes-round3.json) · [Inspected reproduction script](../review-tools/synthetic-probes-round3.py). Provider transports were mocked; no model API was called. SNS generated scripts used invented fixtures, inspected imports and the same sandbox.

| Check | Proposed safeguard met? |
|---|---|
| Default API preserves proposed operation until acceptance | No |
| Explicit fix=False preserves operation | Yes |
| AI-off calls no provider | Yes |

## Companion-audit reproductions

[Exact observations](evidence/supplement-probes.json) · [source](../review-tools/supplement-probes.py). These independently execute the supplemental source concerns on invented fixtures. Busy Beavers has three proposed safeguards met and three unmet, plus a full-engine quantization observation. Cohort Studio has a passing unchanged control and a failed proposed strict-hash safeguard: it explicitly warns and continues. These are not official scoring requirements.

## Local browser workflow — 2026-11-14T20:33:48+00:00

**13 of 13 smoke checks passed.** [Exact checks](evidence/browser-qa.json) · [Browser test](../review-tools/studio-browser-qa.py) · [Pinned visual dependencies](evidence/browser-dependencies.json). The submitted invented fixture has 12 samples from eight patients. In the actual local web app, the built-in parser drafted a primary-tumor protocol, the reviewer could inspect it before execution, the result displayed eight samples/eight patients and Blocked for the stated minimum of 20, the cohort CSV contained eight unique samples, and the audit export accounted for all 12 inputs. The separate verdict export retained Blocked. Theme and advanced-search controls worked; no page-script error or document-level horizontal overflow at 390 CSS pixels was observed.

[Desktop result](evidence/result-synthetic.png) · [Mobile view](evidence/mobile-synthetic.png). Both were visually inspected. The mobile result column remains narrow: its reason is truncated and status labels crowd/wrap. That merits a dedicated responsive-layout check; a passing width assertion is not a complete usability or accessibility result.

AI and upstream hosting were disabled explicitly. The server used the existing restricted sandbox and a disposable SQLite file; external networking and private user-file reads were denied. Chrome used a fresh profile with nonlocal requests blocked. Four exact pinned scripts were fulfilled from recorded local copies; Google fonts were blocked, so screenshots use fallback fonts and reduced motion. The initial harness expected the wrong AI-status text, was corrected to the observed `off`, and is not counted as an application failure. Screenshot capture was corrected to avoid a sticky-header artifact. Repeated smoke checks are not added to the 13 distinct checks. The temporary server was stopped. No hosted service or clinical workflow was tested.
