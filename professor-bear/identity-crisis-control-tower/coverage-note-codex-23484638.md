# Identity Crisis: Built-In Check Declaration Coverage

Checked 2026-11-14T20:38:56.433571+00:00. Pinned submission `380760dc3b7b61097756f2b85c0f462feadc802c`.

## Why This Qualification Matters

The [UI-state follow-through](audit-codex-23484638-pass-03.md) establishes that the browser initializes permissive missing-check handling while the core API defaults strict. That finding is conditional on a required check being unavailable. It must not be read as proof that ordinary built-in cards currently lack implementations.

A follow-up safe YAML/AST inspection found **eight built-in card files and fourteen literal registered check names** in the selected pinned source. Every required check name in those eight cards had a matching source registration declaration. This is a source-coverage observation, not a successful import or execution result.

## Card-Level Evidence

| Built-in card | Required check names | Source declarations found | Card source |
|---|---|---|---|
| `er-alpha-by-er` | `inputs_present`, `missing_values`, `site_shift` | Yes | [checks line](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/cards/er-alpha-by-er.yaml#L22-L22) |
| `esr1-expression-vs-er` | `inputs_present`, `missing_values` | Yes | [checks line](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/cards/esr1-expression-vs-er.yaml#L20-L20) |
| `her2-positive-protein` | `inputs_present`, `her2_field_conflict`, `missing_values`, `site_shift` | Yes | [checks line](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/cards/her2-positive-protein.yaml#L18-L18) |
| `hormone-therapy-response` | `inputs_present`, `outcome_available` | Yes | [checks line](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/cards/hormone-therapy-response.yaml#L29-L29) |
| `os-luminal-a` | `inputs_present`, `endpoint_suitability`, `survival_redacted`, `survival_zero_time`, `patient_double_count`, `subtype_columns_disagree` | Yes | [checks line](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/cards/os-luminal-a.yaml#L20-L20) |
| `pfi-luminal-a` | `inputs_present`, `endpoint_suitability`, `survival_redacted`, `survival_zero_time`, `patient_double_count`, `subtype_columns_disagree` | Yes | [checks line](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/cards/pfi-luminal-a.yaml#L20-L20) |
| `subtype-classifier-rna` | `inputs_present`, `label_derivation`, `leakage_columns` | Yes | [checks line](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/cards/subtype-classifier-rna.yaml#L19-L19) |
| `subtype-mix` | `inputs_present`, `subtype_columns_disagree`, `subtype_missing`, `a2_robustness` | Yes | [checks line](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/cards/subtype-mix.yaml#L19-L19) |

## Registration Evidence

| Check name | Source declaration |
|---|---|
| `a2_robustness` | [tower/checks/design.py:75](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/design.py#L75-L75) |
| `endpoint_suitability` | [tower/checks/fitness.py:88](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/fitness.py#L88-L88) |
| `her2_field_conflict` | [tower/checks/labels.py:158](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/labels.py#L158-L158) |
| `inputs_present` | [tower/checks/fitness.py:59](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/fitness.py#L59-L59) |
| `label_derivation` | [tower/checks/fitness.py:172](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/fitness.py#L172-L172) |
| `leakage_columns` | [tower/checks/design.py:38](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/design.py#L38-L38) |
| `missing_values` | [tower/checks/coverage.py:130](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/coverage.py#L130-L130) |
| `outcome_available` | [tower/checks/fitness.py:208](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/fitness.py#L208-L208) |
| `patient_double_count` | [tower/checks/survival.py:167](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/survival.py#L167-L167) |
| `site_shift` | [tower/checks/bias.py:23](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/bias.py#L23-L23) |
| `subtype_columns_disagree` | [tower/checks/labels.py:95](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/labels.py#L95-L95) |
| `subtype_missing` | [tower/checks/coverage.py:96](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/coverage.py#L96-L96) |
| `survival_redacted` | [tower/checks/survival.py:92](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/survival.py#L92-L92) |
| `survival_zero_time` | [tower/checks/survival.py:127](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/survival.py#L127-L127) |

## Limits And Acceptance Check

- A declaration does not prove the module imports, the registration executes or its check returns a correct result. The loader records import failures separately.
- A required check can become unavailable after an environment/module failure or a future/custom card change. The permissive browser-default concern therefore remains relevant, with the condition stated.
- Custom-card generation and arbitrary supplied cards are outside this eight-file comparison. No submission code, model provider, clinical dataset or sealed material was executed or accessed.
- A fresh-session test should verify the initial browser policy and inject one explicitly unavailable synthetic check. Preserve a normal built-in-card control and the strict API control.

The API default, browser default, declared check coverage and observed runtime availability are four different claims. Judges should keep them separate and avoid double-counting this qualification as a new defect or a score.
