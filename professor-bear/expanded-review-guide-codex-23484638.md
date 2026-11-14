# Expanded Nine-Entry Audit Guide

November 14, 2026. Companion source review `codex-23484638`; later runtime evidence read through review-repository commit `6e0bb1c49eb5707eb087627425eb77ae3d2d1c43`.

This completes the requested expansion to nine entries. The three added repositories have detailed source audits, structured criterion records, one-finding-per-slide HTML/Markdown decks and GitHub-readable PDF copies. Existing reports, later test evidence and other reviewers' work remain preserved. This guide reconciles evidence scope rather than replacing those records or assigning scores.

## Start Here

- [All nine primary review packages](README.md), with separately attributed test records.
- [Original six-entry companion guide](review-guide-codex-23484638.md), including focused Identity Crisis and SNS follow-through.
- [Combined editable presentation: 73 slides](https://chatgpt.com/space/page_7734b980d8808191bc85e09e76b24cf6). Original slides 1-46 remain intact except two scope labels changing six entries to nine. Cohort Firewall is 47-55; HIPPA-cratic is 56-63; ClearAnswer is 64-72; slide 73 states the expanded limits. Source URLs and fuller reasoning are in speaker notes. Readers need access to the Page; the GitHub decks below are separate public copies.
- [Cross-review status](REVIEW-STATUS.md) and [package verification](VERIFICATION.md).

The combined presentation summarizes the source supplements. Later runtime evidence below qualifies the original scope statements without retroactively claiming that this source reviewer ran the submissions. Slide count, finding count and test count are not measures of team quality.

## Added Entries And Artifacts

| Entry | Track / product | Detailed audit | PDF | Browser deck | Slide notes | Runtime review |
|---|---|---|---|---|---|---|
| NinadRao0707/cohort-firewall | Track 1 / cohort-control-tower | [Audit](cohort-firewall/audit-codex-23484638-pass-01.md) | [11 slides](cohort-firewall/slides-codex-23484638-pass-01.pdf) | [HTML](cohort-firewall/slides-codex-23484638-pass-01.html) | [Markdown](cohort-firewall/slides-codex-23484638-pass-01.md) | [Report](cohort-firewall/REPORT.md), [tests](cohort-firewall/TESTS.md) |
| roh9031/HIPPA-cratic | Track 1 / cohort-studio | [Audit](hippa-cratic/audit-codex-23484638-pass-01.md) | [10 slides](hippa-cratic/slides-codex-23484638-pass-01.pdf) | [HTML](hippa-cratic/slides-codex-23484638-pass-01.html) | [Markdown](hippa-cratic/slides-codex-23484638-pass-01.md) | [Report](hippa-cratic/REPORT.md), [tests](hippa-cratic/TESTS.md) |
| GauravBohra2001/clearanswer | Track 2 / research-claim-auditor | [Audit](clearanswer/audit-codex-23484638-pass-01.md) | [11 slides](clearanswer/slides-codex-23484638-pass-01.pdf) | [HTML](clearanswer/slides-codex-23484638-pass-01.html) | [Markdown](clearanswer/slides-codex-23484638-pass-01.md) | [Report](clearanswer/report.md), [tests](clearanswer/TESTS.md) |

HIPPA-cratic's product also calls itself Cohort Studio. It is a separate submission from tammy357/oncosys-cohort-studio. Cohort Firewall is likewise separate from GiorgiKarazanashvili/BusyBeavers, despite overlapping product wording. ClearAnswer uses the Track 2 rubric, not the Track 1 control-tower criteria.

| Repository | Reviewed immutable commit |
|---|---|
| NinadRao0707/cohort-firewall | `ab5084f7caaa57e68636e2cd3fde97b20a47bf69` |
| roh9031/HIPPA-cratic | `9f0ad46f32a1a76af25baf1aa621ab862f991c45` |
| GauravBohra2001/clearanswer | `7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8` |

Organizer reference: `disleveK/oncosys-hackathon-challenge@6e15a399a64ffbf80778db0b462ac239e70086b9`. The observed HIPPA-cratic submission tag resolves to its reviewed commit. Neither a tag nor a local checkout establishes the official final-submission receipt; that remains unverified for the entries.

## Cohort Firewall Reconciliation

The source supplement records three strengths and five risks. Preserve its useful versioned policy, current-content cache hashes and explicit review decision matrix while addressing the following boundaries.

| Companion finding | Relation to main report | Current evidence scope |
|---|---|---|
| CFT-01: missing candidate files can avoid an analysis availability check | New source-derived follow-through, not an additional reproduction of CF-01 | Candidate-present files limit the comparison; a required baseline-only file can remain not_compared while no change triggers a rerun. The complete-entry consequence remains unexecuted. It needs a required-file omission fixture with an optional-RNA positive control. |
| CFT-02: impact routing misses existing samples that become eligible | Same mechanism as main CF-01 | The parallel reviewer used a generic authored count function: actual count changed 1 to 2 while the route marked the analysis unaffected/not_rerun. This is not a reproduced result for the organizers' protected analyses. |
| CFT-03: duplicate IDs disappear before detection | Same mechanism as main CF-02 | Three invented clinical rows loaded as two; no diff finding appeared although hashes changed. The clinical case was observed; the distinct matrix-header case remains a follow-up. |
| CFT-04: review binding omits findings/affected_by | Same mechanism as main CF-03 | A legitimate synthetic certificate with stripped evidence obtained a Conditional review without the original acknowledgment. The Blocked-approval control remained rejected. No signing key was forged and no hosted exploit was shown. |
| CFT-05: question review omits the supplied spec-hash comparison | Same mechanism as main CF-04 | Initial helper evidence now has an in-process API corroboration: both the original question and changed question returned HTTP 200, with changed text stored. No browser or hosted attack was run. |

Read the [initial probe record](cohort-firewall/evidence/independent-tests.json) and [later API results](cohort-firewall/evidence/cohort-firewall-api-probes.json) with [TESTS.md](cohort-firewall/TESTS.md). The main report also covers malformed inputs, funnel answerability and the optional wording guard. Those are separately documented concerns, not claims that a model actually transmitted data or generated bad advice during this review.

Later suite results are **nine collected tests passed**, including the grouped 26 readiness variants, 12 tower scenarios and earlier six disclosure cases. Do not sum those inner cases into additional collected tests. The optional official-schema check was not enabled in that suite. The six API observations also preserve important controls: an empty CSV returned Insufficient Evidence, and unchanged question approval worked. Browser interaction, clean setup, Next.js build, full hosted workflow and protected-analysis outcomes remain unverified.

Acceptance priority: establish required input availability before impact routing; test newly eligible records independently of baseline membership; preserve identity defects before normalization; bind review to the complete immutable subject. Keep optional inputs optional and diagnostic exports distinct from approved use.

## HIPPA-cratic Reconciliation

The source supplement records three strengths and four risks. Its distinction between row inflation and wrong-sample joins, independently translated SQL checks and explanation of repair semantics are useful foundations.

| Companion finding | Relation to main report | Current evidence scope |
|---|---|---|
| HC-01: exported rebuild uses current environment | Main report issue 3 | Later benign subprocess evidence now corroborates the source concern. Same-source control reproduced S1/S2, two rows; another source produced S3, one row, exit 0, with no input-mismatch warning. The original definition recorded hashes. This is a reproducibility boundary, not a claim that every deliberate new analysis must be forbidden. |
| HC-02: request text enters a generated Python docstring | Main report issue 5 | A harmless triple-quoted request failed Python parsing while the ordinary request control parsed. The app downloads generated source; it does not execute it. No malformed generated program was run. |
| HC-03: SQL success/history can outlive input changes | New source-derived state follow-through | Source keys verification/history to steps without equivalent input identity. A browser release-switch/result-state reproduction remains pending. Do not substitute the distinct loader-cache probe for this session-state test. |
| HC-04: custom-data registry/environment is process-wide | New conditional source-derived multi-session concern | Shared globals are visible in source. No cross-session disclosure or hosted multi-user failure was observed. Test two isolated invented datasets in one process before drawing that conclusion. |

Read [changed-source reconstruction](hippa-cratic/evidence/hippa-rebuild-results.json), [initial synthetic probes](hippa-cratic/evidence/synthetic-probes.json), and [the complete test record](hippa-cratic/TESTS.md). Main-report issues 1 and 2 separately cover missing expected checksums and same-path cached data; issue 4 discusses empty-summary ambiguity. These do not mean every empty cohort is invalid or that the source supplement independently reproduced them.

The submitted suite has **170 passed, one skipped**. The earlier eight-test custom-data subset is included, not additional coverage. The practice-B-dependent case skipped. Browser interactions, hosted deployment, changed SQL state and session isolation remain unverified. Preserve exact membership and input fingerprints through fresh-process reconstruction, verification state and exported limitations.

## ClearAnswer Reconciliation

The source supplement records three strengths and five risks. Bounded query operations, report-text pointers, preservation of the tool verdict and explicit evidence-gap paths are valuable. A claim pointer or schema-valid export still does not establish that a claim is true.

| Companion finding | Relation to main report | Current evidence scope |
|---|---|---|
| CA-01: supported finalization need not have a successful relevant query | Same mechanism as main F3 | Initial source evidence now has result-assembly corroboration: a synthetic supported result used model_asserted_match, and an unqueried file became evidence. No real model was induced to make that choice. |
| CA-02: export forces high confidence | Same mechanism as main F2 | A helper probe and a later local JSON export both changed low confidence to high. The completed-job fixture was injected deliberately; no model completed it. An unchanged insufficient_evidence verdict still retained its human-review flag in the plain export. |
| CA-03: first-number tolerance upgrades a compound claim | Same mechanism as main F1 | Two initial helper cases and a later result-assembly check corroborate the shortcut. The compound case's second assertion was materially wrong. This is not measured live-model extraction performance. |
| CA-04: consumed manifests are outside the checksum inventory | Related to main F6 | A two-row manifest and one-row clinical fixture returned two manifest tumors while hashing only clinical.tsv. A shared manifest may intentionally cover a wider collection. Require explicit scope and manifest identity, rather than declaring every wider manifest incorrect. |
| CA-05: malformed/reasonless reviews can clear the review flag | Same mechanism as main F4 | A reasonless override became supported/high and removed the review flag in both helper and local route tests. The original tool verdict remained preserved. No remote authentication bypass or genuine reviewer action was demonstrated. |

Read [the four initial probes](clearanswer/TESTS.md), [later route/result-assembly evidence](clearanswer/evidence/clearanswer-api-probes.json), and the retained [main report](clearanswer/report.md). Both tested local exports returned HTTP 200 and passed the app's fallback public-schema validation; the missing-job control returned 404. Schema compliance is compatible with the confidence/override defects above and is not evidence against them.

Later offline results are **16 data-model tests passed** and **13 numbered foundation checks completed**. Foundation checks overlap other coverage and include trace display; do not combine them into a quality score. Temporary Flask/schema setup omissions were corrected before the successful route run and are not submission defects. Live model calls, extraction recall, browser tasks, hosted behavior and unseen-input performance remain untested. The source-derived advisory input guard concern in main F5 is not an observed transmission event.

Acceptance priority: require claim-relevant successful computation receipts; preserve original uncertainty; match each numeric subclaim to its own denominator and tolerance; include consumed manifests in provenance; validate review decisions before clearing review obligations. Keep a genuine single-number rounding control and a valid, reasoned override control.

## Later Tripwire Qualification

The earlier [Tripwire reconciliation](tripwire/runtime-reconciliation-codex-23484638.md) correctly records its then-current helper-only scope for a finding without a linked repair. A later [supported-importer browser record](tripwire/evidence/no-repair-browser.json), timestamped 21:17:51 UTC, extends that evidence: one schema-valid flagged finding, zero repairs, needs_human_review true, and the actual browser displayed Review (0 open) / Nothing to review. Export retained the flag; no repair was proposed, applied or approved. This is a local importer/UI observation, not proof that a built-in detector produced the case or that a hosted system authorized a repair. It is the same review-counter concern, not another defect to count.

## Review Deliverable Checks

All 32 new companion HTML slides passed current-file-hash browser checks for slide navigation, content containment and a 390-pixel mobile viewport. Each slide was visually inspected. The three PDF copies were reopened, checked for 11/10/11 pages and matching page text, rendered and visually reviewed. Page actions, embedded files and non-link annotations were absent in those PDF checks. These are presentation-artifact checks, not application accessibility or security certification.

The combined native presentation has 73 slides. Its 46-slide prefix matches the saved pre-expansion snapshot exactly after the two explicitly allowed six-to-nine text changes. Added slides 47-73 and the changed cover/scope slides were rendered and visually inspected. Original deck content and the new source notes remain editable.

The source reviewer executed no submission code, tests, installers, hooks, workflows, notebooks, generated rebuild programs or model calls. Runtime results above belong to the separately attributed reviewer and retain their own environment, controls and limitations. No sealed envelopes, answer keys or raw clinical records were accessed for this source review. No official score, cross-team ranking, clinical fitness, production security, full accessibility or accuracy rate is established.

## Local Open Commands

```bash
open "/Users/nik/Documents/agents/neu-oncosys-hackathon-challenge/professor-bear/cohort-firewall/slides-codex-23484638-pass-01.html"
open "/Users/nik/Documents/agents/neu-oncosys-hackathon-challenge/professor-bear/hippa-cratic/slides-codex-23484638-pass-01.html"
open "/Users/nik/Documents/agents/neu-oncosys-hackathon-challenge/professor-bear/clearanswer/slides-codex-23484638-pass-01.html"
```
