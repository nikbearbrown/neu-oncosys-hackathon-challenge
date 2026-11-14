# Rules for checking data quality, especially images and medical data

> Source: user-pasted checklist, 2026-11-14. Transcribed with Markdown headings,
> lists and tables; duplicated display-math artifacts normalized. Citation
> markers/URLs were not present in the pasted text. This is a separate source
> from the attached 72-rule rulebook. It is reference material, not new judging
> requirements or independently verified clinical guidance.

Good data are data whose fitness for a specific use has been demonstrated with evidence. The question is: Good enough for which task, for which people, in which setting, and with what remaining uncertainty? This idea of fitness for purpose underlies established data quality frameworks.

For image and medical datasets, several claims need separate checks:

- Integrity: The files and records are intact.
- Meaning: The values, pixels, measurements, and labels mean what we think they mean.
- Correspondence: Each observation belongs to the correct patient, specimen, examination, location, and time.
- Suitability: The data support the intended question and population.
- Independence: Evaluation is protected from duplication, leakage, and inappropriate dependencies.
- Governance: The intended use and sharing are authorized.
- Reproducibility: Someone can reconstruct the dataset and understand its limitations.

A dataset can satisfy some of these and fail others. A scan can display perfectly while being attached to the wrong patient. A laboratory value can be plausible while using the wrong units. An accurately recorded billing code can be an inadequate measure of disease.

The following is a proposed operating checklist, grounded in the cited standards and research. Acceptance thresholds should reflect the intended use and consequences of error.

## 1. Define “good” before inspecting the results

Write the exact question the data must support. “Detect visible lung nodules on adult chest CT” provides a testable purpose. “Build medical AI” leaves too many requirements undefined.

Define the intended population and setting. Specify relevant ages, conditions, geography, care setting, devices, acquisition practices, and period. Evidence from one setting supports claims about that setting until broader applicability is examined.

Define the unit of observation and the unit of inference. A row might represent a laboratory result; the conclusion might concern a patient. An image might be one slice from a scan. Preserve those relationships.

Specify when the information must be available. For prediction, define the decision time, lookback window, and outcome horizon. This determines which variables are legitimate inputs.

Identify consequential errors. Missing a small lesion, reversing laterality, assigning the wrong patient, and recording a harmless spelling variation have different consequences. Audit effort should reflect those differences.

Set acceptance criteria before reviewing favorable results. Define what triggers acceptance, investigation, restriction, or rejection. Record changes to those criteria and their rationale.

Specify unsupported uses. A dataset may support exploratory research while lacking evidence for screening, treatment selection, pediatric use, or deployment at new hospitals.

The IMDRF’s 2025 medical-device machine-learning principles explicitly connect intended use, representative data, suitable reference standards, and risk-proportionate evaluation. They provide a strong foundation for this planning step.

## 2. Establish provenance, identity, and structural integrity

Know where every data source came from. Record the institution or provider, collection process, acquisition dates, extraction dates, responsible owner, and original purpose.

Preserve controlled originals. Create processed versions through documented transformations. Keep enough lineage to explain how any accepted record or image was produced.

Maintain a manifest. Include stable identifiers, source locations, versions, relationships, and checksums where appropriate. A matching checksum establishes that bytes have not changed; it does not establish that the original information was correct.

Reconcile counts at every transition. Track expected, received, accepted, excluded, duplicated, and failed records. Account for losses during extraction, transfer, conversion, joining, and filtering.

Validate the schema. Check required fields, data types, allowed categories, date formats, coding-system versions, and required relationships. A numeric field containing text should produce an explicit failure.

Validate keys and joins. Check primary-key uniqueness and foreign-key integrity. Investigate joins that unexpectedly multiply rows, lose patients, or attach several incompatible labels to one observation.

Verify identity and correspondence. Audit whether the image, report, pathology result, label, and patient record actually belong together. Correct-looking identifiers can coexist with incorrect underlying links.

Find duplicates at several levels. Examine duplicate records, identical files, identical decoded pixels, repeated exports, and near-duplicates. Review candidates before removing them because legitimate repeated observations may be clinically meaningful.

Compare some records with their source. Schema checks cannot establish whether an extracted value accurately represents the original record. Trace sampled observations back through the pipeline.

The established clinical-data framework of conformance, completeness, and plausibility helps organize mechanical checks. It also distinguishes internal verification from validation against relevant external evidence. Both are needed.

