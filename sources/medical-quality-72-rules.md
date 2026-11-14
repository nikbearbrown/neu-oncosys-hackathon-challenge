# Data Quality Rules for Image and Medical Data

*How do we know our data is good? A falsification-first rulebook.*

## The core problem

"Good data" is not a property a dataset has. It is a relationship between a dataset, a question, and the setting where the answers will be used. The same chest X-ray collection can be excellent for training a view-position classifier and worthless for detecting pneumonia at a community hospital. A rule set that ignores this checks the wrong thing.

Second, data checks are asymmetric. A check can show that data is bad. No check can show that data is good. At the end of an audit you have a ledger of failed attempts to break the dataset. The honest claim is "we tried these specific ways to find problems and didn't find any," never "the data is clean."

Third, the most damaging flaws in medical imaging datasets are usually invisible to mechanical inspection. Every file can open, every tag can be present, every label can sit in the right column, and a model can still learn to read the hospital's identity off the image instead of the disease. The well-known failures in this field passed their integrity checks: pneumonia models keyed to the scanner, COVID detectors keyed to the dataset source, melanoma classifiers keyed to surgical ink. They would have failed definitional and adversarial checks.

So the rules are ordered by where the expensive errors live, not by how easy they are to run.

| Layer | Question it answers | Kahn et al. category |
|---|---|---|
| Part 0: Definition | Good *for what*? | Precondition |
| Parts 1–2: Provenance and integrity | Is the data what it claims to be? | Verification |
| Part 3: Labels | Is the target true? | Validation |
| Part 4: Leakage | Will the evaluation be honest? | Validation |
| Part 5: Shortcuts | Can a model cheat? | Validation |
| Part 6: Representativeness | Does it look like the world it will be used in? | Validation |
| Parts 7–8: Image-specific and privacy | Modality and legal constraints | Both |
| Parts 9–10: Drift and documentation | Does it stay good, and can anyone check? | Ongoing |

Kahn et al. (2016) separate *verification*, which asks whether data matches internal expectations and constraints, from *validation*, which asks whether it agrees with external reality. Most pipelines put most of their effort into verification and little into validation. That is backwards relative to where the risk is.

---

## Part 0: Define "good" before you look

**R1. Write the intended-use statement first.** One paragraph covering the task, the clinical decision the output informs, who acts on it, and what an error costs in each direction. Every later rule is judged against this statement. If you can't write it, you can't audit the data.

**R2. Define the target population and setting.** Write down the inclusion and exclusion criteria, the care setting (screening, ED, inpatient, specialty clinic), the expected prevalence, and the devices in use. "Representative" means nothing without something to represent.

**R3. Fix the unit of analysis.** Choose patient, encounter, study, series, image, slice, or lesion. Write the choice down and enforce it in code. Most leakage bugs come from confusing these levels.

**R4. Define the label operationally.** State what counts as positive, who decides, what information they use, and at what point in time. "Pneumonia" extracted from a radiology report is a statement about what a radiologist wrote, not about the patient's lungs.

**R5. Name and rank the reference standard.** A rough hierarchy, from strongest to weakest: histopathology or a definitive test, then longitudinal outcome or follow-up, then adjudicated multi-reader consensus, then a single expert read, then an NLP-extracted report label, then a billing code. Know which one you have and state the ceiling it imposes on everything downstream.

**R6. Pre-register acceptance criteria.** Before auditing, write the thresholds: tolerable missingness per field, minimum inter-rater agreement, minimum N per subgroup, and maximum near-duplicate rate. Criteria written after seeing the data tend to bend to fit it.

---

## Part 1: Provenance and lineage

**R7. Every record is traceable.** Record the source system, extraction query, extraction date, and software version. If you can't reconstruct how a row entered the dataset, you can't reason about why it's there.

**R8. Document the selection mechanism.** Name the design: consecutive enrollment, random sample, case-control, convenience sample, or aggregation of public datasets. Case-control designs compare clear disease with clearly healthy cases. They inflate accuracy through spectrum bias, and that inflation disappears in deployment.

**R9. Count every exclusion.** Draw a flow diagram (STARD or CONSORT style) from the source population to the final dataset, with counts and reasons at each step. Selection bias hides in exclusions. "Excluded poor-quality images" often means "excluded the sickest patients."

