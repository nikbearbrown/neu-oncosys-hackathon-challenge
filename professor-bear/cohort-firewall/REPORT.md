# Cohort Firewall — independent review

**The submission has a thoughtful evidence architecture, but local probes reproduced gaps in analysis dependency routing, identity checks and the human-review boundary.** Prioritize CF-01 through CF-06 before relying on release verdicts or signed approval records. CF-07 concerns optional generated wording.

## Provenance and scope

- Submission: [NinadRao0707/cohort-firewall](https://github.com/NinadRao0707/cohort-firewall).
- Observed local clone HEAD: `ab5084f7caaa57e68636e2cd3fde97b20a47bf69`, inspected November 14, 2026. This is an observed snapshot, **not a verified official frozen submission**. No remote freshness claim is made.
- Track: Cohort Firewall (Track 1), as identified in the submitted README. No numeric scores or official judgments are assigned.
- Independent source clone: `/tmp/cohort-firewall-source`; review branch: `review/cohort-firewall-independent` in a separate repository clone. Neither submission original nor shared review checkout was edited.
- Readiness engine, rule evaluation, certificate/review/ledger code, release loader/diff/dependency routing, API boundaries and selected tests were inspected. Synthetic direct-function probes were executed only after inspecting their code paths.
- No sealed materials, answer keys, real patient records, hosted endpoints, cloud credentials, installers, migrations, or upstream reference-analysis modules were used. The local review repository's default static-only instructions were superseded only for the safe local tests explicitly requested by the user.

## Evidence standard

**Reproduced** means observed by the independent synthetic harness in [TESTS.md](TESTS.md), with raw results in [independent-tests.json](evidence/independent-tests.json). **Observed source** means the cited implementation was inspected. API/browser consequences are labeled inference when not exercised. Suggested priorities describe repair urgency, not scoring or disqualification. All seven issue mechanisms have high confidence at the tested function boundary; their prevalence on event data remains unknown.

## Strengths to retain

1. **Measurements and policy are separated.** Versioned YAML rules, explicit precedence, missing-check detection and not-evaluable handling are implemented in [cohort_firewall/policy.py:53-114](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/policy.py#L53-L114). Accepted limitations only waive permitted Conditional findings, not Blocked findings. This makes the readiness reasoning reviewable.
2. **Cryptographic and approval safeguards are real components.** Certificate payloads cover data, dictionary, spec, policy and verdict ([cohort_firewall/certificate.py:54-91](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/certificate.py#L54-L91)); review decisions use the signed verdict. The independent Blocked-approval control was rejected. The binding gaps below should be repaired without removing these safeguards.
3. **The evidence model is unusually explicit.** Findings include rule conditions, measured values, fields, effect on intended use, limitations, remedies and reconsideration evidence ([cohort_firewall/evidence.py:112-159](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/evidence.py#L112-L159)). Those fields provide a good foundation for actionable review, though field presence is not proof of correctness.
4. **Failure and uncertainty are acknowledged.** An empty CSV returned Insufficient Evidence in our test; the code documents heuristic identifiers, single-feature leakage checks and configurable thresholds ([cohort_firewall/engine.py:101-108](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/engine.py#L101-L108)). The ledger explicitly documents end-truncation limitations ([cohort_firewall/ledger.py:1-9](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/ledger.py#L1-L9)).
5. **Release findings distinguish observation from correction.** Changed labels and values are proposed for human review rather than assumed erroneous; repair justifications and limits are explicit ([cohort_firewall/tower/findings.py:221-278](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/findings.py#L221-L278)). Six submitted disclosure test cases also passed locally; this does not establish privacy compliance.

## Prioritized findings

### CF-01 · P1 · Newly eligible samples can miss an analysis rerun

**Rubric:** T1-1, T1-2, T1-3. **Evidence:** observed source and reproduced synthetic behavior. **Confidence:** high within the tested scope.

**Source:** [cohort_firewall/tower/analyses.py:101-122](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/analyses.py#L101-L122). The dependency gate intersects changed sample IDs with baseline sample_ids. Only added/new_duplicate changes get a separate eligibility check. A clinical label change on an existing, previously excluded sample therefore does not trigger the rerun, even when the changed column is used by the analysis.

**Reproduction:** A reviewer-authored group-A count changed S2 from group B to A. Direct recomputation returned n=2, but evaluate_analyses returned affected=false, status=not_rerun, after=null and a reason claiming no change touches the analysis. The baseline count was n=1.

**Why it matters:** A release can change who belongs in an analysis while the tool reports that analysis as unaffected. This undermines the central promise of rerunning affected analyses. The probe establishes the generic dependency-routing defect; it does not establish its incidence in the event’s protected analyses.

**Concrete repair:** Treat changes to eligibility/filter columns as relevant across the candidate population, including rows absent from the baseline result. Prefer explicit analysis dependencies; conservatively rerun when membership cannot be proven unchanged.

**Acceptance check:** Change an excluded row so it meets the analysis filter; require a rerun, updated membership, and a reason linking the changed field. Also retain an unrelated-column negative control.

### CF-02 · P1 · Duplicate clinical IDs disappear before comparison

**Rubric:** T1-1, T1-3. **Evidence:** observed source and reproduced synthetic behavior. **Confidence:** high within the tested scope.

**Source:** [cohort_firewall/tower/releases.py:100-110](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/releases.py#L100-L110). The row loader drops duplicate index values with keep="first" before building sample lists and fingerprints. Matrix loaders also retain only the first occurrence of each header ID (lines 122–125 and 151–155).

**Reproduction:** Appending a conflicting S1 clinical row changed the file hash, but load_release retained two rows and diff_releases returned an empty change list. The original first row was unchanged.

**Why it matters:** Identity and join defects are erased from the representation consumed by the detector. A changed file hash remains available, so this is not a claim of byte-identical releases. The specific defect is the absence of a duplicate-ID finding.

**Concrete repair:** Validate key uniqueness before normalization. Preserve duplicate counts, row positions and conflict summaries; emit a material identity finding and keep affected analyses unresolved until a reviewer chooses a deduplication policy.

**Acceptance check:** Append both identical and conflicting duplicate IDs; require explicit duplicate findings. Add duplicate matrix headers as a separate regression case.

### CF-03 · P1 · Release approval can omit signed-result evidence

**Rubric:** T1-3, T1-4. **Evidence:** observed source and reproduced synthetic behavior. **Confidence:** high within the tested scope.

**Source:** [cohort_firewall/review.py:93-123](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/review.py#L93-L123). tower_binding signs only question plus analysis IDs/verdicts (lines 35–39). review_release derives required acknowledgments from the submitted findings and affected_by arrays, which are not in that binding. Certificate creation uses the same binding in tower/findings.py:285–291.

**Reproduction:** For a locally signed synthetic Conditional result, approval without acknowledging F1 was rejected. Removing findings and affected_by while retaining the same valid certificate made approve_with_conditions succeed with an empty acknowledgment list. The resulting review signature verified.

**Why it matters:** A client can obtain a cryptographically valid review record without the evidence acknowledgment the original result required. This does not bypass the Blocked-verdict restriction or forge the signing key.

**Concrete repair:** Bind the full canonical evidence document, including finding IDs, affected_by, analysis outputs, repairs and release identity; or load the immutable server-side result by certificate ID. Reject any changed document before review.

**Acceptance check:** Mutate each protected evidence field independently after certification; all review requests must be refused. The original Conditional result must remain approvable with the required acknowledgments and note.

### CF-04 · P1 · Question approval can record an unbound question

**Rubric:** T1-2, T1-3, T1-4. **Evidence:** observed source and reproduced synthetic behavior. **Confidence:** high within the tested scope.

**Source:** [cohort_firewall/review.py:69-90](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/review.py#L69-L90). review_question correctly takes verdict and rule IDs from the signed certificate, but takes the recorded question text from result.spec without recomputing and checking spec_sha256. The engine signs the canonical spec at engine.py:70–72.

**Reproduction:** A valid certificate created for an original synthetic question was submitted with a different question_text. Approval succeeded, stored the changed question, and verify_review returned true.

**Why it matters:** The audit trail can attach a valid approval to question text not covered by that certificate. The probe exercises the review function directly; an HTTP/browser exploit was not run.

**Concrete repair:** Resolve the canonical question spec from an immutable server record, or hash the received canonical spec and compare it with the signed spec_sha256 before accepting a review.

**Acceptance check:** Changing question_text, intended_use, filters or feature_columns after certification must reject the review; unchanged canonical input must still work.

### CF-05 · P1 · Malformed inputs escape the safe fallback

**Rubric:** T1-4, T1-5. **Evidence:** observed source and reproduced synthetic behavior. **Confidence:** high within the tested scope.

**Source:** [cohort_firewall/engine.py:53-88](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/engine.py#L53-L88). The engine catches SpecError, but _short_circuit assumes spec has .get (line 136). Dictionary access at line 62 assumes an object. run_checks catches a bad comparison, but build_funnel repeats the same filter outside that protection.

**Reproduction:** A nonempty list spec and a nonempty list dictionary each raised AttributeError. A numeric column compared with a string using > raised TypeError. In contrast, an empty CSV returned INSUFFICIENT_EVIDENCE, confirming a working fallback for that input class.

**Why it matters:** Expected user mistakes can terminate evaluation instead of producing a usable Insufficient Evidence result. api/main.py:60–90 decodes JSON without validating object shape, so these shapes can reach the engine; HTTP status behavior is source-based inference, not a reproduced API test.

**Concrete repair:** Validate top-level and nested shapes at the boundary, enforce filter type compatibility, and make fallback formatting type-safe. Isolate funnel failure so an otherwise valid failure report can still return.

**Acceptance check:** Cover nonobject JSON, invalid column metadata, incompatible comparisons, and malformed filters; each must return a structured validation result without uncaught exceptions.

### CF-06 · P1 · The sample export overstates complete cases

**Rubric:** T1-2, T1-3, T1-7. **Evidence:** observed source and reproduced synthetic behavior. **Confidence:** high within the tested scope.

**Source:** [cohort_firewall/funnel.py:46-78](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/funnel.py#L46-L78). build_funnel removes "*" instead of expanding the same feature set as checks._resolve_features. It also skips absent required fields and still writes can_answer_question=yes for retained rows. A missing-feature warning exists in not_in_data, which is useful but contradicts the row-level export.

**Reproduction:** With feature_columns=["*"], a two-row input with one missing x value returned n_final=2 and two yes rows. With an explicitly absent predictor, it again returned two yes rows while listing the missing column in not_in_data.

**Why it matters:** Users downloading the sample list can treat incomplete records as able to answer the question. This finding concerns the funnel/export; it does not claim the overall policy verdict is Ready.

**Concrete repair:** Share one resolved feature/eligibility definition between checks and funnel. For absent required fields, mark eligibility unknown/unavailable rather than yes; distinguish potential cohort membership from complete cases.

**Acceptance check:** Wildcard and equivalent explicit feature lists must produce identical retained IDs. A missing required predictor must never export all rows as answerable.

### CF-07 · P2 · The optional wording guard accepts contradictions

**Rubric:** T1-4, T1-7. **Evidence:** observed source and reproduced synthetic behavior. **Confidence:** high within the tested scope.

**Source:** [cohort_firewall/report.py:28-49](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/report.py#L28-L49). report_passes_guard checks verdict substrings, required IDs for Blocked/Insufficient Evidence, and an alternate verdict marker on the first line. It does not constrain the advice that follows.

**Reproduction:** A synthetic string containing “Blocked [SCOPE]” followed by advice to ignore the warning and use the dataset for direct patient care returned true. No LLM request was made; this tests only acceptance of a supplied string.

**Why it matters:** Optional generated wording can conflict with the deterministic result while passing the guard. The default template path is unaffected, and no claim is made that a live model produced this text.

**Concrete repair:** Keep verdict, safety statement and remedies in immutable template sections. Restrict generated content to a clearly labeled explanatory field that cannot replace authoritative instructions; default to templates on validation failure.

**Acceptance check:** Reject contradiction and negation fixtures, including advice after the required tokens. Verify the standard deterministic report remains available without model credentials.

## Alignment with all seven Track 1 criteria

| Criterion | Supporting evidence | Gap and next evidence needed |
|---|---|---|
| T1-1 Finding data problems | Exact release fingerprints, changed-membership and label checks are present. | CF-01 and CF-02 reproduce missed effects/identity findings. Run approved public baseline and unseen mutation checks after repair. |
| T1-2 Research-question reasoning | Structured specs, question-specific checks and accepted limitations are implemented. | CF-01, CF-04 and CF-06 weaken eligibility and question provenance. Verify changed intended use and equivalent wildcard/explicit features end to end. |
| T1-3 Evidence and sources | Versioned rules, file hashes, fields, remedies and signed payloads provide traceability. | CF-02–CF-04 show why hashes/signatures alone do not establish complete evidence binding. Preserve and verify the exact reviewed document. |
| T1-4 Safety and uncertainty | Blocked approvals are rejected; unreadable CSV fails safely; research-only limits are explicit. | CF-03–CF-05 require boundary hardening; CF-07 affects optional wording. Test malformed requests and changed evidence at the API boundary. |
| T1-5 Working tool and setup | Selected core functions and six submitted disclosure cases ran with installed dependencies. | No clean installation, full submitted suite, production build or browser workflow was run. Malformed-input exceptions are reproduced. |
| T1-6 Useful next steps | Finding remedies, reconsideration evidence and proposed release repairs are structured. | Validate that each recommendation is tied to complete, immutable evidence; repair-simulation accuracy remains untested. |
| T1-7 Communication | Plain summaries, a funnel, shareable summaries and human-review text are implemented. | CF-06 produces conflicting answerability claims; CF-07 permits conflicting wording. User testing and accessibility remain untested. |

## Repair order and release checks

First, repair dependency routing and duplicate preservation (CF-01/02); these affect the underlying evidence. Next, bind reviewed content (CF-03/04) and contain malformed inputs (CF-05). Then reconcile the sample export (CF-06) and constrain optional generated prose (CF-07). Preserve the current default-deny and signed-verdict controls throughout.

Before presenting a repaired version as validated, pin its new SHA, rerun these synthetic regressions, then run the full submitted suite, a clean setup, a public unchanged-release control, approved public mutations and an end-to-end review flow. Keep organizer unseen-input evaluation separate from independent checks.

## Limitations and fairness

This is a bounded independent review under a deadline, not a clinical, security, privacy or accessibility certification. We did not watch the demo, verify README performance claims, test hosted services, access sealed releases, execute external reference-analysis code, run bootstrap/repair simulations, run the full submitted test suite, install dependencies, or build/test the web app. The synthetic analysis in CF-01 is intentionally reviewer-authored; no event analysis result is claimed. API reachability is established by source inspection only. Absence of a runtime check is not a failure or score deduction.

The HTML/PDF deck summarizes each issue separately; this report and TESTS.md carry the detailed qualifications. The reference rubric is the review repository’s captured Track 1 criteria, not a claim of newly verified organizer rules.