## 3. Check measurement meaning, missingness, and plausibility

Create a data dictionary that explains meaning. For each variable, document its definition, source, unit, measurement method, timing, permitted values, missing-value conventions, and derivation.

Preserve original and standardized values. When converting units or mapping codes, retain the source representation and transformation. This makes incorrect mappings discoverable.

Keep missingness states distinct. “Not measured,” “not ordered,” “performed elsewhere,” “not extracted,” “not applicable,” and “unknown” represent different situations. None automatically means zero, normal, or negative.

Measure missingness within important groups. Calculate missingness by variable, patient, site, period, outcome, and relevant subgroup. A low overall rate can conceal a serious local failure.

Investigate the observation process. Ask why a test was ordered, why an image was acquired, and why follow-up occurred. Medical records reflect healthcare activity as well as patient health. Research has demonstrated that healthcare processes themselves can contribute substantial predictive information.

Separate abnormality from error. A value outside a clinical reference range may be the most important observation in the dataset. Distinguish impossible values, unusual but valid values, and documented measurement problems.

Use relationships to identify suspicious records. Check inconsistent dates, incompatible units, unexpected changes within a patient, and disagreement between related fields. Treat these as investigation flags when legitimate explanations are possible.

Preserve censored measurements. Values such as “less than 5” or “greater than 1,000” are bounded observations. Converting them into exact measurements changes their meaning.

Document imputation assumptions. Retain indicators of imputed values and examine sensitivity to the method. Filling empty cells does not establish that the missingness mechanism or resulting analysis is sound.

FDA guidance on electronic health records and claims data emphasizes assessing missing information, variable validity, and traceability in relation to the study question. Its methodological relevance extends beyond simple completeness percentages.

## 4. Apply image-specific integrity and content checks

Decode every accepted image and relevant frame. Checking extensions or reading headers is insufficient. Detect truncated files, unsupported encodings, incomplete animations or sequences, and failures in later frames.

Verify the pixel representation. Check dimensions, channels, numeric type, bit depth, signed versus unsigned values, and expected ranges. Detect unintended conversion of high-bit-depth data into a lower-information representation.

Interpret color and grayscale correctly. Check channel order, color transformations, orientation metadata, and display polarity. For example, DICOM MONOCHROME1 and MONOCHROME2 specify different grayscale display interpretations.

Distinguish original acquisitions from derivatives. Identify screenshots, thumbnails, compressed exports, crops, reconstructions, edited images, and synthetic images. Their evidentiary value may differ.

Check whether the required content is present. Verify the intended object, anatomy, field of view, view angle, and relevant context. A sharp image of the wrong region still fails the task.

Evaluate task-relevant image defects. Depending on the application, inspect blur, motion, noise, exposure, clipping, saturation, occlusion, compression artifacts, missing anatomy, and acquisition artifacts.

Set resolution requirements from the task. Determine whether the smallest relevant feature remains observable after acquisition and processing. A universal minimum pixel count is usually inadequate.

Use automated quality scores as screening tools. Blur, brightness, similarity, and noise measures can identify candidates for review. Establish whether their thresholds correspond to the defects that matter for the actual task.

Review images at an appropriate scale. Contact sheets support triage. Subtle findings may require full resolution, appropriate display settings, complete sequences, or orthogonal views.

Record quality flags and exclusion reasons. Investigate whether exclusions disproportionately remove particular patients, devices, sites, or difficult conditions expected in use.

AAPM’s medical-imaging guidance treats image quality and acquisition characteristics as task-dependent considerations. It also emphasizes understanding how collection and sampling choices affect the resulting evidence.

## 5. Add medical-imaging geometry and acquisition checks

Medical images contain spatial and measurement information that can be lost during apparently harmless conversions.

Verify physical geometry. Check orientation, laterality, image position, pixel spacing, voxel spacing, coordinate systems, and units.

Construct volumes using geometry and acquisition structure. Avoid relying solely on filenames or file order. Detect missing positions, duplicated slices, inconsistent orientations, and accidentally combined series or time points.

Distinguish slice thickness from slice spacing. DICOM defines nominal thickness separately from the center-to-center distance between slices. Substituting one for the other can corrupt measurements and reconstructed geometry.

