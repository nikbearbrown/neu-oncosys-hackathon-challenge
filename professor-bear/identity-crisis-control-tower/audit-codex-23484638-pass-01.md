# Professor Bear Audit: Identity Crisis Control Tower

## Review Identity

This is an independent, provisional source-code audit for judge deliberation. It is not an official grade.

- Entry: `AravindKumar2504/identity-crisis-control-tower`
- Commit: `380760dc3b7b61097756f2b85c0f462feadc802c`
- Organizer reference: `6e15a399a64ffbf80778db0b462ac239e70086b9`
- Product: `cohort-control-tower`; Track 1, Cohort Firewall
- Pass: 1; reviewed 2026-11-14T20:02:51.570691+00:00
- Runtime: **not executed**; official freeze/receipt: **not verified**

## Executive Assessment

This entry connects explicit research-question cards, material checks, evidence lineage and fingerprinted human review. The implementation is stronger than a generic file-difference dashboard, but unavailable validation still permits signed-file creation, optional calculation failures lose their error state, and displayed group counts need measured-value denominators. These are bounded source findings, with two separately attributed parallel helper reproductions; no clinical validity or official score is asserted.

## Workflow Traced

A question card declares intended use, cohort, fields, analyses and limitations. Registered checks return material issues; assessment combines these with relevant release changes and optional robustness/error-budget calculations. The output records rules, fields, sample references and file hashes. A reviewer records decisions and a signed copy tied to evidence digests; the save helper invokes the organizer validator when present and writes review artifacts.

## Findings At A Glance

| ID | Type | Priority | Finding |
|---|---|---|---|
| IC-01 | gap | P1 | Unavailable validation still permits signed review artifacts |
| IC-02 | gap | P2 | Optional calculation failure loses its evidence state |
| IC-03 | gap | P2 | Eligible group size and measured denominator need separate labels |
| IC-04 | strength | P2 | Question cards make materiality and intended use inspectable |
| IC-05 | strength | P2 | Unknown checks and empty measurements have explicit failure routes |
| IC-06 | strength | P2 | Review receipts bind the human decision to evidence fingerprints |

## Inspection Scope

The following files informed the implementation-level conclusions in this pass. Other collected files are not automatically treated as reviewed:

- `cards/er-alpha-by-er.yaml`
- `tower/readiness.py`
- `tower/checks/__init__.py`
- `tower/checks/coverage.py`
- `tower/analyses.py`
- `tower/review.py`
- `app.py`

## Parallel Review Preservation

Existing reports were read and retained. This is a separately versioned supplement; prior conclusions are not silently replaced.

REPORT.md and the updated TESTS.md were read and preserved. The parallel reviewer reports 81 submitted tests passed and 18 skipped, an absent-validator save reproduction and a controlled robustness-failure reproduction. Those are attributed observations, not tests executed by this reviewer. IC-01, IC-02 and IC-03 corroborate its sign-off, omission and denominator concerns. The documented allow_missing development bypass is not the default and is not described here as an unconditional production failure.

This pass does not accept earlier agents' findings as established merely because they were reported. Any correction must identify the earlier claim and the new evidence explicitly.

## Detailed Criterion Review

# Judge review aid: identity-crisis-control-tower

Repository: https://github.com/AravindKumar2504/identity-crisis-control-tower
Commit: `380760dc3b7b61097756f2b85c0f462feadc802c`
Track: 1
Reviewer: Professor Bear / Codex source review

**Not an official result. Source review does not establish runtime behavior.**

This entry connects explicit research-question cards, material checks, evidence lineage and fingerprinted human review. The implementation is stronger than a generic file-difference dashboard, but unavailable validation still permits signed-file creation, optional calculation failures lose their error state, and displayed group counts need measured-value denominators. These are bounded source findings, with two separately attributed parallel helper reproductions; no clinical validity or official score is asserted.

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

