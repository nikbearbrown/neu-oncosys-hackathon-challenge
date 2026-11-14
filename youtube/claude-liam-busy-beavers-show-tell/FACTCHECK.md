# Film evidence ledger

This selective promotional introduction does not replace the independent review. Source pins and actual capture locations are in [SOURCES.md](SOURCES.md); observed runs are in [SESSION.md](SESSION.md). No official judging score, clinical validation or production readiness is claimed.

| Beat | Narration | Evidence category |
|---|---|---|
| BOPEN | Busy Beavers: From Finding To Review. By Team Busy Beavers. Sponsored by Northeastern SEIS, OncoSys AI, The Open Accelerator, and Red Hat. | Supplied sponsor identity and pinned README team attribution |
| BIDEA | Hallo. This is Liam, in for Bear. Busy Beavers turns a data comparison into findings people can explore. It connects detected changes, affected analyses, and possible next steps. The useful idea is to make investigation feel like a coherent workflow. | Source-grounded explanation/interpretation; conceptual visual |
| BDEFS | Three terms. Finding means a detected change with supporting evidence. Dependency means an input an analysis relies on. Derivative means a new output that preserves the original. | Source-grounded explanation/interpretation; conceptual visual |
| B01 | Compare the releases, explain the effect, then invite review. Busy Beavers keeps those stages visible. A finding becomes useful when a person can trace it to evidence and understand which analysis it affects. | Source-grounded explanation/interpretation; conceptual visual |
| B02 | This is the actual local results screen with invented sample data. In our browser checks, a swapped profile exposed evidence and showed one analysis rerun while the unrelated analysis stayed unchanged. The interface makes that relationship inspectable. | Actual recorded local interface or command output; read scope below |
| B03 | The next-steps view carries the investigation forward. The tested swap path kept researcher review pending and did not automatically apply a fix. The downloaded findings also matched the information shown in the interface. | Actual recorded local interface or command output; read scope below |
| B10 | The architecture preserves original releases and produces derivatives separately. That is worth keeping. It lets a researcher compare a proposed correction with the source rather than silently losing the earlier state. | Source-grounded explanation/interpretation; conceptual visual |
| B11 | Next, make every approved derivative follow the review decisions exactly. A proposed exclusion, an accepted exclusion, and a rejected exclusion need different outcomes. Keep previews useful, but label their approval state clearly. | Proposed development or suggested exercise, not a completed feature |
| B12 | Also check input validity before taking an unchanged-file shortcut. A valid unchanged release and two empty folders are different situations. Give each a clear result and a concrete next action. | Proposed development or suggested exercise, not a completed feature |
| B13 | Keep the strengths and make the boundaries more explicit. This is a research prototype, and a useful starting point for further development. The linked independent review contains the detailed evidence and remaining limitations. | Source-grounded explanation/interpretation; conceptual visual |
| BVDT | Let's recap. Show which analysis a change affects. Make evidence and next steps inspectable. Preserve the original release. Bind approved exports to review decisions. | Source-grounded explanation/interpretation; conceptual visual |
| BHTF | Help me extend Busy Beavers using invented data. Compare a proposed repair, an accepted repair, and a rejected repair. Show what each export should contain and how to verify the original release stayed unchanged. | Proposed development or suggested exercise, not a completed feature |
| BOUT | Thank you to the participants and sponsors: Northeastern SEIS, OncoSys AI, The Open Accelerator, and Red Hat. This is Liam, in for Bear. | Supplied sponsor identity and pinned README team attribution |

## Scope

All demonstrated data are invented/synthetic. ClearAnswer shows its actual landing interface only; no model-driven audit or external model call was run for its film. Cohort Firewall shows verbatim local CLI result excerpts, not a browser demo. HIPPA-cratic's SQL cross-check returned 16 matching sample identifiers and step counts in the observed synthetic example. Other browser demonstrations are the actual captured synthetic sessions described in the linked review/test records.

The suggested prompt is not shown as an executed agent response. Conceptual animations explain structure; they are not simulated app results. Next steps preserve the concerns in the full reviews and do not imply fixes have been implemented.
