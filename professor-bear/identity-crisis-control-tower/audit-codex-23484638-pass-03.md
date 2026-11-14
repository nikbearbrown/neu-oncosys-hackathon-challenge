# Professor Bear Audit: Identity Crisis: UI State Follow-Through

## Review Identity

This is an independent, provisional source-code audit for judge deliberation. It is not an official grade.

- Entry: `AravindKumar2504/identity-crisis-control-tower`
- Commit: `380760dc3b7b61097756f2b85c0f462feadc802c`
- Organizer reference: `6e15a399a64ffbf80778db0b462ac239e70086b9`
- Product: `cohort-control-tower`; Track 1, Cohort Firewall
- Pass: 3; reviewed 2026-11-14T20:31:38.600561+00:00
- Runtime: **not executed**; official freeze/receipt: **not verified**

## Executive Assessment

This focused pass corrects an overbroad earlier default claim and follows evidence identity through the browser. The callable assessment API defaults to strict missing-check handling, but the UI initializes allow_missing=True. The analysis cache, optional-summary cache and sign-off invalidation use narrower identities than the complete evidence they represent. These are source-level concerns requiring targeted session tests, not observed live-app failures. The receipt's stored evidence digests remain a real strength and are not alleged to be forged.

## Workflow Traced

The sidebar initializes its missing-check policy and selects a release and card. A cached analyze function reads release files and returns findings/readiness; its extra signature tracks card and tower-code modification times. Review state is retained under release label and card ID, while sign-off invalidation compares decisions, verdict and reviewer fields. Optional AI text is independently retained under the same release/card label pair. Streamlit's documented argument/source-based cache contract informs the cache inference: [official st.cache_data reference](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data), consulted November 14, 2026. No app or model was called.

## Findings At A Glance

| ID | Type | Priority | Finding |
|---|---|---|---|
| IC-07 | gap | P1 | The browser enables permissive missing-check handling by default |
| IC-08 | gap | P1 | The analysis cache signature omits release-file identity |
| IC-09 | gap | P1 | Sign-off invalidation does not compare the evidence digests |
| IC-10 | gap | P2 | The optional summary cache is keyed only by release label and card ID |
| IC-11 | strength | P2 | The AI citation caption accurately describes an ID-membership check |

## Inspection Scope

The following files informed the implementation-level conclusions in this pass. Other collected files are not automatically treated as reviewed:

- `app.py`
- `tower/checks/__init__.py`
- `tower/readiness.py`
- `tower/review.py`
- `tower/cards.py`
- `tower/ai_summary.py`
- `tests/test_ai_summary.py`
- `requirements.txt`

## Parallel Review Preservation

Existing reports were read and retained. This is a separately versioned supplement; prior conclusions are not silently replaced.

Correction to this reviewer's pass-01 IC-05 and its concise/native slide: the nondefault-development qualification applies to the callable API, not to the browser initialization. app.py explicitly turns the browser option on in a fresh session. The main REPORT.md's claim that the UI withdraws sign-off whenever its inputs change also needs the narrower interpretation below: its invalidation signature does not include the evidence digests. Earlier reports, decks and the parallel API-level default probe are preserved. The API-level probe is valid but does not establish the UI default. This supplement does not claim any existing built-in card necessarily has an unregistered check.

This pass does not accept earlier agents' findings as established merely because they were reported. Any correction must identify the earlier claim and the new evidence explicitly.

## Detailed Criterion Review

# Judge review aid: identity-crisis-control-tower

Repository: https://github.com/AravindKumar2504/identity-crisis-control-tower
Commit: `380760dc3b7b61097756f2b85c0f462feadc802c`
Track: 1
Reviewer: Professor Bear / Codex source review

**Not an official result. Source review does not establish runtime behavior.**

This focused pass corrects an overbroad earlier default claim and follows evidence identity through the browser. The callable assessment API defaults to strict missing-check handling, but the UI initializes allow\_missing=True. The analysis cache, optional-summary cache and sign-off invalidation use narrower identities than the complete evidence they represent. These are source-level concerns requiring targeted session tests, not observed live-app failures. The receipt&\#x27;s stored evidence digests remain a real strength and are not alleged to be forged.

## Coverage and limitations

Collection: complete_with_exclusions; 65 text files; 3 excluded entries; recursive tree truncated: False.
Runtime: not tested by this toolkit. Git blob identity and evidence line/quote consistency were checked.

Challenge reference: https://github.com/disleveK/oncosys-hackathon-challenge/tree/6e15a399a64ffbf80778db0b462ac239e70086b9

Product: cohort-control-tower

Product review route: Trace changes between releases to affected analyses, preserve unaffected analyses with reasons, and inspect findings.json in shared format v0.2. Equal row counts do not establish equal membership.

- Pinned local checkout, not a verified official final-submission receipt; branch names and later changes are outside this pass.
- Static source analysis only. No submission code, tests, installers, workflows, notebook, server, hosted endpoint or model was executed.
- No sealed envelopes, answer keys or raw clinical datasets were accessed. Numerical correctness, performance, accessibility and fresh-machine setup remain untested.
- Source-derived control-flow consequences are labeled as such. Proposed acceptance checks are not observed test results.
- The collected text budget is 160 files, 200 KB/file and 4 MB/entry. Complete\_with\_exclusions is not an exhaustive audit; exclusions and focused follow-ups are recorded.
- No official score, cross-team ranking, clinical validity or regulatory/accessibility certification is asserted.

## Priorities

