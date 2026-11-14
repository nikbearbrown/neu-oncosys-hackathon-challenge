# OncoSys Cohort Studio



Professor Bear | Independent Audit

Track 1: cohort-studio
Commit 54aeacb6f6f3
Static source review; no official score


<!-- Speaker notes:  -->

---

# Review Scope



Committed source, not an observed demo

124 text files collected; 188 entries excluded.
Selected implementation paths were inspected.
No submission code, tests, data fetches or sealed inputs were run.
The official freeze commit still needs confirmation.


<!-- Speaker notes:  -->

---

# Step ledgers distinguish rows, samples and patients

Strength | CS-04 | T1-1 | P2

Each applied step records incoming and outgoing row, distinct-sample and distinct-patient counts. The engine identifies growth in rows per sample, records duplicate counts and examples, and the verdict distinguishes unresolved inflation from inflation later resolved by a step or logged fix.

Why it matters: This directly addresses a central Studio failure mode: join multiplicity can increase rows without adding independent samples or patients. The source makes the distinction inspectable instead of presenting one misleading ...
Next check: Join one invented sample to two slide records. Verify rows increase, distinct samples do not, the ledger names the inflating step, and a later exists-style fix retains the intended sample exactly once.

- [Source 1](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/engine.py#L314-L338)
- [Source 2](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/engine.py#L355-L363)
- [Source 3](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/verdict.py#L165-L182)

<!-- Speaker notes: Each applied step records incoming and outgoing row, distinct-sample and distinct-patient counts. The engine identifies growth in rows per sample, records duplicate counts and examples, and the verdict distinguishes unresolved inflation from inflation later resolved by a step or logged fix.

Retain all three count dimensions and the exact join rule. Explain intentional one-to-many data separately from accidental inflation and keep counts before and after any fix visible.

Acceptance: Join one invented sample to two slide records. Verify rows increase, distinct samples do not, the ledger names the inflating step, and a later exists-style fix retains the intended sample exactly once.

Confidence: High for the inspected count and inflation construction; no join fixture was run in this pass. -->

---

# The export path has unique cohort IDs and inspectable operations

Strength | CS-05 | T1-5 | P2

cohort_sample_ids collects IDs into a set and returns them sorted. cohort_frame writes a sample_id column from those IDs. write_all emits the specification, ledger, exclusions, audit trail, sample selections, verdict and reconstruction script alongside cohort_samples.csv. The script serializes most operation arguments with repr.

Why it matters: The artifact set fits the Studio handoff and makes cohort construction more inspectable than a screenshot alone. Unique IDs do not by themselves prove correct inclusion, and the request-docstring issue ...
Next check: For an authorized synthetic specification, compare the app's sorted unique IDs, CSV and reconstructed IDs exactly. Verify the ledger and specification explain each exclusion and that all bundle files share one run identity.

- [Source 1](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/ops.py#L323-L328)
- [Source 2](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L105-L106)
- [Source 3](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L336-L349)
- [Source 4](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L237-L255)

<!-- Speaker notes: cohort_sample_ids collects IDs into a set and returns them sorted. cohort_frame writes a sample_id column from those IDs. write_all emits the specification, ledger, exclusions, audit trail, sample selections, verdict and reconstruction script alongside cohort_samples.csv. The script serializes most operation arguments with repr.

Keep the complete export bundle and bind it to a manifest of input and output hashes. Add exact membership parity checks between the app result and an independently reviewed reconstruction.

Acceptance: For an authorized synthetic specification, compare the app's sorted unique IDs, CSV and reconstructed IDs exactly. Verify the ledger and specification explain each exclusion and that all bundle files share one run identity.

Confidence: High for the export construction; fresh-machine reconstruction and output parity were not executed by this reviewer. -->

---

# Inflation fixes are explicit copied transformations with a log

Strength | CS-06 | T1-2 | P2

suggest_fix chooses exists-style matching for slide/normal joins, sample-level keys for patient-key joins, or a deduplication step. apply_fixes clones the specification and records the old step, row/sample/patient counts, examples and proposed fix. The API retains the first result and list of fixes when it reruns a fixed specification.

Why it matters: This makes the before-versus-after transformation inspectable and preserves evidence of why a cohort changed. Automatic API fixing is not equivalent to human approval, even when the change is logged and ...
Next check: Compare fix=False and fix=True on an inflated synthetic join. Confirm the original specification is unchanged, the first result and exact policy change remain available, and the approved versus preview state is explicit.

- [Source 1](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/engine.py#L392-L403)
- [Source 2](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/engine.py#L406-L424)
- [Source 3](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/api.py#L116-L139)
- [Source 4](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/api.py#L151-L153)

<!-- Speaker notes: suggest_fix chooses exists-style matching for slide/normal joins, sample-level keys for patient-key joins, or a deduplication step. apply_fixes clones the specification and records the old step, row/sample/patient counts, examples and proposed fix. The API retains the first result and list of fixes when it reruns a fixed specification.

Retain copied specifications, first results and fix logs. Show the semantic change and ask for explicit confirmation before representing the fixed cohort as approved for a research use that depends on join meaning.

Acceptance: Compare fix=False and fix=True on an inflated synthetic join. Confirm the original specification is unchanged, the first result and exact policy change remain available, and the approved versus preview state is explicit.

Confidence: High for clone/log and API return structure; researcher acceptance and end-to-end presentation remain untested. -->

---

# An unknown checksum can be described as a matching checksum

Risk | CS-01 | T1-3 | P1

Raw-file status starts verified=None and becomes True or False only when an expected digest exists. available accepts a present file unless verification is explicitly False. The frozen-file verdict looks only for False and otherwise says every raw file used matches sources.csv. A missing expected digest is therefore not distinguished from a verified ...

Why it matters: A hash of current bytes establishes identity of those bytes, not agreement with the organizer's frozen release. The claim can overstate provenance when expected checksum metadata is absent. This does ...
Next check: Use a present synthetic raw file with no expected digest, then a matching digest and a mismatched digest. Only the matching case may claim verification; the unknown case must name the missing reference ...

- [Source 1](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/data.py#L64-L86)
- [Source 2](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/data.py#L89-L93)
- [Source 3](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/verdict.py#L143-L160)

<!-- Speaker notes: Raw-file status starts verified=None and becomes True or False only when an expected digest exists. available accepts a present file unless verification is explicitly False. The frozen-file verdict looks only for False and otherwise says every raw file used matches sources.csv. A missing expected digest is therefore not distinguished from a verified match in that check.

Preserve distinct missing, unverified, mismatched and verified states. Require True for a matching-checksum claim and mark unavailable expected metadata as unknown with a concrete recovery instruction.

Acceptance: Use a present synthetic raw file with no expected digest, then a matching digest and a mismatched digest. Only the matching case may claim verification; the unknown case must name the missing reference metadata.

Confidence: High for the tri-state control flow; the parallel TESTS.md reports a matching helper-level unknown-to-pass reproduction. -->

---

# Request text is inserted into a generated Python docstring

Risk | CS-02 | T1-4 | P1

reproduce_script places spec.request verbatim between triple-quoted Python docstring delimiters. Most operation arguments later use repr formatting, but this leading prose field is not encoded as a Python literal. Quotes and newlines in request text can therefore break script syntax or terminate the docstring and become code in the exported file.

Why it matters: A reproduction artifact should preserve a user's description as data, not reinterpret it as executable syntax. The dangerous transition occurs if someone later runs the generated script; this review did ...
Next check: Generate scripts from ordinary text, multiline text and text containing triple quotes. Parse the generated syntax in an authorized environment and verify the original request remains a literal value with no extra executable ...

- [Source 1](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L154-L171)
- [Source 2](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L237-L255)

<!-- Speaker notes: reproduce_script places spec.request verbatim between triple-quoted Python docstring delimiters. Most operation arguments later use repr formatting, but this leading prose field is not encoded as a Python literal. Quotes and newlines in request text can therefore break script syntax or terminate the docstring and become code in the exported file.

Serialize request text safely as a string literal or external JSON metadata and keep executable code structurally separate. Apply the same rule to every user-controlled value and test the resulting artifact without executing arbitrary text.

Acceptance: Generate scripts from ordinary text, multiline text and text containing triple quotes. Parse the generated syntax in an authorized environment and verify the original request remains a literal value with no extra executable statements.

Confidence: High for literal interpolation; the parallel reviewer reports syntax and statement-boundary probes, which were not rerun here. -->

---

# Reconstruction warns about changed inputs but still writes a cohort

Risk | CS-03 | T1-6 | P2

The generated script compares current file hashes with EXPECTED and prints a warning when they differ, then continues to load and transform the data. It writes cohort_samples.csv and prints the expected count rather than asserting the original membership. This is an intentional-looking permissive path, not a demonstrated numeric failure.

Why it matters: A usable exploratory rerun on new data is different from a faithful reconstruction of the reviewed cohort. Without a distinct mode or failure state, a reader may mistake a warning-bearing ...
Next check: Change one synthetic input after export. Confirm strict reconstruction refuses to certify the old cohort, while any permitted exploratory run has a new identity and cannot silently replace the original reproduction result.

- [Source 1](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L203-L214)
- [Source 2](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L267-L275)

<!-- Speaker notes: The generated script compares current file hashes with EXPECTED and prints a warning when they differ, then continues to load and transform the data. It writes cohort_samples.csv and prints the expected count rather than asserting the original membership. This is an intentional-looking permissive path, not a demonstrated numeric failure.

Decide and document the contract. A strict reproduction mode should stop on hash mismatch and compare membership or an output digest; an exploratory mode can continue but must produce a clearly labeled new run with changed-input provenance.

Acceptance: Change one synthetic input after export. Confirm strict reconstruction refuses to certify the old cohort, while any permitted exploratory run has a new identity and cannot silently replace the original reproduction result.

Confidence: High for the warning-and-continue path; whether strict refusal is required is a product-policy question for judges, not an invented organizer rule. -->

---

# Before A Judging Decision



Resolve evidence gaps before interpreting readiness

Confirm the final commit and intended product.
Run the named synthetic follow-up checks in an authorized environment.
Observe a fresh-machine workflow and exported result.
Keep untested claims, proposed scores and clinical claims out of the conclusion.


<!-- Speaker notes:  -->

---