- P1 · T1-4 · Unavailable validation still permits signed review artifacts: Require an explicit True result for validated sign-off. If review without the validator is useful, emit a separately named, non-approved draft carrying validation\_status=unavailable and do not activate the normal signed success state.
- P2 · T1-1 · Unknown checks and empty measurements have explicit failure routes: Keep fail-explicit defaults and label development-bypass outputs as incomplete and non-approvable. Do not let consumers treat the nondefault bypass as equivalent to a complete checked run.
- P2 · T1-2 · Question cards make materiality and intended use inspectable: Retain explicit cards and version their policies with each export. Demonstrate how changing intended use changes a result while the underlying release remains fixed.
- P2 · T1-3 · Optional calculation failure loses its evidence state: Export separate applicable, attempted, succeeded, unavailable and failed states with bounded error details. Gate only claims that actually depend on that calculation, and keep unrelated checks usable.
- P2 · T1-6 · Review receipts bind the human decision to evidence fingerprints: Keep separate tool and reviewer decisions, retain evidence digests and add authenticated identity only if the deployment claims it. Preserve earlier receipts when a reviewer revises a decision.
- P2 · T1-7 · Eligible group size and measured denominator need separate labels: Preserve eligible counts if the organizer requires them and add measured and missing counts beside each estimate. Use measured counts where an evidence-adequacy rule specifically concerns observed values.

## T1-1: Finding data problems. Finds material data problems in the supplied input without reporting problems the data does not support.

Status: **observed**

Default unknown-check and empty-measurement guards are source-supported. Detector accuracy on unseen inputs remains outside this pass.

### Unknown checks and empty measurements have explicit failure routes

strength · P2 · Confidence: High for source defaults and guards; no runtime checks were performed in this source pass.

By default, an unregistered required check becomes material unknown, and a crashed check becomes material unknown with a limitation. A1 refuses duplicated relevant clinical IDs, missing or repeated ERALPHA rows, and a group with no measured values. allow\_missing=True is a documented nondefault development option that changes the missing-check materiality.

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

