# Busy Beavers Cohort Firewall



Professor Bear | Independent Audit

Track 1: cohort-control-tower
Commit bfb369f231bf
Static source review; no official score


<!-- Speaker notes:  -->

---

# Review Scope



Committed source, not an observed demo

85 text files collected; 84 entries excluded.
Selected implementation paths were inspected.
No submission code, tests, data fetches or sealed inputs were run.
The official freeze commit still needs confirmation.


<!-- Speaker notes:  -->

---

# Invalid schema output is withheld from the successful findings route

Strength | BB-04 | T1-4 | P2

The comparison service packages the detector output, calls write_document and checks returned validation errors. On errors it renames the result to findings.invalid.json, marks the run failed and returns before findings_available is set. findings_path only exposes a completed run with an available file.

Why it matters: This prevents a format-invalid export from silently taking the successful handoff route. Schema validation still does not prove detector correctness, but it is a useful independent packaging boundary.
Next check: Supply a synthetic detector response that fails the organizer schema. Verify the run is failed and the successful findings endpoint does not serve it; then repeat with a valid positive control.

- [Source 1](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/backend/services/comparison.py#L100-L123)
- [Source 2](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/backend/services/comparison.py#L139-L144)

<!-- Speaker notes: The comparison service packages the detector output, calls write_document and checks returned validation errors. On errors it renames the result to findings.invalid.json, marks the run failed and returns before findings_available is set. findings_path only exposes a completed run with an available file.

Retain this failed-versus-completed distinction and keep the rejected file available only as a clearly marked diagnostic. Bind validation to the same bytes served to the next team.

Acceptance: Supply a synthetic detector response that fails the organizer schema. Verify the run is failed and the successful findings endpoint does not serve it; then repeat with a valid positive control.

Confidence: High for the service's control flow; the API and validator were not run. -->

---

# Proposed repairs retain explicit limitations and analysis impact reasons

Strength | BB-05 | T1-6 | P2

Event construction includes source pointers and per-kind limitations, then computes analysis-specific impact reasons. The exported finding retains those reasons and a human-review flag, and repair justification says the action is a proposal that does not modify a release file in this path.

Why it matters: This gives a reviewer an interpretable handoff and preserves the important distinction between detecting a difference and proving which release is correct.
Next check: Follow one synthetic swap from source pointers through affected and unaffected analyses to a reviewer decision. Confirm original input files remain unchanged and the derivative, if any, is explicitly labeled with approval state.

- [Source 1](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L76-L89)
- [Source 2](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L240-L268)

<!-- Speaker notes: Event construction includes source pointers and per-kind limitations, then computes analysis-specific impact reasons. The exported finding retains those reasons and a human-review flag, and repair justification says the action is a proposal that does not modify a release file in this path.

Keep the event-level evidence and uncertainty wording. Apply the same proposal-versus-approved distinction to every downstream derivative export and avoid treating restoration of a baseline number as proof of factual truth.

Acceptance: Follow one synthetic swap from source pointers through affected and unaffected analyses to a reviewer decision. Confirm original input files remain unchanged and the derivative, if any, is explicitly labeled with approval state.

Confidence: High for the inspected detector/export path; derivative export and reviewer UI behavior remain untested. -->

---

# Impact mapping uses the actual analysis input slice

Strength | BB-06 | T1-2 | P2

A1's slice combines primary-tumor protein values with ER labels, while A2's slice uses primary-tumor subtype labels. The impact function compares sample membership and row values in those slices rather than treating every changed file as equally relevant.

Why it matters: This directly supports the product's affected-versus-unaffected analysis workflow. It is a useful design even though the rounded-hash screening concern above limits the implementation's guarantees.
Next check: Alter an unrelated protein row, then ERALPHA for an eligible sample, and then a subtype label. Verify the impact decisions differ for defensible reasons, with baseline and candidate sample sets visible.

- [Source 1](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/impact.py#L7-L20)
- [Source 2](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/impact.py#L23-L34)

<!-- Speaker notes: A1's slice combines primary-tumor protein values with ER labels, while A2's slice uses primary-tumor subtype labels. The impact function compares sample membership and row values in those slices rather than treating every changed file as equally relevant.

Preserve the explicit dependency slices, fix their equality screening and record which slice policy was used in each run. Keep new analyses from silently inheriting A1/A2 assumptions.

Acceptance: Alter an unrelated protein row, then ERALPHA for an eligible sample, and then a subtype label. Verify the impact decisions differ for defensible reasons, with baseline and candidate sample sets visible.

Confidence: High for source structure; numerical parity with organizer reference functions remains untested. -->

---

# Duplicate IDs are removed before the duplicate-ID detector

Risk | BB-01 | T1-1 | P1

diff_file removes duplicate indices from both input frames before hashing. profile_hashes then assigns the already-deduplicated frame index to its output. The later b.index.duplicated check therefore cannot detect the duplicate indices discarded at the beginning of the function. This is a source-level ordering defect; no duplicate-ID fixture was executed here.

Why it matters: Ambiguous repeated records can be silently reduced to the first record instead of being reported for human review. This can hide the exact join or identity problem the workflow is ...
Next check: Use a synthetic table with one repeated ID and conflicting values, plus an identical-duplicate case and a unique-ID control. Confirm the repeated ID is reported, both records remain inspectable and an arbitrary first ...

- [Source 1](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/diff.py#L8-L20)
- [Source 2](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/cfw/fingerprint.py#L4-L8)

<!-- Speaker notes: diff_file removes duplicate indices from both input frames before hashing. profile_hashes then assigns the already-deduplicated frame index to its output. The later b.index.duplicated check therefore cannot detect the duplicate indices discarded at the beginning of the function. This is a source-level ordering defect; no duplicate-ID fixture was executed here.

Inspect and report duplicate identifiers before deduplication. Keep conflicting rows as evidence and prevent ambiguous records from contributing to an approved analytical slice until a documented selection policy or reviewer decision resolves them.

Acceptance: Use a synthetic table with one repeated ID and conflicting values, plus an identical-duplicate case and a unique-ID control. Confirm the repeated ID is reported, both records remain inspectable and an arbitrary first row is not silently accepted.

Confidence: High for the inspected ordering and index propagation; end-to-end runtime behavior remains untested. -->

---

# Rounded-hash equality bypasses the finer tolerance check

Risk | BB-02 | T1-2 | P1

Profile hashes are computed after rounding every column to four decimals. The changed-row predicate calls rows_close only when hashes differ, although rows_close uses rtol=1e-6 and atol=1e-9. Distinct values that round to the same four-decimal value never reach that tolerance check. The analysis-slice impact calculation repeats this pattern.

Why it matters: The implementation can call a profile or analysis slice unchanged even when its values differ beyond the finer stated tolerance. The scientific significance depends on the field and question; this ...
Next check: Compare authorized synthetic values 1.00001 and 1.00004. They round alike at four decimals but differ by more than 1e-6 relative tolerance. Check both detection and analysis impact, and retain a genuinely within-tolerance noise ...

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

Risk | BB-03 | T1-3 | P1

The exported finding evidence is sliced to MAX_EVIDENCE and the repair's targets are independently sliced to the same limit. MAX_EVIDENCE is 500. There is no complete target-set reference or truncation marker in this construction, while summary text can describe the full event.

Why it matters: A downstream consumer cannot infer that an apparently complete repair covers only the first 500 records. The prior report already identified this concern; this pass corroborates the exact source construction ...
Next check: Create a synthetic 501-target event and inspect exported evidence, repair targets and summary counts. Either all intended targets must be addressable or the operation must be visibly partial and non-approvable as a complete ...

- [Source 1](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L25-L29)
- [Source 2](https://github.com/GiorgiKarazanashvili/BusyBeavers/blob/bfb369f231bf97a1d3aa21abade3ba4b1406a355/detection/engine.py#L257-L268)

<!-- Speaker notes: The exported finding evidence is sliced to MAX_EVIDENCE and the repair's targets are independently sliced to the same limit. MAX_EVIDENCE is 500. There is no complete target-set reference or truncation marker in this construction, while summary text can describe the full event.

Separate a bounded evidence preview from the authoritative complete target set. Export total counts, explicit truncation status and a hash-bound complete target artifact, or refuse to represent a partial repair as complete.

Acceptance: Create a synthetic 501-target event and inspect exported evidence, repair targets and summary counts. Either all intended targets must be addressable or the operation must be visibly partial and non-approvable as a complete repair.

Confidence: High for the explicit slices; downstream export behavior has not been executed. -->

---

# Before A Judging Decision



Resolve evidence gaps before interpreting readiness

Confirm the final commit and intended product.
Run the named synthetic follow-up checks in an authorized environment.
Observe a fresh-machine workflow and exported result.
Keep untested claims, proposed scores and clinical claims out of the conclusion.


<!-- Speaker notes:  -->

---
