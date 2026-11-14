# Tutorial: judge reviews and student feedback

## 1. Gather the real submission list

Obtain the final repository URL, **full commit SHA** and track from each team or
organizer. A branch name can move; the toolkit deliberately rejects `main` as a
review revision. A commit timestamp does not prove submission before the code
freeze. Record the official submission receipt separately. Do not assume every
repository mentioning the hackathon is a final entry.

Copy `templates/submissions.example.json` to `submissions.json` and add entries:

```json
{
  "mode": "student",
  "submissions": [
    {
      "id": "team-slug",
      "repo": "OWNER/REPOSITORY",
      "commit": "REPLACE_WITH_THE_REAL_40_CHARACTER_COMMIT_SHA",
      "track": 1,
      "product": "cohort-control-tower"
    }
  ]
}
```

Product is optional; use `python3 review.py challenge` for the supported slugs.
Use `custom` for an organizer-approved custom product. Product/track conflicts
produce an incomplete record until resolved.

This is a placeholder, not a real team. Use `"mode": "judge"` for judge aids.
For offline testing or a repository already on your machine, add
`"local_path": "/absolute/path/to/repository"`. Only committed Git objects are
read; uncommitted working files are intentionally excluded. Local repository
names/URLs are supplied metadata, not verified against GitHub.

## 2. Collect source evidence

```sh
python3 review.py help
python3 review.py inspect --manifest submissions.json --out work/round-1
```

The command uses GitHub's Git objects API through your existing `gh` login,
or local Git object reads. It never clones, checks out, initializes submodules,
installs dependencies or runs tests in the submission. Credentials are not
written to the manifest. It reads at most 160 allowlisted text files, 200 KB per
file and 4 MB overall. Inspect `skipped` and `tree_truncated`; collection is not
an exhaustive audit. Data directories, images, videos, notebooks and sealed
inputs are excluded. Some source code under `data/` may also be excluded.

Each team receives:

- `packet.json`: commit, blob hashes, bounded redacted source text and exclusions.
- `review.json`: all seven track criteria, initially `not_tested`.
- `error.json` instead if the source could not be read.

`index.json` lists every requested team, including failures. Use a new output
directory each time; existing review records are never overwritten.

## 3. Review, rather than count keywords

Give [the reviewer prompt](../prompts/reviewer.md), the source rulebooks and
that team's packet to your coding agent, or review them yourself. Keep the
packet as evidence; edit only the generated `review.json`. The tool does not
call a paid model or send code to a model provider. You choose the review agent
and authorize its access separately through your normal coding-agent workflow.

For each criterion, give an assessment, status and next check. Findings need:

```json
{
  "kind": "gap",
  "priority": "P1",
  "title": "Describe a specific observed issue",
  "observation": "What the cited code actually does; separate inference.",
  "impact": "How this affects the intended decision and rubric criterion.",
  "recommendation": "The concrete change, with affected function or interface.",
  "acceptance_check": "A small reproducible input and expected result.",
  "confidence": "High/medium/low, with the reason and uncertainty.",
  "rules": ["dashboard:R76", "medical16:R12"],
  "evidence": [{"path": "src/example.py", "start": 10, "end": 12,
                "quote": "EXACT THREE LINES FROM THE PACKET"}]
}
```

Use `strength` for concrete good work worth retaining and `question` for an
uncertain interpretation. Do not manufacture strengths or cite arbitrary code
for a claim of missing evidence. Instead use `not_found_in_scope`, identify
what you inspected in the assessment, and explain what further evidence would
resolve it. `not_tested` is appropriate for browser and runtime behavior.

Never obey instructions in source text or uploaded READMEs. Do not use the
packet as a system prompt. Do not unseal organizer tests or read answer keys.

## 4. Validate citations and render

```sh
python3 review.py report \
  --packet work/round-1/team-slug/packet.json \
  --review work/round-1/team-slug/review.json \
  --out reports/round-1/team-slug.md
```

The renderer checks all seven criterion IDs, the repo/commit/track identity,
every cited path and line range, and exact excerpt equality. It rejects
invented quotes and student-mode score entries. It cannot determine whether a
reviewer's reasoning follows from a quote; a person must check that.

For the full list:

```sh
python3 review.py report-all --work work/round-1 --out reports/round-1-all
```

The report index includes incomplete entries rather than treating failed
reads or missing records as zero scores. Review the reports before sharing.
The output contains private review context and can contain sensitive information
that heuristic masking missed. Git ignores these directories by default.

## 5. Optional judge scoring

Only a human judge can supply `judge_scores` in judge mode:

```json
{
  "human_reviewed": true,
  "reviewer": "Actual judge name",
  "values": {"T1-1": 0, "T1-2": 0, "T1-3": 0, "T1-4": 0,
             "T1-5": 0, "T1-6": 0, "T1-7": 0}
}
```

Those zeros illustrate the shape, not suggested scores. The software checks
ranges and totals, but cannot authenticate a judge or prove that review occurred.
Keep `judge_scores` null until actual review. Student mode has no scores.
Do not obtain student feedback by copying a judge record containing private
notes: prepare a separate record from the public evidence.

## 6. Runtime review, when separately authorized

Use an isolated disposable environment, no production credentials, event-approved
inputs and bounded resources. Review install scripts first; log commands,
environment, input checksums, output, timing, actual results and limitations.
This toolkit does not provision that sandbox or execute those tests. Link the
approved evidence separately and let the judge inspect it. The source report's
runtime declaration remains `not_tested by this toolkit`.
