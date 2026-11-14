# Film evidence ledger

This selective promotional introduction does not replace the independent review. Source pins and actual capture locations are in [SOURCES.md](SOURCES.md); observed runs are in [SESSION.md](SESSION.md). No official judging score, clinical validation or production readiness is claimed.

| Beat | Narration | Evidence category |
|---|---|---|
| BOPEN | HIPPA-cratic: Build And Cross-Check. By Team Hippa cratics. Sponsored by Northeastern SEIS, OncoSys AI, The Open Accelerator, and Red Hat. | Supplied sponsor identity and pinned README team attribution |
| BIDEA | Hallo. This is Liam, in for Bear. This is the HIPPA-cratic team's Cohort Studio. It makes cohort construction explicit and offers a second way to check the result. The opportunity is to connect a readable workflow with independently inspectable computation. | Source-grounded explanation/interpretation; conceptual visual |
| BDEFS | Three terms. Cohort means the group selected for a research question. Join grain means which entity each joined record represents. SQL check means a second computation of the same steps. | Source-grounded explanation/interpretation; conceptual visual |
| B01 | Define the steps, build the cohort, then cross-check the computation. The project distinguishes sample-level and patient-level joins. That helps expose situations where records multiply or become linked to the wrong sample. | Source-grounded explanation/interpretation; conceptual visual |
| B02 | Here is the actual application using its explicitly made-up sample, lab, and visit tables. We selected biopsy samples with a lab record from the same sample. The dropdown steps make that request visible without needing an AI service. | Actual recorded local interface or command output; read scope below |
| B03 | The cohort view shows what survives each step. This is a useful teaching and review feature: the researcher can see where membership changes rather than discovering a smaller final table without an explanation. | Actual recorded local interface or command output; read scope below |
| B04 | We ran the independent DuckDB SQL check. On this invented example, both computations returned the same sixteen samples, with matching counts after every step. That checks the implementation; the choice of research question and steps still needs human judgment. | Actual recorded local interface or command output; read scope below |
| B10 | The export retains steps, counts, release identity, and fingerprints. Those are strong ingredients for a reproducible record. The next step is making reconstruction enforce the same input identity that the record describes. | Source-grounded explanation/interpretation; conceptual visual |
| B11 | Bind caches and rebuild scripts to the recorded input contents. When a file changes at the same path, either refresh the computation or explain that the immutable release contract was broken. Keep counts and fingerprints on one snapshot. | Proposed development or suggested exercise, not a completed feature |
| B12 | Also distinguish an empty cohort from an unresolved question about the filter. Zero eligible records can be legitimate. A misspelled value needs a different explanation and a different next action. | Proposed development or suggested exercise, not a completed feature |
| B13 | Keep the strengths and make the boundaries more explicit. This is a research prototype, and a useful starting point for further development. The linked independent review contains the detailed evidence and remaining limitations. | Source-grounded explanation/interpretation; conceptual visual |
| BVDT | Let's recap. Make the cohort steps inspectable. Keep sample and patient joins distinct. Cross-check the computation independently. Bind reconstruction to the recorded inputs. | Source-grounded explanation/interpretation; conceptual visual |
| BHTF | Help me test HIPPA-cratic Cohort Studio with invented tables. Build one sample-level join and one patient-level join. Compare the engine with the SQL check, then change an input and explain what must be refreshed or rejected. | Proposed development or suggested exercise, not a completed feature |
| BOUT | Thank you to the participants and sponsors: Northeastern SEIS, OncoSys AI, The Open Accelerator, and Red Hat. This is Liam, in for Bear. | Supplied sponsor identity and pinned README team attribution |

## Scope

All demonstrated data are invented/synthetic. ClearAnswer shows its actual landing interface only; no model-driven audit or external model call was run for its film. Cohort Firewall shows verbatim local CLI result excerpts, not a browser demo. HIPPA-cratic's SQL cross-check returned 16 matching sample identifiers and step counts in the observed synthetic example. Other browser demonstrations are the actual captured synthetic sessions described in the linked review/test records.

The suggested prompt is not shown as an executed agent response. Conceptual animations explain structure; they are not simulated app results. Next steps preserve the concerns in the full reviews and do not imply fixes have been implemented.