- P1 · T1-3 · The analysis cache signature omits release-file identity: Pass a content-bound release manifest or immutable release-version identity into every cached analysis and board call. Show which version the result represents and invalidate all derived views together. A code/card timestamp signature should remain a separate policy-version input.
- P1 · T1-4 · The browser enables permissive missing-check handling by default: Make strict handling the initial browser default, or give permissive runs a distinct incomplete/development state that cannot be confused with ordinary readiness. Keep the disclosure and test the browser entry point separately from the core API.
- P1 · T1-6 · Sign-off invalidation does not compare the evidence digests: Build the live invalidation identity from the same canonical evidence/policy digests used in the receipt, alongside reviewer decisions. Preserve the old receipt as history and require a new decision for a changed evidence version. Exclude only documented nondeterministic display fields from canonicalization.
- P2 · T1-3 · The AI citation caption accurately describes an ID-membership check: Keep the scoped label and deterministic verdict as authoritative. Add evidence-version binding and targeted contradictory-number/negation cases before making any broader factual-validation claim.
- P2 · T1-7 · The optional summary cache is keyed only by release label and card ID: Bind the summary to a canonical digest of the exact context sent to the model. Invalidate or visibly mark old prose when context changes, retain its prior version if useful, and keep deterministic results available without a model.

## T1-1: Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support.

Status: **not_tested**

Core default unknown-check guards remain source-supported. A browser default can select different materiality, so entry-point coverage matters.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T1-2: Reasoning for the research question. Changes its result appropriately when the research question or intended use changes.

Status: **not_tested**

Card policy must be part of evidence identity, not just a stable card ID or verdict label. No new numerical performance result is asserted.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T1-3: Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion.

Status: **observed**

This pass follows provenance into caches, receipts and captions. The official Streamlit reference supports the cache inference; application consequences remain unexecuted.

### The analysis cache signature omits release-file identity

gap · P1 · Confidence: High for the inspected cache arguments and official cache contract; stale-result behavior has not been reproduced here.

inputs\_sig enumerates card YAML and tower Python paths with modification times, but not release data. analyze is decorated with st.cache\_data and receives the release path, card ID, missing-check option, that signature and optional custom-card JSON. Reading release bytes happens inside the cached body. Replacing data at the same path does not change the explicitly supplied data identity.

[Source lines 257–274](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L257-L274)