Verify intensity meaning. For CT, inspect the required transformation from stored values to output units, including rescale slope and intercept. Confirm the output units before interpreting values as Hounsfield units.

Check image-to-annotation alignment in physical space. Matching array dimensions do not establish that a segmentation or region belongs in the correct location. Review overlays and coordinate transformations.

Inspect format conversions explicitly. For NIfTI, examine voxel dimensions and the qform and sform transformations. The official documentation warns that inconsistent handedness creates ambiguous left-right interpretation.

Record acquisition and equipment context. Retain the scanner or device, software version, protocol, and relevant quality-control information. These help explain differences between sites and changes over time.

A practical modality checklist should include:

| Data type | Additional checks to specify |
|---|---|
| CT | Contrast phase, reconstruction kernel, slice geometry, intensity conversion, truncation, metal artifacts |
| MRI | Sequence identity, acquisition parameters, contrast timing, motion, spatial alignment, intensity-processing method |
| Radiography | Projection and view, laterality, positioning, exposure, portable versus fixed acquisition |
| Ultrasound | Anatomy and view, scale, acquisition settings, frame or cine completeness, measurement overlays |
| Digital pathology | Specimen and slide identity, stain, focus, tissue folds, scanner, physical scale, patch location |
| Retinal or skin images | Anatomical location, laterality where applicable, focus, illumination, color handling, scale, acquisition device |

The table is a starting point for a modality-specific protocol. Qualified imaging experts should determine which defects prevent the intended interpretation.

## 6. Check the clinical meaning of medical records

Separate clinical concepts from their recorded proxies. A diagnosis code, suspected condition, historical condition, billing entry, and confirmed diagnosis can require different interpretations.

Distinguish medication events. Prescribed, dispensed, administered, discontinued, and patient-reported medication use are separate events. Select the one required by the question.

Match laboratory observations by more than their display names. Check analyte, specimen, measurement property, timing, scale, and method. LOINC explicitly represents these components because they help define what was measured.

Separate clinical time from information-availability time. A specimen collected at 9:00 may produce a result available at 11:00. A prediction made at 10:00 cannot use that result merely because the collection preceded it. FHIR distinguishes the clinically relevant observation time from the time a result version became available.

Interpret clinical text with its context. Audit negation, uncertainty, historical mentions, family history, copied text, and references to other patients or body sites. Searching for a disease term alone does not establish a positive finding.

Define observation and follow-up windows. A missing recorded readmission, diagnosis, or death may reflect incomplete follow-up or care outside the system. Represent unresolved outcomes appropriately.

Match evidence to the correct clinical target. Confirm that pathology refers to the relevant specimen or lesion, and that imaging and laboratory results occur within a clinically appropriate interval.

Examine proxy targets for systematic distortion. Healthcare spending may reflect access and utilization as well as illness. A major study found racial bias when a health-management algorithm used cost as a proxy for health need.

Match the study design to the conclusion. Data adequate for describing associations or predicting outcomes may not support conclusions about treatment effects. Confounding, selection, and treatment timing require separate methodological assessment.

## 7. Treat labels and annotations as evidence that needs checking

Define a reference standard. Document how the target condition is established and why that method supports the intended claim. CLAIM 2024 recommends the term “reference standard,” acknowledging that biomedical labels can have limitations.

Match label granularity to the prediction. A patient-level cancer diagnosis does not establish that every examination, slice, patch, or pixel contains visible cancer.

Keep uncertain labels explicit. Distinguish positive, negative, uncertain, unassessable, unverified, and missing. Establish how each category will be used.

Write an annotation protocol. Include definitions, inclusion rules, boundary cases, examples, and instructions for ambiguity. For segmentation, define exactly which structures and boundaries count.

Record annotation provenance. Retain annotator qualifications, instructions, software, dates, label versions, and the evidence available to the annotator.

Use independent review where consequences warrant it. Preserve initial judgments before adjudication. Where appropriate, blind reviewers to model outputs and other information that could bias their assessment.

Measure disagreement and investigate its causes. Distinguish ambiguous cases, inconsistent instructions, differing expertise, and actual errors. Agreement alone does not establish correctness.

Audit both positive and negative labels. A review limited to positive cases cannot establish how many true cases were missed. Examine whether different groups received different reference tests or follow-up.

Validate automatically generated labels independently. For NLP, weak supervision, or model-generated annotations, compare a suitable sample with stronger evidence. Agreement between related models may reflect shared errors.

