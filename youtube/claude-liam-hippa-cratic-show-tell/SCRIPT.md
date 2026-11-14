# HIPPA-cratic: Build And Cross-Check

Local Liam narration (Kokoro am_onyx). Promotional introduction; detailed audit remains separately available.

## BOPEN

HIPPA-cratic: Build And Cross-Check. By Team Hippa cratics. Sponsored by Northeastern SEIS, OncoSys AI, The Open Accelerator, and Red Hat.

## BIDEA

Hallo. This is Liam, in for Bear. This is the HIPPA-cratic team's Cohort Studio. It makes cohort construction explicit and offers a second way to check the result. The opportunity is to connect a readable workflow with independently inspectable computation.

## BDEFS

Three terms. Cohort means the group selected for a research question. Join grain means which entity each joined record represents. SQL check means a second computation of the same steps.

## B01

Define the steps, build the cohort, then cross-check the computation. The project distinguishes sample-level and patient-level joins. That helps expose situations where records multiply or become linked to the wrong sample.

## B02

Here is the actual application using its explicitly made-up sample, lab, and visit tables. We selected biopsy samples with a lab record from the same sample. The dropdown steps make that request visible without needing an AI service.

## B03

The cohort view shows what survives each step. This is a useful teaching and review feature: the researcher can see where membership changes rather than discovering a smaller final table without an explanation.

## B04

We ran the independent DuckDB SQL check. On this invented example, both computations returned the same sixteen samples, with matching counts after every step. That checks the implementation; the choice of research question and steps still needs human judgment.

## B10

The export retains steps, counts, release identity, and fingerprints. Those are strong ingredients for a reproducible record. The next step is making reconstruction enforce the same input identity that the record describes.

## B11

Bind caches and rebuild scripts to the recorded input contents. When a file changes at the same path, either refresh the computation or explain that the immutable release contract was broken. Keep counts and fingerprints on one snapshot.

## B12

Also distinguish an empty cohort from an unresolved question about the filter. Zero eligible records can be legitimate. A misspelled value needs a different explanation and a different next action.

## B13

Keep the strengths and make the boundaries more explicit. This is a research prototype, and a useful starting point for further development. The linked independent review contains the detailed evidence and remaining limitations.

## BVDT

Let's recap. Make the cohort steps inspectable. Keep sample and patient joins distinct. Cross-check the computation independently. Bind reconstruction to the recorded inputs.

## BHTF

Help me test HIPPA-cratic Cohort Studio with invented tables. Build one sample-level join and one patient-level join. Compare the engine with the SQL check, then change an input and explain what must be refreshed or rejected.

## BOUT

Thank you to the participants and sponsors: Northeastern SEIS, OncoSys AI, The Open Accelerator, and Red Hat. This is Liam, in for Bear.