**R10. Keep an immutable raw layer.** Raw data is read-only and has a SHA-256 manifest. Every transformation is code under version control. Nobody edits by hand, including to fix one obviously wrong label.

**R11. Version the dataset and bind models to it.** Use content-addressed manifests, DVC, or an equivalent. Every trained model records the hash of the dataset it saw, so "which data was this trained on?" always has an exact answer.

**R12. Confirm the legal basis.** Check the consent scope, IRB determination, data use agreement, and license. Confirm that secondary use for model development is covered and whether redistribution is allowed. This belongs in a data quality audit because data you can't legally use is not good data.

---

## Part 2: Integrity and conformance (verification)

**R13. Every file decodes.** Count unreadable, truncated, zero-byte, and pixel-decode failures separately. Decode the pixels as well as the header, because a header can parse while the pixel data is corrupt.

**R14. Check format conformance.** Required DICOM attributes must be present and non-empty, and the transfer syntax must be one your pipeline supports. Flag lossy compression (`LossyImageCompression`, 0028,2110). If one site's images are lossy-JPEG and another's are uncompressed, the compression itself becomes a site signature.

**R15. Geometry is consistent.** Check rows and columns, pixel spacing, slice thickness, and `ImageOrientationPatient`. For volumes, look for missing slices using gaps in `ImagePositionPatient`, not only `InstanceNumber`. Spacing should be uniform and orientation consistent across the series.

**R16. Intensities mean what you think.** Compare bits stored with bits allocated, and confirm the rescale slope and intercept are applied exactly once. CT values should fall in plausible Hounsfield ranges (air near −1000, water near 0). Handle `PhotometricInterpretation` explicitly: MONOCHROME1 is inverted relative to MONOCHROME2. Mixing them silently is a classic bug, and the mix often lines up with site.

**R17. No degenerate images.** Look for constant, blank, fully saturated, or nearly empty images. Compute a histogram per file and review the tails.

**R18. Enforce uniqueness at every level.** UIDs should be unique where the standard says they are. Remove exact duplicates by hash and flag near-duplicates with perceptual hashing or embedding similarity. Public datasets often contain the same image under different names, and the same image can appear in several public datasets.

**R19. Check relational integrity.** Every image links to exactly one patient, one study, and one label record. There are no orphans in either direction, and every foreign key resolves.

**R20. Check plausibility.** Ages fall in range, and dates run in order: birth, then acquisition, then report, then outcome. Laterality markers agree with metadata. Sex-specific anatomy and procedures agree with recorded sex. Flag every disagreement for human review and never correct automatically.

```python
# DICOM integrity audit: one row per file; aggregate the rows with pandas.
import hashlib
from pathlib import Path

import numpy as np
import pydicom

REQUIRED = [
    "PatientID", "StudyInstanceUID", "SeriesInstanceUID", "SOPInstanceUID",
    "Modality", "Rows", "Columns", "BitsStored", "PhotometricInterpretation",
]
RECORD = ["Modality", "Manufacturer", "PhotometricInterpretation",
          "LossyImageCompression", "BurnedInAnnotation"]

def audit(path: Path) -> dict:
    row = {"path": str(path),
           "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
           "issues": []}
    try:
        ds = pydicom.dcmread(path)
    except Exception as e:
        row["issues"].append(f"unreadable header: {e}")
        return row

    for kw in REQUIRED:
        if ds.get(kw) in (None, ""):
            row["issues"].append(f"missing {kw}")
    row.update({kw: ds.get(kw) for kw in RECORD})

    try:
        px = ds.pixel_array.astype(np.float32)
    except Exception as e:
        row["issues"].append(f"pixel decode failed: {e}")
        return row

    if px.std() == 0:
        row["issues"].append("constant image")

    if ds.get("Modality") == "CT":
        hu = px * float(ds.get("RescaleSlope", 1)) + float(ds.get("RescaleIntercept", 0))
        inside = hu[hu > -1500]  # drop padding values such as -2000 or -3024
        if inside.size == 0 or inside.min() > -800:
            row["issues"].append("no air-range voxels: rescale missing or misapplied?")

    return row
```

`BurnedInAnnotation` is often absent or wrong. Treat its value as a hint, not a guarantee (see R59).

---

## Part 3: Label quality (validation)

