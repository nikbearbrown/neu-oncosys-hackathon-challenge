# Actual OncoSys challenge: reference and review routes

This independent review toolkit is grounded in the organizer repository
`disleveK/oncosys-hackathon-challenge`, inspected at commit
`6e15a399a64ffbf80778db0b462ac239e70086b9` on 2026-11-14. This is the challenge package, not a team submission.
The earlier local project name was `neu-ai-healthcare-hackathon`; its history
has been preserved under `neu-oncosys-hackathon-challenge`.

## What is integrated

[The reference manifest](../upstream/challenge.json) records immutable links,
byte sizes and SHA-256 hashes for 20 upstream documents. The six product routes
in [products.json](../upstream/products.json) guide source review and appear in
review packets and reports when a product is specified. Run:

```sh
python3 review.py challenge
```

We link upstream rather than vendoring its code, assets or datasets. The inspected
root has no repository-wide LICENSE. DATA_LICENSES.md describes separate data
terms, including TCGA redistribution terms still being confirmed. Public access
does not establish blanket redistribution permission. Preserve the upstream
credits and verify the particular source terms before copying data elsewhere.
The upstream checkout remains intact in the sibling directory.

## The data and what has actually been checked

Upstream documents describe seven packs: TCGA-BRCA, PathMNIST, CPTAC, LIDC-IDRI,
DepMap, ClinicalTrials.gov and CAMELYON17, plus a Wisconsin warm-up. Some compact
extracts and metadata are committed upstream; raw TCGA files are fetched, and
many images remain at their source. This toolkit has **not** downloaded those
packs, verified their numerical contents, opened images, or run their scripts.
Upstream status labels such as “Ready” are upstream claims, not our validation.

RULES.md identifies frozen TCGA-BRCA as the judged core and allows approved
supplemental sources. The product catalogue also describes custom builds using
other packs and rubric-only evaluation. Confirm organizer-approved scope for
custom submissions rather than penalizing them from a guessed interpretation.
Only join different records when a documented match exists; an identifier that
looks similar is not sufficient evidence. Keep patient, sample, slide, patch,
cell line and registry-record units distinct.

## Product-specific evidence

| Product | Track | Inspect or request |
|---|---|---|
| Cohort Control Tower | 1 | Release fingerprints, membership changes despite equal counts, affected versus unaffected analyses, findings.json in shared format v0.2 |
| Cohort Studio | 1 | Editable cohort logic, count changes at joins, distinct samples and patients, rerunnable export and unique sample_id in cohort_samples.csv |
| Multimodal Case Room | 2 | Verified identifiers connecting evidence, visible absent/conflicting layers, source-linked sentences, export |
| Evidence Copilot | 2 | Bounded real queries, checksums, filters, sample counts, calculation, rerun, unsupported-question refusal |
| Research Claim Auditor | 2 | Source sentences, actual calculations, three claim verdicts, preserved human overrides and audit.json with claim_check findings |
| Repair Review Desk | 2 | Import validation, recomputed repair effects, reasons/roles for decisions, preservation of original analyses on export |

Shared format is required upstream for Control Tower, Claim Auditor and Repair
Review Desk; it is optional for other products. Cohort Studio has its own CSV
output requirement. Do not impose every product's outputs on every team.
Featured-product suggestions and stretch features are not extra weighted rubric
criteria. Keep both official seven-criterion rubrics unchanged.

## Review without leaking the judging exercise

The toolkit excludes envelopes and answer-key paths, does not unseal anything,
and does not read practice answers as evidence that a student's implementation
works. Public product briefs describe demonstration behaviors; those descriptions
are not successful runs. Judge-only unseen tests must be handled in the authorized
live judging workflow. No sealed files or access codes are copied here.

Students should set mode to student and select their own pinned commit. They
receive evidence-backed improvement suggestions without scores or private judge
notes. Judges can use the same public evidence and separately enter their reviewed
proposed scores. The toolkit neither submits grades nor makes official decisions.

## Pinned upstream documents

- [README.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/README.md)
- [RULES.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/RULES.md)
- [DATA_LICENSES.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/DATA_LICENSES.md)
- [SUBMISSION_CHECKLIST.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/SUBMISSION_CHECKLIST.md)
- [products/README.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/products/README.md)
- [format/README.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/format/README.md)
- [data/README.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/data/README.md)
- [products/cohort-control-tower.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/products/cohort-control-tower.md)
- [products/cohort-studio.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/products/cohort-studio.md)
- [products/multimodal-case-room.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/products/multimodal-case-room.md)
- [products/evidence-copilot.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/products/evidence-copilot.md)
- [products/research-claim-auditor.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/products/research-claim-auditor.md)
- [products/repair-review-desk.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/products/repair-review-desk.md)
- [data/tcga-brca/README.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/data/tcga-brca/README.md)
- [data/pathmnist/README.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/data/pathmnist/README.md)
- [data/cptac/README.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/data/cptac/README.md)
- [data/lidc-idri/README.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/data/lidc-idri/README.md)
- [data/depmap/README.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/data/depmap/README.md)
- [data/clinical-trials/README.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/data/clinical-trials/README.md)
- [data/camelyon17/README.md](https://github.com/disleveK/oncosys-hackathon-challenge/blob/6e15a399a64ffbf80778db0b462ac239e70086b9/data/camelyon17/README.md)
