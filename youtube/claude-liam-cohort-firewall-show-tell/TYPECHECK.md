# TYPECHECK.md — GATE T

Reel: `claude-liam-cohort-firewall-show-tell`  |  Checked: 2026-11-14T18:36  |  Overall: PASS  |  Beats checked: 13  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [BDEFS] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [BVDT] narration recites the card (1.00) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BOPEN | bookend | light | min-size §8.1: min text-run height 41px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BIDEA | bookend | light | min-size §8.1: min text-run height 41px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BDEFS | bookend | light | min-size §8.1: min text-run height 41px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B01 | remotion | light | no-wordy-card §8.5: OncosysProcess: per-element check passed (max 6 words in 'title') | PASS | — |
| B02 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | remotion | light | no-wordy-card §8.5: OncosysProcess: per-element check passed (max 4 words in 'title') | PASS | — |
| B11 | remotion | light | no-wordy-card §8.5: OncosysProcess: per-element check passed (max 8 words in 'note') | PASS | — |
| B12 | remotion | light | no-wordy-card §8.5: OncosysProcess: per-element check passed (max 8 words in 'note') | PASS | — |
| B13 | remotion | light | no-wordy-card §8.5: OncosysProcess: per-element check passed (max 8 words in 'note') | PASS | — |
| BVDT | bookend | light | min-size §8.1: min text-run height 41px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BHTF | bookend | light | min-size §8.1: min text-run height 41px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BOUT | bookend | light | min-size §8.1: min text-run height 41px >= floor 41px (individual-char fallback at 2×) | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 7 | 0 |
| min-size §8.1 | 13 | 0 |
| overflow §8.2 | 13 | 0 |
| contrast §8.3 | 13 | 0 |
| contrast-local §8.3b | 13 | 0 |
| bbox-overlap §8.6b | 13 | 0 |
| card-clip §8.13 | 13 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 4 | 2 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