Use task-appropriate annotation metrics. For segmentation, inspect overlap, boundary error, small structures, and missing lesions as relevant. One aggregate overlap score may omit important failure modes; the Metrics Reloaded framework explains how metric choice should follow the problem’s characteristics.

## 8. Assess population coverage, selection, and hidden bias

Count independent entities. Report patients, encounters, specimens, studies, lesions, and images separately. Large file counts can arise from relatively few independent people.

Build a coverage matrix. Tabulate relevant population groups, conditions, severity levels, sites, devices, protocols, and periods. Include the number of positive outcomes where performance depends on them.

Inspect meaningful intersections. A dataset may include older patients and a particular scanner while containing almost no older patients scanned with that device.

Describe who could enter the dataset. Examine referral pathways, insurance coverage, geography, test ordering, consent, and follow-up requirements. These determine what the sample can represent.

Check clinically meaningful subtypes. Broad labels can conceal differences in severity, presentation, comorbidity, and treatment status. Research on hidden stratification shows that strong aggregate performance can coexist with failures in clinically important subsets.

Distinguish development sampling from population evaluation. Enriching rare cases may help training or stress testing. Report that sampling explicitly and avoid interpreting the enriched sample as if it reflected deployment prevalence.

Investigate shortcuts. Cross-tabulate labels against hospital, device, ward, date, dimensions, filenames, borders, and embedded text. Test whether source metadata alone predicts the label unexpectedly well.

Use shortcut probes cautiously. They identify concerns requiring investigation. For example, cross-hospital pneumonia research demonstrated that acquisition context and hospital identity could affect apparent performance and transfer to other institutions.

Reassess coverage after cleaning. Compare retained and excluded cases. A cleaning rule that systematically removes difficult patients changes the population supported by the dataset.

## 9. Prevent leakage and verify evaluation independence

These rules apply when data are used for machine learning or other predictive evaluation.

Group related observations appropriately. When evaluating generalization to new patients, keep each patient’s related images, visits, crops, slices, and augmented copies within the same partition.

Match separation to the claim. Patient separation addresses new patients. Claims about new hospitals, future practice, laboratories, or devices require evaluation designs that examine those differences.

Check overlap across source datasets. Different filenames or pseudonyms do not prove independent patients or images. Investigate shared source collections and alternate exports.

Split before learning preprocessing parameters. Fit imputation, normalization parameters, feature selection, learned harmonization, and similar operations using training data or the training portion of each fold. Predetermined conversions that learn nothing from evaluation data are a different case.

Audit temporal leakage. Identify information added after the decision time, such as discharge diagnoses, later pathology, future treatment, or retrospective summaries.

Protect the final evaluation set. Repeated model selection against its results turns it into development data. Record access, prior uses, corrections, and the need for fresh independent evaluation.

Investigate pretraining and benchmark exposure. Record known exposure of pretrained models to evaluation sources. When exposure cannot be established, report that uncertainty.

Calculate uncertainty at the appropriate dependency level. Correlated slices from one scan should not be treated as independent patients. Use analysis methods that reflect clustering.

Improper splitting of related OCT images has been shown to inflate measured test accuracy. TRIPOD+AI also emphasizes separating evaluation data from training, tuning, and model selection.

## 10. Recheck transformations, augmentation, and synthetic data

Audit source-to-output pairs. Inspect representative and difficult cases before and after cropping, resizing, registration, compression, normalization, and conversion.

Preserve measurements and target features. Check whether processing removes small lesions, changes boundaries, alters physical scale, or changes quantitative values.

Transform annotations consistently. Apply spatial changes to images and labels together. Use interpolation appropriate to categorical masks or other annotation types.

Require augmentation to preserve the intended meaning. A left-right flip may change laterality; a crop may remove the target; a distortion may alter diagnostic morphology. Define valid augmentations for each task.

Keep synthetic data identifiable. Record the generator, inputs, version, conditioning, and intended role. Synthetic or augmented images do not add independent real patients to the evidence base.

Verify that harmonization preserves relevant variation. Examine whether processing removes useful biological differences, conceals subgroup failures, or creates site-dependent artifacts.

Evaluate AI image restoration for fidelity. Preserve originals and assess clinically relevant structures. FDA describes how visually appealing restored images can add false structures or remove true ones. Visual attractiveness is therefore insufficient evidence of faithful restoration.

