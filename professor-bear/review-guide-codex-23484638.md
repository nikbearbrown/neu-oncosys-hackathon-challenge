# Companion Audit Reading Guide

Updated 2026-11-14T20:23:49.414971+00:00. Review run `codex-23484638`.

Read this guide with [Cross-review status](REVIEW-STATUS.md), each main REPORT.md and its TESTS.md. This is an additive navigation and interpretation update. Earlier source reports and decks remain intact. No official scores or ranking are assigned.

## Concise Deck Revision 2

These decks replace sentence truncation with complete, shorter slide copy. Each finding retains its own slide and source links. The Markdown deck includes the fuller reasoning in speaker notes. The original first-pass reports remain the detailed source reference.

| Entry | Detailed source supplement | Concise browser deck | Slide notes | Main runtime review |
|---|---|---|---|---|
| ReadySet Control Tower | [Audit](readyset-control-tower/audit-codex-23484638-pass-01.md) | [HTML](readyset-control-tower/slides-codex-23484638-pass-02.html) | [Markdown](readyset-control-tower/slides-codex-23484638-pass-02.md) | [Report](readyset-control-tower/REPORT.md) and [tests](readyset-control-tower/TESTS.md) |
| Tripwire / Driftwire | [Audit](tripwire/audit-codex-23484638-pass-01.md) | [HTML](tripwire/slides-codex-23484638-pass-02.html) | [Markdown](tripwire/slides-codex-23484638-pass-02.md) | [Report](tripwire/REPORT.md) and [tests](tripwire/TESTS.md) |
| Identity Crisis Control Tower | [Audit](identity-crisis-control-tower/audit-codex-23484638-pass-01.md) | [HTML](identity-crisis-control-tower/slides-codex-23484638-pass-02.html) | [Markdown](identity-crisis-control-tower/slides-codex-23484638-pass-02.md) | [Report](identity-crisis-control-tower/REPORT.md) and [tests](identity-crisis-control-tower/TESTS.md) |
| Busy Beavers Cohort Firewall | [Audit](busy-beavers/audit-codex-23484638-pass-01.md) | [HTML](busy-beavers/slides-codex-23484638-pass-02.html) | [Markdown](busy-beavers/slides-codex-23484638-pass-02.md) | [Report](busy-beavers/REPORT.md) and [tests](busy-beavers/TESTS.md) |
| OncoSys Cohort Studio | [Audit](oncosys-cohort-studio/audit-codex-23484638-pass-01.md) | [HTML](oncosys-cohort-studio/slides-codex-23484638-pass-02.html) | [Markdown](oncosys-cohort-studio/slides-codex-23484638-pass-02.md) | [Report](oncosys-cohort-studio/REPORT.md) and [tests](oncosys-cohort-studio/TESTS.md) |
| SNS Cohort Control Tower | [Audit](sns-cohort-control-tower/audit-codex-23484638-pass-01.md) | [HTML](sns-cohort-control-tower/slides-codex-23484638-pass-02.html) | [Markdown](sns-cohort-control-tower/slides-codex-23484638-pass-02.md) | [Report](sns-cohort-control-tower/REPORT.md) and [tests](sns-cohort-control-tower/TESTS.md) |

## SNS Reconstruction Follow-Through

[Focused report](sns-cohort-control-tower/audit-codex-23484638-pass-03.md) - [Slides](sns-cohort-control-tower/slides-codex-23484638-pass-03.html) - [Full slide notes](sns-cohort-control-tower/slides-codex-23484638-pass-03.md).

