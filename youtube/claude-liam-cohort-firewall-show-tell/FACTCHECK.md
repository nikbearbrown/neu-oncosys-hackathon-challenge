# Film evidence ledger

This selective promotional introduction does not replace the independent review. Source pins and actual capture locations are in [SOURCES.md](SOURCES.md); observed runs are in [SESSION.md](SESSION.md). No official judging score, clinical validation or production readiness is claimed.

| Beat | Narration | Evidence category |
|---|---|---|
| BOPEN | Cohort Firewall: Evidence And Policy. By Ninad Rao, Kareesa Rao, Sreelasya Changalasetty, and Sanica Chaudhary. Sponsored by Northeastern SEIS, OncoSys AI, The Open Accelerator, and Red Hat. | Supplied sponsor identity and pinned README team attribution |
| BIDEA | Hallo. This is Liam, in for Bear. Cohort Firewall separates measurements from policy. It makes the rules behind a readiness decision explicit and attaches evidence to the result. That is a useful architecture for a system people must inspect and challenge. | Source-grounded explanation/interpretation; conceptual visual |
| BDEFS | Three terms. Policy means explicit rules for interpreting checks. Evidence means measurements supporting a finding. Certificate means a signed record of selected result fields. | Source-grounded explanation/interpretation; conceptual visual |
| B01 | Measurements feed explicit rules, and the result goes to review. The project's evidence records include fields, limitations, remedies, and what would justify reconsideration. That gives the next person a concrete starting point. | Source-grounded explanation/interpretation; conceptual visual |
| B02 | Here is an actual local command-line result using the supplied synthetic clean variant. The engine returns Ready, with no findings, and its certificate verifies. This is an engine demonstration, not evidence of clinical readiness. | Actual recorded local interface or command output; read scope below |
| B03 | Now the supplied synthetic missingness variant returns Conditional, with one finding. The certificate verifies here too. A valid signature and a favorable readiness verdict answer different questions. The interface should keep that distinction clear. | Actual recorded local interface or command output; read scope below |
| B10 | The review controls include a real restriction against approving a Blocked result, observed in the independent tests. Preserve that boundary while strengthening exactly which evidence and question the signature covers. | Source-grounded explanation/interpretation; conceptual visual |
| B11 | Next, bind the complete question and evidence document to the approval. A signature can verify the fields it covers; it cannot protect fields left outside that contract. Make changes to either invalidate the old receipt. | Proposed development or suggested exercise, not a completed feature |
| B12 | Then broaden the difficult-input tests. Newly eligible samples, duplicate identifiers, and malformed filters deserve explicit outcomes. That builds on the existing insufficient-evidence behavior instead of allowing an unexpected shape to end the workflow. | Proposed development or suggested exercise, not a completed feature |
| B13 | Keep the strengths and make the boundaries more explicit. This is a research prototype, and a useful starting point for further development. The linked independent review contains the detailed evidence and remaining limitations. | Source-grounded explanation/interpretation; conceptual visual |
| BVDT | Let's recap. Separate measurements from policy. Make findings actionable and inspectable. Bind approvals to the complete evidence. Give difficult inputs explicit outcomes. | Source-grounded explanation/interpretation; conceptual visual |
| BHTF | Help me test Cohort Firewall with invented data. Change the question after a result is signed, and add a newly eligible sample. Explain which checks must rerun and why the earlier approval must not silently cover the changed evidence. | Proposed development or suggested exercise, not a completed feature |
| BOUT | Thank you to the participants and sponsors: Northeastern SEIS, OncoSys AI, The Open Accelerator, and Red Hat. This is Liam, in for Bear. | Supplied sponsor identity and pinned README team attribution |

## Scope for this film

All demonstrated data are invented/synthetic. Cohort Firewall shows verbatim local CLI result excerpts, not a browser demo.

The suggested prompt is not shown as an executed agent response. Conceptual animations explain structure; they are not simulated app results. Next steps preserve the concerns in the full reviews and do not imply fixes have been implemented.
