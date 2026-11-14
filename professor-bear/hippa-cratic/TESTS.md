# HIPPA-cratic test record

Pinned commit: `9f0ad46f32a1a76af25baf1aa621ab862f991c45`.

## Completed initial checks

- `pytest tests/test_custom.py -k 'not back_to_tcga' -q --tb=short`: **8 passed, 1 deselected, 0 failed**, 0.67 seconds. This subset uses the repository's explicitly synthetic examples and mocked Supabase requests. The reset-to-real-TCGA case was excluded from this first subset.
- [Independent probes](evidence/synthetic-probes.json): missing checksum entry returned ok; same-path cached row counts were 2 → 2, then 1 after cache clear; zero-row result retained empty/value warnings but no unresolved problems; ordinary generated request parsed and triple-quoted request did not.
- [Static parsing](evidence/static-checks.json) records each parsed Python file. No imports were needed for this structural check.

[Probe source](../review-tools/hippa-probes.py). The probes import submission code and require the inspected sandbox; this is not a safe general executor for arbitrary repositories.

## Environment and scope

Disposable Git-object copy, Python 3.14.6, pandas 2.3.3, NumPy 2.3.5, pytest 9.2.0, Streamlit 1.67.0 and DuckDB 2.0.0. The macOS sandbox denies private user-file reads and writes outside the disposable folder, blocks external networking, and uses a cleared environment. No original student files were changed. No service credentials, model calls, sealed input or malicious generated-program execution.

The full submitted suite subsequently completed: **170 passed, one skipped, zero failures/errors**, 59.63 seconds reported by pytest. [Log](evidence/submitted-tests.log) · [command](evidence/submitted-command.json). It used the checksum-verified public frozen files and committed public sample/slide manifests. The practice-B release was not built and its dependent test skipped. The earlier eight-test subset is not added to this total. Browser interaction and hosted deployment remain unverified; the changed-environment reconstruction is recorded below. Passing selected tests does not negate targeted findings or establish a general detection rate. 171 cases were collected; one was skipped, so this review does not repeat the README's claim that all 171 passed.

## Reconstruction follow-through — 2026-11-14T21:40:17+00:00

A benign exported rebuild script was run twice in the restricted subprocess environment with invented data. With the original source selected, it reproduced S1/S2 (two rows). With ONCOSYS_DATA pointing at another fixture, it exited successfully and wrote S3 (one row), with no input-mismatch warning. The original definition had recorded input hashes. This reproduces report issue 3; it does not assert that a user intended the second run as reproduction rather than a new analysis. [Results](evidence/hippa-rebuild-results.json) · [Probe](../review-tools/hippa-rebuild-probe.py). No malformed generated program was executed.
