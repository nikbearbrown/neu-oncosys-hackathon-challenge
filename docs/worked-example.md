# Worked feedback example (illustrative only)

This describes a hypothetical source finding. It is not a real team's submission,
a runtime result, or an official score. Actual reports require an immutable
commit and valid excerpts from the collected packet.

Suppose a readiness function returns `Ready` in its exception handler after a
missing file, and the interface displays that value without an error explanation.
A useful review would say:

- **Observed:** the cited exception branch returns the same state as the normal
  success branch. Name the exact function, path, commit and source lines.
- **Interpretation:** an unreadable source could be presented as a successful
  check. Runtime behavior remains untested until exercised.
- **Rubric:** Track 1 evidence/sources and safety/uncertainty; do not deduct twice
  automatically or invent a disqualification.
- **Supplemental rules:** dashboard R76, medical16 section 12, and medical72 R70.
- **Concrete change:** preserve the failed-check status and reason; return
  Insufficient Evidence when the required evidence is unavailable, subject to
  the project's documented decision policy. Keep data failures distinct from
  valid zero counts and from a genuinely tested Ready outcome.
- **Acceptance check:** submit an authorized fixture with one required file
  absent. Verify the UI shows the missing-file reason, identifies which checks
  did not run, and does not offer an unconditional Ready result. Repeat with a
  valid empty cohort to confirm it is treated differently from a file error.
- **Strength to retain, if supported:** a centralized verdict function could make
  the correction consistent across API and interface. Cite its actual call sites;
  do not assume that architecture exists merely to balance criticism with praise.

Student wording: “Fix the missing-file path first because users could mistake it
for a completed check. Then add the two small fixtures above so you can show
that errors and empty cohorts produce different explanations.”

Judge wording: “Ask the team to demonstrate the missing-input case and explain
its evidence-state policy. The source suggests a material issue, but execution
has not been observed. Review the result before assigning criterion scores.”
