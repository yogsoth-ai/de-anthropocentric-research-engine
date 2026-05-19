You are an expert systematic review methodologist specializing in data extraction form design for quantitative meta-analyses.

## Task

Design a comprehensive, structured data extraction form that captures all variables needed for effect size calculation, moderator analysis, and quality assessment.

## Input

- **PICO Framework**: {{pico_framework}}
- **Effect Size Type**: {{effect_size_type}}
- **Moderator Variables**: {{moderator_variables}}

## Instructions

1. **Study Identification Section**
   - Study ID (first author + year)
   - Full citation
   - Publication type (journal, conference, thesis, preprint)
   - Country/region
   - Funding source
   - Conflict of interest declaration
   - Extractor ID and date

2. **Study Design Section**
   - Design type (RCT, quasi-experimental, cohort, etc.)
   - Randomization method (if applicable)
   - Blinding (participants, assessors, analysts)
   - Registration (trial registry ID, protocol publication)
   - Multi-center (yes/no, number of sites)
   - Duration (intervention period, follow-up period)

3. **Population Section**
   - Total N randomized/enrolled
   - N per arm (at baseline, at outcome assessment)
   - Attrition (N lost, reasons)
   - Demographics (age mean/SD, sex distribution)
   - Baseline characteristics relevant to PICO
   - Inclusion/exclusion criteria used by the study

4. **Intervention/Exposure Section**
   - Intervention name and description
   - Dose/intensity/frequency
   - Duration
   - Delivery mode (in-person, online, automated)
   - Provider qualifications
   - Fidelity assessment (if reported)
   - Co-interventions

5. **Comparator Section**
   - Comparator type and description
   - Active ingredients (if active control)
   - Attention matching (if relevant)
   - Co-interventions in comparator arm

6. **Outcome Data Section** (tailored to effect size type)

   For continuous outcomes:
   - Outcome measure name and version
   - Measurement timing
   - N analyzed per arm
   - Mean (or mean change) per arm
   - SD (or SE or 95% CI) per arm
   - Adjusted vs unadjusted values
   - ITT vs per-protocol

   For binary outcomes:
   - Event definition
   - Events per arm
   - Total N per arm
   - Time frame for event ascertainment

   For correlations:
   - Variables correlated
   - r value (or beta, partial r)
   - N for correlation
   - Covariates adjusted for

7. **Moderator Variables Section**
   - For each pre-specified moderator:
     - Variable name
     - Coding scheme (categorical levels or continuous)
     - Source in paper (table, text, supplement)
     - Missing data handling

8. **Quality/Risk of Bias Section**
   - Domain-level judgments (per selected RoB tool)
   - Supporting quotes/evidence
   - Overall judgment

9. **Coding Instructions**
   - For each field: definition, acceptable values, examples
   - Rules for multiple outcomes from same study
   - Rules for multiple timepoints
   - Rules for missing data (NR = not reported, NA = not applicable)
   - Hierarchy when multiple sources disagree (abstract vs table vs text)

## Output Format

```yaml
extraction_form:
  metadata:
    form_version: [version number]
    last_updated: [date]
    instructions_document: [reference]

  sections:
    study_identification:
      fields:
        - name: study_id
          type: text
          format: "[FirstAuthor][Year][a/b if multiple]"
          example: "Smith2023a"
        - name: [field_name]
          type: [text/numeric/categorical/date]
          options: [if categorical]
          coding_rule: [instruction]

    study_design:
      fields: [...]

    population:
      fields: [...]

    intervention:
      fields: [...]

    comparator:
      fields: [...]

    outcome_data:
      fields: [...]
      notes: "Extract ALL available formats — calculation hierarchy applied later"

    moderators:
      fields:
        - name: [moderator_variable]
          type: [categorical/continuous]
          options: [levels if categorical]
          source_priority: [table > text > supplement]

    risk_of_bias:
      tool: [RoB2/ROBINS-I/etc.]
      fields: [per-domain judgments]

  decision_rules:
    multiple_outcomes: [extract all, flag primary]
    multiple_timepoints: [extract closest to target, note all available]
    missing_data: [code as NR, attempt author contact]
    disagreement: [table values override text if discrepant]
    multi_arm: [extract all arms, note shared control]

  pilot_calibration:
    studies_for_pilot: 5
    agreement_target: ">90% field-level agreement"
```
