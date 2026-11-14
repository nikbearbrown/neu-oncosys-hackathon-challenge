# ReadySet Control Tower: independent review

**Review date:** November 14, 2026. **Team:** Automyte. **Track:** Cohort Firewall. **Product:** Cohort Control Tower.
**Reviewed commit:** [`4dd07736e99f96dd46cb6199c32bea32465bd20e`](https://github.com/a7ussein/readyset-control-tower/tree/4dd07736e99f96dd46cb6199c32bea32465bd20e). Later revisions are outside this review.

The project has a working deterministic comparison engine, an inspectable interface, and substantial tests. All **107 submitted tests passed**, the TypeScript check and Vite production build passed, and **10 browser smoke checks passed**. The largest gap is at the boundary between “nothing relevant changed” and “there is enough valid evidence to use this release.” Two empty directories returned **Ready**, with zero findings and neither analysis rerun.

The independent synthetic probes exercise that boundary and other review controls. **2 of 14 checks met the proposed expectations; 12 did not.** These deliberately targeted checks are not a random sample of behavior, twelve distinct official rubric failures, an official score, or an estimate of product accuracy. Some probe expectations propose additional guards for the documented narrow scope. Findings below explain that distinction.

[Issue-by-issue slide deck](slides.html) · [Editable slide content](slides.json) · [Test record](TESTS.md) · [Synthetic observations](evidence/observations.json) · [Reproduction script](reproductions/checks.py)

## Evidence and execution scope

This review uses source evidence plus execution of a pinned disposable copy. The original student checkout remained unchanged. The user explicitly authorized tests for this review; this does not change the repository collector's default non-execution policy.

Tests ran on macOS 26.5.1 ARM64, Python 3.14.6, Node 25.9.0 and headless Chrome 157.0.8103.51. A macOS sandbox denied private user-file contents, external networking and writes outside the temporary review folder. Credentials were absent. Loopback was allowed for server tests, with the usual local model port blocked. Browser checks used a fresh unsigned-in profile and blocked non-loopback page requests. Dependency installation used the lockfile, disabled lifecycle scripts, and empty npm config files. Build execution then ran without external networking.

No organizer sealed envelope was opened. Two submitted envelope tests use synthetic fake unsealing scripts in temporary folders; those passed. The 15 recipe files under tests/releases require event data and a separate scoring workflow and were not executed. The initial run did not fetch real data. The later verified public A-versus-A control is documented below; no altered-real-data performance test, live deployment, external model service, clinical evaluation or full accessibility audit was run. Screenshots and reproduced values here use invented samples.

## What works well

- **Deterministic detection and traceability.** The engine fingerprints content and emits kinds, affected analyses, evidence, limitations and proposed repairs. The positive swap probe detected a swap affecting A1 and left A2 unrelated. Keep the separation between detection, interpretation and action. See [control_tower/detect.py:128](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/detect.py#L128) and [control_tower/compare.py:185](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L185).
- **Question-dependent behavior.** In the browser, the synthetic swap gave Conditional when A1 was selected and Ready when only A2 was selected. Toggling back restored Conditional. This supports the core dependency behavior for the tested example; it does not validate arbitrary research questions.
- **Inspectable evidence.** The synthetic browser view displayed before/after values, an effect calculation, suggested repair and limits. The assistant answered the visible question from the findings. The interface required a name before its review button enabled, and a normal review survived reload. The direct backend has a separate weakness below.
- **Useful tests and portability.** The 107 tests cover detectors, [control_tower/__main__.py:76](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/__main__.py#L76), unusual input formats, server behavior and deterministic responses. The Python engine uses the standard library. The production frontend built from its lockfile. These are observed results, not merely README claims.
- **Reviews bind to evidence.** The review key incorporates evidence and file hashes; the submitted test for changed evidence under the same release name passed. Preserve this behavior while improving the event history. See [control_tower/webserver.py:696](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/webserver.py#L696).
- **The half-percent convention is disclosed.** README describes it as a convention rather than a validated standard. The recommendation below concerns how it is used, not a missing explanation. See [README.md:51](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/README.md#L51).

## Issue 1: required-input failures can produce Ready

**Priority: high. Status: reproduced.** Both empty directories, both releases missing clinical/protein inputs, identical zero-byte required files, and identical plain invalid bytes all returned Ready, zero findings and `not_rerun` for A1/A2.

**Evidence:** compare skips a file absent from both releases, skips equal hashes, and skips an analysis with no associated finding; its final fallback is Ready. The [control_tower/__main__.py:76](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/__main__.py#L76) checks that its arguments are directories, without establishing required input validity. See [control_tower/compare.py:58](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L58), [control_tower/compare.py:151](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L151), [control_tower/compare.py:220](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L220) and [control_tower/__main__.py:76](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/__main__.py#L76).

**Why it matters:** a successful comparison of no usable evidence can be read as permission to proceed. Hash equality establishes unchanged content, including unchanged invalid content. The synthetic output also passes the organizer JSON schema, demonstrating that format validation cannot establish readiness.

**Concrete change:** add preflight for each selected analysis before change detection: resolve required inputs, decode and validate schema, establish required rows/columns and compute availability. Return Insufficient Evidence with specific missing or unreadable artifacts when comparison cannot be supported. Cache successful baseline-validation receipts against hashes to preserve efficient selective reruns.

**Acceptance:** the four named probes should produce Insufficient Evidence without a crash or successful readiness exit code. A valid unchanged pair must remain distinguishable and fast. Supplemental lenses: medical16 sections 1–3 and 12–13; dashboard missing/error-state guidance.

## Issue 2: a change comparison needs an explicit baseline-quality boundary

**Priority: high for broad readiness wording. Status: reproduced behavior; scope interpretation requires judge judgment.** An identical synthetic duplicate present in both releases returned Ready and no findings. The code explicitly limits itself to changes between releases, so failure to rediscover every old defect is not itself a violation of that documented comparison contract.

**Evidence:** the `SCOPE` statement and hash shortcut in [control_tower/compare.py:58](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L58). The UI question “Can I use B for my analyses?” is broader than a change-only guarantee, observed in the browser screenshot.

**Concrete change:** separately expose baseline validation and release-change compatibility. Require a trusted baseline receipt or show “No relevant new change; baseline fitness not established.” Record who accepted the baseline, for what analysis, and against which hashes. Do not imply that a hash proves clinical or statistical suitability.

**Acceptance:** carry a known preexisting duplicate or missingness defect through both releases. The UI must make the unassessed baseline visible even when the change result is empty. A judge should decide whether the submitted baseline assumption is adequate for the actual challenge, rather than apply an invented penalty.

## Issue 3: no measured values, but a Conditional result

**Priority: high. Status: reproduced.** Blanking the full ERALPHA row in the new synthetic release produced Conditional. A1 reported five sample IDs, positive/negative group counts of three/two, but both means and their difference were null. The submitted test explicitly expects Conditional for this input.

**Evidence:** [control_tower/analyses.py:155](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/analyses.py#L155) and [tests/test_empty_inputs.py:61](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/tests/test_empty_inputs.py#L61). Counts include eligible IDs even when their target measurements are absent; the mean becomes NaN and is converted to null. A function returning a dictionary is treated as a completed analysis.

**Concrete change:** report eligible count, measured count and missing count separately for each group. Add an analysis-availability result. With no measured target values, prevent the analysis from being treated as usable. Use Blocked or Insufficient Evidence according to a documented distinction between a known preventing defect and evidence that cannot support assessment.

**Acceptance:** the blank-row probe must report zero measured values and an unavailable analysis. It should identify the data required to reconsider the result. Keep the detector's existing missing-data evidence and repair suggestion.

## Issue 4: numerical effect classification needs separate precision and adequacy controls

**Priority: medium, potentially higher for a consequential question. Status: reproduced helper/analysis behavior.** These are computational probes, not proof of harm on the real dataset:

| Probe | Observed result | Suggested rule |
|---|---|---|
| Difference changes from 0 to 0.01 | Relative fraction set to 1.0 | Relative change is undefined at zero; show absolute change and an explicit tolerance |
| Sample count falls from 1,000 to 1 while difference remains 2.9 | `_size` reports small with 0.999 count loss | Assess sample adequacy/coverage separately from movement in a headline estimate |
| Positive mean increases by 0.0004 | Both means round to 2.0; effect reports none | Compare full precision; round for display |

**Evidence:** [control_tower/compare.py:303](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L303) and [control_tower/compare.py:342](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/compare.py#L342) compare the outputs returned by [control_tower/analyses.py:155](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/analyses.py#L155), which rounds to three decimal places. Headline selection prefers a difference over group means/counts. [README.md:51](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/README.md#L51) discloses the 0.5% threshold as a convention.

**Concrete change:** keep raw numeric results for calculation, store display values separately, represent an undefined relative change explicitly, and use absolute plus relative tolerances appropriate to the selected analysis. Introduce data-adequacy warnings independent of effect magnitude. Do not describe the half-percent threshold as a universal scientific acceptance threshold.

**Acceptance:** regression tests cover zero/near-zero baselines, opposite signs, precision near thresholds and large count loss with unchanged means. A statistician should review the adequacy criteria; this review does not prescribe a universal sample-size minimum.

## Issue 5: modification time silently selects the data

**Priority: high for reproducibility. Status: reproduced.** A folder held a changed `protein_rppa.tsv.gz` and an unchanged `protein_rppa.tsv`. With the plain file newer, the verdict was Ready. Making only the gzip file's timestamp newer changed the verdict to Conditional. Neither file's contents changed between comparisons.

**Evidence:** [control_tower/release.py:33](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/release.py#L33) chooses the candidate with maximum modification time. Alternate formats are a useful convenience, but timestamps do not establish which dataset the user intended.

**Concrete change:** reject conflicting aliases, or require an explicit user selection recorded in the manifest. If aliases are semantically equal, document the equivalence before accepting one. Record the actual resolved filename as well as its hash.

**Acceptance:** touching, extracting or copying files must not silently change a review's input selection. Present the conflict and its resolution clearly. Preserve support for a single valid TSV, CSV or workbook.

## Issue 6: the backend can remove human-review requirements without a name

**Priority: high for review integrity. Status: reproduced over loopback HTTP.** Posting a valid finding key, confirmed status and approved fix without a reviewer returned HTTP 200, stored an empty reviewer, and set `needs_human_review` to false. The UI correctly disables its button until a name exists, but that guard is not enforced by the endpoint.

**Evidence:** [control_tower/webserver.py:258](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/webserver.py#L258) validates key/status then converts an absent reviewer to an empty string. [control_tower/webserver.py:664](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/webserver.py#L664) changes the outgoing review state. The normal named UI path passed browser checks.

**Concrete change:** validate nonblank reviewer and applicable role/reason on the server before updating state; verify the key is associated with the current evidence. For a single-user local prototype, call the identity self-attested. If deployed for multiple reviewers, bind authority to authenticated identities. Authentication infrastructure is not automatically a hackathon requirement, but an interface field alone cannot verify identity.

**Acceptance:** blank/malformed reviewers receive an error and leave findings unchanged; a valid named review succeeds. Test the API as well as the UI. No claim of remote exploitation or production exposure is made.

## Issue 7: review state does not preserve a decision history

**Priority: medium. Status: reproduced.** A second decision replaced the first stored record; clearing the decision left zero records. This is current-state persistence, not an append-only audit trail.

**Evidence:** [control_tower/webserver.py:258](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/webserver.py#L258) assigns `saved[key]` or removes it; [control_tower/webserver.py:732](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/webserver.py#L732) rewrites the JSON dictionary. Comparison history separately replaces matching comparison entries and retains only its latest 200 entries in [control_tower/webserver.py:182](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/webserver.py#L182).

**Concrete change:** retain immutable decision events with actor, time, evidence fingerprint, prior/new decision and reason. A withdrawal should create an event instead of erasing history. Derive the current state from those events. Protect writes against partial-file loss and concurrent updates.

**Acceptance:** confirm, dismiss and clear a synthetic finding; the complete ordered event sequence remains exportable, while the current UI state reflects the last event. Preserve the existing evidence-key invalidation behavior.

## Optional routing: disclosure exists; no actual leak demonstrated

**Status: source review and a mocked request.** The first suspicion that cloud transmission was undisclosed is not supported: [web/src/Ask.tsx:209](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/web/src/Ask.tsx#L209) explicitly says only the question goes to Anthropic. The mocked probe confirmed the typed question appears in the payload and findings are not attached. No real API request or sensitive input was sent.

The improvement is narrower: user-entered questions can themselves contain sensitive information. Add a visible instruction to use no patient identifiers or confidential text, and show the actual provider near the opt-in. Verify an intended “local” endpoint remains local if configurable. These are prospective safeguards, not evidence of a breach. See [control_tower/understand_ai.py:63](https://github.com/a7ussein/readyset-control-tower/blob/4dd07736e99f96dd46cb6199c32bea32465bd20e/control_tower/understand_ai.py#L63).

## Cohort Firewall rubric mapping

Weights below are the official maxima, not awarded points. No numerical score is assigned.

| Official criterion | Maximum | Supported strengths | Evidence needing attention |
|---|---:|---|---|
| Finding data problems | 20 | Deterministic swap detection; broad submitted detector tests pass | Missing-in-both/identical-invalid inputs escape readiness assessment; baseline boundary |
| Reasoning for the research question | 20 | A1/A2 selection changes verdict in observed browser test | Null-result availability and task-specific adequacy; severity helper limitations |
| Evidence and sources | 15 | Hashes, witnesses, limitations and affected/unaffected analyses | Explicit physical filename selection; baseline receipt; preserved review events |
| Safety and uncertainty | 15 | Clinical refusal tests, named UI review, visible limitations | Backend blank identity; Ready on absent evidence; broader interpretation of baseline fitness |
| Working tool and clear setup | 15 | 107 tests, build and browser smoke checks pass locally | Verified public A-versus-A control now exists; unseen exercise and other operating systems remain unverified |
| Useful next steps | 10 | Concrete suggested repairs and priority explanations visible | Availability-specific remediation, traceable actor/event records, threshold justification |
| Communication | 5 | Plain-language synthetic walkthrough, source-linked evidence | Separate change compatibility, baseline quality and statistical adequacy clearly |

## Suggested repair order and judge questions

1. Required-input and analysis-availability gates, including missing-in-both inputs.
2. Deterministic file resolution and explicit baseline status.
3. Server-side reviewer validation and append-only decision events.
4. Full-precision effects, zero handling and an independent adequacy assessment.
5. Repeat the synthetic cases, then an organizer-authorized real-data and unseen-input run.

Ask the team to show an empty comparison, a missing target measurement, conflicting file variants and a direct blank-name request. Then ask them to explain what Ready guarantees and show a historical decision after it has been changed. These are review suggestions, not additional official scoring rules.

This is a promising working comparison prototype with concrete, fixable gaps. It is suitable for evidence-based judging with those limits visible. Data fitness, clinical suitability, accessibility conformance and production readiness have not been established by this review.

Latest unchanged-public-input control: verified frozen Release A versus itself returned Ready and zero findings. [Scope and aggregate evidence](TESTS.md#frozen-public-baseline-control). This does not invalidate the synthetic missing-input or small-matrix findings.

## Companion source audit

A separate reviewer supplied [a detailed source audit](audit-codex-23484638-pass-01.md) and [an issue deck](slides-codex-23484638-pass-01.html) ([Markdown version](slides-codex-23484638-pass-01.md)), committed 2026-11-14T14:53:45-05:00. The companion is a source audit. The main report adds 107 submitted tests, synthetic regressions, a production build and browser checks, plus the later public unchanged-input control. The companion's “not run” statements describe that reviewer's pass, not all testing in this folder. [Cross-review status](../REVIEW-STATUS.md) explains the relationship.