- **SN-08, source only:** a required clinical filter has no failure branch when its field is absent. An unchanged cohort count can conceal that its eligibility test did not run.
- **SN-09, source only:** the main export can fall back to clinical data from A, while its reconstruction reads only B clinical data. Exact membership parity needs a targeted fixture.
- **SN-10, corroborated separately:** JSON booleans enter generated Python as names. The parallel reviewer independently reproduced the A2 NameError with an A1 passing control before this supplement was merged. This is the same issue as main REPORT.md issue 6, not a second scoring event. See the [pinned parallel observation](https://github.com/nikbearbrown/neu-oncosys-hackathon-challenge/blob/07721d9/professor-bear/sns-cohort-control-tower/REPORT.md#6-the-generated-a2-reproduction-script-fails-on-json-booleans).

The source reviewer did not execute the submission or generated script. The separate runtime evidence must retain its own environment and limitations.

## Evidence Reconciliation

**Tripwire:** the first companion source pass discussed an early tiny-fixture control that returned Blocked. A corrected four-sample full-API fixture later returned Ready for release compatibility while its question-specific adequacy correctly returned Insufficient Evidence. The concise deck reflects the later observation. This supports distinguishing the meanings of Ready, not claiming that the question checker ignores sample size. The [main report](tripwire/REPORT.md) and [cross-review status](REVIEW-STATUS.md) retain this history.

**Identity Crisis and Studio:** earlier companion test-count references describe the parallel review state at that time. Later public-release runs are recorded in current TESTS.md. Do not sum retries or treat suites with different assertions as comparable quality measurements. This source reviewer did not rerun them.

**Busy Beavers:** duplicate-ID ordering and rounded-hash screening are source findings in the companion. The 500-target scope concern is shared with the main review and has separately reported runtime corroboration. Do not count it twice. Conditional-versus-Blocked policy still needs a question-specific explanation rather than a universal clinical cutoff.

**Unchanged public controls:** a passing A-versus-A control demonstrates a useful baseline path. It does not refute a distinct missing-input, small-matrix or rejected-repair fixture. Likewise, a targeted failing fixture does not measure population accuracy.

## Decision Boundaries

- Confirm each official final-submission commit and product declaration. Pinned local branches are evidence identities, not official freeze receipts.
- Distinguish observed source, helper reproduction, full-engine execution, browser observation and qualified human judgment.
- Keep compatibility, input fitness, statistical adequacy and human approval separate.
- A hash identifies content. It does not authenticate a reviewer or establish that a baseline is scientifically correct.
- A diagnostic export can be useful while remaining unapproved. Its restrictions must survive separation from the companion report.
- No report here establishes clinical validity, unseen-input performance, production security or full accessibility.

## Local Viewing

The HTML decks are self-contained. For example:

```bash
open "/Users/nik/Documents/agents/neu-oncosys-hackathon-challenge/professor-bear/tripwire/slides-codex-23484638-pass-02.html"
```

## Later Evidence And UI Correction

Update after the initial guide snapshot, November 14, 2026, 20:34 UTC:

- **Identity Crisis defaults need a correction.** The callable API defaults to strict missing-check handling, but the browser initializes its permissive setting to on. Earlier companion wording that called the bypass nondefault applies to the API only. The [UI-state follow-through](identity-crisis-control-tower/audit-codex-23484638-pass-03.md) and [separate deck](identity-crisis-control-tower/slides-codex-23484638-pass-03.html) trace the initialization, data-cache identity, optional-summary cache and sign-off applicability checks. These new session-level consequences are source-derived and need targeted runs. No claim is made that every built-in card currently has an unregistered check.
- **SNS SN-08 and SN-09 now have separate runtime corroboration.** The parallel reviewer published four invented-data CLI/reconstruction cases in [reconstruction-parity.json](sns-cohort-control-tower/evidence/reconstruction-parity.json). The ordinary case retained exact membership. A missing required column exported 40 rows without an eligibility error. The missing-B-clinical and clinical-CSV cases exported 39 rows from the main path but reconstructed 40, adding one member. These are targeted cases with positive controls, not an accuracy estimate. This source reviewer did not execute them.
- **Busy Beavers BB-01 and BB-02 now have separate runtime corroboration.** The parallel [supplement probes](busy-beavers/evidence/supplement-probes.json) report missed repeated IDs and a rounded-hash miss, with within-tolerance and larger-change controls. The original source report remains a record of its own unexecuted pass.
- **Studio CS-03 now has a separate warning-policy probe.** The parallel [supplement probes](oncosys-cohort-studio/evidence/supplement-probes.json) report unchanged reconstruction producing eight rows and a changed-manifest rerun warning but continuing to seven rows. Whether exploratory continuation is appropriate remains a product-policy question. A warning does not itself certify faithful reproduction.

Later observations qualify the earlier snapshot only for the paths actually tested. Preserve the positive controls and the distinction between compatibility, adequacy, evidence identity and human approval.
