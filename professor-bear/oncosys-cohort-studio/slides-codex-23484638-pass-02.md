# OncoSys Cohort Studio - Concise Slides

Revision 2. Earlier artifacts remain unchanged. One finding per slide. Updated 2026-11-14T20:20:41.947618+00:00.

# OncoSys Cohort Studio



Professor Bear - Independent Audit

Track 1: cohort-studio
Commit 54aeacb6f6f3
Static source review; no official score


<!-- Speaker notes:  -->

---

# Review Scope



Pinned source with separately attributed test evidence

The source reviewer did not run submission code.
Read the retained REPORT.md and TESTS.md for parallel runtime observations.
No official score, clinical validity or comparative accuracy rate is asserted.


<!-- Speaker notes:  -->

---

# Step ledgers distinguish rows, samples and patients

Strength - CS-04 - T1-1

Step ledgers separately count rows, distinct samples and patients. They expose join inflation and retain examples of records counted more than once.

Judge follow-up: Join one sample to two slides. Show the counts before and after a meaningful fix.

- [Source 1](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/engine.py#L314-L338)
- [Source 2](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/engine.py#L355-L363)
- [Source 3](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/verdict.py#L165-L182)

<!-- Speaker notes: Each applied step records incoming and outgoing row, distinct-sample and distinct-patient counts. The engine identifies growth in rows per sample, records duplicate counts and examples, and the verdict distinguishes unresolved inflation from inflation later resolved by a step or logged fix.

Retain all three count dimensions and the exact join rule. Explain intentional one-to-many data separately from accidental inflation and keep counts before and after any fix visible.

Acceptance: Join one invented sample to two slide records. Verify rows increase, distinct samples do not, the ledger names the inflating step, and a later exists-style fix retains the intended sample exactly once.

Confidence: High for the inspected count and inflation construction; no join fixture was run in this pass. -->

---

# The export path has unique cohort IDs and inspectable operations

Strength - CS-05 - T1-5

Studio exports sorted unique sample IDs with the specification, ledger, exclusions, selection records and reconstruction script. The bundle makes cohort construction inspectable.

Judge follow-up: Compare exact membership across the app, CSV and reconstruction. Keep the generated-code safety fix separate.

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

Strength - CS-06 - T1-2

Inflation fixes operate on a copied specification and record what changed. The API retains the first result. Automatic fixing still needs a distinct approval state.

Judge follow-up: Compare fixing enabled and disabled. Preserve the original meaning and ask a researcher to approve the change.

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

Risk - CS-01 - T1-3

A raw file without an expected checksum keeps verified=None. The verdict rejects only False and can describe that unknown state as a matching frozen checksum.

Judge follow-up: Test unknown, matching and mismatched digests. Only the matching state should claim verification.

- [Source 1](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/data.py#L64-L86)
- [Source 2](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/data.py#L89-L93)
- [Source 3](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/verdict.py#L143-L160)

<!-- Speaker notes: Raw-file status starts verified=None and becomes True or False only when an expected digest exists. available accepts a present file unless verification is explicitly False. The frozen-file verdict looks only for False and otherwise says every raw file used matches sources.csv. A missing expected digest is therefore not distinguished from a verified match in that check.

Preserve distinct missing, unverified, mismatched and verified states. Require True for a matching-checksum claim and mark unavailable expected metadata as unknown with a concrete recovery instruction.

Acceptance: Use a present synthetic raw file with no expected digest, then a matching digest and a mismatched digest. Only the matching case may claim verification; the unknown case must name the missing reference metadata.

Confidence: High for the tri-state control flow; the parallel TESTS.md reports a matching helper-level unknown-to-pass reproduction. -->

---

# Request text is inserted into a generated Python docstring

Risk - CS-02 - T1-4

The reconstruction generator inserts request text directly into a Python docstring. Triple quotes can break syntax or turn description text into code when the file is later run.

Judge follow-up: Encode request text as data and parse generated scripts containing multiline and quoted requests.

- [Source 1](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L154-L171)
- [Source 2](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L237-L255)

<!-- Speaker notes: reproduce_script places spec.request verbatim between triple-quoted Python docstring delimiters. Most operation arguments later use repr formatting, but this leading prose field is not encoded as a Python literal. Quotes and newlines in request text can therefore break script syntax or terminate the docstring and become code in the exported file.

Serialize request text safely as a string literal or external JSON metadata and keep executable code structurally separate. Apply the same rule to every user-controlled value and test the resulting artifact without executing arbitrary text.

Acceptance: Generate scripts from ordinary text, multiline text and text containing triple quotes. Parse the generated syntax in an authorized environment and verify the original request remains a literal value with no extra executable statements.

Confidence: High for literal interpolation; the parallel reviewer reports syntax and statement-boundary probes, which were not rerun here. -->

---

# Reconstruction warns about changed inputs but still writes a cohort

Open question - CS-03 - T1-6

The reconstruction script warns when input hashes differ and then continues to write a cohort. That behavior needs a clear distinction between strict reproduction and exploration.

Judge follow-up: A strict rerun should reject changed inputs. An exploratory rerun needs a new identity and provenance.

- [Source 1](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L203-L214)
- [Source 2](https://github.com/tammy357/oncosys-cohort-studio/blob/54aeacb6f6f355a1dcaa42d7abf2ce174315ad69/cohort_studio/exports.py#L267-L275)

<!-- Speaker notes: The generated script compares current file hashes with EXPECTED and prints a warning when they differ, then continues to load and transform the data. It writes cohort_samples.csv and prints the expected count rather than asserting the original membership. This is an intentional-looking permissive path, not a demonstrated numeric failure.

Decide and document the contract. A strict reproduction mode should stop on hash mismatch and compare membership or an output digest; an exploratory mode can continue but must produce a clearly labeled new run with changed-input provenance.

Acceptance: Change one synthetic input after export. Confirm strict reconstruction refuses to certify the old cohort, while any permitted exploratory run has a new identity and cannot silently replace the original reproduction result.

Confidence: High for the warning-and-continue path; whether strict refusal is required is a product-policy question for judges, not an invented organizer rule. -->

---

# Judging Limits



The official rubric and human judges determine the result.

Confirm the final submission commit.
Separate source conclusions from observed runs and policy recommendations.
Different test counts do not establish a cross-team ranking.


<!-- Speaker notes:  -->

---
