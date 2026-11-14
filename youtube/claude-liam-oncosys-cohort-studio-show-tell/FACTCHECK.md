# Film evidence ledger

This selective promotional introduction does not replace the independent review. Source pins and actual capture locations are in [SOURCES.md](SOURCES.md); observed runs are in [SESSION.md](SESSION.md). No official judging score, clinical validation or production readiness is claimed.

| Beat | Narration | Evidence category |
|---|---|---|
| BOPEN | Cohort Studio: See Who Remains. By Lily Tammy, Seth Barribeau, Hriday Desai, Aayam Raj Shakya, and Yanyun Ma. Sponsored by Northeastern SEIS, OncoSys AI, The Open Accelerator, and Red Hat. | Supplied sponsor identity and pinned README team attribution |
| BIDEA | Hallo. This is Liam, in for Bear. Cohort Studio focuses on a different part of the problem: building the research group itself. Filters and joins change who remains. This project makes those changes visible before we rely on the final table. | Source-grounded explanation/interpretation; conceptual visual |
| BDEFS | Three terms. Cohort means the group selected for a research question. Join means combining records through shared identifiers. Grain means what one row represents. | Source-grounded explanation/interpretation; conceptual visual |
| B01 | Start with the sources, apply explicit steps, and inspect the resulting cohort. Count rows, samples, and people separately. A join can increase rows without adding people, and that difference matters to the analysis. | Source-grounded explanation/interpretation; conceptual visual |
| B02 | Here is the real Cohort Studio interface with an invented test fixture. The observed workflow connected cohort construction with its result and export. The useful feature is the ability to inspect how the selected group was produced. | Actual recorded local interface or command output; read scope below |
| B03 | The underlying checks distinguish join inflation from repeated patients and retain selection rules. That is a strong analytical foundation: the tool asks what the rows mean, rather than treating a bigger table as automatically better data. | Actual recorded local interface or command output; read scope below |
| B10 | The reproduction export records expected input hashes and includes the operation implementation. That moves beyond a prose recipe toward an executable account of the work. Keep the explanation and the runnable steps together. | Source-grounded explanation/interpretation; conceptual visual |
| B11 | Next, make provenance status precise. An unavailable expected checksum should say unverified; a matching checksum should say verified. Those states give the researcher different evidence, even when both files can be read. | Proposed development or suggested exercise, not a completed feature |
| B12 | Then separate a proposed automatic correction from an accepted change. Show the requested join beside the suggested join, retain the original run, and record the person's choice before describing an output as approved. | Proposed development or suggested exercise, not a completed feature |
| B13 | Keep the strengths and make the boundaries more explicit. This is a research prototype, and a useful starting point for further development. The linked independent review contains the detailed evidence and remaining limitations. | Source-grounded explanation/interpretation; conceptual visual |
| BVDT | Let's recap. Make cohort-building steps explicit. Count rows, samples and people separately. Distinguish verified from unverified inputs. Keep proposed and accepted changes distinct. | Source-grounded explanation/interpretation; conceptual visual |
| BHTF | Help me test Cohort Studio with invented tables. Build a join that multiplies rows, then propose a correction. Show rows, samples, and people before and after. Preserve the original steps and explain what a reviewer must approve. | Proposed development or suggested exercise, not a completed feature |
| BOUT | Thank you to the participants and sponsors: Northeastern SEIS, OncoSys AI, The Open Accelerator, and Red Hat. This is Liam, in for Bear. | Supplied sponsor identity and pinned README team attribution |

## Scope

All demonstrated data are invented/synthetic. ClearAnswer shows its actual landing interface only; no model-driven audit or external model call was run for its film. Cohort Firewall shows verbatim local CLI result excerpts, not a browser demo. HIPPA-cratic's SQL cross-check returned 16 matching sample identifiers and step counts in the observed synthetic example. Other browser demonstrations are the actual captured synthetic sessions described in the linked review/test records.

The suggested prompt is not shown as an executed agent response. Conceptual animations explain structure; they are not simulated app results. Next steps preserve the concerns in the full reviews and do not imply fixes have been implemented.
