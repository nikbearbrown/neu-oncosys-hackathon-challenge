# Busy Beavers Cohort Firewall - Concise Slides

Revision 2. Earlier artifacts remain unchanged. One finding per slide. Updated 2026-11-14T20:20:41.938308+00:00.

# Busy Beavers Cohort Firewall



Professor Bear - Independent Audit

Track 1: cohort-control-tower
Commit bfb369f231bf
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

# Invalid schema output is withheld from the successful findings route

Strength - BB-04 - T1-4

The comparison service withholds schema-invalid findings from its successful download route. Validation errors produce a failed run and a diagnostic file.

Judge follow-up: Keep a valid-output positive control. Confirm served bytes match the bytes validated.

- [Source 1](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/backend/services/comparison.py#L100-L123)
- [Source 2](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/backend/services/comparison.py#L139-L144)

<!-- Speaker notes: The comparison service packages the detector output, calls write_document and checks returned validation errors. On errors it renames the result to findings.invalid.json, marks the run failed and returns before findings_available is set. findings_path only exposes a completed run with an available file.

Retain this failed-versus-completed distinction and keep the rejected file available only as a clearly marked diagnostic. Bind validation to the same bytes served to the next team.

Acceptance: Supply a synthetic detector response that fails the organizer schema. Verify the run is failed and the successful findings endpoint does not serve it; then repeat with a valid positive control.

Confidence: High for the service's control flow; the API and validator were not run. -->

---

# Proposed repairs retain explicit limitations and analysis impact reasons

Strength - BB-05 - T1-6

Findings include source pointers, limitations and analysis-impact reasons. Repairs remain proposals in the detector path, with human review explicitly requested.

Judge follow-up: Keep that distinction in every derivative export and record the reviewer decision.

- [Source 1](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L76-L89)
- [Source 2](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L240-L268)

<!-- Speaker notes: Event construction includes source pointers and per-kind limitations, then computes analysis-specific impact reasons. The exported finding retains those reasons and a human-review flag, and repair justification says the action is a proposal that does not modify a release file in this path.

Keep the event-level evidence and uncertainty wording. Apply the same proposal-versus-approved distinction to every downstream derivative export and avoid treating restoration of a baseline number as proof of factual truth.

Acceptance: Follow one synthetic swap from source pointers through affected and unaffected analyses to a reviewer decision. Confirm original input files remain unchanged and the derivative, if any, is explicitly labeled with approval state.

Confidence: High for the inspected detector/export path; derivative export and reviewer UI behavior remain untested. -->

---

# Impact mapping uses the actual analysis input slice

Strength - BB-06 - T1-2

Impact mapping compares the actual A1 and A2 input slices. Membership, target measurements and labels receive different treatment from unrelated changes.

Judge follow-up: Change an irrelevant row, then a target value and subtype label. Explain the impact decisions.

- [Source 1](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/impact.py#L7-L20)
- [Source 2](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/impact.py#L23-L34)

<!-- Speaker notes: A1's slice combines primary-tumor protein values with ER labels, while A2's slice uses primary-tumor subtype labels. The impact function compares sample membership and row values in those slices rather than treating every changed file as equally relevant.

Preserve the explicit dependency slices, fix their equality screening and record which slice policy was used in each run. Keep new analyses from silently inheriting A1/A2 assumptions.

Acceptance: Alter an unrelated protein row, then ERALPHA for an eligible sample, and then a subtype label. Verify the impact decisions differ for defensible reasons, with baseline and candidate sample sets visible.

Confidence: High for source structure; numerical parity with organizer reference functions remains untested. -->

---

# Duplicate IDs are removed before the duplicate-ID detector

Risk - BB-01 - T1-1

The detector removes repeated sample IDs before reaching its duplicate-ID check. The later check cannot recover the duplicate indices already discarded.

Judge follow-up: Report identical and conflicting repeated IDs before selecting or deduplicating records.

- [Source 1](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/diff.py#L8-L20)
- [Source 2](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/fingerprint.py#L4-L8)

<!-- Speaker notes: diff_file removes duplicate indices from both input frames before hashing. profile_hashes then assigns the already-deduplicated frame index to its output. The later b.index.duplicated check therefore cannot detect the duplicate indices discarded at the beginning of the function. This is a source-level ordering defect; no duplicate-ID fixture was executed here.

Inspect and report duplicate identifiers before deduplication. Keep conflicting rows as evidence and prevent ambiguous records from contributing to an approved analytical slice until a documented selection policy or reviewer decision resolves them.

Acceptance: Use a synthetic table with one repeated ID and conflicting values, plus an identical-duplicate case and a unique-ID control. Confirm the repeated ID is reported, both records remain inspectable and an arbitrary first row is not silently accepted.

Confidence: High for the inspected ordering and index propagation; end-to-end runtime behavior remains untested. -->

---

# Rounded-hash equality bypasses the finer tolerance check

Risk - BB-02 - T1-2

Four-decimal hash equality can bypass a finer numerical tolerance check. Values that quantize alike never reach that check, including in analysis-impact slices.

Judge follow-up: Compare values that round alike but exceed the stated tolerance. Keep a within-tolerance control.

- [Source 1](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/fingerprint.py#L4-L8)
- [Source 2](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/fingerprint.py#L11-L24)
- [Source 3](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/diff.py#L18-L20)
- [Source 4](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/impact.py#L26-L34)

<!-- Speaker notes: Profile hashes are computed after rounding every column to four decimals. The changed-row predicate calls rows_close only when hashes differ, although rows_close uses rtol=1e-6 and atol=1e-9. Distinct values that round to the same four-decimal value never reach that tolerance check. The analysis-slice impact calculation repeats this pattern.

Use an exact or lossless canonical hash for screening, then apply the explicit numeric tolerance to candidate differences. Alternatively define one consistent, field-specific quantization policy and disclose the information it intentionally discards.

Acceptance: Compare authorized synthetic values 1.00001 and 1.00004. They round alike at four decimals but differ by more than 1e-6 relative tolerance. Check both detection and analysis impact, and retain a genuinely within-tolerance noise control.

Confidence: High for the predicate mismatch; the proposed fixture has not been run. -->

---

# A display cap also truncates the actionable repair scope

Risk - BB-03 - T1-3

The 500-item preview cap also truncates machine-consumed repair targets. A summary can describe more affected records than the exported repair addresses.

Judge follow-up: Separate bounded evidence previews from a complete, hash-bound target set.

- [Source 1](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L25-L29)
- [Source 2](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L257-L268)

<!-- Speaker notes: The exported finding evidence is sliced to MAX_EVIDENCE and the repair's targets are independently sliced to the same limit. MAX_EVIDENCE is 500. There is no complete target-set reference or truncation marker in this construction, while summary text can describe the full event.

Separate a bounded evidence preview from the authoritative complete target set. Export total counts, explicit truncation status and a hash-bound complete target artifact, or refuse to represent a partial repair as complete.

Acceptance: Create a synthetic 501-target event and inspect exported evidence, repair targets and summary counts. Either all intended targets must be addressable or the operation must be visibly partial and non-approvable as a complete repair.

Confidence: High for the explicit slices; downstream export behavior has not been executed. -->

---

# Judging Limits



The official rubric and human judges determine the result.

Confirm the final submission commit.
Separate source conclusions from observed runs and policy recommendations.
Different test counts do not establish a cross-team ranking.


<!-- Speaker notes:  -->

---