## 11. Check permissions, privacy, and de-identification

Document permitted uses. Establish whether collection, secondary analysis, model development, redistribution, and deployment fit the applicable permissions and research arrangements. Public availability alone does not establish those rights.

Control sensitive access. Use appropriate access restrictions, protected linkage keys, audit records, and approved processing environments. Include derived files and temporary exports in the controls.

Inspect all places where identifiers may occur. Examine filenames, metadata, private fields, free text, embedded thumbnails, overlays, and burned-in pixel text.

Assess recognizable visual information. Depending on the data, identifying information can include facial appearance or anatomy reconstructable from image volumes. DICOM explicitly warns that de-identifying attributes does not guarantee de-identification of the complete information object.

Verify the result of de-identification. Check both residual disclosure risk and damage to analytical usefulness. Date shifting, redaction, and defacing can affect the relationships or structures needed for the task.

Use the applicable legal pathway. Where HIPAA applies, HHS describes Expert Determination and Safe Harbor as de-identification methods. Consent, research approval, authorization, and de-identification should each be considered according to their actual role.

## 12. Combine automated checks with a statistically honest human audit

### Check at several levels

| Audit scope | Main purpose | Examples |
|---|---|---|
| Every accepted record or file | Detect mechanical failures | Decoding, schema, required fields, identifiers, geometry, linkage |
| Every dataset version | Detect collection-wide problems | Counts, distributions, missingness, duplicates, exclusions, coverage |
| Probability-based human sample | Estimate defect frequency | Source-record agreement, label accuracy, image-record correspondence |
| Targeted challenge sample | Discover consequential failure modes | Rare conditions, difficult images, unusual devices, ambiguous cases |
| Independent or prospective evaluation | Assess the intended-use claim | Transfer to relevant settings, later data, and actual workflows |

Keep random and targeted audits distinct. A random sample can support a population error estimate. A deliberately enriched collection of suspicious cases supports failure discovery. Combining them without accounting for sampling changes the interpretation.

Additional audit rules:

- Record checks that did not run. An execution error, skipped check, or unsupported test cannot become a pass. OHDSI’s Data Quality Dashboard explicitly distinguishes errors and non-applicable checks from pass/fail outcomes.
- Test the checking process. Use controlled examples with known defects to establish whether validators detect the intended problems.
- Use independent evidence for consequential judgments. Another model can help identify suspicious cases, but high-stakes acceptance should be supported by appropriate source evidence and expertise.
- Report numerators and denominators. “Twelve incorrect links among 400 independently sampled studies” is more useful than “97% quality.”
- Preserve uncertainty. Include confidence intervals and explain clustering, sampling, and reviewer limitations.

### What does “we found no errors” establish?

Suppose an independent random audit examines n units, finds zero defects, and detects the relevant defect reliably. The one-sided 95% upper binomial bound is:

`p_upper = 1 - 0.05^(1/n) ≈ 3/n`.

Calculated examples:

| Independent units reviewed | Defects found | Approximate upper 95% bound on defect rate |
|---|---|---|
| 100 | 0 | 2.95% |
| 300 | 0 | 0.99% |
| 3,000 | 0 | 0.10% |

These are statistical illustrations, not universal audit requirements. Correlated images, imperfect reviewers, and inadequate subgroup coverage weaken what the audit establishes. NIST describes exact binomial methods for small defect counts and sample sizes.

A clean audit of 300 patients does not establish a zero error rate or provide strong evidence about a subgroup represented by only five patients.

## 13. Make acceptance depend on evidence and consequences

A proposed release policy should distinguish critical failures from tolerable limitations.

| Finding | Appropriate response |
|---|---|
| Unresolved wrong-patient or wrong-specimen linkage | Quarantine affected data; establish scope and correct the source |
| Unknown units or corrupted geometry needed for the task | Hold the affected use until interpretation is established |
| Patient overlap in a supposedly independent test set | Rebuild the evaluation and invalidate affected performance claims |
| Labels do not establish the claimed condition | Improve the reference standard or narrow the claim |
| Important intended groups have inadequate evidence | Restrict the supported population or collect additional evidence |
| Unexpected missingness or abnormal distributions | Investigate the collection and processing causes |
| Unresolved permissions or disclosure requirements | Hold the affected use or release |
| Documented residual limitations compatible with the task | Accept with explicit restrictions, ownership, and review triggers |

