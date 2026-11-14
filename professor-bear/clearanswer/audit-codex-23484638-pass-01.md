# Professor Bear Audit: ClearAnswer Research Claim Auditor

## Review Identity

This is an independent, provisional source-code audit for judge deliberation. It is not an official grade.

- Entry: `GauravBohra2001/clearanswer`
- Commit: `7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8`
- Organizer reference: `6e15a399a64ffbf80778db0b462ac239e70086b9`
- Product: `research-claim-auditor`; Track 2, Evidence Navigator
- Pass: 1; reviewed 2026-11-14T21:33:17.492550+00:00
- Runtime: **not executed**; official freeze/receipt: **not verified**

## Executive Assessment

ClearAnswer is an Evidence Navigator / Research Claim Auditor, so this review uses the seven Track 2 criteria. Its source separates claim extraction, bounded tool queries, semantic scope checks, review and shared-format export. The most consequential gaps are at the handoff from computation to trusted verdict: a supported result can be assembled without a successful query, export unconditionally raises confidence to high, and a first-number tolerance shortcut can override a compound contradiction without checking every part. Manifest-driven answers also lack complete input fingerprint coverage, and malformed review objects can clear the human-review flag. These are inspected control-flow findings, not observed provider or browser failures. The review does not establish extraction recall, claim-verification accuracy, hosted usability or clinical validity.

## Workflow Traced

A Flask endpoint receives report text or extracts selectable PDF text, stores a per-job report and starts an orchestrator. The extractor asks a model for factual sentences and retains normalized substrings present in the input. For each retained claim, the verifier either applies a static cannot-answer topic rule or runs a bounded model/tool loop using schema, manifest and pandas query tools. It assembles a ClaimResult, applies tolerance and human-review heuristics, converts results to one claim_check finding per retained claim, and offers JSON/standalone HTML exports with browser-supplied review decisions. Model prompts request correct denominators and compound-claim checking; this audit separately examines which of those requests are enforced by code. No model or query was run.

## Findings At A Glance

| ID | Type | Priority | Finding |
|---|---|---|---|
| CA-01 | gap | P1 | A supported verdict does not require a successful computation |
| CA-02 | gap | P1 | Export replaces every confidence value with high |
| CA-03 | gap | P1 | The tolerance shortcut checks only the first number |
| CA-04 | gap | P1 | Manifest-based answers omit their manifests from file fingerprints |
| CA-05 | gap | P1 | Malformed review objects can clear the review requirement |
| CA-06 | strength | P2 | Queries use a bounded operation vocabulary with source metadata |
| CA-07 | strength | P2 | The interface preserves the tool verdict beside a human override |
| CA-08 | strength | P2 | Unsupported topics and incomplete verification have explicit evidence-gap paths |

## Inspection Scope

The following files informed the implementation-level conclusions in this pass. Other collected files are not automatically treated as reviewed:

- `README.md`
- `agents/base.py`
- `agents/extractor.py`
- `agents/orchestrator.py`
- `agents/verifier.py`
- `core/evidence.py`
- `core/guard.py`
- `core/loader.py`
- `core/data_model.py`
- `core/tolerance.py`
- `tools/data_tool.py`
- `tools/manifest_tool.py`
- `output.py`
- `app.py`
- `templates/index.html`

## Parallel Review Preservation

No earlier Markdown reports existed in this matching entry folder at the time this pass was prepared.

No earlier matching report existed in the local review tree when this source supplement was prepared. The original six entries and HIPPA-cratic work are preserved. Precomputed outputs, test_audit.json and raw/data-bearing material were conservatively excluded; they were not treated as observed successful runs. README statements about 16 data-model tests and valid exports are author claims, not executions in this review. In particular, deterministic helper tests do not by themselves validate the model/tool orchestration or export conversion. Official final-submission identity is not independently verified.

This pass does not accept earlier agents' findings as established merely because they were reported. Any correction must identify the earlier claim and the new evidence explicitly.

## Detailed Criterion Review

# Judge review aid: clearanswer

Repository: https://github.com/GauravBohra2001/clearanswer
Commit: `7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8`
Track: 2
Reviewer: Professor Bear / Codex source review

**Not an official result. Source review does not establish runtime behavior.**

ClearAnswer is an Evidence Navigator / Research Claim Auditor, so this review uses the seven Track 2 criteria. Its source separates claim extraction, bounded tool queries, semantic scope checks, review and shared-format export. The most consequential gaps are at the handoff from computation to trusted verdict: a supported result can be assembled without a successful query, export unconditionally raises confidence to high, and a first-number tolerance shortcut can override a compound contradiction without checking every part. Manifest-driven answers also lack complete input fingerprint coverage, and malformed review objects can clear the human-review flag. These are inspected control-flow findings, not observed provider or browser failures. The review does not establish extraction recall, claim-verification accuracy, hosted usability or clinical validity.

## Coverage and limitations

Collection: complete_with_exclusions; 31 text files; 20 excluded entries; recursive tree truncated: False.
Runtime: not tested by this toolkit. Git blob identity and evidence line/quote consistency were checked.

Challenge reference: https://github.com/disleveK/oncosys-hackathon-challenge/tree/6e15a399a64ffbf80778db0b462ac239e70086b9

Product: research-claim-auditor

Product review route: Trace report sentence to claim to calculation to human confirmation/override. Inspect audit.json in shared format with one claim\_check per claim, claim\_text, claim\_verdict and correct\_value where contradicted.

- Pinned local checkout, not a verified official final-submission receipt; branch names and later changes are outside this pass.
- Static source analysis only. No submission code, tests, installers, workflows, notebook, server, hosted endpoint or model was executed.
- No sealed envelopes, answer keys or raw clinical datasets were accessed. Numerical correctness, performance, accessibility and fresh-machine setup remain untested.
- Source-derived control-flow consequences are labeled as such. Proposed acceptance checks are not observed test results.
- The collected text budget is 160 files, 200 KB/file and 4 MB/entry. Complete\_with\_exclusions is not an exhaustive audit; exclusions and focused follow-ups are recorded.
- No official score, cross-team ranking, clinical validity or regulatory/accessibility certification is asserted.

## Priorities

- P1 · T2-1 · The tolerance shortcut checks only the first number: Represent numeric subclaims structurally, with measure, value, unit, population, denominator and a matching computed result. Apply tolerance to each matched pair and retain contradicted if any material subclaim fails. If matching is ambiguous, request review instead of upgrading the sentence. Keep exact counts and percentage-point/relative conventions distinct.
- P1 · T2-2 · A supported verdict does not require a successful computation: Require a successful, claim-relevant computation receipt before supported or contradicted. Bind tool arguments, resolved inputs, denominator and returned values to the claim and validate the final verdict against that receipt. Keep schema-only refusals as a separately labelled insufficient-evidence path. Model-declared but unqueried files should remain proposed sources, not executed evidence.
- P1 · T2-2 · Manifest-based answers omit their manifests from file fingerprints: Track every actually consumed file, including manifests, with its resolved path, role and content hash. Have manifest tools return explicit source and query metadata just as data\_query does. Distinguish release-specific measurements from shared baseline metadata and verify those identities on rerun.
- P1 · T2-4 · Export replaces every confidence value with high: Preserve tool confidence and its stated basis through export. If confidence in execution is a separate concept, expose it under a distinct field and keep evidence/interpretation uncertainty unchanged. Do not let format preparation increase epistemic confidence by default. Preserve enough provenance to explain any deliberate human reassessment.
- P1 · T2-4 · Malformed review objects can clear the review requirement: Validate the review payload before modifying findings: known finding IDs, explicit supported decisions, allowed replacement verdicts and an appropriate recorded reason for overrides. Preserve the original verdict and record actor/role as self-attested if this is a local prototype, with time and evidence identity. Invalid payloads should leave the review state unchanged. Do not impose a login service merely to repair these local semantics.
- P2 · T2-2 · Queries use a bounded operation vocabulary with source metadata: Retain this separation and expose the exact query/result receipt per claim. Extend the same metadata to manifest lookups and require receipt relevance before assigning a supported verdict. Test semantic field selection independently of arithmetic correctness.
- P2 · T2-3 · The interface preserves the tool verdict beside a human override: Preserve the original text and both verdicts. Add stable sentence/page offsets, explicit extraction omissions and validated decision metadata. Keep the same underlying evidence across summary and detailed views rather than generating independent narratives for each audience.
- P2 · T2-4 · Unsupported topics and incomplete verification have explicit evidence-gap paths: Retain the fail-incomplete paths, label schema-only evidence accurately and test static topic assumptions against authorized release schemas. Do not equate a regex match with a full clinical scope assessment. Preserve original confidence and review flags as in CA-02 and CA-05.

