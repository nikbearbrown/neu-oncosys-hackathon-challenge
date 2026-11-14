# Source index, provenance and interpretation

Captured for this repository on 2026-11-14. These are supplied source snapshots,
not a claim that the event site has been rechecked or that every reference was
independently verified. [manifest.json](manifest.json) records sizes, hashes,
redactions and transcription status.

| File | Origin and treatment |
|---|---|
| [Event snapshot](event-2026-11-14.txt) | Library attachment `Pasted text(20261114-170927).txt`, 15,411 original bytes. Entire text retained except the recording passcode. |
| [Medical/image 72-rule rulebook](medical-quality-72-rules.md) | Library attachment `Pasted text(20261114-170939).txt`, 34,419 bytes, preserved byte-for-byte. Includes original examples and reference lineage. |
| [Medical/image 16-section checklist](medical-quality-16-sections.md) | Separate user-pasted checklist. Full prose transcribed with normalized Markdown tables and math; not a byte-verified attachment. |
| [Dashboard 100-rule guideline](dashboard-100-rules.txt) | User's local `figma-data-visualization/references/sources/dashboard-rules-original.txt`, 30,190 bytes, preserved byte-for-byte. Matches the supplied A–N/100-rule text with numbered rules and source-name markers. |

The event recording credential is retained only in the original local attachment
outside this Git repository, at `/tmp/neu-hackathon-sources-20261114/event.txt`.
Temporary files may be cleared by the system; the Library original remains the
source of record. No credentials are needed to use this toolkit. No secret value
is recorded in the manifest. The medical and event attachments have verified
byte sizes and local Library identity metadata.

Use [rule-index.json](../rule-index.json) to distinguish `medical72:R51`,
`medical16:R4` and `dashboard:R51`. The 16-section IDs identify sections, not
188 independently validated requirements. Source locations are included.

## Authority and conflicts

The seven criteria in each track of the event brief determine judging weights.
The rulebooks are supplementary review lenses, not official event rules.
The source copyright and citation context remain intact. See [NOTICE](../NOTICE.md).

- **Schedule:** the main brief has doors at 9:30 AM, overview at 10:00 AM and
  finals through 5:00 PM ET. The separately pasted Luma summary says the in-person
  event begins at 10:00 AM. These may refer to doors versus programming; confirm
  with organizers rather than silently treating one as a correction. The captured
  countdown is a historical page state, not a live clock.
- **Data:** the main brief permits the frozen de-identified, patient-derived
  TCGA-BRCA release for nonclinical research. The Luma summary uses the broader
  phrase “No patient data.” Do not expand authorization from that ambiguity:
  use event-approved sources and ask organizers about disputed additions. No
  identifiable or participant-supplied patient records or clinical decisions.
- **Clinical examples:** the attached medical rulebook refers to clinical
  deployment, diagnosis and patient risk. These examples are not authorization
  to build prohibited clinical tools. It also contains code snippets; they are
  preserved as text and have not been run or validated here.
- **Absolute wording:** statements such as “require an external test set for any
  generalization claim,” “every image links to ... one label record,” and the
  proposed hierarchy of reference standards need task-specific expert review.
  Do not convert them into automatic score deductions. The 16-section checklist
  emphasizes fitness for a stated task and recognizes annotation granularity.
- **Timing and leakage:** medical72 R25's categorical language about later
  diagnosis labels should be reviewed alongside medical16 sections 6 and 9,
  which distinguish prediction inputs from explicitly defined future outcomes.
  Request the question's decision time, label definition and availability window.
- **Shortcut probes:** the event forbids inferring sensitive patient attributes.
  Do not execute medical72 R43's race-inference discussion as a hackathon task.
  R37–R40 are research examples, not automatic mandatory experiments.
- **Agreement, missingness and quality:** medical72's broad claims about label
  agreement, missingness mechanisms and “good” data warrant statistical review.
  Do not use an unverified numeric threshold as proof, or replace human review
  with a global average quality score. The two medical sources intentionally
  remain distinct rather than being silently blended.
- **Privacy and accessibility:** legal, imaging, statistical and accessibility
  conclusions require qualified review. Neither this toolkit nor an included
  checklist certifies privacy, compliance, clinical safety or accessibility.

## Primary-source orientation checked on 2026-11-14

The [FDA GMLP page](https://www.fda.gov/medical-devices/artificial-intelligence-enabled-medical-devices/good-machine-learning-practice-medical-device-development-guiding-principles)
identifies the January 2025 IMDRF final document and its ten guiding principles,
building on the 2021 FDA/Health Canada/MHRA principles. This is context about
medical-device development, not a certification or a new hackathon requirement.

[W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) is the primary accessibility
reference for interpreting the dashboard checklist. Review the actual success
criteria and exceptions for any proposed accessibility finding. This repository
has not verified every upstream reference preserved in the supplied documents.
