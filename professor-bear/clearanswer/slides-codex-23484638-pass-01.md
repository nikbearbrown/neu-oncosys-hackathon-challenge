# ClearAnswer Research Claim Auditor



Professor Bear | Independent Audit

Track 2: research-claim-auditor
Commit 7ede1f8fb84b
Static source review; no official score


<!-- Speaker notes:  -->

---

# Review Scope



Pinned source with explicit limits

31 text files collected; 20 entries excluded.
Selected implementation paths were inspected.
No submission code, tests, data fetches or sealed inputs were run.
The official freeze commit still needs confirmation.


<!-- Speaker notes:  -->

---

# Queries use a bounded operation vocabulary with source metadata

Strength | CA-06 | T2-2 | P2

The model chooses from bounded query operations. Pandas performs the calculation and returns source and count metadata.

Keep exact queries and denominators visible.
Connect these receipts to the final verdict.

- [Source 1](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/tools/data_tool.py#L69-L94)
- [Source 2](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/tools/data_tool.py#L98-L125)
- [Source 3](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/tools/data_tool.py#L206-L218)
- [Source 4](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/tools/data_tool.py#L248-L264)

<!-- Speaker notes: DataTool exposes enumerated layers and operations instead of asking the model to execute arbitrary Python. It validates known layers, dispatches the selected operation, reports errors explicitly, and attaches source_file and query_description. Value counts include total_counted and row_count, and group comparisons report measured sample sizes. These are useful ingredients for checking denominators and following the calculation rather than trusting prose alone. Their presence does not enforce the finalization boundary discussed in CA-01.

Retain this separation and expose the exact query/result receipt per claim. Extend the same metadata to manifest lookups and require receipt relevance before assigning a supported verdict. Test semantic field selection independently of arithmetic correctness.

Acceptance: With invented data, trace count, distribution and grouped comparison from requested filters through row_count/total_counted to the displayed answer. Unknown columns/layers must remain errors rather than guessed values. Confirm that each final claim points to the computation that actually supports it.

Confidence: High for the operation vocabulary and response fields; no numerical query was executed. -->

---

# The interface preserves the tool verdict beside a human override

Strength | CA-07 | T2-3 | P2

Source-text matching and side-by-side verdicts help reviewers distinguish the report, the tool and their own override.

Substring matching does not establish extraction completeness.
Preserve both verdicts with a validated decision record.

- [Source 1](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/extractor.py#L92-L102)
- [Source 2](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/extractor.py#L141-L151)
- [Source 3](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/templates/index.html#L1718-L1738)
- [Source 4](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/app.py#L442-L453)

<!-- Speaker notes: The extractor filters candidate claims to normalized substrings actually present in the report, reducing unsupported paraphrase pointers. The UI stores per-finding review state and shows the original and replacement verdicts side by side. The export helper also retains tool_verdict when a reviewer touches a finding. This supports a summary-to-detail review workflow grounded in the report's words, although normalized substring matching does not establish complete sentence extraction or recall, and the review record still needs CA-05's validation.

Preserve the original text and both verdicts. Add stable sentence/page offsets, explicit extraction omissions and validated decision metadata. Keep the same underlying evidence across summary and detailed views rather than generating independent narratives for each audience.

Acceptance: Use a short invented report with duplicate sentences, wrapped lines and a compound sentence. Verify each retained finding maps to its source span and compare accept/override displays with both export formats. Measure omitted/duplicated claims separately; a substring check alone does not establish complete coverage.

Confidence: High for the inspected source-linking and verdict-preservation paths; no usability, extraction-recall or browser test was performed. -->

---

# Unsupported topics and incomplete verification have explicit evidence-gap paths

Strength | CA-08 | T2-4 | P2

Unsupported topics and exhausted verification produce explicit insufficient-evidence results with reasons.

These are useful limits to retain.
Ensure export keeps the original uncertainty and review obligation.

- [Source 1](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L239-L265)
- [Source 2](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L348-L373)
- [Source 3](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L377-L405)
- [Source 4](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/guard.py#L99-L113)

<!-- Speaker notes: The verifier short-circuits topics matched by its semantic cannot-answer layer to insufficient_evidence with a reason and labelled schema evidence. If the model never finalizes within the bounded loop, it returns low-confidence insufficient evidence with partial query pointers rather than manufacturing a numerical answer. The post-check marks low-confidence and sparse-evidence results for human review. These controls are explicit source behavior, but the topic dictionary is a static scope model and the export policy must preserve the resulting uncertainty.

Retain the fail-incomplete paths, label schema-only evidence accurately and test static topic assumptions against authorized release schemas. Do not equate a regex match with a full clinical scope assessment. Preserve original confidence and review flags as in CA-02 and CA-05.

Acceptance: Use authorized invented unsupported-topic claims, a no-finalization mock, failed-query mocks and a normal successful calculation. Verify different reasons remain visible through UI, JSON and HTML, with no unsupported clinical conclusion and no claim that file rows were scanned when only schema metadata was used.

Confidence: High for the explicit fallback branches; no model response or clinical scenario was evaluated. -->

---

# A supported verdict does not require a successful computation

Risk | CA-01 | T2-2 | P1

The verifier accepts a supported finalization without requiring a successful relevant query. A model-asserted marker can fill the evidence list.

Sparse evidence still triggers a human-review flag.
Require a claim-bound calculation receipt before supported.

- [Source 1](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L301-L321)
- [Source 2](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L455-L467)
- [Source 3](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L519-L525)
- [Source 4](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/evidence.py#L86-L94)
- [Source 5](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/guard.py#L107-L113)

<!-- Speaker notes: The verifier accepts finalize_verdict as soon as the model supplies it, without first requiring successful data or manifest queries. _build_result then permits supported with no evidence and creates an analysis pointer named model_asserted_match. Model-declared evidence filenames are also accepted even when no successful tool touched them. The ClaimResult contract only requires a nonempty evidence list, not proof of a relevant computation. A later guard marks sparse evidence for human review, which is useful, but does not change the supported verdict. Thus the source does not enforce the stated guarantee that every supported numerical result is backed by a deterministic calculation.

Require a successful, claim-relevant computation receipt before supported or contradicted. Bind tool arguments, resolved inputs, denominator and returned values to the claim and validate the final verdict against that receipt. Keep schema-only refusals as a separately labelled insufficient-evidence path. Model-declared but unqueried files should remain proposed sources, not executed evidence.

Acceptance: In an authorized follow-up using mock model responses and invented tool results, finalize supported before any query, after an errored query and after an unrelated successful query. All must remain unverified/Insufficient Evidence or explicitly awaiting review. A relevant successful numerical query is the positive control. Inspect the exported evidence type, not only its nonempty length.

Confidence: High for the inspected branch ordering and evidence construction; no model call or mocked submission execution occurred in this pass. -->

---

# Export replaces every confidence value with high

Risk | CA-02 | T2-4 | P1

Export sets every finding to high confidence, replacing the confidence retained by the internal result.

This also affects incomplete or unqueried paths.
Preserve uncertainty and its basis in both JSON and HTML.

- [Source 1](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/output.py#L106-L120)
- [Source 2](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/app.py#L409-L425)
- [Source 3](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/app.py#L438-L459)
- [Source 4](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L348-L373)
- [Source 5](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/app.py#L263-L273)

<!-- Speaker notes: The internal finding conversion retains each ClaimResult confidence. The web export conversion then unconditionally sets every finding's confidence to high, including low-confidence budget-exhaustion results or model-asserted matches. The code comment attributes this policy to deterministic pandas computation, but CA-01 shows that not every accepted verdict requires such a computation. The same conversion feeds JSON and standalone HTML exports. A high confidence in a well-established inability to answer can be legitimate; the problem is replacing the original confidence without inspecting why it was low.

Preserve tool confidence and its stated basis through export. If confidence in execution is a separate concept, expose it under a distinct field and keep evidence/interpretation uncertainty unchanged. Do not let format preparation increase epistemic confidence by default. Preserve enough provenance to explain any deliberate human reassessment.

Acceptance: Compare stored and exported findings for low/medium/high confidence, budget exhaustion, static cannot-answer, successful computation and unqueried supported cases. Confidence must remain faithful to its basis; JSON and HTML must agree. A reviewer override should retain both tool and reviewer confidence rather than rewriting history.

Confidence: High for the unconditional assignment and both export callers; no endpoint was exercised. -->

---

# The tolerance shortcut checks only the first number

Risk | CA-03 | T2-1 | P1

Tolerance compares the first number in each string, then can upgrade the whole sentence from contradicted to supported.

A close total does not validate a different share in the same sentence.
Match each numeric subclaim to its measure and denominator.

- [Source 1](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/tolerance.py#L21-L34)
- [Source 2](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/tolerance.py#L62-L90)
- [Source 3](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L431-L440)
- [Source 4](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L49-L64)

<!-- Speaker notes: check_tolerance extracts the first number from the entire claim and the first number from correct_value, determines percentage/approximation flags from the whole strings, and returns a tolerance note when that pair is close. _build_result uses any such note to replace a contradicted verdict with supported and severity none. This does not align values with the same measure, unit or denominator and does not verify the remaining subclaims. It conflicts with the verifier prompt's own worst-part-wins rule for compound sentences. The source permits a close first pair to mask a different contradicted part; no live erroneous audit was observed here.

Represent numeric subclaims structurally, with measure, value, unit, population, denominator and a matching computed result. Apply tolerance to each matched pair and retain contradicted if any material subclaim fails. If matching is ambiguous, request review instead of upgrading the sentence. Keep exact counts and percentage-point/relative conventions distinct.

Acceptance: Use invented compound claims where an approximate first total is close but a later share is wrong, where a leading year is unrelated, and where counts and percentages differ in units. A genuine single-percentage rounding control may pass. Reordering sentence clauses must not change the verdict when the asserted facts are the same.

Confidence: High for first-number extraction and unconditional whole-verdict promotion; actual extraction/model behavior remains untested. -->

---

# Manifest-based answers omit their manifests from file fingerprints

Risk | CA-04 | T2-2 | P1

Manifest lookups determine cohort counts, but the exported checksum list includes only the clinical and molecular layer files.

External shared manifests need content identity too.
Record every consumed manifest and its actual query.

- [Source 1](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/tools/manifest_tool.py#L47-L77)
- [Source 2](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/loader.py#L56-L72)
- [Source 3](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/loader.py#L206-L213)
- [Source 4](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/output.py#L64-L75)
- [Source 5](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L491-L504)

<!-- Speaker notes: ManifestTool computes cohort counts, layer availability and overlap from sample_manifest.csv. TCGARelease can locate manifests outside the selected release directory. However, file_checksums iterates only LAYER_FILES, omitting sample_manifest.csv and slide_manifest.csv, and build_audit_json exports only that checksum mapping. ManifestTool results also omit a source_file field, while the verifier's automatic file-evidence path expects one. The selected manifest can therefore materially determine an answer without receiving the same content-bound provenance as molecular/clinical layer files.

Track every actually consumed file, including manifests, with its resolved path, role and content hash. Have manifest tools return explicit source and query metadata just as data_query does. Distinguish release-specific measurements from shared baseline metadata and verify those identities on rerun.

Acceptance: Use two invented manifests with identical layer files but different cohort membership or availability flags. The answer's provenance must differ, name the manifest and reproduce the correct denominator. Keep a same-manifest positive control and a missing-manifest explicit error.

Confidence: High for omitted files and tool metadata in the complete inspected functions; no manifest or raw dataset was opened. -->

---

# Malformed review objects can clear the review requirement

Risk | CA-05 | T2-4 | P1

Any matching review object can clear needs_human_review. Decision and replacement-verdict validation are missing at this boundary.

The original tool verdict remains preserved.
Reject malformed decisions before changing review state.

- [Source 1](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/app.py#L432-L458)
- [Source 2](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/templates/index.html#L1808-L1811)
- [Source 3](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/templates/index.html#L2075-L2086)
- [Source 4](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/app.py#L209-L221)

<!-- Speaker notes: The export helper indexes any dictionary containing a finding_id. Any matching nonempty object is treated as a touched review: decision defaults to accept, arbitrary decision strings are retained, a replacement verdict is applied when supplied, and needs_human_review is set false. There is no decision-enum, allowed-verdict or required-reason validation before this state change. The ordinary UI also forwards an override reason even when blank and omits the browser timestamp from the export payload. The original tool verdict is retained, which is a useful control. This source finding is about review-state validation and record completeness, not demonstrated remote exploitation or a requirement for enterprise authentication.

Validate the review payload before modifying findings: known finding IDs, explicit supported decisions, allowed replacement verdicts and an appropriate recorded reason for overrides. Preserve the original verdict and record actor/role as self-attested if this is a local prototype, with time and evidence identity. Invalid payloads should leave the review state unchanged. Do not impose a login service merely to repair these local semantics.

Acceptance: Submit a finding-id-only object, an unknown decision, a blank-reason override, an invalid replacement verdict and a valid accept/override pair using invented audits. Invalid records must not clear needs_human_review. Verify both tool and final verdicts remain visible and that JSON and HTML export the same complete decision record.

Confidence: High for the export helper and browser payload construction; API/UI behavior was not run. -->

---

# Before A Judging Decision



Resolve evidence gaps before interpreting readiness

Confirm the final commit and intended product.
Run the named synthetic follow-up checks in an authorized environment.
Observe a fresh-machine workflow and exported result.
Keep untested claims, proposed scores and clinical claims out of the conclusion.


<!-- Speaker notes:  -->

---
