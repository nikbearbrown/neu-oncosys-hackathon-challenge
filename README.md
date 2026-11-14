# NEU OncoSys Hackathon Challenge

Review final GitHub submissions and give students specific, evidence-backed
feedback for the November 11–14, 2026 AI Healthcare Hackathon at Northeastern.
This independent toolkit was prepared for Nik Bear Brown. It is not an official
organizer publication, a hackathon submission, or a medical system.

The workflow gathers bounded source evidence at an immutable commit, prepares
all seven criteria for the selected track, and produces detailed Markdown
reports from a reviewer-completed record. It does **not** score repositories
from keywords or pretend that source inspection proves a working demo.

## Start here

- [Actual challenge repository and product checks](docs/oncosys-challenge.md).
- [Tutorial](docs/tutorial.md): inspect one repository or an entire submission list.
- [Review method](docs/review-method.md): evidence, priorities, scoring and limitations.
- [Reviewer prompt](prompts/reviewer.md): use with Claude Code, Codex or a human reviewer.
- [Source index and caveats](sources/README.md): event brief and supplied rulebooks.
- [Official track criteria, transcribed from the supplied brief](rubrics.json).
- [Submission list template](templates/submissions.example.json).
- [Worked feedback example](docs/worked-example.md): illustrative, not a submitted team.
- [Verification record](docs/verification.md).

Requires Python 3.10+ and, for remote GitHub access, an already authenticated
GitHub CLI (`gh`). No Python package installation or model API is required.

```sh
python3 review.py help
python3 review.py inspect --manifest submissions.json --out work
python3 review.py report --packet work/TEAM/packet.json --review work/TEAM/review.json --out reports/TEAM.md
python3 review.py report-all --work work --out reports
```

**Judge mode:** findings, strengths, concrete fixes, criterion-by-criterion
evidence, limitations and optional explicitly human-reviewed proposed scores.
**Student mode:** the same standard of evidence, with prioritized next steps
and acceptance checks; no scoring section. Students can review their own
work repeatedly at new commit SHAs. Judge-only notes belong in separate files,
never in a student record.

The upstream challenge is linked at a pinned commit in [upstream/challenge.json](upstream/challenge.json). It is reference material, not a team submission.

No actual final submission list has been supplied. The example manifest is
empty deliberately. No team has been reviewed or scored by this repository.
To review finals, provide each GitHub owner/repository, final commit SHA and
track (1 or 2). Default collection limits and exclusions are recorded in every
packet. Large repositories may need a focused follow-up inspection.

## What this contains

The event snapshot, 72-rule medical/image rulebook and 100-rule dashboard
guideline retain their original wording, with the event recording passcode
redacted. The separate 16-section medical checklist is also preserved as a
normalized transcription; 188 rule/section IDs are indexed in [rule-index.json](rule-index.json).
The [source manifest](sources/manifest.json) records hashes and the
redaction. The two rulebooks are supplemental review lenses, not extra scoring
weights. The original medical rulebook includes research/clinical examples
that must not be executed as hackathon instructions; see the caveats.

The repository starts private. Generated submissions, reports and review
packets are ignored by Git. Review their contents before sharing: automatic
secret masking is a limited safeguard, not a privacy certification.

There is no blanket license on supplied third-party material. See
[rights and attribution](NOTICE.md). No raw TCGA files, clinical records,
organizer keys or recording credentials belong here.
