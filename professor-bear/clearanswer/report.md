# ClearAnswer: initial independent review

Reviewed commit: `7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8`. Track 2, Evidence Navigator / Research Claim Auditor. Preliminary source and narrow runtime review; not an official score or verified final submission receipt.

## Summary
ClearAnswer is a substantive research-claim auditor with a clear reviewer workflow: extract sentences, use deterministic data tools, inspect evidence, review findings, and export JSON or HTML. The semantic layer explicitly documents questions the data cannot answer. These are good foundations. However, numeric tolerance and export transformations can overstate support or confidence. Fix these before trusting the exported verdicts.

## Verified strengths
- Separate agent, semantic, and data layers make behavior inspectable and allow deterministic computations rather than free-form numeric answers.
- A bounded verification loop returns insufficient evidence when it does not finalize.
- Evidence records, release file hashes, alternative interpretations, impact explanations and reviewer overrides are represented.
- The UI and CLI are documented, with standalone HTML and shared-schema JSON exports. These paths were inspected but not end-to-end tested.

## F1: compound-claim tolerance can erase a contradiction (high)
**Reproduced narrow runtime behavior:** `check_tolerance('50.1% are LumA and 90% are Basal', '50% are LumA; 10% are Basal')` returns a note saying to treat the claim as supported. It compares only the first number, although the second number is materially wrong. `_build_result` changes the entire contradicted verdict to supported when this note exists.

Evidence: [core/tolerance.py](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/tolerance.py#L19-L91), [agents/verifier.py](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L403-L456).

Fix: represent each subclaim explicitly with matched unit, denominator and computed value; apply tolerance separately and preserve worst-subclaim status. Do not parse the first number from free prose. Add cases where the first quantity is rounded correctly but later quantities, units or populations are wrong.

## F2: export overwrites uncertainty with high confidence (high)
**Reproduced narrow runtime behavior:** an insufficient-evidence finding with low confidence becomes high confidence in `_prepare_for_submission`, even with no evidence. This is independent of reviewer approval. The function inserts a claim pointer when evidence is empty. A claim pointer establishes what was asserted, not that it is true.

Evidence: [app.py](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/app.py#L409-L459).

Fix: retain original confidence and evidence strength. Expose extraction, computation, semantic-match and reviewer uncertainty separately. Schema validity should not be achieved by upgrading epistemic certainty.

## F3: unsupported model conclusions can satisfy the evidence shape (high; source observation)
A supported result with no evidence receives `model_asserted_match`. The model may also name files that no successful tool call touched; these become evidence pointers. Therefore the guarantee that every verdict is backed by deterministic computation is not enforced at finalization.

Evidence: [agents/verifier.py](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L444-L525).

Fix: require successful relevant computation evidence for supported numeric claims, validate declared files against actual trace, and return insufficient evidence when that contract is unmet. Distinguish model assertions from checked evidence.

## F4: review overrides need stronger meaning and provenance (medium-high)
**Reproduced narrow runtime behavior:** an override with just a finding ID, `decision=override`, and `verdict=supported` changes an insufficient finding to supported, clears human-review status and assigns high confidence. No reason or identity is required by this function. The original tool verdict is preserved, which is useful, but human preference is not new data evidence.

Evidence: [app.py](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/app.py#L432-L458).

Fix: require identity, reason, timestamp and supporting evidence for consequential overrides. Preserve machine verdict separately from reviewer disposition and preserve an append-only history. Label identities self-attested unless authenticated.

## F5: input guard is advisory, not a transmission barrier (medium-high; source observation)
The orchestrator records flagged phrases but continues to the extractor with the report. Its comment explicitly says to keep processing. Consequently regex recognition of identifying content does not prevent sending the report to the external model. This review found no actual disclosure.

Evidence: [agents/orchestrator.py](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/orchestrator.py#L44-L66), [agents/base.py](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/base.py#L38-L68).

Fix: show a pre-submission disclosure and stop or redact prohibited content before external calls. Treat report instructions as untrusted data; regex matching is not a comprehensive injection defense.

## F6: frozen schema and manifest assumptions need changed-release validation (medium; source observation)
The semantic pre-check is a static schema and can short-circuit without reading the current file. Loader manifest lookup searches ancestors and can locate a manifest separate from the chosen release; manifest-derived counts therefore need explicit release binding. Checksums include layer files, not manifests.

Evidence: [core/semantic.py](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/semantic.py#L340-L366), [core/loader.py](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/loader.py#L47-L75), [core/loader.py](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/loader.py#L206-L216).

Fix: bind schemas and manifests to the chosen release, record their hashes, and reconcile manifest counts to available files. Demonstrate behavior under a changed question or release rather than relying only on fixed reference counts.

## Other improvements
Dependencies are unpinned. README demo video remains a placeholder. The Flask app binds all interfaces with debug enabled; keep this development-only and do not expose it as production. Role-specific comprehension, keyboard accessibility and unattended judge task completion still need direct testing.

## Track 2 rubric discussion (no invented total)
- Decision usefulness (20): explicit claim verdict and next-step fields are useful; false-support and confidence problems are material.
- Understanding evidence (20): traceability structure is good; model-declared evidence must be distinguished from executed evidence.
- Role fit (15): reviewer persona clear; multiple-role behavior not independently verified.
- Safety/uncertainty (15): explicit cannot-answer categories and human review are positive; export and guard weaknesses need fixes.
- Usability/accessibility (15): not tested live in this pass.
- Working setup (10): documented CLI/UI; hosted/API pipeline not executed in this pass.
- Communication (5): clear scope and architecture; demo link incomplete.

## Tests actually performed
Four synthetic pure-function probes: two tolerance cases, one low-confidence export case, one reasonless override case. The exact submitted tolerance module was imported after inspection; the export function was extracted unchanged with Python AST and executed with only its `copy` dependency. No app startup, API key use, network call, patient data or sealed material was involved. These probes establish narrow function behavior, not full end-to-end exploitability.

## Not performed
The submitted ground-truth suite requires TCGA files and dependencies not provisioned in this isolated checkout. No submitted suite pass is claimed. No LLM audit, browser, official-envelope, accessibility or clinical validation was performed. This is an initial review of the observed commit, not necessarily the competition freeze commit.