> def inputs\_sig\(\) -&gt; tuple:
>     &quot;&quot;&quot;Changes whenever a card or the tower code changes, so a cached verdict is never stale.&quot;&quot;&quot;
>     root = pathlib.Path\(\_\_file\_\_\).resolve\(\).parent
>     return tuple\(\(str\(p.relative\_to\(root\)\), p.stat\(\).st\_mtime\_ns\)
>                  for p in sorted\(\[\*root.glob\(&quot;cards/\*.yaml&quot;\), \*root.glob\(&quot;tower/\*\*/\*.py&quot;\)\]\)\)
> 
> 
> @st.cache\_data\(show\_spinner=False\)     \# the caller shows a spinner naming the release and question
> def analyze\(b\_path: str &\#124; None, card\_id: str, allow\_missing: bool, sig: tuple = \(\), card\_json: str = &quot;&quot;\):
>     card = json.loads\(card\_json\) if card\_json else load\_card\(card\_id\)   \# a question asked on screen has no file
>     a = load\_release\(RAW, &quot;release-A&quot;\)
>     if b\_path is None:
>         return None, assess\(card, a, allow\_missing=allow\_missing\), \[\], \[\]
>     b = load\_release\(b\_path\)
>     cmp = compare\(a, b\)
>     results, impact = rerun\(a, b, cmp.changes\)
>     findings = build\(cmp, results, impact\)
>     return findings, assess\(card, b, cmp, results, allow\_missing=allow\_missing\), membership\(cmp\), file\_summary\(cmp\)

[Source lines 277–292](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L277-L292)

> @st.cache\_data\(show\_spinner=&quot;Judging every question on this release...&quot;\)
> def board\(b\_path: str &\#124; None, allow\_missing: bool, sig: tuple = \(\), extra\_json: str = &quot;\[\]&quot;\) -&gt; list\[dict\]:
>     &quot;&quot;&quot;Every question card judged on the same release, so the screen can show that the verdict depends on the question.&quot;&quot;&quot;
>     a = load\_release\(RAW, &quot;release-A&quot;\)
>     rel, cmp, results = a, None, None
>     if b\_path is not None:
>         rel = load\_release\(b\_path\)
>         cmp = compare\(a, rel\)
>         results, \_ = rerun\(a, rel, cmp.changes\)
>     out = \[\]
>     for c in list\_cards\(\) + json.loads\(extra\_json\):
>         try:
>             d = assess\(c, rel, cmp, results, allow\_missing=allow\_missing\)
>             out.append\(\{&quot;id&quot;: c\[&quot;id&quot;\], &quot;title&quot;: c\[&quot;title&quot;\], &quot;short&quot;: c.get\(&quot;short\_title&quot;, c\[&quot;title&quot;\]\),
>                         &quot;verdict&quot;: d\[&quot;verdict&quot;\], &quot;reason&quot;: d\[&quot;reasons&quot;\]\[0\] if d\[&quot;reasons&quot;\] else &quot;&quot;,
>                         &quot;pending&quot;: len\(d.get\(&quot;pending\_checks&quot;\) or \[\]\)}\)

[Source lines 537–541](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L537-L541)

> b\_path = opts\[release\_label\]
> try:
>     with st.spinner\(f&quot;Checking \{release\_label} for \{card.get\(&\#x27;short\_title&\#x27;\) or card\[&\#x27;title&\#x27;\]}…&quot;\):
>         findings, ready, members, files = analyze\(b\_path, card\[&quot;id&quot;\], allow\_missing, inputs\_sig\(\),
>                                            json.dumps\(card\) if card\[&quot;id&quot;\].startswith\(&quot;custom-&quot;\) else &quot;&quot;\)

Supplemental rules: None cited; official criterion above applies.

Impact: Under the documented cache contract, unchanged arguments and source can reuse an earlier result even when a release file changed in place. This is conditional on path reuse and a retained cache; immutable per-run release directories avoid that condition. It is not evidence that the frozen baseline changed during judging.

Concrete change: Pass a content-bound release manifest or immutable release-version identity into every cached analysis and board call. Show which version the result represents and invalidate all derived views together. A code/card timestamp signature should remain a separate policy-version input.

Acceptance check: On invented data, run a comparison, replace one value at the same release path without changing code/cards, and rerun. The cached result must either refresh to the new input digest or explicitly refuse the changed immutable release. Retain an unchanged-input cache-hit control.

### The AI citation caption accurately describes an ID-membership check

strength · P2 · Confidence: High for checker and caption wording. The test file contains definitions, not this reviewer&\#x27;s observed test results, and no model was called.

The checker identifies unknown finding/sample references and whether the verdict word appears. The UI describes its result narrowly as an ID existing in this result, rather than claiming that all prose is factually verified. The system prompt separately tells the model to use only supplied facts and avoid clinical advice.

[Source lines 107–118](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/ai_summary.py#L107-L118)

> def check\(text: str, ready: dict, findings: dict &\#124; None\) -&gt; dict:
>     &quot;&quot;&quot;Every finding and sample id the text cites must be one the model was given: a release change that touches
>     this question, or a sample named in this question&\#x27;s results.&quot;&quot;&quot;
>     ctx = context\(ready, findings\)
>     known\_f = \{f\[&quot;id&quot;\] for f in ctx.get\(&quot;release\_changes\_that\_touch\_this\_question&quot;, \[\]\)}
>     known\_s = set\(SAMPLE.findall\(json.dumps\(ctx, default=str\)\)\)
>     cited\_f = sorted\(set\(FINDING.findall\(text\)\), key=lambda x: int\(x\[1:\]\)\)
>     cited\_s = sorted\(set\(SAMPLE.findall\(text\)\)\)
>     unknown = \[x for x in cited\_f if x not in known\_f\] + \[
>         s for s in cited\_s if s not in known\_s and not any\(k.startswith\(s + &quot;-&quot;\) for k in known\_s\)\]
>     states = bool\(re.search\(rf&quot;\\b\{re.escape\(ready\[&\#x27;verdict&\#x27;\]\)}\\b&quot;, text, re.I\)\)
>     return \{&quot;cited&quot;: len\(cited\_f\) + len\(cited\_s\), &quot;unknown&quot;: unknown, &quot;states\_verdict&quot;: states}

[Source lines 675–687](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L675-L687)

>         elif got:
>             st.markdown\(got\[&quot;text&quot;\]\)
>             bad, n = got\[&quot;citations&quot;\]\[&quot;unknown&quot;\], got\[&quot;citations&quot;\]\[&quot;cited&quot;\]
>             if bad:
>                 st.warning\(f&quot;The model cited \{plural\(len\(bad\), &\#x27;id&\#x27;\)} that this result doesn&\#x27;t contain: &quot;
>                            f&quot;\{&\#x27;, &\#x27;.join\(bad\)}. Don&\#x27;t rely on that part of the summary.&quot;\)
>             else:
>                 st.caption\(&quot;Citation check: it cites no finding or sample ids.&quot; if not n else
>                            &quot;Citation check: the one id it cites is in this result.&quot; if n == 1 else
>                            f&quot;Citation check: all \{n} finding and sample ids it cites are in this result.&quot;\)
>             if not got\[&quot;states\_verdict&quot;\]:
>                 st.caption\(f&quot;It doesn&\#x27;t use the verdict&\#x27;s own word \(\{ready\[&\#x27;verdict&\#x27;\]}\); the verdict above is the tool&\#x27;s.&quot;\)
>             st.caption\(f&quot;Written by \{got\[&\#x27;model&\#x27;\]} in \{got\[&\#x27;seconds&\#x27;\]:.0f} s.&quot;\)

[Source lines 28–36](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/ai_summary.py#L28-L36)

> SYSTEM = &quot;&quot;&quot;You write a short plain-English summary of a data-quality tool&\#x27;s results for a research data engineer.
> Rules:
> - Use only facts in the JSON you are given. Never add numbers, sample ids, causes or advice that are not in it.
> - Start with the verdict for the research question, using the exact verdict word.
> - Then say which release changes touch this question and why they matter. If none touch it, say so and explain the verdict from the reasons.
> - Cite only the finding ids listed under release\_changes\_that\_touch\_this\_question, in square brackets, like \[F1\]. Never put anything else in square brackets.
> - Then give the first next step and one thing the tool can&\#x27;t tell.
> - Write 4 to 6 sentences in one paragraph: no lists, no headings, no em dashes.
> - No diagnosis, treatment advice or clinical claims.&quot;&quot;&quot;

[Source lines 32–50](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tests/test_ai_summary.py#L32-L50)

>     def test\_a\_change\_that\_does\_not\_touch\_the\_question\_counts\_as\_unknown\(self\):
>         c = ai.check\(&quot;Conditional, because of \[F2\] and TCGA-E2-A1L7-01.&quot;, READY, FINDINGS\)
>         self.assertEqual\(c\[&quot;unknown&quot;\], \[&quot;F2&quot;, &quot;TCGA-E2-A1L7-01&quot;\]\)
> 
>     def test\_citations\_flag\_ids\_that\_are\_not\_in\_the\_results\(self\):
>         c = ai.check\(&quot;Conditional: \[F1\] swapped TCGA-A8-A09K-01 with TCGA-ZZ-0000-01, see \[F7\].&quot;, READY, FINDINGS\)
>         self.assertEqual\(c\[&quot;unknown&quot;\], \[&quot;F7&quot;, &quot;TCGA-ZZ-0000-01&quot;\]\)
>         self.assertEqual\(c\[&quot;cited&quot;\], 4\)
>         self.assertTrue\(c\[&quot;states\_verdict&quot;\]\)
> 
>     def test\_a\_patient\_level\_id\_counts\_as\_found\(self\):
>         self.assertEqual\(ai.check\(&quot;TCGA-A8-A09K was swapped.&quot;, READY, FINDINGS\)\[&quot;unknown&quot;\], \[\]\)
> 
>     def test\_summary\_strips\_thinking\_and\_checks\_it\(self\):
>         with mock.patch.object\(ai, &quot;ask&quot;, return\_value=\(&quot;&lt;think&gt;notes&lt;/think&gt;Conditional. \[F1\] matters.&quot;, &quot;fake&quot;\)\):
>             out = ai.summarize\(READY, FINDINGS\)
>         self.assertEqual\(out\[&quot;text&quot;\], &quot;Conditional. \[F1\] matters.&quot;\)
>         self.assertEqual\(out\[&quot;citations&quot;\], \{&quot;cited&quot;: 1, &quot;unknown&quot;: \[\]}\)
>         self.assertTrue\(out\[&quot;states\_verdict&quot;\]\)

Supplemental rules: None cited; official criterion above applies.

Impact: This appropriately limits what an automated citation check proves. Existing IDs and a verdict word do not validate numbers, negation or the meaning of a generated sentence, so the narrow caption is a strength worth preserving.

Concrete change: Keep the scoped label and deterministic verdict as authoritative. Add evidence-version binding and targeted contradictory-number/negation cases before making any broader factual-validation claim.

Acceptance check: With mocked responses, compare an unknown ID, a known ID with an unsupported numeric statement, and the wrong verdict embedded in a negation. Keep identity checks separate from semantic correctness and do not label all passing IDs as verified facts.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-4: Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review.

Status: **observed**

Correct the overbroad nondefault claim: the callable API is strict by default and the browser initializes permissive handling. Sign-off state must match current evidence.

### The browser enables permissive missing-check handling by default

gap · P1 · Confidence: High for initialization and call flow. The browser was not executed by this reviewer; an API-only default probe does not answer this UI question.

The sidebar sets st.session\_state.allow\_missing to True when the key is absent and passes that value into analyze and assess. With this option, an unregistered required check is unknown but nonmaterial. The callable assess and run\_checks signatures default to False. Thus the strict API default and permissive browser default are different source facts.

[Source lines 495–501](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L495-L501)

>     with st.expander\(&quot;Settings&quot;\):
>         st.caption\(&quot;How checks that aren&\#x27;t built yet are counted.&quot;\)
>         if &quot;allow\_missing&quot; not in st.session\_state:     \# the default lives here, so the toggle keeps its state by key
>             st.session\_state\[&quot;allow\_missing&quot;\] = True
>         allow\_missing = st.toggle\(&quot;List unbuilt checks as pending&quot;, key=&quot;allow\_missing&quot;,
>                                   help=&quot;On: a check that isn&\#x27;t built yet is listed as pending and doesn&\#x27;t decide the &quot;
>                                        &quot;verdict. Off: it counts as &\#x27;can&\#x27;t tell&\#x27;, the strict reading.&quot;\)

[Source lines 537–541](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L537-L541)

> b\_path = opts\[release\_label\]
> try:
>     with st.spinner\(f&quot;Checking \{release\_label} for \{card.get\(&\#x27;short\_title&\#x27;\) or card\[&\#x27;title&\#x27;\]}…&quot;\):
>         findings, ready, members, files = analyze\(b\_path, card\[&quot;id&quot;\], allow\_missing, inputs\_sig\(\),
>                                            json.dumps\(card\) if card\[&quot;id&quot;\].startswith\(&quot;custom-&quot;\) else &quot;&quot;\)

[Source lines 264–274](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L264-L274)

> @st.cache\_data\(show\_spinner=False\)     \# the caller shows a spinner naming the release and question
> def analyze\(b\_path: str &\#124; None, card\_id: str, allow\_missing: bool, sig: tuple = \(\), card\_json: str = &quot;&quot;\):
>     card = json.loads\(card\_json\) if card\_json else load\_card\(card\_id\)   \# a question asked on screen has no file
>     a = load\_release\(RAW, &quot;release-A&quot;\)
>     if b\_path is None:
>         return None, assess\(card, a, allow\_missing=allow\_missing\), \[\], \[\]
>     b = load\_release\(b\_path\)
>     cmp = compare\(a, b\)
>     results, impact = rerun\(a, b, cmp.changes\)
>     findings = build\(cmp, results, impact\)
>     return findings, assess\(card, b, cmp, results, allow\_missing=allow\_missing\), membership\(cmp\), file\_summary\(cmp\)

[Source lines 79–105](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/checks/__init__.py#L79-L105)

> def run\_checks\(release, card: dict, allow\_missing: bool = False\) -&gt; list\[Issue\]:
>     &quot;&quot;&quot;Run every check the card lists.
> 
>     A listed check that doesn&\#x27;t exist yet comes back as &\#x27;unknown&\#x27; \(material\), which makes the verdict Insufficient
>     Evidence: the honest answer when part of the question can&\#x27;t be judged. While checks are still being written,
>     allow\_missing=True lists them as pending without letting them decide the verdict.
>     &quot;&quot;&quot;
>     load\_all\(\)
>     out: list\[Issue\] = \[\]
>     for name in card.get\(&quot;checks&quot;, \[\]\):
>         fn = CHECKS.get\(name\)
>         if fn is None:
>             broken = &quot;; &quot;.join\(f&quot;\{k}.py: \{v}&quot; for k, v in LOAD\_ERRORS.items\(\)\)
>             out.append\(Issue\(id=name, title=f&quot;Check &\#x27;\{name}&\#x27; is not built yet&quot;
>                              + \(f&quot; \(or its file failed to load: \{broken}\)&quot; if broken else &quot;&quot;\), status=&quot;unknown&quot;,
>                              material=not allow\_missing, pre\_existing=False, numbers=\{&quot;pending&quot;: True},
>                              limitation=&quot;The tool cannot judge this part of the question yet.&quot;\)\)
>             continue
>         try:
>             got = fn\(release, card\)
>             if not isinstance\(got, list\) or not all\(isinstance\(x, Issue\) for x in got\):
>                 raise TypeError\(&quot;it must return a list of Issue objects&quot;\)
>             out.extend\(got\)
>         except Exception as e:      \# a broken check must never take the whole report down
>             out.append\(Issue\(id=name, title=f&quot;Check &\#x27;\{name}&\#x27; failed: \{e}&quot;, status=&quot;unknown&quot;, material=True,
>                              pre\_existing=False, limitation=&quot;The check crashed, so this part can&\#x27;t be judged.&quot;\)\)
>     return out

[Source lines 133–148](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L133-L148)

>     verdict, deciding = &quot;Ready&quot;, \[\]
>     for status, label in ORDER:
>         hits = \[x for x in material if x.status == status\]
>         if hits or \(status == &quot;warn&quot; and touching\):
>             verdict, deciding = label, hits
>             break
>     reasons = \[f&quot;\{x.title}.&quot; for x in deciding\]
>     if verdict == &quot;Conditional&quot; and touching:
>         reasons += \[\_touch\_reason\(t\) for t in touching\]
>     pending = \[x.id for x in issues if \(x.numbers or \{}\).get\(&quot;pending&quot;\) and not x.material\]
>     if verdict == &quot;Ready&quot;:
>         checked = \[x.id for x in issues if x.status == &quot;pass&quot;\]
>         reasons = \[f&quot;Nothing material found in the checks that ran \(\{&\#x27;, &\#x27;.join\(checked\) or &\#x27;none&\#x27;}\).&quot;
>                    + \(&quot; No release change touches what this question reads.&quot; if cmp else &quot;&quot;\)\]
>     if pending:
>         reasons.append\(f&quot;Not built yet, so not counted: \{&\#x27;, &\#x27;.join\(pending\)}.&quot;\)

Supplemental rules: None cited; official criterion above applies.

Impact: If a required check is unavailable, a fresh browser session can exclude it from the deciding material set unless the user changes Settings. The UI does disclose pending checks and its toggle meaning; this is an active default-policy concern, not a hidden setting or proof that every current card is incomplete.

Concrete change: Make strict handling the initial browser default, or give permissive runs a distinct incomplete/development state that cannot be confused with ordinary readiness. Keep the disclosure and test the browser entry point separately from the core API.

Acceptance check: In an authorized fresh-session test with a synthetic card requiring an unregistered check, inspect the initial toggle and resulting state. Compare the strict API, initial UI and explicit permissive opt-in. No ordinary approved result should conceal the pending requirement.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-5: Working tool and clear setup. Judges can run the core workflow from the submitted repository.

Status: **not_tested**

The proposed checks require an authorized fresh browser session with invented inputs and mocked models. This reviewer did not run the application or alter submitted code.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T1-6: Useful next steps. Suggested fixes are specific and match the size and importance of the problem.

Status: **observed**

Preserve prior receipts while invalidating their applicability to new evidence. A stored digest and a live applicability check are distinct controls.

### Sign-off invalidation does not compare the evidence digests

gap · P1 · Confidence: High for the missing fields in the invalidation signature and the Signed display predicate; no session-level reproduction was executed here.

signed stores findings and readiness digests in the receipt. The live UI&\#x27;s separate signature contains current repair/issue decisions, verdict, sign-off choice, note and reviewer fields, but no findings/readiness digest, input-file digest or complete card policy. It clears signed state only when that narrower signature changes, and the overview reports Signed whenever the retained signed object exists.

[Source lines 47–63](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L47-L63)

> def signed\(readiness\_doc: dict, findings\_doc: dict &\#124; None, repair\_dec: dict, issue\_dec: dict,
>            reviewer: str, role: str, decision: str, note: str\) -&gt; dict:
>     &quot;&quot;&quot;A copy of readiness.json with every review decision and the sign-off, fingerprinted.&quot;&quot;&quot;
>     doc = copy.deepcopy\(readiness\_doc\)
>     doc\[&quot;review&quot;\]\[&quot;items&quot;\] = \(
>         \[\{&quot;id&quot;: rid, &quot;type&quot;: &quot;repair&quot;, \*\*d, &quot;reviewer&quot;: reviewer, &quot;role&quot;: role} for rid, d in repair\_dec.items\(\)\]
>         + \[\{&quot;id&quot;: iid, &quot;type&quot;: &quot;issue&quot;, \*\*d, &quot;reviewer&quot;: reviewer, &quot;role&quot;: role} for iid, d in issue\_dec.items\(\)\]\)
>     inputs = \{&quot;release&quot;: doc\[&quot;release&quot;\], &quot;findings&quot;: \_digest\(findings\_doc\), &quot;readiness&quot;: \_digest\(readiness\_doc\)}
>     doc\[&quot;review&quot;\]\[&quot;signed\_off&quot;\] = \{&quot;by&quot;: reviewer, &quot;role&quot;: role, &quot;decision&quot;: decision, &quot;note&quot;: note, &quot;at&quot;: now\(\),
>                                    &quot;verdict\_at\_sign\_off&quot;: doc\[&quot;verdict&quot;\], &quot;inputs&quot;: inputs}
>     return doc
> 
> 
> def \_digest\(d: dict &\#124; None\) -&gt; str &\#124; None:
>     if d is None:
>         return None
>     return hashlib.sha256\(json.dumps\(d, sort\_keys=True, default=str\).encode\(\)\).hexdigest\(\)

[Source lines 575–588](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L575-L588)

> repairs = findings\[&quot;repairs&quot;\] if findings else \[\]
> required\_issues = list\(dict.fromkeys\(i for i in ready\[&quot;review&quot;\]\[&quot;required&quot;\] if not i.startswith\(&quot;F&quot;\)\)\)
> state\[&quot;repairs&quot;\] = collect\(&quot;rep&quot;, \[r\[&quot;id&quot;\] for r in repairs\]\)
> state\[&quot;issues&quot;\] = collect\(&quot;iss&quot;, required\_issues\)
> total = len\(repairs\) + len\(required\_issues\)
> decided = len\(state\[&quot;repairs&quot;\]\) + len\(state\[&quot;issues&quot;\]\)
> \# A sign-off covers exactly what was decided. If any decision, the verdict or the reviewer changes afterwards, the
> \# sign-off is withdrawn so the record can never disagree with the screen.
> signature = json.dumps\(\{&quot;repairs&quot;: \{k: \[v\[&quot;decision&quot;\], v\[&quot;reason&quot;\]\] for k, v in state\[&quot;repairs&quot;\].items\(\)},
>                         &quot;issues&quot;: \{k: \[v\[&quot;decision&quot;\], v\[&quot;reason&quot;\]\] for k, v in state\[&quot;issues&quot;\].items\(\)},
>                         &quot;verdict&quot;: ready\[&quot;verdict&quot;\], &quot;decision&quot;: st.session\_state.get\(dkey\),
>                         &quot;note&quot;: st.session\_state.get\(nkey\) or &quot;&quot;, &quot;reviewer&quot;: reviewer, &quot;role&quot;: role}, sort\_keys=True\)
> if state\[&quot;signed&quot;\] and state.get\(&quot;signed\_inputs&quot;\) \!= signature:
>     state\[&quot;signed&quot;\], state\[&quot;withdrawn&quot;\] = None, True

[Source lines 690–713](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L690-L713)

> def page\_overview\(\) -&gt; None:
>     n\_changes = len\(findings\[&quot;findings&quot;\]\) if findings else 0
>     signed\_by = state\[&quot;signed&quot;\]\[&quot;review&quot;\]\[&quot;signed\_off&quot;\]\[&quot;by&quot;\] if state\[&quot;signed&quot;\] else None
>     signed\_as = state\[&quot;signed&quot;\]\[&quot;review&quot;\]\[&quot;signed\_off&quot;\]\[&quot;decision&quot;\] if state\[&quot;signed&quot;\] else None
>     st.markdown\(&\#x27;&lt;div class=&quot;ct-intro&quot;&gt;&\#x27; + esc\(INTRO\) + &\#x27;&lt;/div&gt;&\#x27;, unsafe\_allow\_html=True\)
>     left, right = st.columns\(\[3, 2\], gap=&quot;medium&quot;\)
>     left.markdown\(f&quot;&quot;&quot;
> &lt;div class=&quot;ct-hero&quot; style=&quot;--c:\{colour}; --bg:\{tint}&quot;&gt;
>   &lt;div class=&quot;ct-eyebrow&quot; title=&quot;\{esc\(SECTION\_HELP\[&quot;verdict&quot;\]\)}&quot;&gt;Verdict for this question&lt;/div&gt;
>   &lt;div class=&quot;ct-verdict&quot; title=&quot;\{esc\(VERDICT\_HELP\[ready\[&\#x27;verdict&\#x27;\]\]\)}&quot;&gt;\{esc\(ready\[&\#x27;verdict&\#x27;\]\)}&lt;/div&gt;
>   &lt;div class=&quot;ct-q&quot;&gt;\{esc\(card\[&\#x27;title&\#x27;\]\)}&lt;/div&gt;
>   &lt;div class=&quot;ct-meta&quot;&gt;\{esc\(where\)} · \{ready\[&\#x27;group\_size&\#x27;\]} samples studied&lt;/div&gt;
>   &lt;div class=&quot;ct-sum&quot;&gt;\{esc\(headline\(\)\)}&lt;/div&gt;
> &lt;/div&gt;&quot;&quot;&quot;, unsafe\_allow\_html=True\)
>     kpis = \[   \# label, value, what it means in one plain line, state
>         \(&quot;Changes found&quot;, f&quot;\{n\_changes}&quot; if findings else &quot;n/a&quot;,
>          &quot;things that differ between the new data and release A&quot;, &quot;warn&quot; if n\_changes else &quot;done&quot;\),
>         \(&quot;Touch this question&quot;, f&quot;\{len\(touching\)}&quot; if findings else &quot;n/a&quot;,
>          &quot;of those, changes in data this question uses&quot;, &quot;warn&quot; if touching else &quot;done&quot;\),
>         \(&quot;Decisions&quot;, f&quot;\{decided} of \{total}&quot;,
>          &quot;flagged items a reviewer has approved, rejected or questioned&quot;, &quot;done&quot; if decided == total else &quot;warn&quot;\),
>         \(&quot;Sign-off&quot;, &quot;Signed&quot; if signed\_by else &quot;Pending&quot;,
>          f&quot;by \{signed\_by}: \{signed\_as}&quot; if signed\_by else &quot;whether a named reviewer has approved this result&quot;,
>          &quot;done&quot; if signed\_by else &quot;todo&quot;\),

[Source lines 1141–1153](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L1141-L1153)

>         if st.button\(&quot;Sign off&quot;, type=&quot;primary&quot;, disabled=not can\_sign\):
>             signed\_doc = signed\(ready, findings, state\[&quot;repairs&quot;\], state\[&quot;issues&quot;\], reviewer, role, decision, note\)
>             reviewed = with\_decisions\(findings, state\[&quot;repairs&quot;\], reviewer, role\) if findings else None
>             slug = re.sub\(r&quot;\[^A-Za-z0-9\]+&quot;, &quot;-&quot;, release\_label\).strip\(&quot;-&quot;\).lower\(\)
>             out = REPO / &quot;out&quot; / &quot;reviews&quot; / f&quot;\{card\[&\#x27;id&\#x27;\]}-\{slug}-\{now\(\).replace\(&\#x27;:&\#x27;, &\#x27;&\#x27;\)}&quot;
>             try:
>                 check = save\_review\(out, signed\_doc, reviewed, reviewed, CHALLENGE / &quot;format&quot; / &quot;validate.py&quot;\)
>             except Exception as e:
>                 st.error\(f&quot;Not signed off: \{e}&quot;\)
>             else:
>                 state\[&quot;signed&quot;\], state\[&quot;signed\_inputs&quot;\] = signed\_doc, signature
>                 state\[&quot;flash&quot;\] = \(f&quot;Signed off by \{reviewer} \(\{role}\): \{decision}. Saved in \{out.relative\_to\(REPO\)}&quot;, check\)
>                 st.rerun\(\)                           \# redraw so the header and the Overview show the sign-off

Supplemental rules: None cited; official criterion above applies.

Impact: A changed policy or refreshed evidence can retain the same verdict and decision IDs while differing from the evidence a reviewer signed. The saved old receipt still identifies its old evidence; the concern is associating that retained sign-off state with a newly displayed result. This narrows the earlier broad claim that any input change withdraws sign-off.

Concrete change: Build the live invalidation identity from the same canonical evidence/policy digests used in the receipt, alongside reviewer decisions. Preserve the old receipt as history and require a new decision for a changed evidence version. Exclude only documented nondeterministic display fields from canonicalization.

Acceptance check: Sign an invented result, then change a card&\#x27;s material policy or evidence while keeping verdict and decision IDs the same. After recomputation, the current result must be Pending or explicitly show that the retained signature covers an older version. The original receipt must remain unchanged.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-7: Communication. Someone without specialist knowledge can understand the result and next step.

Status: **observed**

Keep the narrow citation caption, but prevent stale optional prose from appearing to describe current results. No factual or clinical certification is implied.

### The optional summary cache is keyed only by release label and card ID

gap · P2 · Confidence: High for session key construction and reuse. Actual model behavior and UI refresh were not tested.

ai\_box retrieves generated text under ai&\#124;release\_label&\#124;card\_id and reuses it until the user requests another summary. That key excludes current findings, readiness, card policy and missing-check setting. The analysis path can recompute when those settings or card timestamps change, while the stored summary remains under the same key.

[Source lines 655–674](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L655-L674)

> def ai\_box\(\) -&gt; None:
>     &quot;&quot;&quot;Optional: a language model puts this result into plain words. The rules made the verdict; every id the model
>     cites is checked against the results it was given \(tower/ai\_summary.py\).&quot;&quot;&quot;
>     key = f&quot;ai&\#124;\{release\_label}&\#124;\{card\[&\#x27;id&\#x27;\]}&quot;
>     got = st.session\_state.get\(key\)
>     with st.expander\(&quot;AI summary \(optional\): this result in plain English&quot;, expanded=bool\(got\)\):
>         st.caption\(&quot;A language model rewrites this page&\#x27;s results in plain words. It reads the verdict, the reasons, &quot;
>                    &quot;the next steps and the release changes that touch this question, never the raw data files, and it &quot;
>                    f&quot;never makes the call: the rules above do. It runs on \{ai\_summary.backend\(\)}.&quot;\)
>         if st.button\(&quot;Write the summary&quot;, key=f&quot;ai\_go&\#124;\{card\[&\#x27;id&\#x27;\]}&quot;, icon=&quot;:material/auto\_awesome:&quot;\):
>             with st.spinner\(&quot;Writing the summary \(5 to 20 seconds on the local model\)...&quot;\):
>                 try:
>                     got = ai\_summary.summarize\(ready, findings, where\)
>                 except ai\_summary.ModelUnavailable as e:
>                     got = \{&quot;error&quot;: str\(e\)}
>                 except Exception as e:                       \# a model problem must never stop the screen
>                     got = \{&quot;error&quot;: f&quot;The summary failed \(\{type\(e\).\_\_name\_\_}\). The results above are unaffected.&quot;}
>             st.session\_state\[key\] = got
>         if got and got.get\(&quot;error&quot;\):
>             st.info\(got\[&quot;error&quot;\]\)

[Source lines 675–687](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L675-L687)

>         elif got:
>             st.markdown\(got\[&quot;text&quot;\]\)
>             bad, n = got\[&quot;citations&quot;\]\[&quot;unknown&quot;\], got\[&quot;citations&quot;\]\[&quot;cited&quot;\]
>             if bad:
>                 st.warning\(f&quot;The model cited \{plural\(len\(bad\), &\#x27;id&\#x27;\)} that this result doesn&\#x27;t contain: &quot;
>                            f&quot;\{&\#x27;, &\#x27;.join\(bad\)}. Don&\#x27;t rely on that part of the summary.&quot;\)
>             else:
>                 st.caption\(&quot;Citation check: it cites no finding or sample ids.&quot; if not n else
>                            &quot;Citation check: the one id it cites is in this result.&quot; if n == 1 else
>                            f&quot;Citation check: all \{n} finding and sample ids it cites are in this result.&quot;\)
>             if not got\[&quot;states\_verdict&quot;\]:
>                 st.caption\(f&quot;It doesn&\#x27;t use the verdict&\#x27;s own word \(\{ready\[&\#x27;verdict&\#x27;\]}\); the verdict above is the tool&\#x27;s.&quot;\)
>             st.caption\(f&quot;Written by \{got\[&\#x27;model&\#x27;\]} in \{got\[&\#x27;seconds&\#x27;\]:.0f} s.&quot;\)

[Source lines 537–541](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L537-L541)

> b\_path = opts\[release\_label\]
> try:
>     with st.spinner\(f&quot;Checking \{release\_label} for \{card.get\(&\#x27;short\_title&\#x27;\) or card\[&\#x27;title&\#x27;\]}…&quot;\):
>         findings, ready, members, files = analyze\(b\_path, card\[&quot;id&quot;\], allow\_missing, inputs\_sig\(\),
>                                            json.dumps\(card\) if card\[&quot;id&quot;\].startswith\(&quot;custom-&quot;\) else &quot;&quot;\)

[Source lines 50–66](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/ai_summary.py#L50-L66)

> def context\(ready: dict, findings: dict &\#124; None, release: str &\#124; None = None\) -&gt; dict:
>     &quot;&quot;&quot;The tool&\#x27;s own results for one question, as the screen shows them. No raw data, and only the release
>     changes that touch this question.&quot;&quot;&quot;
>     ctx = \{&quot;research\_question&quot;: ready\[&quot;card&quot;\]\[&quot;title&quot;\], &quot;release&quot;: release or ready\[&quot;release&quot;\]\[&quot;name&quot;\],
>            &quot;verdict&quot;: ready\[&quot;verdict&quot;\], &quot;reasons&quot;: list\(ready\[&quot;reasons&quot;\]\)\[:6\],
>            &quot;next\_steps&quot;: \[s\[&quot;step&quot;\] for s in ready.get\(&quot;next\_steps&quot;\) or \[\]\]\[:4\],
>            &quot;what\_the\_tool\_cant\_tell&quot;: list\(ready.get\(&quot;cannot\_tell&quot;\) or \[\]\)\[:3\]}
>     if findings:
>         touching = \{t\[&quot;finding&quot;\] for t in ready.get\(&quot;release\_changes&quot;\) or \[\]}
>         rel = \[f for f in findings\[&quot;findings&quot;\] if f\[&quot;id&quot;\] in touching\]
>         ctx\[&quot;release\_changes\_that\_touch\_this\_question&quot;\] = \[
>             \{&quot;id&quot;: f\[&quot;id&quot;\], &quot;kind&quot;: PLAIN.get\(f\[&quot;kind&quot;\], f\[&quot;kind&quot;\]\), &quot;severity&quot;: f\[&quot;severity&quot;\],
>              &quot;samples&quot;: \[e\[&quot;id&quot;\] for e in f\[&quot;evidence&quot;\] if e.get\(&quot;kind&quot;\) == &quot;sample&quot;\]\[:12\],
>              &quot;affects&quot;: f.get\(&quot;affects\_analyses&quot;\) or \[\], &quot;summary&quot;: f\[&quot;summary&quot;\]}
>             for f in rel\[:12\]\]
>         ctx\[&quot;release\_changes\_that\_do\_not\_touch\_this\_question&quot;\] = len\(findings\[&quot;findings&quot;\]\) - len\(rel\)
>     return ctx

[Source lines 121–131](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/ai_summary.py#L121-L131)

> def summarize\(ready: dict, findings: dict &\#124; None, release: str &\#124; None = None\) -&gt; dict:
>     &quot;&quot;&quot;Write the summary and check it. Raises ModelUnavailable when no model can be reached.&quot;&quot;&quot;
>     user = &quot;Results:\\n\`\`\`json\\n&quot; + json.dumps\(context\(ready, findings, release\), indent=1\) + &quot;\\n\`\`\`\\nWrite the summary.&quot;
>     t0 = time.time\(\)
>     text, model = ask\(SYSTEM, user\)
>     text = re.sub\(r&quot;&lt;think&gt;.\*?&lt;/think&gt;&quot;, &quot;&quot;, text, flags=re.S\).strip\(\)
>     if not text:
>         raise ModelUnavailable\(&quot;The model returned an empty answer. Try again.&quot;\)
>     c = check\(text, ready, findings\)
>     return \{&quot;text&quot;: text, &quot;model&quot;: model, &quot;seconds&quot;: time.time\(\) - t0,
>             &quot;citations&quot;: \{&quot;cited&quot;: c\[&quot;cited&quot;\], &quot;unknown&quot;: c\[&quot;unknown&quot;\]}, &quot;states\_verdict&quot;: c\[&quot;states\_verdict&quot;\]}

Supplemental rules: None cited; official criterion above applies.

Impact: Optional prose can describe an older result beside a newly recomputed verdict or reason. The UI&\#x27;s accurate citation-ID captions do not establish that cached prose belongs to the current evidence version. No stale model output or provider call was observed in this review.

Concrete change: Bind the summary to a canonical digest of the exact context sent to the model. Invalidate or visibly mark old prose when context changes, retain its prior version if useful, and keep deterministic results available without a model.

Acceptance check: Mock model output for one invented context, then change the missing-check policy or a card&\#x27;s reasons with the same release label and card ID. The old summary must disappear or carry an explicit old-version label until regenerated. No network call is required.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## Excluded scope

- .gitignore: non-allowlisted file type
- docs/Cohort-Control-Tower-pitch.pptx: file-size limit
- docs/demo.mp4: file-size limit

## Judge Follow-Up Sequence

1. Verify the official final commit and product declaration.
2. Start with the highest-priority synthetic acceptance checks above.
3. Follow one finding through evidence, affected versus unaffected analyses, proposed repair and human decision.
4. Verify the exported artifact against the organizer contract without reading sealed answers.
5. Record actual results separately from this static audit; revise only claims the new evidence supports.