[Source lines 28–45](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/analyses.py#L28-L45)

> def run\_a1\(rel: Release\) -&gt; dict:
>     clinical, protein = \_clinical\(rel\), \_protein\(rel\)
>     er = clinical.set\_index\(&quot;sampleID&quot;\)\[ER\]
>     twice = set\(er.index\[er.index.duplicated\(\)\]\) &amp; \{str\(s\) for s in protein.columns}
>     if twice:                       \# the reference script can&\#x27;t run either: each id must have one ER status
>         raise ValueError\(f&quot;A1 cannot run: \{len\(twice\)} protein sample\(s\) appear on more than one clinical row &quot;
>                          f&quot;\(\{&\#x27;, &\#x27;.join\(sorted\(twice\)\[:3\]\)}\)&quot;\)
>     samples = \[s for s in protein.columns if sample\_type\(str\(s\)\) == &quot;01&quot; and er.get\(s\) in \(&quot;Positive&quot;, &quot;Negative&quot;\)\]
>     if &quot;ERALPHA&quot; not in protein.index or not samples:
>         raise ValueError\(&quot;A1 cannot run: the ERALPHA row or the ER-labelled primary tumors are missing&quot;\)
>     if int\(\(protein.index == &quot;ERALPHA&quot;\).sum\(\)\) &gt; 1:
>         raise ValueError\(&quot;A1 cannot run: the protein file has more than one ERALPHA row&quot;\)
>     vals = protein.loc\[&quot;ERALPHA&quot;, samples\]
>     groups = \{k: vals\[\[s for s in samples if er\[s\] == k\]\] for k in \(&quot;Positive&quot;, &quot;Negative&quot;\)}
>     empty = \[k for k, g in groups.items\(\) if int\(g.count\(\)\) == 0\]
>     if empty:
>         raise ValueError\(&quot;A1 cannot run: no ER-alpha value for the ER-&quot; + &quot; or ER-&quot;.join\(k.lower\(\) for k in empty\)
>                          + &quot; primary tumors&quot;\)

Supplemental rules: None cited; official criterion above applies.

Impact: The default path distinguishes missing evidence from a passing check and avoids manufacturing a numeric estimate for an empty measurement group. This strength coexists with the narrower optional-calculation omission in IC-02.

Concrete change: Keep fail-explicit defaults and label development-bypass outputs as incomplete and non-approvable. Do not let consumers treat the nondefault bypass as equivalent to a complete checked run.

Acceptance check: Omit a required registered check, induce a check error and create a zero-measurement group. Verify each names the uncertainty; compare the development option and confirm its output cannot be confused with fully assessed readiness.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-2: Reasoning for the research question. Changes its result appropriately when the research question or intended use changes.

Status: **observed**

Question cards and material lineage support task-specific reasoning. Policy validity, confidence intervals and sampling assumptions require statistical review.

### Question cards make materiality and intended use inspectable

strength · P2 · Confidence: High for the inspected card and lineage construction; cross-card numerical behavior remains untested here.

The A1 card states its descriptive research use, eligible group, target field, acceptable limitations, unacceptable identity problems and excluded clinical uses. Assessment selects material issues in its declared verdict order and attaches fields, rules, source references, row counts and file hashes to lineage.

[Source lines 1–22](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/cards/er-alpha-by-er.yaml#L1-L22)

> id: er-alpha-by-er
> title: ER-alpha protein in ER-positive vs ER-negative primary tumors \(A1\)
> short\_title: ER-alpha by ER \(A1\)
> intended\_use: A descriptive figure for a research report comparing mean ER-alpha protein \(RPPA\) between primary tumors that tested ER-positive and ER-negative in the clinic.
> group\_studied: Primary tumors \(sample type 01\) with protein data and a clinical ER status of Positive or Negative.
> outcome: Mean ER-alpha protein \(the ERALPHA row of protein\_rppa.tsv.gz\) in each ER group, and the difference between them.
> acceptable\_limitations: Up to 10% of primary tumors without a usable ER status, and a modest shift in which hospitals contributed samples, if both are reported.
> not\_acceptable: Any sample carrying another sample&\#x27;s protein data, or a profile counted twice.
> out\_of\_scope: Diagnosis, treatment advice, risk scores or any clinical claim about a patient.
> uses:
>   clinical.tsv: \[breast\_carcinoma\_estrogen\_receptor\_status\]
>   protein\_rppa.tsv.gz: \[ERALPHA\]
> group:
>   sample\_type: &quot;01&quot;
>   in\_files: \[protein\_rppa.tsv.gz\]
>   values:
>     breast\_carcinoma\_estrogen\_receptor\_status: \[Positive, Negative\]
> analyses: \[A1\]
> limits:
>   missing\_fraction: 0.10
>   site\_shift\_tvd: 0.15
> checks: \[inputs\_present, missing\_values, site\_shift\]

[Source lines 133–158](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L133-L158)

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
> 
>     files = \{f: release.content\_sha256.get\(f\) for f in \(card.get\(&quot;uses&quot;\) or \{}\) if release.has\(f\)}
>     lineage = \[\{&quot;conclusion&quot;: x.title, &quot;issue&quot;: x.id, &quot;status&quot;: x.status, &quot;rule&quot;: x.rule, &quot;source&quot;: x.source,
>                 &quot;fields&quot;: x.fields, &quot;rows&quot;: x.rows, &quot;row\_count&quot;: len\(x.rows\), &quot;numbers&quot;: x.numbers,
>                 &quot;files&quot;: \{f.split\(&\#x27;:&\#x27;\)\[0\]: files.get\(f.split\(&\#x27;:&\#x27;\)\[0\]\) for f in x.fields if f.split\(&\#x27;:&\#x27;\)\[0\] in files}}
>                for x in issues if x.material\]
>     lineage += \[\{&quot;conclusion&quot;: t\[&quot;summary&quot;\], &quot;finding&quot;: t\[&quot;finding&quot;\], &quot;status&quot;: &quot;warn&quot;, &quot;rule&quot;:
>                  &quot;A release change that touches what the question reads needs a person&\#x27;s review before use.&quot;,
>                  &quot;source&quot;: &quot;findings.json \(release comparison\)&quot;, &quot;fields&quot;: \[f&quot;\{t\[&\#x27;file&\#x27;\]}:\*&quot;\], &quot;rows&quot;: t\[&quot;samples&quot;\],
>                  &quot;row\_count&quot;: len\(t\[&quot;samples&quot;\]\), &quot;files&quot;: \{t\[&quot;file&quot;\]: files.get\(t\[&quot;file&quot;\]\)}} for t in touching\]

[Source lines 175–205](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L175-L205)

>     next\_steps = \[\{&quot;for&quot;: x.id, &quot;step&quot;: x.next\_step, &quot;evidence\_needed&quot;: x.evidence\_needed}
>                   for x in deciding if x.next\_step\]
>     if not next\_steps:                        \# no check named an action: say what evidence would settle it
>         next\_steps = \[\{&quot;for&quot;: x.id, &quot;step&quot;: &quot;Get &quot; + x.evidence\_needed\[:1\].lower\(\) + x.evidence\_needed\[1:\],
>                        &quot;evidence\_needed&quot;: x.evidence\_needed} for x in deciding if x.evidence\_needed\]
>     if verdict == &quot;Conditional&quot;:
>         next\_steps += \[\_touch\_step\(t\) for t in touching\]
>     review\_items = list\(dict.fromkeys\(\[x.id for x in material if x.status \!= &quot;pass&quot;\] + \[t\[&quot;finding&quot;\] for t in touching\]\)\)
>     \# What this result can&\#x27;t tell the user, shown under the verdict: the limits of the checks and changes behind it.
>     limits = \[x.limitation for x in deciding if x.limitation\] + \[CHANGE\_LIMITS.get\(t\[&quot;kind&quot;\], CHANGE\_LIMITS\[&quot;other&quot;\]\)
>                                                                  for t in touching\]
>     if robust:
>         limits.append\(&quot;Whether a systematic error such as a mislabelled ER test changed the result: the 95% range &quot;
>                       &quot;covers sampling variation only.&quot;\)
>     limits = limits or \[x.limitation for x in issues if x.material and x.limitation\]
>     cannot\_tell = list\(dict.fromkeys\(limits + \[GENERAL\_LIMIT\]\)\)\[:3\]
>     group\_ids = sorted\(card\_group\(release, card\)\)
>     doc = \{
>         &quot;card&quot;: \{k: card.get\(k\) for k in \(&quot;id&quot;, &quot;title&quot;, &quot;intended\_use&quot;, &quot;group\_studied&quot;, &quot;outcome&quot;,
>                                           &quot;acceptable\_limitations&quot;, &quot;not\_acceptable&quot;, &quot;out\_of\_scope&quot;\)},
>         &quot;release&quot;: \{&quot;name&quot;: release.name, &quot;files&quot;: files},
>         &quot;compared\_with&quot;: cmp.a.name if cmp else None,
>         &quot;group\_size&quot;: len\(group\_ids\),
>         &quot;group\_samples&quot;: group\_ids,
>         &quot;cannot\_tell&quot;: cannot\_tell,
>         &quot;verdict&quot;: verdict,
>         &quot;reasons&quot;: reasons,
>         &quot;summary&quot;: summary\(verdict, reasons, next\_steps, pending\),
>         &quot;issues&quot;: \[x.to\_dict\(\) &\#124; \{&quot;rows&quot;: x.rows\[:50\], &quot;row\_count&quot;: len\(x.rows\)} for x in issues\],
>         &quot;checked\_not\_material&quot;: \[x.id for x in issues if not x.material and not \(x.numbers or \{}\).get\(&quot;pending&quot;\)\],
>         &quot;pending\_checks&quot;: pending,

Supplemental rules: None cited; official criterion above applies.

Impact: A reviewer can relate a warning to the specific research task instead of receiving one context-free data-quality score. The policy choices remain prototype choices requiring human evaluation, not clinical standards.

Concrete change: Retain explicit cards and version their policies with each export. Demonstrate how changing intended use changes a result while the underlying release remains fixed.

Acceptance check: Use the same synthetic release with descriptive and training-oriented cards. Explain each difference using declared dependencies and limits, and verify exported lineage identifies the fields and policy behind the decision.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-3: Evidence and sources. Shows the checks, data fields, decision rules, and limitations behind each conclusion.

Status: **observed**

Lineage and file digests are strengths; optional calculation errors need explicit states instead of empty outputs.

### Optional calculation failure loses its evidence state

gap · P2 · Confidence: High for exception handling; the parallel review reports a controlled robustness fault, not an ordinary-data failure rate.

The conclusion calculation and error-budget calculation catch broad exceptions and replace their outputs with empty dictionaries. A conclusion issue is appended only when the robustness object is nonempty. The source therefore does not distinguish a calculation that failed from one that was inapplicable or absent in these fields.

[Source lines 108–131](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/readiness.py#L108-L131)

> def assess\(card: dict, release: Release, cmp: Comparison &\#124; None = None, results: dict &\#124; None = None,
>            allow\_missing: bool = False\) -&gt; dict:
>     issues = run\_checks\(release, card, allow\_missing=allow\_missing\)
>     touching = changes\_touching\(card, cmp\) if cmp else \[\]
>     robust = \{}
>     if &quot;A1&quot; in \(card.get\(&quot;analyses&quot;\) or \[\]\):
>         try:
>             robust = conclusion\(cmp if cmp else release, sorted\(\{s for t in touching for s in t\[&quot;samples&quot;\]}\)\)
>         except Exception:  \# the robustness readout must never break the verdict
>             robust = \{}
>         if robust:
>             issues.append\(\_conclusion\_issue\(robust, bool\(cmp\)\)\)
>     material = \[x for x in issues if x.material\]
>     eb = \{}
>     if set\(card.get\(&quot;analyses&quot;\) or \[\]\) &amp; \{&quot;A1&quot;, &quot;A2&quot;} and release.has\(&quot;clinical.tsv&quot;\):
>         try:                                     \# the error budget is context; it must never break the verdict
>             clin = \_clinical\(release\)
>             f1 = \(a1\_frames\(clin, \_protein\(release\)\) if &quot;A1&quot; in card\[&quot;analyses&quot;\] and release.has\(&quot;protein\_rppa.tsv.gz&quot;\)
>                   else None\)
>             c2 = \(clin\[clin.sampleID.str\[13:15\] == &quot;01&quot;\].dropna\(subset=\[PAM50\]\)\[PAM50\].value\_counts\(\).to\_dict\(\)
>                   if &quot;A2&quot; in card\[&quot;analyses&quot;\] else None\)
>             eb = error\_budget\(card, f1, c2, cmp, touching, clin.set\_index\(&quot;sampleID&quot;\)\[ER\].to\_dict\(\) if cmp else \{}\)
>         except Exception:
>             eb = \{}

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

Impact: Keeping optional context from crashing the workflow is sensible, but missing context cannot be interpreted correctly without an execution state and reason. This does not establish that normal inputs cause a crash or that every question must be blocked by an optional failure.

Concrete change: Export separate applicable, attempted, succeeded, unavailable and failed states with bounded error details. Gate only claims that actually depend on that calculation, and keep unrelated checks usable.

Acceptance check: Inject a controlled robustness error and a separate error-budget error in an authorized synthetic run. The output must identify each missing calculation and affected claim, while a non-applicable question remains explicitly not applicable.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-4: Safety and uncertainty. Avoids clinical claims, makes uncertainty visible, and requires human review.

Status: **observed**

Human sign-off is fingerprinted, but unavailable validation must remain distinct from validated approval. The development bypass is nondefault.

### Unavailable validation still permits signed review artifacts

gap · P1 · Confidence: High for helper and UI control flow; the retained parallel TESTS.md independently reports the helper-level missing-validator write.

validate returns None when the organizer validator is absent. save rejects only False and then writes readiness.signed.json and findings.reviewed.json for the None case too. The UI records the signed state after save returns normally. The returned message does disclose that findings were not checked: this is permissive policy, not a hidden assertion that validation ran.

[Source lines 103–115](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L103-L115)

> def validate\(doc: dict, validator: pathlib.Path\) -&gt; tuple\[bool &\#124; None, str\]:
>     &quot;&quot;&quot;Run the organizers&\#x27; validator: \(True, &quot;&quot;\), \(False, its message\), or \(None, why\) if it isn&\#x27;t there.&quot;&quot;&quot;
>     if not validator.exists\(\):
>         return None, &quot;the organizers&\#x27; validator wasn&\#x27;t found&quot;
>     with tempfile.TemporaryDirectory\(\) as tmp:
>         path = pathlib.Path\(tmp\) / &quot;findings.reviewed.json&quot;
>         path.write\_text\(json.dumps\(doc, indent=2\), encoding=&quot;utf-8&quot;\)
>         r = subprocess.run\(\[sys.executable, str\(validator\), str\(path\)\], capture\_output=True, text=True,
>                            encoding=&quot;utf-8&quot;, errors=&quot;replace&quot;\)
>         said = \(r.stdout or r.stderr or &quot;&quot;\).replace\(str\(path\), &quot;findings.reviewed.json&quot;\).strip\(\)
>     if r.returncode == 0:
>         return True, &quot;&quot;
>     return False, said or f&quot;it stopped with exit code \{r.returncode}&quot;

[Source lines 118–134](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L118-L134)

> def save\(out\_dir: pathlib.Path, signed\_doc: dict, reviewed: dict &\#124; None, findings\_doc: dict &\#124; None,
>          validator: pathlib.Path\) -&gt; str:
>     &quot;&quot;&quot;Validate the reviewed findings, then write the review files. Raises NotSaved if rejected.&quot;&quot;&quot;
>     check = &quot;&quot;
>     if reviewed is not None:
>         ok, said = validate\(reviewed, validator\)
>         if ok is False:
>             raise NotSaved\(f&quot;the organizers&\#x27; validator rejected findings.reviewed.json: \{said}&quot;\)
>         check = \(&quot;Organizers&\#x27; validator on findings.reviewed.json: valid&quot; if ok
>                  else f&quot;findings.reviewed.json was not checked: \{said}&quot;\)
>     record = record\_markdown\(signed\_doc, findings\_doc\)
>     out\_dir.mkdir\(parents=True, exist\_ok=True\)
>     write\_atomic\(out\_dir / &quot;readiness.signed.json&quot;, json.dumps\(signed\_doc, indent=2, default=str\)\)
>     write\_atomic\(out\_dir / &quot;review\_record.md&quot;, record\)
>     if reviewed is not None:
>         write\_atomic\(out\_dir / &quot;findings.reviewed.json&quot;, json.dumps\(reviewed, indent=2\)\)
>     return check

[Source lines 1136–1159](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/app.py#L1136-L1159)

>         overrules = ready\[&quot;verdict&quot;\] in \(&quot;Blocked&quot;, &quot;Insufficient Evidence&quot;\) and decision.startswith\(&quot;Approve&quot;\)
>         if overrules:
>             st.warning\(f&quot;The tool says \{ready\[&\#x27;verdict&\#x27;\]}. Approving overrules it, so the note must say why.&quot;\)
>         can\_sign = \(bool\(reviewer and role\) and not missing and not unexplained
>                     and not \(overrules and not \(note or &quot;&quot;\).strip\(\)\)\)
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
>     if state\[&quot;signed&quot;\]:
>         sd = state\[&quot;signed&quot;\]
>         msg, check = state.get\(&quot;flash&quot;, \(&quot;Signed off.&quot;, &quot;&quot;\)\)
>         st.success\(msg\)
>         if check:
>             st.caption\(check\)

Supplemental rules: None cited; official criterion above applies.

Impact: A downstream reader can encounter a signed artifact without the expected format-validation guarantee. A human signature and successful schema validation are different claims and should not be collapsed into one success state.

Concrete change: Require an explicit True result for validated sign-off. If review without the validator is useful, emit a separately named, non-approved draft carrying validation\_status=unavailable and do not activate the normal signed success state.

Acceptance check: With a missing validator, no validated signed artifact or success state should be created. Repeat with passing and rejecting validators, and inspect both files and UI state rather than the message alone.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-5: Working tool and clear setup. Judges can run the core workflow from the submitted repository.

Status: **not_tested**

The retained parallel review reports 81 passed and 18 skipped tests with environment limits. This reviewer did not run those tests or a deployed application.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. This pass does not establish runtime behavior or user comprehension.

## T1-6: Useful next steps. Suggested fixes are specific and match the size and importance of the problem.

Status: **observed**

Evidence-bound review records and evidence-needed next steps are useful. Persisting a record alone does not prove its schema was checked.

### Review receipts bind the human decision to evidence fingerprints

strength · P2 · Confidence: High for receipt construction; authentication, tamper-resistant storage and UI invalidation were not verified at runtime.

signed copies the readiness document, records repair and issue decisions, and includes reviewer, role, timestamp and digests of findings and readiness at sign-off. The Markdown record presents the tool verdict separately from the reviewer&\#x27;s decision. A digest detects content changes; it does not authenticate the named person.

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

[Source lines 66–80](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/review.py#L66-L80)

> def record\_markdown\(readiness\_doc: dict, findings\_doc: dict &\#124; None\) -&gt; str:
>     &quot;&quot;&quot;A human-readable record of the review, for the README, the demo or an email.&quot;&quot;&quot;
>     r, so = readiness\_doc\[&quot;review&quot;\], readiness\_doc\[&quot;review&quot;\]\[&quot;signed\_off&quot;\] or \{}
>     c = readiness\_doc\[&quot;card&quot;\]
>     lines = \[f&quot;\# Review record: \{c\[&\#x27;title&\#x27;\]}&quot;, &quot;&quot;,
>              f&quot;- Release: \{readiness\_doc\[&\#x27;release&\#x27;\]\[&\#x27;name&\#x27;\]}&quot; + \(f&quot; \(compared with \{readiness\_doc\[&\#x27;compared\_with&\#x27;\]}\)&quot;
>                                                                   if readiness\_doc.get\(&quot;compared\_with&quot;\) else &quot;&quot;\),
>              f&quot;- Tool verdict: \*\*\{readiness\_doc\[&\#x27;verdict&\#x27;\]}\*\*&quot;,
>              f&quot;- Signed off by: \{so.get\(&\#x27;by&\#x27;, &\#x27;\(not signed\)&\#x27;\)}, \{so.get\(&\#x27;role&\#x27;, &\#x27;&\#x27;\)}, at \{so.get\(&\#x27;at&\#x27;, &\#x27;&\#x27;\)}&quot;,
>              f&quot;- Reviewer&\#x27;s decision: \*\*\{so.get\(&\#x27;decision&\#x27;, &\#x27;\(none\)&\#x27;\)}\*\*&quot; + \(f&quot;. Note: \{so\[&\#x27;note&\#x27;\]}&quot; if so.get\(&quot;note&quot;\) else &quot;&quot;\),
>              &quot;&quot;, &quot;\#\# Decisions&quot;, &quot;&quot;, &quot;&\#124; Item &\#124; Type &\#124; Decision &\#124; Reason &\#124;&quot;, &quot;&\#124;---&\#124;---&\#124;---&\#124;---&\#124;&quot;\]
>     for it in r\[&quot;items&quot;\]:
>         lines.append\(f&quot;&\#124; \{it\[&\#x27;id&\#x27;\]} &\#124; \{it\[&\#x27;type&\#x27;\]} &\#124; \{it\[&\#x27;decision&\#x27;\]} &\#124; \{it.get\(&\#x27;reason&\#x27;, &\#x27;&\#x27;\)} &\#124;&quot;\)
>     lines += \[&quot;&quot;, &quot;\#\# Fingerprints of what was reviewed&quot;, &quot;&quot;\]
>     for f, h in \(readiness\_doc\[&quot;release&quot;\].get\(&quot;files&quot;\) or \{}\).items\(\):

Supplemental rules: None cited; official criterion above applies.

Impact: This is a useful basis for accountable handoff and distinguishes a human override from the tool&\#x27;s own verdict. Its value should be preserved while fixing the unavailable-validation policy.

Concrete change: Keep separate tool and reviewer decisions, retain evidence digests and add authenticated identity only if the deployment claims it. Preserve earlier receipts when a reviewer revises a decision.

Acceptance check: Sign a synthetic record, change one evidence field and compare its digest. Confirm the old receipt remains tied to the old evidence, the tool verdict is not rewritten as the human decision, and missing validation is visibly non-approved.

Next evidence/check: Demonstrate this criterion with authorized synthetic inputs and record the exact command, environment, input hashes, output and reviewer-observed result. Prioritize the acceptance checks attached to this criterion.

## T1-7: Communication. Someone without specialist knowledge can understand the result and next step.

Status: **observed**

Clarify eligible versus measured denominators and tool versus reviewer decisions. Fresh-user comprehension and accessibility remain untested.

### Eligible group size and measured denominator need separate labels

gap · P2 · Confidence: High for the count-versus-mean distinction; no missing-value fixture was executed by this reviewer.

A1 rejects a group with zero observed values, then computes means using Series.mean while reporting n\_positive and n\_negative using Series.size. With some missing values, size includes entries that do not contribute to the mean. This may preserve a reference-compatible eligible count, but it is not the measured denominator.

[Source lines 35–51](https://github.com/AravindKumar2504/identity-crisis-control-tower/blob/380760dc3b7b61097756f2b85c0f462feadc802c/tower/analyses.py#L35-L51)

>     samples = \[s for s in protein.columns if sample\_type\(str\(s\)\) == &quot;01&quot; and er.get\(s\) in \(&quot;Positive&quot;, &quot;Negative&quot;\)\]
>     if &quot;ERALPHA&quot; not in protein.index or not samples:
>         raise ValueError\(&quot;A1 cannot run: the ERALPHA row or the ER-labelled primary tumors are missing&quot;\)
>     if int\(\(protein.index == &quot;ERALPHA&quot;\).sum\(\)\) &gt; 1:
>         raise ValueError\(&quot;A1 cannot run: the protein file has more than one ERALPHA row&quot;\)
>     vals = protein.loc\[&quot;ERALPHA&quot;, samples\]
>     groups = \{k: vals\[\[s for s in samples if er\[s\] == k\]\] for k in \(&quot;Positive&quot;, &quot;Negative&quot;\)}
>     empty = \[k for k, g in groups.items\(\) if int\(g.count\(\)\) == 0\]
>     if empty:
>         raise ValueError\(&quot;A1 cannot run: no ER-alpha value for the ER-&quot; + &quot; or ER-&quot;.join\(k.lower\(\) for k in empty\)
>                          + &quot; primary tumors&quot;\)
>     return \{&quot;n\_samples&quot;: len\(samples\), &quot;sample\_ids&quot;: sorted\(samples\),
>             &quot;repeated\_ids&quot;: sorted\(set\(repeated\(header\_ids\(rel.path / &quot;protein\_rppa.tsv.gz&quot;\)\)\) &amp; set\(samples\)\),
>             &quot;n\_positive&quot;: int\(groups\[&quot;Positive&quot;\].size\), &quot;n\_negative&quot;: int\(groups\[&quot;Negative&quot;\].size\),
>             &quot;mean\_positive&quot;: round\(float\(groups\[&quot;Positive&quot;\].mean\(\)\), 3\),
>             &quot;mean\_negative&quot;: round\(float\(groups\[&quot;Negative&quot;\].mean\(\)\), 3\),
>             &quot;difference&quot;: round\(float\(groups\[&quot;Positive&quot;\].mean\(\) - groups\[&quot;Negative&quot;\].mean\(\)\), 3\)}

Supplemental rules: None cited; official criterion above applies.

Impact: Readers can overestimate the amount of measured evidence behind an estimate. The concern is incomplete count labeling, not that every mean is wrong or that the implementation accepts entirely empty measurement groups.

Concrete change: Preserve eligible counts if the organizer requires them and add measured and missing counts beside each estimate. Use measured counts where an evidence-adequacy rule specifically concerns observed values.

Acceptance check: Keep at least one measured value per ER group and blank several other values. Show eligible, measured and missing counts separately and identify which denominator drives each limit and interval.

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