**R21. Measure inter-rater agreement.** Have at least two independent readers label a random sample, blinded to each other. Report Cohen's κ for two readers, or Fleiss' κ or Krippendorff's α for more, with bootstrap confidence intervals. Agreement limits the performance you can meaningfully measure. A model that "beats" a noisy reference standard is usually measuring the noise.

**R22. Control what readers see.** Readers should not see model outputs, each other's reads, or information that leaks the outcome. Document the clinical context they did have, because that context defines what the label means.

**R23. Audit how labels were produced.** NLP-extracted labels inherit negation errors, hedges such as "cannot exclude," and selection effects, because reports describe what the radiologist chose to mention rather than everything present. Validate a sample of extracted labels against human reads before trusting the whole set.

**R24. Hunt for label errors, then adjudicate.** Use confident learning (for example, cleanlab) on *out-of-fold* predicted probabilities to rank likely mislabels, and send the ranked list to human adjudication. Never relabel automatically. A flagged disagreement is a lead, not a verdict.

**R25. Check the timing of labels.** The label must come either from information available at prediction time or from an explicitly defined future outcome. A diagnosis code entered after treatment is not a valid label for a pre-treatment image, because post-treatment information leaks into it.

**R26. Look for hidden stratification.** The positive class is often several subtypes that differ in difficulty and clinical stakes. Annotate subtypes on a sample and check whether the easy ones dominate the label (Oakden-Rayner et al., 2020).

**R27. Treat uncertainty as its own value.** "Uncertain," "not mentioned," and "negative" are three different values, and collapsing them changes the label definition. Store them separately, decide the mapping for each experiment, and record the mapping.

**R28. Audit segmentation masks as data.** Mask geometry must match image geometry (spacing, orientation, origin), and mask volumes should be anatomically plausible. Measure inter-annotator Dice and Hausdorff distance on a sample. Boundary conventions, such as whether to include the capsule or the necrotic core, must be consistent across annotators.

**R29. Track annotator identity.** Store who labeled each item and check whether positive rates differ by annotator or annotation batch. The annotator is a confounder like any other.

```python
import numpy as np
from cleanlab.filter import find_label_issues
from sklearn.metrics import cohen_kappa_score
from sklearn.model_selection import GroupKFold, cross_val_predict

# Inter-rater agreement with a bootstrap CI.
# Use weights="quadratic" for ordinal grades. With several images per patient,
# resample patients rather than images.
def kappa_ci(a, b, n_boot=2000, seed=0):
    a, b = np.asarray(a), np.asarray(b)
    rng = np.random.default_rng(seed)
    point = cohen_kappa_score(a, b)
    boots = [cohen_kappa_score(a[idx], b[idx])
             for idx in (rng.integers(0, len(a), len(a)) for _ in range(n_boot))]
    return point, np.percentile(boots, [2.5, 97.5])

# Label-error candidates from out-of-fold probabilities, grouped by patient to avoid leakage.
# `model` is any sklearn-compatible classifier with predict_proba.
oof_probs = cross_val_predict(model, X, y, groups=patient_ids,
                              cv=GroupKFold(n_splits=5), method="predict_proba")
suspects = find_label_issues(labels=y, pred_probs=oof_probs,
                             return_indices_ranked_by="self_confidence")
# Send `suspects` to human adjudication. Do not relabel automatically.
```

---

## Part 4: Leakage and splitting

**R30. Split at the patient level or higher.** Never split at the image, slice, or study level. If one patient's images appear on both sides of a split, the test measures memorization of that patient, not detection of the disease. Assert disjointness in code.

**R31. Scan for near-duplicates across splits after splitting.** Look for re-acquisitions, augmentations saved to disk, different crops or exports of the same image, and the same image appearing in two public datasets under different IDs. Patient IDs won't catch these when datasets have been merged.

**R32. Fit everything on training data only.** That covers normalization statistics, intensity standardization, feature selection, dimensionality reduction, oversampling, and hyperparameter search. Anything fit on the full dataset leaks test information.

**R33. Remove label proxies.** Some inputs encode the outcome instead of predicting it: treatment devices visible in the image, burned-in text ("PORTABLE," "ICU," "STAT"), report text, the ordering indication, and downstream codes.

**R34. Use temporal splits for anything deployed prospectively.** Train on earlier data and test on later data. Random splits hide drift in protocols, scanners, and coding practice.

**R35. Require an external test set for any generalization claim.** The external set should come from a different institution with different scanners, ideally serving a different population. An internal held-out split is not external validation, however carefully it was drawn.

