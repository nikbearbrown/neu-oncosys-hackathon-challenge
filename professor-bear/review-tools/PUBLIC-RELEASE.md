# Public frozen-release test round

The six public Release A files were fetched from the URLs in the organizer source manifest at commit `6e15a399a64ffbf80778db0b462ac239e70086b9`. Every byte count and SHA-256 matched. [Verification metadata](public-release-verification.json) contains only file metadata, not records. These are TCGA-BRCA data distributed through UCSC Xena; upstream attribution and permitted-use restrictions remain applicable. No sealed envelope or answer key was opened.

Files lived only in the disposable review environment. Tripwire, Identity Crisis and Cohort Studio were rerun against their unchanged pinned source with public raw inputs available. Other suites retain their earlier synthetic-run counts. Logs published here replace TCGA-shaped sample/patient identifiers and local disposable paths with markers. This redaction does not change test totals or exception types.

Identity Crisis discovers the organizer checkout by checking for its public `envelopes/unseal.py` script. An initial run lacked that discovery marker and failed UI setup; the public script was copied from the pinned organizer commit, never executed, and the suite rerun. The final run passed 96 tests and skipped three practice-envelope checks. Tripwire skipped one practice-envelope check. Cohort Studio passed all 299 collected tests. These are software assertions, not independent clinical validation or unseen judging results.

The test environment and network/filesystem restrictions are recorded in [environment.json](environment.json) and each submission's TESTS.md. No real model provider was called. No raw clinical records, generated patient-level outputs, or sealed judging inputs are published.
