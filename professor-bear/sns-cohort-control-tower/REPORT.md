# SNS Cohort Control Tower: independent first-pass review

Reviewed commit: `c1e8b79a2987cee6087d847867f9895deaa109a4`. Updated: **2026-11-14T19:40:03+00:00**. Track 1: Cohort Firewall.

**Status: source review, not a verified live demo.** No official score is assigned. Source findings below are hypotheses about reachable runtime behavior unless labelled otherwise; exact branches and limitations are stated. No student code or files were changed.

The source connects file and profile fingerprints to per-analysis results, proposed repairs and a cohort export. The strongest first-pass concern is that the export consumes proposed repairs directly and can restore records merely flagged for review. Verdict precedence and small-cohort format recognition also warrant direct probes.

## What it does well

### Analysis results include before, after and repair simulation

The output records each analysis, dependencies, affecting findings and simulated repair results. This makes changes inspectable, provided simulations are labelled as assumptions. [sns/engine/findings.py:427](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/findings.py#L427)

### Provenance distinguishes content hashes

Output lists file names and SHA-256 content fingerprints for each release. [sns/engine/findings.py:458](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/findings.py#L458)

### Analysis failures are not automatically Ready

An error on the new-release analysis is explicitly mapped to Insufficient Evidence before ordinary comparison. [sns/engine/impact.py:187](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/impact.py#L187)

## Issue-by-issue findings

### 1. Cohort export does not consult review decisions

**Priority: high. Evidence: source inspection; runtime reproduction pending.**

parse_repairs reads every proposed repair and run_cohort applies that mapping. Neither path checks the findings decisions section or an approval record. This converts proposals into cohort membership changes without a per-repair approval gate.

**Evidence:** [sns/engine/cohort.py:45](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L45); [sns/engine/cohort.py:123](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L123).

**Concrete change:** Require accepted decisions bound to the findings digest for approved exports; keep an explicit unapproved simulation mode for demonstrations.

**Acceptance check:** A rejected exclusion and an undecided restoration must not affect an approved cohort; a separately labelled preview may simulate them.

### 2. Flag for review can restore a missing record

**Priority: high. Evidence: source inspection; runtime reproduction pending.**

If a flagged record is absent from B but found in A, _apply_file_repairs adds it back and labels it flag_for_review_restored. Flagging asks for investigation; it does not establish that removal was an error. A deliberate withdrawal or corrected membership should not be reversed implicitly.

**Evidence:** [sns/engine/cohort.py:89](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/cohort.py#L89).

**Concrete change:** Keep flagged absences absent until an explicit restore decision with supporting evidence is recorded.

**Acceptance check:** A synthetic record intentionally removed from B stays absent when merely flagged; an approved restore is a separate tested action.

### 3. No affecting finding bypasses movement and minimum-group checks

**Priority: high. Evidence: source inspection; runtime reproduction pending.**

verdict_for returns Ready when affected_by is empty before comparing before/after values or sample adequacy. The report says unaffected analyses were rerun to confirm they did not move, but this branch does not enforce that confirmation. A detector miss or undersized unchanged cohort can therefore escape those safeguards at helper level.

**Evidence:** [sns/engine/impact.py:187](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/impact.py#L187); [sns/engine/findings.py:427](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/findings.py#L427).

**Concrete change:** Evaluate analysis validity, minimum evidence and unexplained output movement before the unaffected Ready path.

**Acceptance check:** Call the helper with no findings but changed results, then with an unchanged undersized group; neither should be an unqualified Ready.

### 4. Small wide matrices are silently unrecognized

**Priority: medium. Evidence: source inspection; runtime reproduction pending.**

Wide layout recognition requires more than ten TCGA-named columns. A valid wide file with ten or fewer samples falls through to long-layout detection and may return None, after which load_release omits it. Small cohorts are precisely where explicit insufficient-evidence handling matters.

**Evidence:** [sns/engine/release.py:60](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/release.py#L60); [sns/engine/release.py:88](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/release.py#L88).

**Concrete change:** Recognize layout from declared schema or robust headers independent of cohort size; retain a record of unsupported files instead of silently omitting them.

**Acceptance check:** Load valid wide synthetic matrices with 1, 10 and 11 samples. Each is either parsed correctly or rejected with an explicit reason.

### 5. Restoring baseline values is not independent correctness evidence

**Priority: medium. Evidence: source inspection; runtime reproduction pending.**

repair_restores_before compares the simulated repaired result with baseline output. That verifies recovery relative to the assumed trusted release, not whether the baseline record or proposed repair is factually correct. The README treats A as trusted; that assumption must remain visible at the repair decision.

**Evidence:** [sns/engine/findings.py:440](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/sns/engine/findings.py#L440); [README.md:1](https://github.com/saigunavardhan/sns-cohort-control-tower/blob/c1e8b79a2987cee6087d847867f9895deaa109a4/README.md#L1).

**Concrete change:** Label the result as baseline-recovery simulation and attach the evidence needed to approve each repair. Do not present recovery as proof of truth.

**Acceptance check:** Demonstrate a documented correction in B: the tool should preserve uncertainty about A rather than recommend automatic reversal solely to recover the old number.

## Exact official rubric: evidence, not scores

The maximum points below reproduce the official track weights. They are not points awarded. Supplemental dashboard and data-quality rules do not add scoring criteria.

| Criterion | Maximum | Evidence and question for judges |
|---|---:|---|
| Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support. | 20 | Fingerprint and subgroup logic exist; small-layout handling and independent adversarial controls need testing. |
| Reasoning for the research question. Changes its result appropriately when the research question or intended use changes. | 20 | Analysis dependencies are explicit; movement must be checked even when no finding points to it. |
| Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion. | 15 | Content hashes and before/after results support inspection; simulation assumptions need clear labels. |
| Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review. | 15 | Proposed repair application and flagged restoration need human authority controls. |
| Working tool and clear setup. Judges can run the core workflow from the submitted repository. | 15 | CLI and two interfaces exist; no automated test suite was found under a conventional tests directory in this pass. |
| Useful next steps. Suggested fixes are specific and match the size and importance of the problem. | 10 | Cohort export is concrete, but approved corrections and simulated repairs must remain separate. |
| Communication. Someone without specialist knowledge can understand the result and next step. | 5 | The README explains the workflow; clarify that repair recovery is conditional on baseline trust. |

## Checks actually performed

- Pinned and read source at `c1e8b79a2987cee6087d847867f9895deaa109a4`; original checkout was clean when inspected.
- Parsed **19/19** selected Python source files with `ast.parse`; **0** syntax failures. Parsing does not execute or validate behavior.
- Counted **0** `test_` function definitions in the inspected source set. This is a source count, not collected tests or passed tests.
- Validated every cited source path and starting line against the pinned commit.
- Rendered deck QA is recorded separately in `evidence/deck-qa.json` after rendering.
- No application builds, dependency installs, submitted runtime tests, live deployment checks, real-data evaluation, sealed-envelope runs or model-provider calls in this first pass.

[Machine-readable static checks](evidence/static-checks.json). No raw TCGA records, answer keys or credentials are included.

## Next investigation

Work through the issues above in order. Reproduce them in an isolated copy with invented inputs, including positive controls. Retain the recorded commit when comparing results. Changes after this review require a new commit-specific update; they do not retroactively change the evidence.

A statistician should review adequacy thresholds, interval assumptions and claims of bias or representativeness. A domain expert should review clinical meaning. Neither source inspection nor passing software tests establishes clinical validity.
