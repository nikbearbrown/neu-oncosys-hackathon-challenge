# Cohort Firewall Control Tower



Professor Bear | Independent Audit

Track 1: cohort-control-tower
Commit ab5084f7caaa
Static source review; no official score


<!-- Speaker notes:  -->

---

# Review Scope



Pinned source with explicit limits

99 text files collected; 39 entries excluded.
Selected implementation paths were inspected.
No submission code, tests, data fetches or sealed inputs were run.
The official freeze commit still needs confirmation.


<!-- Speaker notes:  -->

---

# Policy separates measurements from versioned rules and missing-check states

Strength | CFT-06 | T1-4 | P2

Versioned rules and measured checks have separate roles. Missing expected checks and absent metrics have explicit evidence-gap paths.

Conditional acceptance cannot ordinarily waive Blocked findings.
Retain these controls while hardening input boundaries.

- [Source 1](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/policy.py#L32-L37)
- [Source 2](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/policy.py#L53-L66)
- [Source 3](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/policy.py#L68-L87)
- [Source 4](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/policy.py#L99-L114)

<!-- Speaker notes: Policy loads YAML with safe_load and records the rule-file hash. Evaluation produces explicit Insufficient Evidence for missing expected checks, not-evaluable checks and rule references to absent metrics. Conditions use a fixed operator mapping rather than eval. Accepted limitations apply only to allowed Conditional findings, and ignored acceptances remain visible. These paths are useful controls, not a guarantee that all input shapes or metric values are valid.

Retain the policy/measurement separation, version hash and explicit unavailable states. Keep malformed-input validation separate and test None/type mismatches rather than assuming the generic evaluator covers every shape. Preserve the parallel report's distinct malformed-input findings.

Acceptance: Omit an expected check, return not_evaluable, remove a referenced metric and submit an unrecognized acceptance. Verify each has a visible and distinct result. Confirm a permitted Conditional acceptance works while Blocked cannot be waived. Do not infer success from source definitions alone.

Confidence: High for inspected evaluator controls; no policy tests were run in this pass. -->

---

# Baseline cache identity includes current file-content hashes

Strength | CFT-07 | T1-3 | P2

The baseline cache key includes current file hashes, rather than only a path or release label.

File and decompressed-content hashes have explicit conventions.
Keep the selected-file scope and candidate availability visible.

- [Source 1](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/releases.py#L181-L201)
- [Source 2](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/releases.py#L208-L219)
- [Source 3](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/run.py#L27-L35)
- [Source 4](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/findings.py#L264-L268)

<!-- Speaker notes: The release cache key combines a cache-version token with file_sha256 for every selected present file. A same-path content change therefore selects a different cache entry rather than reusing a path-only result. The loader also records both compressed-file and decompressed-content hashes, and the run checks compared baseline file hashes against the frozen checksum map. The verification scope is the selected compared-file set, not a proof of all required candidate inputs or of scientific truth.

Keep content-bound cache keys and explicit hash conventions. Record the selected-file scope and include required-input availability before judging compatibility. Treat a matching hash as byte identity, not confirmation that an analysis or baseline is scientifically suitable.

Acceptance: With invented inputs, reuse an unchanged release, replace a file at the same path, and change only compression metadata. Confirm cache and provenance behavior match the declared file/content conventions. Verify omitted required files are still handled by CFT-01's separate gate.

Confidence: High for complete cache-key and hash code; no cache read/write or dataset load occurred in this review. -->

---

# Approval policy distinguishes unavailable results and explicit conditions

Strength | CFT-08 | T1-6 | P2

The decision matrix separates approval, conditional approval, rejection and requests for more evidence.

A separate Blocked-approval control was rejected.
Preserve the policy and bind its complete reviewed subject.

- [Source 1](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/review.py#L19-L27)
- [Source 2](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/review.py#L42-L51)
- [Source 3](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/review.py#L102-L122)
- [Source 4](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/ledger.py#L47-L67)
- [Source 5](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/ledger.py#L1-L8)

<!-- Speaker notes: Allowed decisions depend on the signed verdict. Blocked and Insufficient Evidence allow reject/request_more but no approval; Conditional allows approve_with_conditions. Approval requires the relevant acknowledgments and nontrivial notes under the inspected policy, and release review requires a decision for every supplied analysis. The published Blocked-approval synthetic control was rejected. These are meaningful safeguards even though CFT-04/05 show that surrounding document binding is incomplete. Reviewer names are self-attested strings, not authenticated identity.

Preserve the decision matrix and original records. Bind the complete reviewed subject before applying those rules, and surface ledger-write errors distinctly from a successfully recorded decision. Keep the documented end-truncation limitation visible when presenting the hash-chained ledger.

Acceptance: Exercise each verdict/decision pair with missing versus complete acknowledgments and notes. Retain the rejected Blocked-approval control. Then verify the resulting review subject matches the immutable evidence and that a logging failure is visible without claiming a complete ledger.

Confidence: High for source decision controls and separately reported narrow rejection control; authentication, multi-process persistence and full API behavior remain untested. -->

---

# Missing candidate inputs can bypass analysis availability checks

Risk | CFT-01 | T1-1 | P1

Candidate-present files determine the diff. Missing required files can be listed as not compared while no change triggers a rerun.

This complete-entry consequence is source-derived and unexecuted.
Preflight each analysis; preserve the optional-RNA control.

- [Source 1](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/run.py#L24-L37)
- [Source 2](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/run.py#L78-L82)
- [Source 3](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/analyses.py#L93-L122)
- [Source 4](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/diff.py#L227-L236)
- [Source 5](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/findings.py#L67-L77)
- [Source 6](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/rules/tower_v0_1.yaml#L9-L21)

<!-- Speaker notes: run_tower builds in_b from files present in the candidate and loads baseline fingerprints only for that set. Files missing from B are listed as not_compared, so the diff never receives the baseline-only file needed to emit file_missing. evaluate_analyses runs the baseline from its full path, but only tries B when a detected relevant change exists. An unchanged carried file plus an omitted required clinical file can therefore leave no relevant change, skip B's analysis and retain the Ready policy fallback when compared baseline hashes verify. A limitation lists the omitted file, but no independent per-analysis candidate-input gate precedes the not_rerun branch. This is a source-derived full-path inference, not an executed Ready result.

Preflight each protected analysis's required inputs in A and B before dependency filtering. Represent omitted optional/unneeded modalities separately from missing required inputs. Preserve the not_compared disclosure, but give an unavailable analysis Insufficient Evidence even if other compared bytes are unchanged. Do not require RNA for an analysis that does not read it.

Acceptance: With invented complete A and matching public-style expected hashes, compare B containing unchanged protein but no clinical file; verify A1/A2 cannot be labelled unqualified Ready or unaffected. Use valid unchanged A/B as a positive control and omitted RNA with A1/A2 as an optional-modality control. Record the complete run_tower result rather than only diff_releases.

Confidence: High for the file-selection and rerun control flow; the stated complete-entry outcome remains unexecuted and requires the named control. -->

---

# Dependency routing considers baseline members but can miss new entrants

Risk | CFT-02 | T1-2 | P1

The impact gate usually checks baseline result members. An existing excluded sample can become eligible without triggering a rerun.

A separate generic count probe corroborates this gate.
Test actual protected analyses with newly eligible records.

- [Source 1](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/analyses.py#L101-L122)
- [Source 2](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/analyses.py#L123-L133)
- [Source 3](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/analyses.py#L38-L44)

<!-- Speaker notes: evaluate_analyses takes used from the baseline result's sample_ids and generally requires changed IDs to intersect that set. Only added/new_duplicate changes receive a separate sample-type route. A label change on an existing previously excluded row can alter eligibility without intersecting baseline used, so the candidate result is not run. The separately published invented group-count probe reports baseline n=1, actual changed n=2, but affected=false/not_rerun/after=null. That probe exercises a reviewer-authored analysis, not the actual event A1/A2 functions; this source review traced the generic gate and the corresponding eligibility risk without running it.

Declare eligibility/filter dependencies explicitly and evaluate the relevant candidate population, not only the baseline output IDs. Use the union of before/after potential members or conservatively rerun when an eligibility change cannot be proven irrelevant. Preserve precise reasons for genuinely unrelated changes.

Acceptance: Start with an existing primary sample excluded for an unknown label, then give it an allowed ER/PAM50 label in B. Demonstrate affected analysis, updated membership and linked evidence; retain an unrelated-field negative control and a still-ineligible label-change case. Verify actual protected analyses in a separately authorized test, not just a generic counting function.

Confidence: High for inspected routing and separately reported generic helper reproduction; protected-analysis prevalence and full application behavior are not established. -->

---

# Duplicate identifiers disappear before detection

Risk | CFT-03 | T1-1 | P1

Loaders keep the first repeated ID before detection. A separate clinical fixture changed bytes but produced no duplicate finding.

The file hash still changed.
Preserve duplicate diagnostics before normalization.

- [Source 1](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/releases.py#L100-L110)
- [Source 2](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/releases.py#L119-L137)
- [Source 3](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/releases.py#L149-L174)
- [Source 4](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/diff.py#L77-L90)

<!-- Speaker notes: The row loader drops duplicate index values with keep=first before creating the sample list and fingerprints. Numeric and text matrix loaders similarly select the first occurrence of each header ID without retaining duplicate diagnostics. diff_file then compares sets and fingerprints from those normalized views. A parallel invented clinical-row probe reported three input rows reduced to two loaded rows and an empty change list even though the file hash changed. That corroborates the clinical loader/diff case; duplicate matrix headers remain a separate proposed check rather than an executed result here.

Validate uniqueness before deduplication and retain occurrence counts, positions and conflicts as evidence. Keep original records intact. If a normalized view is needed for continued diagnostics, label its policy and keep affected analyses unresolved until a person accepts a suitable resolution.

Acceptance: Append both identical and conflicting repeated clinical IDs with the first record unchanged. Then repeat a matrix sample header, varying the second profile. Require explicit identity diagnostics and separate analysis status. Include unique-ID unchanged inputs as a quiet control.

Confidence: High for source and the separately reported clinical fixture; no duplicate-header or end-to-end engine run was performed by this reviewer. -->

---

# Release review checks verdict binding but not the full evidence document

Risk | CFT-04 | T1-4 | P1

The signed release binding covers question and verdicts, but acknowledgments depend on unsigned findings and affected_by fields.

A separate probe stripped evidence and obtained a signed Conditional review.
Blocked approval remained rejected; no signing key was forged.

- [Source 1](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/review.py#L35-L39)
- [Source 2](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/review.py#L93-L112)
- [Source 3](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/tower/findings.py#L285-L291)
- [Source 4](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/api/main.py#L302-L321)

<!-- Speaker notes: tower_binding contains the question and analysis IDs/verdicts only. Certificate creation uses that binding, while review_release derives required acknowledgments from client-supplied findings and affected_by arrays that are not covered by it. The API passes the supplied findings document directly to the review function. The parallel synthetic probe reports that original Conditional evidence required F1 acknowledgment, but stripping findings/affected_by while retaining the valid certificate allowed a signed approve_with_conditions record with no acknowledgments. The Blocked-verdict guard still rejected approval; no private key was forged and no HTTP/browser exploit was reproduced.

Review an immutable server-side result selected by certificate ID, or bind and verify the complete canonical document used for decisions, including findings, analysis evidence, affected_by, repairs and release identity. Reject changed decision inputs before constructing the review. Keep the current signed-verdict restrictions and note requirements.

Acceptance: Change findings, affected_by, before/after values, repairs and release metadata independently after issuing a certificate. Each changed review request should be rejected or clearly treated as a new unsigned result. The original Conditional result with all required acknowledgments and note is the positive control; Blocked approval must remain rejected.

Confidence: High for the partial binding and separately reported direct-function reproduction; no application request or key material was accessed. -->

---

# Question review records text without checking its signed spec hash

Risk | CFT-05 | T1-3 | P1

Question review verifies the certificate but records supplied question text without comparing its spec hash.

A separate helper probe accepted changed question text.
Review the immutable signed spec or require a new evaluation.

- [Source 1](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/engine.py#L70-L72)
- [Source 2](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/certificate.py#L50-L63)
- [Source 3](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/cohort_firewall/review.py#L69-L90)
- [Source 4](https://github.com/NinadRao0707/cohort-firewall/blob/ab5084f7caaa57e68636e2cd3fde97b20a47bf69/api/main.py#L281-L299)

<!-- Speaker notes: The engine signs qs.canonical_json through spec_sha256. review_question verifies the certificate and reads verdict/rule IDs from that signed payload, but records question_text from the supplied result.spec without recomputing its canonical hash. The API accepts that client result. The parallel direct-function probe reports an accepted signed review with a changed question string while the certificate remained from the original question. It does not establish that every field or every UI interaction is similarly accepted, and it does not forge a certificate.

Resolve the original canonical spec from immutable storage, or validate the received canonical spec against the signed spec_sha256 before saving a review. Bind dataset identity, policy and question together and present older reviews as historical when any bound input changes.

Acceptance: After certification, change question_text, intended use, filters and predictor lists independently. Require rejection or a new evaluation before review. Reordered equivalent JSON keys should remain valid under canonical serialization, and the untouched signed spec should still be reviewable.

Confidence: High for the missing verification and separately reported changed-text helper fixture; no browser flow or broader mutation matrix was executed. -->

---

# Before A Judging Decision



Resolve evidence gaps before interpreting readiness

Confirm the final commit and intended product.
Run the named synthetic follow-up checks in an authorized environment.
Observe a fresh-machine workflow and exported result.
Keep untested claims, proposed scores and clinical claims out of the conclusion.


<!-- Speaker notes:  -->

---
