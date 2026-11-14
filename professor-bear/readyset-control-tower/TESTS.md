# Test record

Source: `a7ussein/readyset-control-tower@4dd07736e99f96dd46cb6199c32bea32465bd20e`.
Reviewed 2026-11-14 in a disposable Git-object copy. The original checkout was unchanged.

| Check | Result | Evidence |
|---|---|---|
| Submitted unittest suite | 107 passed, 0 failures, 0 errors, 0 skipped; 15.624 seconds | [Log](evidence/upstream-tests.log) |
| Independent proposed guardrails and controls | 14 checks: 2 passed, 12 failed expectations, 0 probe exceptions | [Observations](evidence/observations.json), [log](evidence/independent.log) |
| Organizer JSON schema plus finding/repair references | 7 synthetic outputs valid, 0 invalid | [Results](evidence/schema-checks.json) |
| Frontend TypeScript | exit 0, no diagnostics | [Log](evidence/typescript.log) |
| Vite production build | exit 0, 26 modules transformed | [Log](evidence/vite-build.log) |
| Review deck | 15 slides rendered and visually inspected; no overflow; keyboard and pause controls passed | [QA](evidence/deck-qa.json), [contact sheet](evidence/deck-contact-sheet.png) |
| Browser smoke checks | 10 passed, 0 failed, no page script errors | [Results](evidence/browser-checks.json) |

These counts measure different things and must not be combined into a quality
percentage. The independent probes intentionally target suspected gaps. Schema
validity includes the erroneous Ready outputs; it establishes structure only.

## Commands and environment

Python 3.14.6; macOS 26.5.1 ARM64; Node 25.9.0; npm 11.12.1;
Vite 8.3.7 from the lockfile; Chrome 157.0.8103.51.

Commands inside the isolated copy:

```sh
python3 -m unittest discover -s tests -v
node node_modules/typescript/bin/tsc -b
node node_modules/vite/bin/vite.js build
python3 checks.py /absolute/disposable/source /absolute/output
```

For frontend dependencies, `npm ci --ignore-scripts --no-audit --no-fund`
used separate empty user/global config files and a disposable cache. No npm
lifecycle scripts were allowed. The initial attempt stopped before installing
because npm rejected a shared /dev/null config path; a retry with distinct empty
files succeeded. The initial TypeScript attempt encountered a sandbox directory
metadata denial; after permitting metadata lookups, the same compiler passed.
These harness failures are not submission failures.

The inner macOS sandbox blocked private user-file contents, external networking
and writes outside its disposable directory. It allowed loopback for local server
tests and blocked port 11434. An empty environment supplied PATH, TMPDIR and
PYTHONNOUSERSITE only; the runtime added LC_CTYPE and CF encoding metadata.
Browser checks used a new unsigned-in profile and a page-request allowlist for
the local test server. No signed-in browser session was used.

The independent script imports the submission's invented TinyRelease fixture.
Run it only after inspecting the pinned source and reproducing an isolated
environment. Exit 1 indicates unmet recommended expectations; observations.json
records each result. The supplied browser harness is the exact observed harness,
with session-specific temporary paths; adapt those paths and port for another
isolated run. It is not a one-command production installation script.

No raw event records, organizer answer keys or envelope credentials are included.
No actual envelope was opened: the suite's two unsealing tests use fake scripts
and invented inputs. The separate 15 event-data recipe files under tests/releases,
real-data reference analyses, hosted deployment, paid API calls, performance at
full scale, screen-reader tasks and complete accessibility/clinical validation
were not tested. The screenshot shows only invented fixture values.