**R36. Touch the test set once.** Each additional look feeds information back through your decisions. Once you've looked many times, it has become a validation set, and you need a new test set.

```python
import imagehash
from PIL import Image
from sklearn.model_selection import GroupShuffleSplit

# Patient-level split with an enforced invariant.
gss = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=0)
train_idx, test_idx = next(gss.split(df, groups=df["patient_id"]))
train, test = df.iloc[train_idx], df.iloc[test_idx]
assert set(train.patient_id).isdisjoint(test.patient_id), "patient leakage"

# Cross-split near-duplicate scan: perceptual hash, Hamming distance on 64 bits.
# This is O(n*m) for clarity. At scale, use a BK-tree or an ANN index such as FAISS,
# and add embedding similarity, which catches crops and re-exports that pHash misses.
def phash(p):
    return imagehash.phash(Image.open(p).convert("L"))

train_h = {p: phash(p) for p in train.png_path}
test_h = {p: phash(p) for p in test.png_path}
THRESH = 6  # tune on known duplicate pairs from your own data
leaks = [(t, r) for t, ht in test_h.items()
         for r, hr in train_h.items() if ht - hr <= THRESH]
```

---

## Part 5: Shortcuts and confounders

Make this section non-negotiable. Models learn whatever signal predicts the label most cheaply, and in clinical data, acquisition and workflow signals are often cheaper than pathology (Geirhos et al., 2020).

**R37. Run the site-predictability probe.** Train a classifier to predict site, scanner, or source dataset from the images. Frozen embeddings plus a linear model are enough. The probe will usually succeed. That alone isn't fatal, but it becomes fatal when combined with R39, where site also predicts the label. Zech et al. (2018) found that pneumonia models could identify the hospital system almost perfectly while disease prevalence differed between hospitals. DeGrave et al. (2021) found that COVID-19 detectors relied on cues tied to the dataset source rather than on lung pathology.

**R38. Run the metadata-only baseline.** Predict the label from acquisition metadata alone: site, scanner, view position, portable versus fixed, time of day, ordering department. An AUC well above 0.5 means the label is entangled with workflow, and an image model can learn that workflow from the pixels.

**R39. Cross-tabulate the label against every acquisition variable.** Compute prevalence by site, scanner, protocol, view, time period, and annotator. Large differences are shortcut opportunities. Balance or stratify where you can, and at a minimum report them.

**R40. Run intervention tests, not just inspections.** Mask the anatomy of interest: if performance holds, the model is using something else. Mask borders, corners, and text regions: if performance drops, the model was using them. Remove or swap artifacts and measure the change.

**R41. Inventory non-anatomical signal.** List rulers, skin markings, text overlays, laterality markers, chest drains, lines, pacemakers, ECG leads, positioning aids, and cropping or padding conventions. Annotate their presence on a sample and test their correlation with the label. Surgical skin markings raised melanoma probabilities in a dermoscopy CNN (Winkler et al., 2019). Chest drains, which show that a pneumothorax has already been treated, drove pneumothorax detection (Oakden-Rayner et al., 2020).

**R42. Treat saliency maps as hypotheses.** Heatmaps can look plausible for models that have learned nothing, and some saliency methods barely change when the model's weights are randomized (Adebayo et al., 2018). Use saliency to generate hypotheses, then test them with R40.

**R43. Assume demographics are encoded in the pixels.** Deep models predict self-reported race from chest X-rays, CT, and mammography with high accuracy, even when experts can't and even from degraded images (Gichoya et al., 2022). Dropping the demographic column removes your ability to audit for it. It doesn't remove the information.

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold, cross_val_score

cv = GroupKFold(n_splits=5)
clf = LogisticRegression(max_iter=5000)

# R37: can frozen image embeddings identify the site?
site_auc = cross_val_score(clf, embeddings, df["site"], groups=df["patient_id"],
                           cv=cv, scoring="roc_auc_ovr").mean()

# R38: can metadata alone predict the label?
meta_cols = ["site", "scanner_model", "view_position", "portable", "hour_bin", "ordering_dept"]
meta = pd.get_dummies(df[meta_cols].astype(str))
meta_auc = cross_val_score(clf, meta, df["label"], groups=df["patient_id"],
                           cv=cv, scoring="roc_auc").mean()

