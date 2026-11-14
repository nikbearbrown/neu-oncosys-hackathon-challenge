# ClearAnswer test record

## Runtime follow-through — 2026-11-14T21:40:17+00:00

- Submitted `pytest -q core/tests`: **16 passed**, zero failed/skipped, 0.42 seconds. [Log](evidence/clearanswer-tests.log) · [JUnit](evidence/clearanswer-junit.xml).
- Submitted `python test_foundation.py`: all **13 numbered foundation checks completed**. These include a trace-display check and overlap the data-model suite; they are not 13 additional independent requirements or a detection benchmark. [Log](evidence/clearanswer-foundation.log).
- The four original synthetic probes were independently repeated with the same observations. [Results](evidence/clearanswer-probes-confirmed.jsonl).
- Six additional observations exercised real result-assembly methods, local Flask test-client routes and the loader. Compound claim assembly returned supported; an unqueried file was accepted as evidence; an unknown export job returned 404. With a deliberately injected synthetic completed-job fixture, normal export changed low confidence to high, and a reasonless override changed insufficient evidence to supported and removed the review flag. Both exports returned HTTP 200, downloaded successfully and passed the app's fallback validator against the public v0.2 schema. No model completed that fixture and no remote authentication bypass is claimed. A two-row manifest over a one-row clinical fixture returned two manifest primary tumors; only clinical.tsv was hashed. Manifests may intentionally represent the wider collection, so the repair is explicit scope/binding, not an assumption that every global manifest is wrong. [Results](evidence/clearanswer-api-probes.json) · [Reproducer](../review-tools/new-entry-api-probes.py).

The first API attempt lacked Flask, and a subsequent attempt lacked the JSON schema in the disposable checkout. These were test-environment omissions, not submission failures. Flask wheels were installed only into the temporary venv, and the public organizer schema was supplied before the successful run. The final fixture is schema-complete; an earlier minimal fixture correctly failed validation.

Environment: Python 3.14.6, pandas 2.3.3, NumPy 2.3.5, pytest 9.2.0, Flask 3.1.3, Werkzeug 3.1.9. Public baseline files were the [previously checksum-verified release](../review-tools/PUBLIC-RELEASE.md), with its public sample/slide manifests. No patient rows were published. Code ran in the restricted macOS sandbox with a cleared environment and dotenv disabled; no credentials, model calls, sealed inputs or student-checkout changes. The provided API reproducer expects disposable copies beside it.

These are all discovered submitted offline tests, not verification of model extraction, hosted operation, browser tasks, accessibility, or unseen-input performance. Live model evaluation requires a separately agreed provider/cost scope and remains untested.

## Initial four narrow synthetic checks


1. Compound claim 50.1% LumA / 90% Basal against 50% / 10%: tolerance note says supported.
2. Approximate 100 reviewed / 99 responded against 101 / 1: tolerance note says supported.
3. Export insufficient-evidence low-confidence finding: becomes confidence high.
4. Reasonless supported override: clears human-review flag, preserves prior tool verdict but becomes supported/high.

No external API, patient data, submitted full suite or browser execution. See report for exact boundaries.
