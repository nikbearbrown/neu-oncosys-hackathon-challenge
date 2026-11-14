# Independent synthetic safeguards

`synthetic-probes.py` contains small, invented cases for the five named pinned submissions. It imports submission code: inspect it and run only inside an isolated disposable environment with no credentials, outbound network or access to original data. It is not a general safe runner for arbitrary repositories. The recorded run used the exact commits in each report.

Expected outcomes are reviewer-proposed safeguards, not an organizer answer key. A false `safeguard_met` identifies a behavior to review; it is not an official score. Helper-level probes and controlled fault injection are identified in the reports. Generated Python delimiter cases are parsed, never executed.

Usage inside the isolation described in each TESTS.md: `python synthetic-probes.py /disposable/path/to/submission`. It writes observations to stdout and uses temporary invented fixtures. It does not edit the submission.