A high average quality score should never cancel a critical identity, measurement, privacy, or leakage failure.

For each rule, retain an evidence record with:

- Rule identifier and rationale.
- Dataset and pipeline version.
- Records or groups examined.
- Method and acceptance criterion.
- Result, denominator, and uncertainty.
- Examples of failures.
- Responsible reviewer.
- Remediation and disposition.

### Minimum release package

The accepted dataset should have a reproducible manifest, data dictionary, source and permission records, selection and exclusion counts, transformation history, labeling protocol, partition definitions where applicable, automated-check results, human-audit results, coverage assessment, unresolved issues, and an accountable owner.

Dataset documentation frameworks such as Datasheets for Datasets support recording collection, composition, processing, recommended uses, and maintenance. The evidence package should let another person assess the specific quality claims.

## 14. Separate data acceptance from claims about clinical performance

Data checking is necessary for credible clinical evaluation, but each later claim needs its own evidence.

- Internal evaluation examines performance within the sampled environment.
- External evaluation examines transfer to a separately assembled relevant cohort.
- Temporal evaluation examines later observations and changing practice.
- Prospective workflow evaluation examines what happens when inputs arrive and people use the system.
- Clinical-benefit evaluation examines whether use improves relevant decisions or outcomes under an appropriate study design.

A dataset audit cannot establish all of these. DECIDE-AI specifically addresses early live clinical evaluation, including actual performance, safety, and human factors.

Use established frameworks according to their purpose:

| Framework | Appropriate role |
|---|---|
| CLAIM 2024 | Reporting medical-imaging AI studies |
| TRIPOD+AI | Reporting clinical prediction-model studies |
| STARD-AI | Reporting AI diagnostic-accuracy studies |
| PROBAST+AI | Assessing prediction-study quality, risk of bias, and applicability |

Reporting checklists make methods inspectable. They do not themselves certify study quality. PROBAST+AI is specifically designed for quality, bias, and applicability assessment.

## 15. Worked example: a dataset that looks clean but is not ready

Consider a hypothetical dataset containing 60,000 chest radiographs from 20,000 patients at three hospitals.

The intended use is supporting pneumonia assessment in adult emergency-department patients.

| Audit finding | Interpretation |
|---|---|
| Every file decodes | File readability is supported |
| Repeat examinations from the same patients appear in training and testing | Evaluation independence fails |
| “Pneumonia” labels come from any mention in reports, including uncertain and historical mentions | Label meaning needs validation |
| One hospital supplies most positive examples | Site-related shortcuts and sampling require investigation |
| A clinically important subgroup has very few positive patients | Precise subgroup performance claims are unsupported |
| A random audit of 300 independent studies finds no image-record mismatches | Useful evidence about linkage, with roughly a 1% upper bound under the stated assumptions |

The release decision should identify these separately. The files may be suitable for limited exploratory work while the proposed diagnostic evaluation remains on hold. Correct the partitioning, establish label validity, investigate site effects, and obtain sufficient evidence for the intended population.

## 16. Continue checking after release

Quality can change when collection and processing change. Establish a monitoring plan with named owners and actions.

- Monitor incoming-data integrity: decoding failures, incomplete studies, invalid fields, duplicate rates, and linkage errors.
- Monitor acquisition changes: new sites, devices, protocols, software, laboratory methods, and coding systems.
- Monitor the observation process: missingness, follow-up delays, label availability, and changes in who receives tests.
- Monitor population coverage: case mix, disease prevalence, important subgroups, and exclusion or rejection rates.
- Monitor outcomes when reliable labels arrive: relevant performance, calibration, serious failures, and subgroup results.
- Track feedback effects: system use may change which patients are tested, what clinicians record, or which labels become available.
- Version corrections: identify affected derivatives, analyses, and performance claims; rerun the relevant checks.
- Define response triggers: investigate, restrict use, pause processing, recollect data, or repeat evaluation.

NIST’s AI Risk Management Framework supports ongoing measurement, documentation, risk tracking, and management throughout use. A drift signal should trigger investigation; the absence of a measured drift signal does not establish that performance is unchanged.

Every accepted release should end with a concrete record of the supported task, population, setting, dataset version, evidence reviewed, remaining limitations, approving owner, and conditions that require reassessment.
