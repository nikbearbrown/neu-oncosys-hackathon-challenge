# Tests and limits

Tested snapshot: `ab5084f7caaa57e68636e2cd3fde97b20a47bf69` of NinadRao0707/cohort-firewall. Date: November 14, 2026. This is the observed local commit, not a verified official frozen submission. Exact environment versions are in [provenance.json](evidence/provenance.json).

## Safety and execution scope

The reviewer inspected the imported implementation before execution. An independent source clone was used under `/tmp`; no installers, setup scripts, migrations, hosted services, cloud credentials, sealed materials, answer keys, real patient data, or external reference-analysis modules were executed/accessed. The probes use synthetic in-memory tables and tiny temporary TSV files. Review signatures use a fresh throwaway key; review records are written only in a fresh temporary directory. The harness replaces socket.socket.connect with a rejecting function and never enables the LLM paths. This is a bounded safety measure, not an operating-system network-isolation certification.

The repository's default static-only review instructions were superseded for these inspected local tests by the explicit request for safe feasible testing. No other execution authorization was inferred.

## Independent direct-function probes

Command, using already installed dependencies:

```sh
python3 professor-bear/cohort-firewall/reproductions/checks.py /path/to/pinned/cohort-firewall
```

The harness is an observation runner: it catches expected and unexpected exceptions, emits JSON, and does not treat process exit 0 as a product test pass. Compare outputs with this table and [raw results](evidence/independent-tests.json). Each probe ran once at the pinned source, then the full harness was rerun after the final two probes were added.

| Probe | Expected safe behavior | Actual observation | Interpretation |
|---|---|---|---|
| Question text changed after certification | Reject a spec hash mismatch | Different question stored in a signed, verifiable approval | CF-04 reproduced |
| Release findings/affected_by removed | Reject tampering or preserve required acknowledgment | Untampered missing acknowledgment rejected; stripped result accepted with no acknowledgment | CF-03 reproduced |
| Wildcard feature complete cases | Exclude the row with missing x | Both rows retained/exported yes | CF-06 reproduced |
| Entire required predictor absent | Mark answerability unavailable | Both rows exported yes; warning lists absent field | CF-06 reproduced; warning retained |
| Nonempty list spec | Structured invalid-spec result | AttributeError: list has no get | CF-05 reproduced |
| Nonempty list dictionary | Structured invalid-dictionary result | AttributeError: list has no get | CF-05 reproduced |
| Numeric column > string filter | Structured invalid-filter result | TypeError from comparison | CF-05 reproduced |
| Empty/unreadable CSV | Insufficient Evidence | INSUFFICIENT_EVIDENCE | Positive control |
| Approve a signed Blocked result | Reject approval | ReviewError with allowed reject/request_more actions | Positive control |
| Contradictory optional report string | Reject contradictory advice | report_passes_guard returned true | CF-07 guard-level reproduction; no model call |
| Append conflicting duplicate clinical row | Detect duplicate/identity defect | Three input rows become two loaded rows; zero diff changes; hashes differ | CF-02 reproduced |
| Existing excluded sample becomes eligible | Rerun analysis and update count | not_rerun, affected=false, after=null; direct count changes 1→2 | CF-01 reproduced using reviewer-authored analysis |

The review-boundary probes create legitimate local synthetic certificates with the submission's issue function. They do not forge a private key, alter a production record, or demonstrate an authenticated remote exploit. The analysis-routing probe uses a small reviewer-defined function, never the organizers' reference analyses.

## Selected submitted test

After inspecting `tests/test_disclosure.py` and its imported module:

```sh
python3 /tmp/cohort-firewall-source/tests/test_disclosure.py
```

All **six cases passed**; exact output: [upstream-disclosure.log](evidence/upstream-disclosure.log). These are formatting cases for small-count suppression and preservation of IDs/decimals. This is not evidence of full privacy protection or full-suite success.

## Presentation verification

The deck copies the existing Professor Bear Lato, red/white, two-column visual style, with one slide per finding and detailed presenter notes. The local review deck (not the submitted web application) is rendered with installed Playwright and headless Chrome. The reproduction script blocks HTTP/HTTPS requests and reads local files only.

- [Deck geometry and JavaScript check](evidence/deck-qa.json).
- [PDF page checks](evidence/pdf-qa.json).
- [All-slide contact sheet](evidence/deck-contact-sheet.png).
- [Renderer](reproductions/render_deck.py).

Full-size slide images are retained under `evidence/slide-01.png` through `slide-11.png`. Render checks measure containment and headline wrapping; they do not establish accessibility compliance or real-room legibility. See [deck review](evidence/deck-review.md) for the per-slide visual assessment.

## Not run

The complete submitted test suite; clean dependency installation; API server and HTTP requests; Next.js build; submitted browser interactions; protected event analyses; public or sealed mutation challenges; bootstrap/repair simulation; optional LLM output generation; Supabase persistence; demo-video/user-task evaluation; assistive-technology testing. README success claims were not adopted as independent test results. No official accuracy rate or score follows from these tests.
