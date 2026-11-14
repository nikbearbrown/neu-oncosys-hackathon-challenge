# HIPPA-cratic: independent review

Pinned source: `roh9031/HIPPA-cratic@9f0ad46f32a1a76af25baf1aa621ab862f991c45`. Updated 2026-11-14T21:25:17+00:00. Track 1: Cohort Firewall; cohort-builder product.

The README calls this product Cohort Studio. It is a separate submission from tammy357/oncosys-cohort-studio. The local submission tag resolves to this same commit; the official submission form/freeze receipt is not verified. No official score is assigned.

The full submitted suite completed: **170 passed, one skipped, zero failures**. Independent invented-data probes now corroborate all five issue mechanisms, including the changed-source rebuild. The earlier eight-test custom-data subset is included in that total, not additional coverage. No student checkout was edited.

## Strengths

### Explicit cohort and join semantics

A deterministic step language distinguishes sample-level and patient-level joins, reports inflation and cross-sample links, and offers explicit fixes. This directly fits the cohort-builder product. [cohort_studio/engine.py:413](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/engine.py#L413)

### Independent SQL comparison

The SQL path is a separate implementation and the submitted trap cases compare results. Agreement checks implementation, not whether the research question was specified correctly; the app says this explicitly. [cohort_studio/sqlcheck.py:1](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/sqlcheck.py#L1)

### Inspectable exports

Definitions retain steps, row/sample/patient counts, selected release and file fingerprints. Preserve this information while binding reconstruction to it. [cohort_studio/export.py:21](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/export.py#L21)

## Issues and concrete next steps

### 1. Unknown checksum status becomes ok

**Priority: medium. Evidence: reproduced.**

With an invented sample manifest and no sources.csv, check_data returned ok. The source also takes this branch when an existing file has no frozen checksum entry. The app maps ok to a green check. This conflates readable/present with compared against a known expected checksum. It is not evidence that a file actually changed or that all sidebar statuses claim clinical correctness.

**Sources:** [cohort_studio/data.py:125](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/data.py#L125) · [app.py:103](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L103)

**Suggested change:** Use distinct present-but-unverified, hash-verified, changed and missing states. Explain that a checksum verifies byte identity, not clinical meaning.

**Acceptance check:** Remove one expected hash, then supply the correct hash and an incorrect hash. Unknown must remain distinct from verified and changed.

### 2. Same-path replacements leave cached data stale

**Priority: high. Evidence: reproduced.**

A two-row invented sample file was loaded, then replaced with one row at the same path. load still returned two rows; clearing _load restored the correct one-row result. _load keys on table and resolved location, and check_data caches by location too. Choosing a different release path is a supported positive design; this finding concerns changed bytes at an unchanged path, not evidence that an immutable official release normally changes.

**Sources:** [cohort_studio/data.py:163](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/data.py#L163) · [cohort_studio/data.py:222](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/data.py#L222) · [cohort_studio/data.py:125](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/data.py#L125)

**Suggested change:** Bind caches to immutable release/content identity, or reject same-path modification. Keep displayed counts, recorded hashes and export inputs on the same snapshot.

**Acceptance check:** Load two rows, replace with one at the same path, and confirm all counts and exports refresh or an immutable-release violation is explicit. Retain the different-path release control.

### 3. Rebuild script does not enforce recorded inputs

**Priority: medium. Evidence: source and reproduced subprocess behavior.**

cohort.json records data directory, release and fingerprints, which is useful. The separate generated script embeds steps but calls run(STEPS) using the current environment. It neither reads that definition nor enforces its input hashes. Running it with another ONCOSYS_DATA or ONCOSYS_RELEASE can therefore rebuild against different inputs. A later changed-environment subprocess test reproduced this: the original two-row source rebuilt as a different one-row source with exit 0 and no mismatch warning; the same-source control retained two rows. See TESTS.md.

**Sources:** [cohort_studio/export.py:21](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/export.py#L21) · [cohort_studio/export.py:36](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/export.py#L36) · [cohort_studio/data.py:82](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/data.py#L82)

**Suggested change:** Make the script consume the definition and verify resolved files and hashes before rebuilding. Support an explicit new-input mode separately from reproduction.

**Acceptance check:** Export against invented dataset A, run the script with dataset B selected, and require a clear mismatch or an explicitly new analysis rather than silent reproduction.

### 4. Empty cohort warning is absent from final problem summary

**Priority: medium. Evidence: reproduced.**

Filtering the invented fixture to a nonexistent type returned zero rows and value_not_found/empty warnings, but unresolved_problems returned an empty list. The source then selects the success text No unresolved problems: one row per sample, and every joined record belongs to its own sample. The narrow join-grain claim is vacuously true, and an empty result may be legitimate. The concern is that the broad lead-in can hide the need to distinguish a genuinely empty population from a misspelled or unsupported filter. The live UI has not yet been observed for this case.

**Sources:** [cohort_studio/engine.py:281](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/engine.py#L281) · [cohort_studio/engine.py:550](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/engine.py#L550) · [app.py:450](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/app.py#L450)

**Suggested change:** State empty cohort explicitly and preserve its reason at export. Distinguish zero eligible records from an unevaluated or invalid filter; do not universally prohibit legitimate empty exports.

**Acceptance check:** Exercise a valid zero-result query, a misspelled value and an unavailable field. Each final summary should retain the different reason and limitation.

### 5. Quoted request breaks generated Python

**Priority: high. Evidence: reproduced by parsing.**

A normal request produced parseable Python. A request containing triple double quotes produced a SyntaxError when the generated script was parsed. The request is inserted into a triple-quoted module string without safe encoding; steps are also placed inside a raw triple-quoted JSON literal. Generated adversarial text was not executed. This demonstrates broken reproduction and a code-generation boundary, not an exploited deployment.

**Sources:** [cohort_studio/export.py:36](https://github.com/roh9031/HIPPA-cratic/blob/9f0ad46f32a1a76af25baf1aa621ab862f991c45/cohort_studio/export.py#L36)

**Suggested change:** Serialize text and structured data with safe literal encoding or load a separate JSON file. Validate generated syntax without executing user-controlled source.

**Acceptance check:** Round-trip requests and values containing both quote styles, newlines, backslashes and triple quotes. Compare exact steps and cohort membership for benign generated scripts.

## Exact official rubric: evidence, not scores

Maximum points below reproduce the official Track 1 weights, not points awarded. Supplemental rules do not add judging requirements.

| Criterion | Maximum | Evidence and question for judges |
|---|---:|---|
| Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support. | 20 | Join-grain detection and SQL checks are strengths; selected synthetic probes are not an accuracy estimate. |
| Reasoning for the research question. Changes its result appropriately when the research question or intended use changes. | 20 | Structured steps and AND/OR distinctions make question intent inspectable; human intent still needs review. |
| Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion. | 15 | Definition hashes and funnel counts help; checksum unknown states and rebuild binding need attention. |
| Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review. | 15 | Warnings and explicit fixes exist; keep empty and unverifiable states visible without claiming clinical readiness. |
| Working tool and clear setup. Judges can run the core workflow from the submitted repository. | 15 | 170 submitted tests passed and one practice-dependent case skipped. Hosted setup and the official unseen input are unverified. |
| Useful next steps. Suggested fixes are specific and match the size and importance of the problem. | 10 | Fix proposals are concrete; preserve user control and exact reproduction. |
| Communication. Someone without specialist knowledge can understand the result and next step. | 5 | The intended non-SQL researcher is clear. Keep file presence, hash verification and cohort adequacy distinct. |

## Checks and limits

See [TESTS.md](TESTS.md) for exact observed results, isolation and outstanding tests. Every cited file/line was checked against the pinned Git object. Source parsing is not behavior verification. Runtime probes used invented records; no model provider, hosted application or sealed input was used. Generated malformed programs were parsed, never executed.

Clinical meaning, sampling adequacy and the relevance of a cohort to a research question require domain review. No claim of clinical validity, production security or full accessibility is made.