## T2-1: Decision usefulness. Helps the user make the decision in the scenario and clearly identifies the next step.

Status: **observed**

The audit queue aims to support a report-trust decision and supplies next-step fields. First-number tolerance and unverified supported paths can change that decision without adequate evidence. No claim-verification accuracy was measured.

### The tolerance shortcut checks only the first number

gap · P1 · Confidence: High for first-number extraction and unconditional whole-verdict promotion; actual extraction/model behavior remains untested.

check\_tolerance extracts the first number from the entire claim and the first number from correct\_value, determines percentage/approximation flags from the whole strings, and returns a tolerance note when that pair is close. \_build\_result uses any such note to replace a contradicted verdict with supported and severity none. This does not align values with the same measure, unit or denominator and does not verify the remaining subclaims. It conflicts with the verifier prompt&\#x27;s own worst-part-wins rule for compound sentences. The source permits a close first pair to mask a different contradicted part; no live erroneous audit was observed here.

[Source lines 21–34](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/tolerance.py#L21-L34)

> def extract\_first\_number\(text: str\) -&gt; Optional\[float\]:
>     &quot;&quot;&quot;Pull the first numeric value from a string.&quot;&quot;&quot;
>     m = \_NUMBER\_RE.search\(text\)
>     if m:
>         return float\(m.group\(\).replace\(&quot;,&quot;, &quot;&quot;\)\)
>     return None
> 
> 
> def is\_percentage\(text: str\) -&gt; bool:
>     return bool\(\_PERCENT\_RE.search\(text\)\)
> 
> 
> def is\_approximate\(text: str\) -&gt; bool:
>     return bool\(\_APPROX\_RE.search\(text\)\)

[Source lines 62–90](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/tolerance.py#L62-L90)

> def check\_tolerance\(
>     claim\_text: str,
>     correct\_value\_str: str,
> \) -&gt; Optional\[str\]:
>     &quot;&quot;&quot;Compare numbers in a claim against correct\_value.
> 
>     Returns a note string if values are within tolerance \(meaning
>     verdict should be &\#x27;supported&\#x27; not &\#x27;contradicted&\#x27;\), or None if
>     genuinely different.
>     &quot;&quot;&quot;
>     claimed\_num = extract\_first\_number\(claim\_text\)
>     actual\_num = extract\_first\_number\(correct\_value\_str\)
> 
>     if claimed\_num is None or actual\_num is None:
>         return None
> 
>     is\_pct = is\_percentage\(claim\_text\) or is\_percentage\(correct\_value\_str\)
>     is\_approx = is\_approximate\(claim\_text\)
> 
>     if within\_tolerance\(claimed\_num, actual\_num, is\_pct, is\_approx\):
>         if claimed\_num == actual\_num:
>             return None  \# Exact match, should not be contradicted anyway
>         return \(
>             f&quot;Claimed \{claimed\_num}\{&\#x27;%&\#x27; if is\_pct else &\#x27;&\#x27;} vs actual &quot;
>             f&quot;\{actual\_num}\{&\#x27;%&\#x27; if is\_pct else &\#x27;&\#x27;} - within &quot;
>             f&quot;\{&\#x27;approximate &\#x27; if is\_approx else &\#x27;&\#x27;}tolerance&quot;
>             f&quot;\{&\#x27; \(+/- 1.5pp / 5%\)&\#x27; if is\_approx else &\#x27; \(+/- 0.5pp\)&\#x27; if is\_pct else &\#x27;&\#x27;}. &quot;
>             f&quot;Treating as supported.&quot;
>         \)

[Source lines 431–440](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L431-L440)

>         \# Tolerance safety net: if Claude says contradicted but the numbers
>         \# are within rounding tolerance, upgrade to supported with a note.
>         if verdict == &quot;contradicted&quot; and correct\_value:
>             tolerance\_note = check\_tolerance\(claim\_text, correct\_value\)
>             if tolerance\_note:
>                 verdict = &quot;supported&quot;
>                 severity = &quot;none&quot;
>                 reasoning = f&quot;\{reasoning} \[Tolerance: \{tolerance\_note}\]&quot;
>                 if not limitation:
>                     limitation = tolerance\_note

[Source lines 49–64](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L49-L64)

> COMPOUND SENTENCES \(worst-part-wins rule\):
> A sentence can carry several numbers \(&quot;Of the 1,101 primary tumors in the
> release, 535 have survival, mutation, copy number, RNA and protein data&quot;\).
> Check EVERY number in the sentence. The sentence gets ONE verdict:
> - supported: every sub-claim matched the data within reasonable rounding.
> - contradicted: AT LEAST ONE sub-claim disagrees. correct\_value must list
>   what the data shows for the wrong sub-claim\(s\). If more than one is wrong,
>   list all of them, separated by &\#x27;; &\#x27;.
> 
> Verdict rules:
> - supported: every checkable part of the sentence agrees with the data.
> - contradicted: any part disagrees. You MUST provide correct\_value. For
>   distributional claims \(&quot;largest subtype at 62%&quot;\) include the correct share
>   AND the full distribution in correct\_value, e.g.
>   &\#x27;49.9% \(421 of 844\); full distribution: LumA 49.9%, LumB 22.7%, Basal 16.7%,
>    Her2 7.9%, Normal 2.7%&\#x27;.

Supplemental rules: None cited; official criterion above applies.

Impact: Approximate language is useful, but tolerance must apply to the relevant quantity. A multi-number sentence can contain a year, a total, a subgroup count and a percentage. A global first-number comparison can change the decision for the wrong reason and erase the contradiction the model had already identified.

Concrete change: Represent numeric subclaims structurally, with measure, value, unit, population, denominator and a matching computed result. Apply tolerance to each matched pair and retain contradicted if any material subclaim fails. If matching is ambiguous, request review instead of upgrading the sentence. Keep exact counts and percentage-point/relative conventions distinct.

Acceptance check: Use invented compound claims where an approximate first total is close but a later share is wrong, where a leading year is unrelated, and where counts and percentages differ in units. A genuine single-percentage rounding control may pass. Reordering sentence clauses must not change the verdict when the asserted facts are the same.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T2-2: Understanding the evidence. Users can move from summary to source evidence without losing context.

Status: **observed**

Bounded deterministic tools, source fields and report text pointers support drill-down. Unqueried evidence pointers and omitted manifest fingerprints weaken reproducibility; inspect actual calculation receipts rather than pointer counts.

### A supported verdict does not require a successful computation

gap · P1 · Confidence: High for the inspected branch ordering and evidence construction; no model call or mocked submission execution occurred in this pass.

The verifier accepts finalize\_verdict as soon as the model supplies it, without first requiring successful data or manifest queries. \_build\_result then permits supported with no evidence and creates an analysis pointer named model\_asserted\_match. Model-declared evidence filenames are also accepted even when no successful tool touched them. The ClaimResult contract only requires a nonempty evidence list, not proof of a relevant computation. A later guard marks sparse evidence for human review, which is useful, but does not change the supported verdict. Thus the source does not enforce the stated guarantee that every supported numerical result is backed by a deterministic calculation.

[Source lines 301–321](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L301-L321)

>             tool\_results\_block: list\[dict\] = \[\]
>             finalized = False
>             for tu in tool\_use\_blocks:
>                 name = tu.name
>                 tool\_input = tu.input or \{}
>                 if name == &quot;finalize\_verdict&quot;:
>                     final\_input = tool\_input
>                     with self.trace\_collector.start\_step\(self.name, &quot;interpret&quot;\) as step:
>                         step.input\_data = \{
>                             &quot;verdict&quot;: tool\_input.get\(&quot;verdict&quot;\),
>                             &quot;correct\_value&quot;: tool\_input.get\(&quot;correct\_value&quot;\),
>                         }
>                         step.output\_data = \_verdict\_summary\(tool\_input\)
>                         step.reasoning = tool\_input.get\(&quot;reasoning&quot;\) or &quot;&quot;
>                     tool\_results\_block.append\(\{
>                         &quot;type&quot;: &quot;tool\_result&quot;,
>                         &quot;tool\_use\_id&quot;: tu.id,
>                         &quot;content&quot;: &quot;Verdict recorded.&quot;,
>                     }\)
>                     finalized = True
>                     continue

[Source lines 455–467](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L455-L467)

>         elif verdict == &quot;supported&quot;:
>             if not evidence:
>                 \# output.py always prepends a claim pointer; use a distinct
>                 \# analysis marker here so the two do not duplicate on screen.
>                 evidence = \[Evidence\(kind=&quot;analysis&quot;, id=&quot;model\_asserted\_match&quot;\)\]
>             result = supported\(
>                 claim\_text=claim\_text,
>                 evidence=evidence,
>                 reasoning=reasoning,
>                 confidence=confidence,
>                 severity=severity or &quot;none&quot;,
>                 limitation=limitation,
>             \)

[Source lines 519–525](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L519-L525)

>         \# Any files the model explicitly cited but no successful tool touched.
>         for fname in declared\_files:
>             if \(&quot;file&quot;, fname\) not in seen:
>                 evidence.append\(Evidence\(kind=&quot;file&quot;, id=fname\)\)
>                 seen.add\(\(&quot;file&quot;, fname\)\)
> 
>         return evidence

[Source lines 86–94](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/evidence.py#L86-L94)

>         if self.claim\_verdict == &quot;contradicted&quot; and not self.correct\_value:
>             raise ValueError\(
>                 &quot;A contradicted claim requires a non-empty correct\_value &quot;
>                 &quot;\(e.g. &\#x27;49.9% \(421 of 844\)&\#x27;\).&quot;
>             \)
>         if self.claim\_verdict in \(&quot;supported&quot;, &quot;contradicted&quot;\) and not self.evidence:
>             raise ValueError\(
>                 f&quot;A \{self.claim\_verdict\!r} claim requires at least one evidence entry.&quot;
>             \)

[Source lines 107–113](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/guard.py#L107-L113)

>     if result.confidence == &quot;low&quot;:
>         result.needs\_human\_review = True
>     \# Raw verifier evidence of 1 means the model relied on a single tool call;
>     \# worth a human glance even if the verdict is otherwise clean.
>     if result.claim\_verdict in \(&quot;supported&quot;, &quot;contradicted&quot;\) and len\(result.evidence\) &lt; 2:
>         result.needs\_human\_review = True
>     return result

Supplemental rules: None cited; official criterion above applies.

Impact: A pointer-shaped record can satisfy structural validation while representing an assertion rather than execution. A reviewer needs to distinguish a tool result, a static scope rule and an unverified model statement before relying on a supported badge. This is a reachable source path, not evidence that a live model actually took it in the submitted demo.

Concrete change: Require a successful, claim-relevant computation receipt before supported or contradicted. Bind tool arguments, resolved inputs, denominator and returned values to the claim and validate the final verdict against that receipt. Keep schema-only refusals as a separately labelled insufficient-evidence path. Model-declared but unqueried files should remain proposed sources, not executed evidence.

Acceptance check: In an authorized follow-up using mock model responses and invented tool results, finalize supported before any query, after an errored query and after an unrelated successful query. All must remain unverified/Insufficient Evidence or explicitly awaiting review. A relevant successful numerical query is the positive control. Inspect the exported evidence type, not only its nonempty length.

### Manifest-based answers omit their manifests from file fingerprints

gap · P1 · Confidence: High for omitted files and tool metadata in the complete inspected functions; no manifest or raw dataset was opened.

ManifestTool computes cohort counts, layer availability and overlap from sample\_manifest.csv. TCGARelease can locate manifests outside the selected release directory. However, file\_checksums iterates only LAYER\_FILES, omitting sample\_manifest.csv and slide\_manifest.csv, and build\_audit\_json exports only that checksum mapping. ManifestTool results also omit a source\_file field, while the verifier&\#x27;s automatic file-evidence path expects one. The selected manifest can therefore materially determine an answer without receiving the same content-bound provenance as molecular/clinical layer files.

[Source lines 47–77](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/tools/manifest_tool.py#L47-L77)

>     def \_a\_count\_samples\(self, query: dict\) -&gt; dict:
>         sm = self.release.load\_layer\(&quot;sample\_manifest&quot;\)
>         st = query.get\(&quot;sample\_type&quot;\)
>         df = sm if not st else sm\[sm\[&quot;sample\_type&quot;\] == st\]
>         return \{
>             &quot;ok&quot;: True,
>             &quot;action&quot;: &quot;count\_samples&quot;,
>             &quot;sample\_type&quot;: st,
>             &quot;count&quot;: int\(len\(df\)\),
>             &quot;total\_in\_manifest&quot;: int\(len\(sm\)\),
>         }
> 
>     def \_a\_count\_with\_layers\(self, query: dict\) -&gt; dict:
>         sm = self.release.load\_layer\(&quot;sample\_manifest&quot;\)
>         st = query.get\(&quot;sample\_type&quot;, &quot;Primary Tumor&quot;\)
>         df = sm\[sm\[&quot;sample\_type&quot;\] == st\] if st else sm
>         layers = query.get\(&quot;layers&quot;\) or list\(ALL\_LAYER\_FLAGS\)
>         missing = \[col for col in layers if col not in df.columns\]
>         if missing:
>             raise KeyError\(f&quot;unknown layer flags: \{missing}&quot;\)
>         mask = df\[layers\[0\]\].astype\(bool\).copy\(\)
>         for col in layers\[1:\]:
>             mask &amp;= df\[col\].astype\(bool\)
>         return \{
>             &quot;ok&quot;: True,
>             &quot;action&quot;: &quot;count\_with\_layers&quot;,
>             &quot;sample\_type&quot;: st,
>             &quot;layers\_required&quot;: layers,
>             &quot;count&quot;: int\(mask.sum\(\)\),
>             &quot;denominator&quot;: int\(len\(df\)\),
>         }

[Source lines 56–72](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/loader.py#L56-L72)

>     def \_find\_manifest\_dir\(self\) -&gt; Path:
>         &quot;&quot;&quot;Walk up until we find a directory containing sample\_manifest.csv.&quot;&quot;&quot;
>         candidates = \[self.release\_dir.parent, self.release\_dir\]
>         \# Also try data/tcga-brca/ relative to the repo root.
>         for ancestor in self.release\_dir.parents:
>             if \(ancestor / &quot;sample\_manifest.csv&quot;\).exists\(\):
>                 return ancestor
>             \# Catch envelopes/opened/&lt;n&gt;/release/ → repo/data/tcga-brca/
>             cand = ancestor.parent.parent / &quot;data&quot; / &quot;tcga-brca&quot;
>             if cand.exists\(\) and \(cand / &quot;sample\_manifest.csv&quot;\).exists\(\):
>                 return cand
>         for c in candidates:
>             if \(c / &quot;sample\_manifest.csv&quot;\).exists\(\):
>                 return c
>         \# Fall back to release\_dir.parent even if missing - callers that need
>         \# manifests will get a clear FileNotFoundError.
>         return self.release\_dir.parent

[Source lines 206–213](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/loader.py#L206-L213)

>     def file\_checksums\(self\) -&gt; dict\[str, str\]:
>         &quot;&quot;&quot;SHA-256 of each layer file as downloaded \(for audit.json \`data\`\).&quot;&quot;&quot;
>         out: dict\[str, str\] = \{}
>         for name, fname in LAYER\_FILES.items\(\):
>             path = self.\_layer\_path\(name\)
>             if path.exists\(\):
>                 out\[fname\] = \_sha256\(path\)
>         return out

[Source lines 64–75](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/output.py#L64-L75)

>         &quot;data&quot;: \{
>             &quot;dataset&quot;: &quot;TCGA-BRCA&quot;,
>             &quot;releases&quot;: \[
>                 \{
>                     &quot;name&quot;: release\_name,
>                     &quot;files&quot;: \[
>                         \{&quot;file&quot;: fname, &quot;sha256&quot;: sha, &quot;hash\_of&quot;: &quot;file&quot;}
>                         for fname, sha in release.file\_checksums\(\).items\(\)
>                     \],
>                 }
>             \],
>         },

[Source lines 491–504](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L491-L504)

>         \# Every successful tool call that cites a source file becomes a file
>         \# evidence pointer, so a reviewer can retrace exactly what was queried.
>         for entry in tool\_history:
>             result = entry.get\(&quot;result&quot;\) or \{}
>             if not result.get\(&quot;ok&quot;\):
>                 continue
>             source = result.get\(&quot;source\_file&quot;\)
>             if source and \(ident := \(&quot;file&quot;, source\)\) not in seen:
>                 evidence.append\(Evidence\(
>                     kind=&quot;file&quot;,
>                     id=source,
>                     note=result.get\(&quot;query\_description&quot;\),
>                 \)\)
>                 seen.add\(ident\)

Supplemental rules: None cited; official criterion above applies.

Impact: A future reviewer may reproduce all listed layer hashes and still use a different manifest, yielding a different cohort denominator or availability answer. A release label or model-declared filename does not establish the exact external metadata bytes used. This is an input-identity gap, not proof that the frozen official manifest is incorrect.

Concrete change: Track every actually consumed file, including manifests, with its resolved path, role and content hash. Have manifest tools return explicit source and query metadata just as data\_query does. Distinguish release-specific measurements from shared baseline metadata and verify those identities on rerun.

Acceptance check: Use two invented manifests with identical layer files but different cohort membership or availability flags. The answer&\#x27;s provenance must differ, name the manifest and reproduce the correct denominator. Keep a same-manifest positive control and a missing-manifest explicit error.

### Queries use a bounded operation vocabulary with source metadata

strength · P2 · Confidence: High for the operation vocabulary and response fields; no numerical query was executed.

DataTool exposes enumerated layers and operations instead of asking the model to execute arbitrary Python. It validates known layers, dispatches the selected operation, reports errors explicitly, and attaches source\_file and query\_description. Value counts include total\_counted and row\_count, and group comparisons report measured sample sizes. These are useful ingredients for checking denominators and following the calculation rather than trusting prose alone. Their presence does not enforce the finalization boundary discussed in CA-01.

[Source lines 69–94](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/tools/data_tool.py#L69-L94)

>     def schema\(self\) -&gt; dict:
>         &quot;&quot;&quot;JSON schema for Anthropic tool\_use input\_schema.&quot;&quot;&quot;
>         return \{
>             &quot;type&quot;: &quot;object&quot;,
>             &quot;required&quot;: \[&quot;operation&quot;, &quot;layer&quot;\],
>             &quot;properties&quot;: \{
>                 &quot;operation&quot;: \{
>                     &quot;type&quot;: &quot;string&quot;,
>                     &quot;enum&quot;: \[&quot;count&quot;, &quot;filter&quot;, &quot;aggregate&quot;, &quot;value\_counts&quot;,
>                              &quot;describe&quot;, &quot;compare&quot;, &quot;unique&quot;\],
>                 },
>                 &quot;layer&quot;: \{&quot;type&quot;: &quot;string&quot;, &quot;enum&quot;: \_LAYER\_NAMES},
>                 &quot;column&quot;: \{&quot;type&quot;: &quot;string&quot;},
>                 &quot;columns&quot;: \{&quot;type&quot;: &quot;array&quot;, &quot;items&quot;: \{&quot;type&quot;: &quot;string&quot;}},
>                 &quot;where&quot;: \{&quot;type&quot;: &quot;object&quot;},
>                 &quot;filter&quot;: \{&quot;type&quot;: &quot;object&quot;},
>                 &quot;agg&quot;: \{
>                     &quot;type&quot;: &quot;string&quot;,
>                     &quot;enum&quot;: \[&quot;mean&quot;, &quot;sum&quot;, &quot;min&quot;, &quot;max&quot;, &quot;median&quot;, &quot;count&quot;\],
>                 },
>                 &quot;group\_by&quot;: \{&quot;type&quot;: &quot;string&quot;},
>                 &quot;primary\_only&quot;: \{&quot;type&quot;: &quot;boolean&quot;},
>                 &quot;dropna&quot;: \{&quot;type&quot;: &quot;boolean&quot;},
>                 &quot;limit&quot;: \{&quot;type&quot;: &quot;integer&quot;, &quot;minimum&quot;: 1, &quot;maximum&quot;: 1000},
>             },
>         }

[Source lines 98–125](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/tools/data_tool.py#L98-L125)

>     def execute\(self, query: dict\) -&gt; dict:
>         try:
>             op = query.get\(&quot;operation&quot;\)
>             layer = query.get\(&quot;layer&quot;\)
>             if not op:
>                 return self.\_err\(&quot;missing &\#x27;operation&\#x27;&quot;, query\)
>             if not layer:
>                 return self.\_err\(&quot;missing &\#x27;layer&\#x27;&quot;, query\)
>             if layer not in \_LAYER\_NAMES:
>                 return self.\_err\(
>                     f&quot;unknown layer \{layer\!r}; available: \{\_LAYER\_NAMES}&quot;, query
>                 \)
>             df = self.\_select\(layer, query\)
>             method = getattr\(self, f&quot;\_op\_\{op}&quot;, None\)
>             if method is None:
>                 return self.\_err\(f&quot;unknown operation \{op\!r}&quot;, query\)
>             result = method\(df, query\)
>             source = LAYER\_FILES.get\(layer, MANIFEST\_FILES.get\(layer, layer\)\)
>             return \{
>                 &quot;ok&quot;: True,
>                 &quot;operation&quot;: op,
>                 &quot;layer&quot;: layer,
>                 &quot;source\_file&quot;: source,
>                 &quot;query\_description&quot;: \_describe\(query\),
>                 \*\*result,
>             }
>         except Exception as e:  \# noqa: BLE001 - surfaced to the agent
>             return self.\_err\(f&quot;\{type\(e\).\_\_name\_\_}: \{e}&quot;, query\)

[Source lines 206–218](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/tools/data_tool.py#L206-L218)

>     def \_op\_value\_counts\(self, df: pd.DataFrame, query: dict\) -&gt; dict:
>         column = query\[&quot;column&quot;\]
>         if column not in df.columns:
>             raise KeyError\(f&quot;column \{column\!r} not in layer&quot;\)
>         dropna = bool\(query.get\(&quot;dropna&quot;, True\)\)
>         counts = df\[column\].value\_counts\(dropna=dropna\)
>         total = int\(counts.sum\(\)\)
>         return \{
>             &quot;result&quot;: \{str\(k\): int\(v\) for k, v in counts.items\(\)},
>             &quot;row\_count&quot;: int\(len\(df\)\),
>             &quot;total\_counted&quot;: total,
>             &quot;percent&quot;: \{str\(k\): round\(100 \* int\(v\) / total, 2\) for k, v in counts.items\(\)} if total else \{},
>         }

[Source lines 248–264](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/tools/data_tool.py#L248-L264)

>     def \_op\_compare\(self, df: pd.DataFrame, query: dict\) -&gt; dict:
>         column = query\[&quot;column&quot;\]
>         group\_by = query\[&quot;group\_by&quot;\]
>         agg = query.get\(&quot;agg&quot;, &quot;mean&quot;\)
>         if column not in df.columns:
>             raise KeyError\(f&quot;column \{column\!r} not in layer&quot;\)
>         if group\_by not in df.columns:
>             raise KeyError\(f&quot;group\_by \{group\_by\!r} not in layer&quot;\)
>         series = pd.to\_numeric\(df\[column\], errors=&quot;coerce&quot;\)
>         summary = \{}
>         for key, sub in series.groupby\(df\[group\_by\]\):
>             s = sub.dropna\(\)
>             summary\[str\(key\)\] = \{
>                 &quot;n&quot;: int\(s.size\),
>                 agg: \_num\(getattr\(s, agg\)\(\)\) if s.size else None,
>             }
>         return \{&quot;result&quot;: summary, &quot;row\_count&quot;: int\(series.notna\(\).sum\(\)\)}

Supplemental rules: None cited; official criterion above applies.

Impact: The source separates the model&\#x27;s query choice from the deterministic calculation, making a human audit possible. Typed operations and explicit errors reduce the ambiguity of an unconstrained code-execution agent.

Concrete change: Retain this separation and expose the exact query/result receipt per claim. Extend the same metadata to manifest lookups and require receipt relevance before assigning a supported verdict. Test semantic field selection independently of arithmetic correctness.

Acceptance check: With invented data, trace count, distribution and grouped comparison from requested filters through row\_count/total\_counted to the displayed answer. Unknown columns/layers must remain errors rather than guessed values. Confirm that each final claim points to the computation that actually supports it.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T2-3: Role fit. Gives technical and non-technical users the detail they need, based on the same evidence.

Status: **observed**

Summary/detail and original-versus-override views use the same finding records. No distinct role modes are required for this product; whether actual reviewers receive the right depth remains an unguided-use question.

### The interface preserves the tool verdict beside a human override

strength · P2 · Confidence: High for the inspected source-linking and verdict-preservation paths; no usability, extraction-recall or browser test was performed.

The extractor filters candidate claims to normalized substrings actually present in the report, reducing unsupported paraphrase pointers. The UI stores per-finding review state and shows the original and replacement verdicts side by side. The export helper also retains tool\_verdict when a reviewer touches a finding. This supports a summary-to-detail review workflow grounded in the report&\#x27;s words, although normalized substring matching does not establish complete sentence extraction or recall, and the review record still needs CA-05&\#x27;s validation.

[Source lines 92–102](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/extractor.py#L92-L102)

>             raw = \_first\_text\_block\(response\)
>             claims = \_parse\_claims\(raw\)
>             \# Keep only sentences the model actually quoted from the report.
>             \# Paraphrases would make later evidence pointers unreliable.
>             verified = \[c for c in claims if \_appears\_in\(report\_text, c\)\]
>             step.reasoning = \(
>                 f&quot;Model returned \{len\(claims\)} candidate sentences; &quot;
>                 f&quot;\{len\(verified\)} matched the report verbatim.&quot;
>             \)
>             step.output\_data = \{&quot;claims&quot;: verified}
>             return verified

[Source lines 141–151](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/extractor.py#L141-L151)

> def \_appears\_in\(report: str, sentence: str\) -&gt; bool:
>     &quot;&quot;&quot;True when the model&\#x27;s sentence is really a substring of the report.
> 
>     Whitespace is collapsed on both sides because Markdown wrapping often
>     inserts line breaks inside what logically reads as one sentence.
>     &quot;&quot;&quot;
>     norm\_report = re.sub\(r&quot;\\s+&quot;, &quot; &quot;, report\).strip\(\).lower\(\)
>     norm\_claim = re.sub\(r&quot;\\s+&quot;, &quot; &quot;, sentence\).strip\(\).lower\(\)
>     if not norm\_claim:
>         return False
>     return norm\_claim in norm\_report

[Source lines 1718–1738](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/templates/index.html#L1718-L1738)

>     // Apply styling for an override: both verdicts stay visible side by side
>     // so the reviewer can see what the tool said and what they chose instead.
>     function applyOverrideUI\(claim, newVerdict, reason, verdictStack, origBadge, acceptBtn, overrideBtn, needsBadge, body\) \{
>       // Strike the original and prepend an arrow + new badge.
>       origBadge.classList.add\(&\#x27;strike&\#x27;\);
>       // Clear anything added by a previous override attempt.
>       verdictStack.querySelectorAll\(&\#x27;.badge:not\(:first-child\), .arrow&\#x27;\).forEach\(n =&gt; n.remove\(\)\);
>       const arrow = document.createElement\(&\#x27;span&\#x27;\);
>       arrow.className = &\#x27;arrow&\#x27;;
>       arrow.textContent = &\#x27;\\u2192&\#x27;;
>       const newBadge = makeBadge\(newVerdict, true\);
>       verdictStack.appendChild\(arrow\);
>       verdictStack.appendChild\(newBadge\);
> 
>       overrideBtn.textContent = &\#x27;\\u270e Overridden&\#x27;;
>       overrideBtn.classList.add\(&\#x27;muted&\#x27;\);
>       acceptBtn.style.display = &\#x27;none&\#x27;;
>       if \(needsBadge\) needsBadge.remove\(\);
> 
>       const reasonLine = document.getElementById\(&\#x27;reason-&\#x27; + claim.id\);
>       if \(reasonLine\) reasonLine.textContent = reason ? &\#x27;Reason: &\#x27; + reason : &\#x27;&\#x27;;

[Source lines 442–453](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/app.py#L442-L453)

>         ov = override\_map.get\(fid\)
>         if ov:
>             finding\[&quot;tool\_verdict&quot;\] = verdict
>             decision = ov.get\(&quot;decision&quot;, &quot;accept&quot;\)
>             finding\[&quot;reviewer\_decision&quot;\] = decision
>             if decision == &quot;override&quot; and ov.get\(&quot;verdict&quot;\):
>                 finding\[&quot;claim\_verdict&quot;\] = ov\[&quot;verdict&quot;\]
>                 verdict = ov\[&quot;verdict&quot;\]
>             if ov.get\(&quot;reason&quot;\):
>                 finding\[&quot;reviewer\_reason&quot;\] = ov\[&quot;reason&quot;\]
>             \# A claim the reviewer touched no longer needs review.
>             finding\[&quot;needs\_human\_review&quot;\] = False

Supplemental rules: None cited; official criterion above applies.

Impact: Technical and nontechnical reviewers can distinguish the claim, the tool&\#x27;s conclusion and their own decision. Keeping both verdicts is specifically relevant to the Research Claim Auditor product and avoids silently presenting an override as the model&\#x27;s original answer.

Concrete change: Preserve the original text and both verdicts. Add stable sentence/page offsets, explicit extraction omissions and validated decision metadata. Keep the same underlying evidence across summary and detailed views rather than generating independent narratives for each audience.

Acceptance check: Use a short invented report with duplicate sentences, wrapped lines and a compound sentence. Verify each retained finding maps to its source span and compare accept/override displays with both export formats. Measure omitted/duplicated claims separately; a substring check alone does not establish complete coverage.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T2-4: Safety and uncertainty. Limitations and conflicts are visible; the interface avoids unsupported clinical conclusions.

Status: **observed**

Static cannot-answer and incomplete-verification paths are constructive. Export confidence promotion and weak review-payload validation can obscure those safeguards. No privacy breach, clinical validity or deployment-security certification is asserted.

### Export replaces every confidence value with high

gap · P1 · Confidence: High for the unconditional assignment and both export callers; no endpoint was exercised.

The internal finding conversion retains each ClaimResult confidence. The web export conversion then unconditionally sets every finding&\#x27;s confidence to high, including low-confidence budget-exhaustion results or model-asserted matches. The code comment attributes this policy to deterministic pandas computation, but CA-01 shows that not every accepted verdict requires such a computation. The same conversion feeds JSON and standalone HTML exports. A high confidence in a well-established inability to answer can be legitimate; the problem is replacing the original confidence without inspecting why it was low.

[Source lines 106–120](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/output.py#L106-L120)

>     finding: dict = \{
>         &quot;id&quot;: finding\_id,
>         &quot;kind&quot;: &quot;claim\_check&quot;,
>         &quot;summary&quot;: \_summary\_for\(result\),
>         &quot;severity&quot;: result.severity,
>         &quot;confidence&quot;: result.confidence,
>         &quot;evidence&quot;: \_build\_evidence\(result, finding\_id, release\_name, limitation\),
>         &quot;claim\_text&quot;: result.claim\_text,
>         &quot;claim\_verdict&quot;: verdict,
>         &quot;needs\_human\_review&quot;: bool\(result.needs\_human\_review\),
>     }
>     if result.correct\_value:
>         finding\[&quot;correct\_value&quot;\] = result.correct\_value
>     if limitation:
>         finding\[&quot;limitation&quot;\] = limitation

[Source lines 409–425](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/app.py#L409-L425)

> def \_prepare\_for\_submission\(audit: dict, overrides: list\[dict\] &\#124; None = None\) -&gt; dict:
>     &quot;&quot;&quot;Return a copy of the audit dict shaped for the judges&\#x27; checker.
> 
>     Changes vs the stored audit:
>     - drops the private \_trace key the shared format does not define
>     - applies reviewer accept/override decisions so the shipped verdict is
>       the one the human confirmed, while preserving the tool&\#x27;s original
>       verdict under tool\_verdict for provenance
>     - applies the submission severity policy to the FINAL verdict: high for
>       contradicted, medium for insufficient\_evidence, none for supported
>     - sets confidence to high on every finding, because the verdict comes
>       from a deterministic pandas computation, not from model sampling
>     - guarantees every finding carries at least one evidence entry, since
>       the schema requires it
>     &quot;&quot;&quot;
>     submission = copy.deepcopy\(audit\)
>     submission.pop\(&quot;\_trace&quot;, None\)

[Source lines 438–459](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/app.py#L438-L459)

>     for finding in submission.get\(&quot;findings&quot;, \[\]\):
>         fid = finding.get\(&quot;id&quot;\)
>         verdict = finding.get\(&quot;claim\_verdict&quot;, &quot;&quot;\)
> 
>         ov = override\_map.get\(fid\)
>         if ov:
>             finding\[&quot;tool\_verdict&quot;\] = verdict
>             decision = ov.get\(&quot;decision&quot;, &quot;accept&quot;\)
>             finding\[&quot;reviewer\_decision&quot;\] = decision
>             if decision == &quot;override&quot; and ov.get\(&quot;verdict&quot;\):
>                 finding\[&quot;claim\_verdict&quot;\] = ov\[&quot;verdict&quot;\]
>                 verdict = ov\[&quot;verdict&quot;\]
>             if ov.get\(&quot;reason&quot;\):
>                 finding\[&quot;reviewer\_reason&quot;\] = ov\[&quot;reason&quot;\]
>             \# A claim the reviewer touched no longer needs review.
>             finding\[&quot;needs\_human\_review&quot;\] = False
> 
>         finding\[&quot;severity&quot;\] = severity\_by\_verdict.get\(verdict, finding.get\(&quot;severity&quot;, &quot;none&quot;\)\)
>         finding\[&quot;confidence&quot;\] = &quot;high&quot;
>         if not finding.get\(&quot;evidence&quot;\):
>             finding\[&quot;evidence&quot;\] = \[\{&quot;kind&quot;: &quot;claim&quot;, &quot;id&quot;: finding.get\(&quot;claim\_text&quot;, &quot;&quot;\)\[:60\]}\]
>     return submission

[Source lines 348–373](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L348-L373)

>         if final\_input is None:
>             \# The model exhausted its budget without finalizing. Return a
>             \# defensive insufficient\_evidence verdict rather than crashing,
>             \# but keep pointers to whatever files the verifier DID check
>             \# before it ran out of steps. A reviewer needs to see what we
>             \# looked at, not just a bare &quot;budget\_exhausted&quot; marker.
>             partial\_evidence = self.\_build\_evidence\(tool\_history, declared\_files=\[\]\)
>             partial\_evidence.append\(
>                 Evidence\(
>                     kind=&quot;analysis&quot;,
>                     id=&quot;budget\_exhausted&quot;,
>                     note=\(
>                         f&quot;Verifier gave up after \{\_MAX\_STEPS} tool calls without &quot;
>                         f&quot;emitting finalize\_verdict. Evidence above lists the &quot;
>                         f&quot;files and queries it did run.&quot;
>                     \),
>                 \)
>             \)
>             fallback = insufficient\(
>                 claim\_text=claim\_text,
>                 reason=&quot;Verifier exhausted its reasoning budget without reaching a verdict.&quot;,
>                 confidence=&quot;low&quot;,
>                 evidence=partial\_evidence,
>             \)
>             fallback.reasoning = &quot;Verifier did not emit finalize\_verdict within the step budget.&quot;
>             return fallback

[Source lines 263–273](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/app.py#L263-L273)

>     overrides = None
>     body = request.get\_json\(silent=True\)
>     if isinstance\(body, dict\):
>         candidate = body.get\(&quot;overrides&quot;\)
>         if isinstance\(candidate, list\):
>             overrides = candidate
> 
>     audit = \_prepare\_for\_submission\(job\[&quot;result&quot;\], overrides=overrides\)
>     from html\_report import build\_html\_report
> 
>     html\_bytes = build\_html\_report\(audit\).encode\(&quot;utf-8&quot;\)

Supplemental rules: None cited; official criterion above applies.

Impact: An uncertainty signal shown during analysis can disappear from the artifact a reviewer circulates. Determinism of a calculation does not establish correct claim extraction, field selection, denominator, interpretation or complete evidence. The original trace is stripped from the submission copy, making this silent promotion harder to reconstruct from the exported artifact alone.

Concrete change: Preserve tool confidence and its stated basis through export. If confidence in execution is a separate concept, expose it under a distinct field and keep evidence/interpretation uncertainty unchanged. Do not let format preparation increase epistemic confidence by default. Preserve enough provenance to explain any deliberate human reassessment.

Acceptance check: Compare stored and exported findings for low/medium/high confidence, budget exhaustion, static cannot-answer, successful computation and unqueried supported cases. Confidence must remain faithful to its basis; JSON and HTML must agree. A reviewer override should retain both tool and reviewer confidence rather than rewriting history.

### Malformed review objects can clear the review requirement

gap · P1 · Confidence: High for the export helper and browser payload construction; API/UI behavior was not run.

The export helper indexes any dictionary containing a finding\_id. Any matching nonempty object is treated as a touched review: decision defaults to accept, arbitrary decision strings are retained, a replacement verdict is applied when supplied, and needs\_human\_review is set false. There is no decision-enum, allowed-verdict or required-reason validation before this state change. The ordinary UI also forwards an override reason even when blank and omits the browser timestamp from the export payload. The original tool verdict is retained, which is a useful control. This source finding is about review-state validation and record completeness, not demonstrated remote exploitation or a requirement for enterprise authentication.

[Source lines 432–458](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/app.py#L432-L458)

>     override\_map: dict\[str, dict\] = \{}
>     if overrides:
>         for o in overrides:
>             if isinstance\(o, dict\) and o.get\(&quot;finding\_id&quot;\):
>                 override\_map\[o\[&quot;finding\_id&quot;\]\] = o
> 
>     for finding in submission.get\(&quot;findings&quot;, \[\]\):
>         fid = finding.get\(&quot;id&quot;\)
>         verdict = finding.get\(&quot;claim\_verdict&quot;, &quot;&quot;\)
> 
>         ov = override\_map.get\(fid\)
>         if ov:
>             finding\[&quot;tool\_verdict&quot;\] = verdict
>             decision = ov.get\(&quot;decision&quot;, &quot;accept&quot;\)
>             finding\[&quot;reviewer\_decision&quot;\] = decision
>             if decision == &quot;override&quot; and ov.get\(&quot;verdict&quot;\):
>                 finding\[&quot;claim\_verdict&quot;\] = ov\[&quot;verdict&quot;\]
>                 verdict = ov\[&quot;verdict&quot;\]
>             if ov.get\(&quot;reason&quot;\):
>                 finding\[&quot;reviewer\_reason&quot;\] = ov\[&quot;reason&quot;\]
>             \# A claim the reviewer touched no longer needs review.
>             finding\[&quot;needs\_human\_review&quot;\] = False
> 
>         finding\[&quot;severity&quot;\] = severity\_by\_verdict.get\(verdict, finding.get\(&quot;severity&quot;, &quot;none&quot;\)\)
>         finding\[&quot;confidence&quot;\] = &quot;high&quot;
>         if not finding.get\(&quot;evidence&quot;\):
>             finding\[&quot;evidence&quot;\] = \[\{&quot;kind&quot;: &quot;claim&quot;, &quot;id&quot;: finding.get\(&quot;claim\_text&quot;, &quot;&quot;\)\[:60\]}\]

[Source lines 1808–1811](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/templates/index.html#L1808-L1811)

>       confirm.addEventListener\(&\#x27;click&\#x27;, \(e\) =&gt; \{
>         e.stopPropagation\(\);
>         handlers.onConfirm\(selected, reason.value.trim\(\)\);
>       }\);

[Source lines 2075–2086](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/templates/index.html#L2075-L2086)

>       try \{
>         // Pack reviewer decisions into the shape the backend expects.
>         const overrides = Object.entries\(reviewState\).map\(\(\[id, r\]\) =&gt; \{
>           const o = \{ finding\_id: id, decision: r.decision };
>           if \(r.verdict\) o.verdict = r.verdict;
>           if \(r.reason\)  o.reason  = r.reason;
>           return o;
>         }\);
>         const res = await fetch\(&\#x27;/api/export/&\#x27; + currentJobId, \{
>           method: &\#x27;POST&\#x27;,
>           headers: \{ &\#x27;Content-Type&\#x27;: &\#x27;application/json&\#x27; },
>           body: JSON.stringify\(\{ overrides }\),

[Source lines 209–221](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/app.py#L209-L221)

>     overrides = None
>     body = request.get\_json\(silent=True\)
>     if isinstance\(body, dict\):
>         candidate = body.get\(&quot;overrides&quot;\)
>         if isinstance\(candidate, list\):
>             overrides = candidate
> 
>     audit = \_prepare\_for\_submission\(job\[&quot;result&quot;\], overrides=overrides\)
>     OUTPUTS\_DIR.mkdir\(parents=True, exist\_ok=True\)
>     out\_path = OUTPUTS\_DIR / f&quot;audit-\{job\_id}.json&quot;
>     out\_path.write\_text\(json.dumps\(audit, indent=2\), encoding=&quot;utf-8&quot;\)
> 
>     valid, validator\_output = \_run\_validator\(out\_path\)

Supplemental rules: None cited; official criterion above applies.

Impact: A malformed client payload can be interpreted as a completed human decision, and an unexplained override can be difficult to audit after the browser session ends. Structural schema validation may catch an invalid claim\_verdict later, but it does not validate the added reviewer\_decision field or restore the cleared review state.

Concrete change: Validate the review payload before modifying findings: known finding IDs, explicit supported decisions, allowed replacement verdicts and an appropriate recorded reason for overrides. Preserve the original verdict and record actor/role as self-attested if this is a local prototype, with time and evidence identity. Invalid payloads should leave the review state unchanged. Do not impose a login service merely to repair these local semantics.

Acceptance check: Submit a finding-id-only object, an unknown decision, a blank-reason override, an invalid replacement verdict and a valid accept/override pair using invented audits. Invalid records must not clear needs\_human\_review. Verify both tool and final verdicts remain visible and that JSON and HTML export the same complete decision record.

### Unsupported topics and incomplete verification have explicit evidence-gap paths

strength · P2 · Confidence: High for the explicit fallback branches; no model response or clinical scenario was evaluated.

The verifier short-circuits topics matched by its semantic cannot-answer layer to insufficient\_evidence with a reason and labelled schema evidence. If the model never finalizes within the bounded loop, it returns low-confidence insufficient evidence with partial query pointers rather than manufacturing a numerical answer. The post-check marks low-confidence and sparse-evidence results for human review. These controls are explicit source behavior, but the topic dictionary is a static scope model and the export policy must preserve the resulting uncertainty.

[Source lines 239–265](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L239-L265)

>     def run\(self, claim\_text: str\) -&gt; ClaimResult:
>         \# Semantic-layer pre-check: if the claim&\#x27;s topic is in cannot\_answer
>         \# \(hormone therapy, treatment response, drug efficacy, causal claims\)
>         \# we short-circuit instead of burning tool calls. This is what turns
>         \# a 24-step fumble into a single decisive step.
>         blocked = check\_cannot\_answer\(claim\_text\)
>         if blocked:
>             with self.trace\_collector.start\_step\(self.name, &quot;plan&quot;\) as step:
>                 step.input\_data = \{&quot;claim&quot;: claim\_text}
>                 step.reasoning = \(
>                     f&quot;Semantic pre-check: claim matches cannot\_answer topic &quot;
>                     f&quot;&\#x27;\{blocked\[&\#x27;topic&\#x27;\]}&\#x27;. Skipping tool calls.&quot;
>                 \)
>                 step.output\_data = \{&quot;short\_circuit&quot;: True, &quot;topic&quot;: blocked\[&quot;topic&quot;\]}
>             with self.trace\_collector.start\_step\(self.name, &quot;interpret&quot;\) as step:
>                 step.input\_data = \{&quot;verdict&quot;: &quot;insufficient\_evidence&quot;}
>                 step.output\_data = \{
>                     &quot;verdict&quot;: &quot;insufficient\_evidence&quot;,
>                     &quot;confidence&quot;: &quot;high&quot;,
>                 }
>                 step.reasoning = blocked\[&quot;reason&quot;\]
>             return insufficient\(
>                 claim\_text=claim\_text,
>                 reason=blocked\[&quot;reason&quot;\],
>                 confidence=&quot;high&quot;,
>                 evidence=self.\_pre\_check\_evidence\(blocked\),
>             \)

[Source lines 348–373](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L348-L373)

>         if final\_input is None:
>             \# The model exhausted its budget without finalizing. Return a
>             \# defensive insufficient\_evidence verdict rather than crashing,
>             \# but keep pointers to whatever files the verifier DID check
>             \# before it ran out of steps. A reviewer needs to see what we
>             \# looked at, not just a bare &quot;budget\_exhausted&quot; marker.
>             partial\_evidence = self.\_build\_evidence\(tool\_history, declared\_files=\[\]\)
>             partial\_evidence.append\(
>                 Evidence\(
>                     kind=&quot;analysis&quot;,
>                     id=&quot;budget\_exhausted&quot;,
>                     note=\(
>                         f&quot;Verifier gave up after \{\_MAX\_STEPS} tool calls without &quot;
>                         f&quot;emitting finalize\_verdict. Evidence above lists the &quot;
>                         f&quot;files and queries it did run.&quot;
>                     \),
>                 \)
>             \)
>             fallback = insufficient\(
>                 claim\_text=claim\_text,
>                 reason=&quot;Verifier exhausted its reasoning budget without reaching a verdict.&quot;,
>                 confidence=&quot;low&quot;,
>                 evidence=partial\_evidence,
>             \)
>             fallback.reasoning = &quot;Verifier did not emit finalize\_verdict within the step budget.&quot;
>             return fallback

[Source lines 377–405](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/agents/verifier.py#L377-L405)

>     def \_pre\_check\_evidence\(self, blocked: dict\) -&gt; list\[Evidence\]:
>         &quot;&quot;&quot;Evidence for a cannot\_answer short-circuit.
> 
>         The pre-check didn&\#x27;t run any tools, but a reviewer still needs to see
>         what the semantic layer looked at and found lacking. We point at the
>         clinical and protein files \(the two that most topics would need\) plus
>         a schema-layer analysis pointer naming the blocked topic.
>         &quot;&quot;&quot;
>         topic = blocked.get\(&quot;topic&quot;, &quot;unknown&quot;\)
>         reason = blocked.get\(&quot;reason&quot;, &quot;&quot;\)
>         evidence = \[
>             Evidence\(
>                 kind=&quot;analysis&quot;,
>                 id=&quot;semantic\_pre\_check&quot;,
>                 note=f&quot;Topic &\#x27;\{topic}&\#x27; is in cannot\_answer. Reason: \{reason}&quot;,
>             \),
>             Evidence\(
>                 kind=&quot;file&quot;,
>                 id=LAYER\_FILES\[&quot;clinical&quot;\],
>                 note=&quot;Schema inspected; no matching column for the claimed topic.&quot;,
>             \),
>         \]
>         \# Protein-specific topics also benefit from naming the RPPA file,
>         \# even though we did not scan its rows.
>         if any\(k in topic.lower\(\) for k in \(&quot;protein&quot;, &quot;er-alpha&quot;, &quot;er alpha&quot;, &quot;hormone&quot;, &quot;response&quot;\)\):
>             evidence.append\(Evidence\(
>                 kind=&quot;file&quot;,
>                 id=LAYER\_FILES\[&quot;protein&quot;\],
>                 note=&quot;RPPA protein file available but carries no treatment-response data.&quot;,

[Source lines 99–113](https://github.com/GauravBohra2001/clearanswer/blob/7ede1f8fb84b6d23f3dba13a7c77688b32eab7b8/core/guard.py#L99-L113)

> def post\_check\(result: &quot;ClaimResult&quot;\) -&gt; &quot;ClaimResult&quot;:
>     &quot;&quot;&quot;Flag findings that warrant a human look.
> 
>     Sets needs\_human\_review on weak verdicts. We no longer stamp the limitation
>     field with an &quot;Auto-guard:&quot; prefix because the final finding is enriched
>     downstream \(see output.\_build\_evidence\) and adding the prefix here
>     duplicates or confuses a reviewer looking at the UI.
>     &quot;&quot;&quot;
>     if result.confidence == &quot;low&quot;:
>         result.needs\_human\_review = True
>     \# Raw verifier evidence of 1 means the model relied on a single tool call;
>     \# worth a human glance even if the verdict is otherwise clean.
>     if result.claim\_verdict in \(&quot;supported&quot;, &quot;contradicted&quot;\) and len\(result.evidence\) &lt; 2:
>         result.needs\_human\_review = True
>     return result

Supplemental rules: None cited; official criterion above applies.

Impact: Missing data and an incomplete reasoning process are distinguishable from a contradicted factual claim. This supports a safe research-auditing workflow, provided users can see what was not checked and export does not erase the limits.

Concrete change: Retain the fail-incomplete paths, label schema-only evidence accurately and test static topic assumptions against authorized release schemas. Do not equate a regex match with a full clinical scope assessment. Preserve original confidence and review flags as in CA-02 and CA-05.

Acceptance check: Use authorized invented unsupported-topic claims, a no-finalization mock, failed-query mocks and a normal successful calculation. Verify different reasons remain visible through UI, JSON and HTML, with no unsupported clinical conclusion and no claim that file rows were scanned when only schema metadata was used.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T2-5: Usability and accessibility. People can find what they need, understand the wording, and use the tool under time pressure.

Status: **not_tested**

Source includes progress, review controls and drill-down, but this reviewer ran no browser, keyboard, screen-reader, contrast, mobile or time-pressure task. The report-upload and export workflows need observed user checks.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T2-6: Working tool and clear setup. Judges can run and test the submitted experience.

Status: **not_tested**

README describes Flask/CLI setup and a provider key requirement. No installer, model call, submitted test, hosted endpoint, PDF parser or export validator was executed in this pass. Claimed helper tests do not establish orchestration correctness.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T2-7: Communication. The demo explains the problem, user, decision, and outcome clearly.

Status: **not_tested**

The README names the user, decision, workflow and export. This pass did not observe a demo; the inspected README contains a demo-video placeholder. Communicate the distinction between schema-valid output and a verified factual claim.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## Excluded scope

- .env.example: sensitive, data, sealed, or dependency path
- .gitignore: non-allowlisted file type
- ClearAnswer\_Architecture.png: file-size limit
- outputs/audit-2593b3f34f8f4466814a79de4f2bd201.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-5909e15e60204f9e8db757c5d2f85d1d.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-5b5a8d1a73384359a1895725124b1dfb.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-5da3143497a04b45a485a5a5262ad853.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-62c3930ad9d547b681dade89c481d480.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-63e824c4137644fcb3421acf5a92dae5.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-740801c3aa09477b97a275f141ef3f24.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-78edc7e4fa03425ca49699f66140cd49.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-7f4f1948f94646ed966d286496c43ac8.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-b8d7ae9e6b8b4ac19eed427be27b3659.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-bc91f2b3aa8b4217bd13921351fba607.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-bd86e25596da4c1eba74ad431684a97d.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-c736e2e8d1924c919a364827774fe2c2.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-dd6e56b975d747f6acb4bcc0ad349354.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-e4a3a0d51d59432eb66465c268a5bd3f.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- outputs/audit-ece5e8f570f6489f935e81890b80ba67.json: extra conservative exclusion: answer-bearing, precomputed or data-bearing artifact
- test\_audit.json: file-size limit

## Judge Follow-Up Sequence

1. Verify the official final commit and product declaration.
2. Start with the highest-priority synthetic acceptance checks above.
3. Follow one finding through evidence, affected versus unaffected analyses, proposed repair and human decision.
4. Verify the exported artifact against the organizer contract without reading sealed answers.
5. Record actual results separately from this static audit; revise only claims the new evidence supports.
