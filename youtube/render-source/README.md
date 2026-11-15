# Local renderer sources

These project-specific components extend the existing Brutalist Remotion renderer. OncosysProcess is the Northeastern retint of the registered DesignPipelineClaim Show Tell isometric geometry. OncosysLecture implements event-branded opening, definitions, recap, prompt and ending. BrowserCapture retains its original default and adds a neu option for the surrounding frame only; the actual screenshot pixels are preserved.

Register OncosysLecture and OncosysProcess in the toolkit Root.tsx, with their exported schemas, 1920×1080 at 24 fps, and durationInFrames = ceil(durationSeconds × 24). Use the canonical remotion_scenes.py renderer, not an ad-hoc Remotion command. The renderer uses Remotion 4.0.543. Lato and official Northeastern marks come from the existing toolkit.

The typography checker recognizes OncosysLecture as a structural bookend/literal prompt, and OncosysProcess as a structured diagram. Pixel-size, contrast, overflow and final-frame gates remain required. Application text remains part of the captured source, with authored captions checked separately. No blanket gate override is used.

The event-specific six-beat contract is checked by `build-tools/verify_films.py`. The legacy bookend checker expects Claude-specific components and does not recognize these explicitly requested event cards; its incompatible-template result is recorded rather than called a pass. All six structural roles, measured narration, project/team names and four spoken sponsors are checked by the event validator. The outro visibly retains @NikBearBrown.

The local typography integration uses the unmasked source frame for declared regional contrast (masking a browser screenshot first incorrectly reports its text as absent). A synthetic regression confirmed real black-on-white heading passes while the masked placeholder fails. Explicit text inventories retain all designed headings, labels, notes and footers while excluding isometric hatching/edges that are not glyphs. Gate V still inspects the full composition.

`metadata.render_concurrency: 4` is an opt-in extension to the canonical renderer; legacy default remains 1, accepted values are integers 1–8. It changes throughput, not resolution, PNG sampling, CRF or measured clocks.

The local renderer also locks its shared consumers index, reloads the latest contents inside that lock, and replaces the index atomically. Different reels can render concurrently without overwriting each other's index entries. Never edit an individual beat sheet while its renderer or compiler is running: those tools update the sheet after completing work.
