# Verification record — 2026-11-14

Performed locally on macOS with Python 3 and Git:

- `python3 -m unittest discover -s tests -v`: **25 tests passed**.
  Coverage includes SHA identity, exact evidence quotes and line ranges, invalid
  paths, symlink/binary/oversized/data exclusions, dirty-tree isolation, no shell
  execution, secret/PEM masking, hostile HTML/Markdown, collection limits,
  unavailable repositories, batch reporting, rule IDs, and judge/student scoring
  controls. Remote GitHub responses were mocked in these tests.
- `python3 -m py_compile review.py`: passed.
- `python3 review.py help`: exercised; provides tutorial and review-method pointers.
- Both Library attachments downloaded successfully with their Library metadata.
  Original byte counts: event 15,411; medical rulebook 34,419. Medical source and
  local dashboard source were copied byte-for-byte. The event differs only by
  replacing its recording credential with `[REDACTED]`.
- The additional 16-section checklist is a normalized transcription of the user
  message; it was not available as a byte-identical attachment. The message-read
  tool was temporarily unavailable; the inherited message supplied the text.
- Source hashes, local documentation links, rule-index locations and exact rubric
  transcription are checked by `python3 scripts/verify_docs.py`.
- FDA GMLP and W3C WCAG 2.2 primary-reference pages were opened for orientation.
  This was not an exhaustive validation of every supplied rule or citation.

No actual team submission list was available. No participant repository, demo,
medical dataset, clinical result, accessibility conformance or unseen-input run
has been verified. No organizer keys were accessed. No submitted code was run.
Source inspection and citation consistency cannot establish the correctness of
reviewer reasoning, authenticity of a human sign-off, or absence of every secret.
Generated reports remain ignored by Git and need human review before sharing.

## Earlier publication attempt

The independent local repository was committed on `main`. GitHub creation and
push were **not executed**: automatic approval review rejected the requested
private `nikbearbrown/neu-ai-healthcare-hackathon` publication, stating that
uploading the supplied source materials to the external destination needed more
explicit authorization. The message-history evidence lookup was temporarily
unavailable. No workaround or repeat publication attempt was made. Publication
remains blocked pending authorization that explicitly covers those materials.

## OncoSys integration — 2026-11-14

The user subsequently supplied the actual organizer repository and requested
our version be named NEU-Oncosys Hackathon Challenge. The local repository was
renamed to `neu-oncosys-hackathon-challenge`, preserving its Git history.

- Read upstream rules, README, submission checklist, shared-format guide, data
  index and all six product briefs at `6e15a399a64ffbf80778db0b462ac239e70086b9`.
- Added 20 pinned documentation links with verified SHA-256 and byte sizes.
- Added six product review routes plus custom-product handling to packets and
  reports. No upstream code, data, assets, envelopes or answer keys copied.
- Re-ran 25 unit tests, Python compilation, help/challenge CLI and 217 source/
  documentation checks successfully. Remote collection tests use mocked responses.
- Rechecked both retained Library source hashes against the original byte counts.
- GitHub read-only lookup confirmed the new target did not exist before creation.

The prior rejected publication has not been described as successful. The new
name and user-supplied upstream integration provide additional authorization
context for one publication attempt; its result will be recorded separately.

## Successful publication

The newly authorized target was created and pushed successfully on 2026-11-14:
https://github.com/nikbearbrown/neu-oncosys-hackathon-challenge

Visibility is private; default branch is main. The first published OncoSys
integration commit is `c3d5eaf`. This supersedes the earlier blocked attempt
under the old name. No private recording credential or upstream datasets were
included. Real submissions remain pending; no team scores or runtime claims
have been produced.
