# Film evidence ledger

This selective promotional introduction does not replace the independent review. Source pins and actual capture locations are in [SOURCES.md](SOURCES.md); observed runs are in [SESSION.md](SESSION.md). No official judging score, clinical validation or production readiness is claimed.

| Beat | Narration | Evidence category |
|---|---|---|
| BOPEN | ReadySet: Evidence Before Action. By Team Automyte. Sponsored by Northeastern SEIS, OncoSys AI, The Open Accelerator, and Red Hat. | Supplied sponsor identity and pinned README team attribution |
| BIDEA | Hallo. This is Liam, in for Bear. ReadySet asks a useful question: what changed in our data, and does that change matter for the analysis we want to run? | Source-grounded explanation/interpretation; conceptual visual |
| BDEFS | Three terms. A release is one version of the data. A finding is a change supported by evidence. A review is a person deciding what to do with that evidence. | Source-grounded explanation/interpretation; conceptual visual |
| B01 | The useful idea is to connect three things: the data, the analysis, and the evidence for a decision. A change matters because of what it affects. That makes the question part of the checking process. | Source-grounded explanation/interpretation; conceptual visual |
| B02 | Here is the actual ReadySet interface, running locally with invented test data. A deliberately swapped measurement triggers a review. The headline tells us to pause, and the analysis cards tell us where to look. | Actual recorded local interface or command output; read scope below |
| B03 | Now the question changes. We leave out the affected protein analysis and keep the unrelated analysis. In this tested example, the verdict becomes Ready. That is a concrete demonstration of question-dependent checking. | Actual recorded local interface or command output; read scope below |
| B04 | Bring the affected analysis back, and the finding returns. This evidence view is a strength: the reader can inspect what changed, consider the suggested repair, and see the limits of the explanation. | Actual recorded local interface or command output; read scope below |
| B05 | The next strength is the handoff. Detection produces a finding; a person reviews it before deciding on action. The normal named-review path worked in our browser checks. That makes the decision inspectable. | Source-grounded explanation/interpretation; conceptual visual |
| B06 | Next steps can build on that foundation. Add an input-validity gate before comparing changes. If required evidence is missing, the process should stop there and explain what is needed to continue. | Proposed development or suggested exercise, not a completed feature |
| B07 | Then preserve each review as an event. A decision can change, but its earlier evidence and reasoning should remain inspectable. This is a practical extension of the evidence fingerprints the project already uses. | Proposed development or suggested exercise, not a completed feature |
| B08 | For the team, the opportunity is clear: keep the efficient detector and the readable evidence, then strengthen those boundaries. This is a promising research prototype. The demonstration does not establish clinical or production readiness. | Source-grounded explanation/interpretation; conceptual visual |
| BVDT | Let's recap. Connect changes to the selected analysis. Let people inspect the evidence. Validate inputs before interpreting changes. Preserve the history of human decisions. | Source-grounded explanation/interpretation; conceptual visual |
| BHTF | Help me extend ReadySet with an input-validity gate. Use invented data. Show one valid unchanged release and one missing-input case. Explain the expected decision and the evidence needed to justify it. | Proposed development or suggested exercise, not a completed feature |
| BOUT | Thank you to the participants and sponsors: Northeastern SEIS, OncoSys AI, The Open Accelerator, and Red Hat. This is Liam, in for Bear. | Supplied sponsor identity and pinned README team attribution |

## Scope

All demonstrated data are invented/synthetic. ClearAnswer shows its actual landing interface only; no model-driven audit or external model call was run for its film. Cohort Firewall shows verbatim local CLI result excerpts, not a browser demo. HIPPA-cratic's SQL cross-check returned 16 matching sample identifiers and step counts in the observed synthetic example. Other browser demonstrations are the actual captured synthetic sessions described in the linked review/test records.

The suggested prompt is not shown as an executed agent response. Conceptual animations explain structure; they are not simulated app results. Next steps preserve the concerns in the full reviews and do not imply fixes have been implemented.