# R39: prevalence by acquisition variable.
for col in meta_cols:
    print(df.groupby(col)["label"].agg(["mean", "size"]).sort_values("mean"))

print(f"site AUC={site_auc:.3f}  metadata->label AUC={meta_auc:.3f}")
```

---

## Part 6: Representativeness and subgroups

**R44. Compare against real denominators.** Compare the dataset with the target population on age, sex, race and ethnicity, disease severity, comorbidity, care setting, and device. Use registries, institutional census data, or epidemiological sources, not intuition about who "usually" gets imaged. Dermatology models, for example, lost substantial performance on darker skin tones that were scarce in their training data (Daneshjou et al., 2022).

**R45. Compute the subgroup N you need, then check you have it.** For each subgroup you plan to report, calculate the sample size needed for a confidence interval of useful width at the expected prevalence. If you don't have that N, you can't claim subgroup performance. Say so instead of reporting an unstable point estimate.

**R46. Check the disease spectrum.** Look at the severity distribution, early and borderline cases, mimics, normal variants, and common co-occurring findings. A dataset of florid disease against pristine controls produces numbers that collapse in a real referral population.

**R47. Know your prevalence and where it will move.** PPV and NPV depend on prevalence. A model validated at 30% prevalence behaves very differently in a screening population at 2%. Report metrics at the expected deployment prevalence, not just AUC.

**R48. Check acquisition diversity.** Record manufacturer, model, software version, field strength, kVp and mAs, reconstruction kernel, slice thickness, contrast phase, and coil. A single-vendor dataset produces a single-vendor model.

**R49. Treat missingness as data.** Record which fields are missing, for whom, and why. Missing patients are rarely random: some never received the scan, some had images fail QC, some were lost to follow-up. Classify the plausible mechanisms (MCAR, MAR, MNAR) and test them.

**R50. Check label rates by subgroup.** If the source labels underdiagnose some populations, a model trained on them will too, and evaluating against the same labels will hide the problem (Seyyed-Kalantari et al., 2021). Where possible, compare against a stronger reference standard on a sample stratified by subgroup.

---

## Part 7: Image-specific acquisition and preprocessing

**R51. Quantify image quality objectively.** Use modality-appropriate metrics: SNR, CNR, blur (variance of the Laplacian), exposure index, and for MRI the MRIQC image quality metrics. Flag outliers per modality and per site rather than pooled, because site differences will dominate a pooled analysis.

**R52. Catalog artifacts and set a policy.** Inventory motion, metal streak, beam hardening, aliasing, ring, compression blocking, and grid lines, and decide inclusion according to the intended use. Excluding every artifact produces a model that has never seen what deployment will send it.

**R53. Document every preprocessing step and visualize it.** This includes resampling, windowing, normalization, cropping, registration, and skull-stripping. Render before-and-after images for a random sample from every site and class, and confirm the output can be reproduced from the raw layer.

**R54. Don't destroy signal in conversion.** Common losses include down-converting 12- or 16-bit DICOM to 8-bit PNG, windowing that clips pathology (a lung window applied to a mediastinal finding), lossy JPEG export, and interpolation that smooths away small lesions. Compare information content before and after.

**R55. Verify orientation and laterality after every format conversion.** DICOM-to-NIfTI and DICOM-to-PNG conversions are a common source of silent left-right flips and axis permutations. Check a sample against known landmarks or laterality markers.

**R56. Augmentations must preserve the label.** Horizontal flips change laterality, which is wrong for situs-dependent anatomy, side-specific labels, and anything containing text. Intensity augmentations shouldn't push values outside physical ranges. Inspect augmentation outputs visually.

**R57. Look at the data, on a schedule.** Review a random contact sheet stratified by class, site, and time period, at full resolution, with someone who has domain knowledge. Repeat after every pipeline change. Most catastrophic dataset bugs are visible to a human within thirty seconds of looking.

---

## Part 8: Privacy and de-identification

**R58. Apply a standard de-identification profile and audit it.** Use the DICOM PS3.15 Annex E profiles and HIPAA Safe Harbor or Expert Determination as applicable. Then audit at the tag level, including private tags, sequences, and free-text fields such as `ImageComments` and `StudyDescription`.

**R59. Scan pixel data for burned-in PHI.** Ultrasound, secondary captures, scanned documents, screenshots, and dose reports often carry names, MRNs, and dates in the pixels. Run OCR and review the hits. Don't rely on the `BurnedInAnnotation` tag.

**R60. Deface head and neck imaging.** Faces can be reconstructed from MRI and CT and matched to photographs with face-recognition software (Schwarz et al., 2019). Deface the images, or document why not and restrict access accordingly. Then check that defacing didn't remove anatomy the task needs.

**R61. Shift dates and remap UIDs consistently.** Preserve intervals within each patient, and keep remapped UIDs stable across the dataset so relational integrity survives de-identification. Verify both afterward.

**R62. Assess linkage risk, and watch for new shortcuts.** Rare diseases, extreme ages (Safe Harbor aggregates ages over 89), small geographic units, and unusual devices can re-identify individuals in combination. De-identification can also create shortcuts. If one site's pipeline leaves a distinctive tag pattern or black border, that becomes a site signature (R37).

---

## Part 9: Drift and deployment

**R63. Data checks are continuous, not a one-time gate.** Run the integrity, distribution, and quality checks on incoming production data as well as the training set. Monitor intensity histograms, metadata distributions, and embedding drift.

**R64. Log acquisition changes as events.** Scanner replacements, software upgrades, protocol changes, and new sites are each a distribution shift with a known timestamp. Logging them lets you correlate performance changes with them later.

**R65. Monitor label drift.** Clinical definitions change (sepsis was redefined with Sepsis-3 in 2016), and so do coding practices and referral patterns. A stable model can appear to degrade because the labels moved.

**R66. Run a silent-mode prospective evaluation before clinical use.** In silent mode the model runs on live data without affecting care, and its outputs are compared with outcomes later. Retrospective external validation is not a substitute. A widely deployed proprietary sepsis model performed substantially worse in independent external validation than its developer had reported (Wong et al., 2021).

**R67. Expect feedback loops.** Once a model influences care, it changes who gets imaged, what gets ordered, and what gets labeled. Future training data will be shaped by the model's own decisions, so plan for that from the start.

---

## Part 10: Documentation and sign-off

**R68. Ship a datasheet with every dataset release.** Cover motivation, composition, collection process, preprocessing, intended uses, distribution, and maintenance (Gebru et al., 2021). For health data, use or adapt Healthsheet (Rostamzadeh et al., 2022).

**R69. Report against the relevant checklist.** Use CLAIM for AI in medical imaging, TRIPOD+AI for prediction models, STARD and its AI extension STARD-AI for diagnostic accuracy studies, and PROBAST+AI and QUADAS-2 for risk-of-bias assessment. These checklists encode the failure modes reviewers will look for.

**R70. Write a limitations section that names what you couldn't check.** Include the checks that found problems and what you did about them. Also name the checks you couldn't run, such as having no external site or no reference standard stronger than single reads. Unstated limitations do more damage than stated ones.

**R71. Separate builder from auditor.** The person who assembled the dataset does not sign off on it alone. An independent reviewer reruns the adversarial checks in Part 5 without the builder's assumptions.

**R72. Every rule produces an artifact.** Each check leaves a number, a plot, a table, or a file in the repository. "We looked at it" is not evidence, and a check that left no artifact didn't happen.

---

## The adversarial minimum

If you only have time for six checks, run these. They catch the failure modes that have actually sunk published medical imaging models.

| Check | Rules | Artifact | Red flag |
|---|---|---|---|
| Patient-level split plus cross-split near-duplicate scan | R30, R31 | Disjointness assertion; list of near-duplicate pairs | Any patient overlap; any unexplained near-duplicate |
| Site-predictability probe | R37, R39 | Site AUC from frozen embeddings; prevalence by site | High site AUC **and** prevalence that differs by site |
| Metadata-only baseline | R38 | AUC for predicting the label from acquisition metadata | AUC meaningfully above 0.5 |
| Blinded inter-rater agreement | R21 | κ or α with CI on a random sample | Reported model performance higher than reader agreement can support |
| Subgroup counts vs. target population | R44, R45 | N and prevalence per subgroup next to population denominators | Any reported subgroup below the precomputed minimum N |
| External test set | R35 | Performance at a different institution, reported next to internal results | No external set, or a large drop with no explanation |

## What no rule can tell you

Some questions are out of reach for any check run on the dataset itself. No check can tell you whether the label definition corresponds to something clinically meaningful, whether the target population was defined correctly in the first place, whether deployment will resemble the test set, or which confounders nobody thought to record. People and process address these, not code: the clinicians who will use the output reviewing R1–R5, external validation, prospective evaluation, and monitoring after deployment.

A dataset that passes every rule above is a dataset you have failed to break in seventy-two specific ways. That is worth a lot, but it is not the same as "good."

---

## Reference lineage

**Data quality frameworks and reporting standards**

- Kahn MG et al. (2016). A harmonized data quality assessment terminology and framework for the secondary use of electronic health record data. *eGEMs*. Conformance, completeness, and plausibility, each assessed by verification and by validation.
- Gebru T et al. (2021). Datasheets for datasets. *Communications of the ACM*.
- Rostamzadeh N et al. (2022). Healthsheet: Development of a transparency artifact for health datasets. *ACM FAccT*.
- Mongan J, Moy L, Kahn CE (2020). Checklist for Artificial Intelligence in Medical Imaging (CLAIM). *Radiology: Artificial Intelligence*. Updated in 2024 (Tejani et al.).
- Collins GS et al. (2024). TRIPOD+AI statement. *BMJ*.
- Whiting PF et al. (2011). QUADAS-2. *Annals of Internal Medicine*.
- STARD-AI (Sounderajah et al.) and PROBAST+AI (Moons et al.). AI extensions of the diagnostic-accuracy and risk-of-bias standards.
- FDA, Health Canada, MHRA (2021). Good Machine Learning Practice for Medical Device Development: Guiding Principles. Principles 3–5 cover representativeness, train/test independence, and reference standards.
- EU AI Act (Regulation (EU) 2024/1689), Article 10, on data and data governance for high-risk systems.
- DICOM PS3.15 Annex E, attribute confidentiality profiles for de-identification.

**Shortcut learning and confounding**

- Geirhos R et al. (2020). Shortcut learning in deep neural networks. *Nature Machine Intelligence*.
- Zech JR et al. (2018). Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs. *PLOS Medicine*.
- DeGrave AJ, Janizek JD, Lee SI (2021). AI for radiographic COVID-19 detection selects shortcuts over signal. *Nature Machine Intelligence*.
- Roberts M et al. (2021). Common pitfalls and recommendations for using machine learning to detect and prognosticate for COVID-19 using chest radiographs and CT scans. *Nature Machine Intelligence*.
- Winkler JK et al. (2019). Association between surgical skin markings in dermoscopic images and diagnostic performance of a deep learning CNN for melanoma recognition. *JAMA Dermatology*.
- Oakden-Rayner L et al. (2020). Hidden stratification causes clinically meaningful failures in machine learning for medical imaging. *ACM CHIL*.
- Adebayo J et al. (2018). Sanity checks for saliency maps. *NeurIPS*.

**Labels and leakage**

- Northcutt CG, Jiang L, Chuang IL (2021). Confident learning: Estimating uncertainty in dataset labels. *JAIR*.
- Northcutt CG, Athalye A, Mueller J (2021). Pervasive label errors in test sets destabilize machine learning benchmarks. *NeurIPS Datasets and Benchmarks*.
- Irvin J et al. (2019). CheXpert: A large chest radiograph dataset with uncertainty labels and expert comparison. *AAAI*.
- Kapoor S, Narayanan A (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns*.

**Bias, representativeness, and deployment**

- Gichoya JW et al. (2022). AI recognition of patient race in medical imaging: a modelling study. *Lancet Digital Health*.
- Seyyed-Kalantari L et al. (2021). Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations. *Nature Medicine*.
- Daneshjou R et al. (2022). Disparities in dermatology AI performance on a diverse, curated clinical image set. *Science Advances*.
- Wong A et al. (2021). External validation of a widely implemented proprietary sepsis prediction model in hospitalized patients. *JAMA Internal Medicine*.

**Image quality and privacy**

- Esteban O et al. (2017). MRIQC: Advancing the automatic prediction of image quality in MRI from unseen sites. *PLOS ONE*.
- Schwarz CG et al. (2019). Identification of anonymous MRI research participants with face-recognition software. *NEJM*.

**Tools referenced**

pydicom, dcm2niix, SimpleITK, MONAI, TorchIO, MRIQC, cleanlab and CleanVision, imagehash, FAISS, DVC, Great Expectations or pandera for tabular metadata, and RSNA CTP or pydicom-deid for de-identification.