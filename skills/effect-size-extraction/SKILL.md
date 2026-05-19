---
name: effect-size-extraction
description: Systematically extract effect sizes and conditions from papers for meta-analytic synthesis
execution: tactic
used-by: meta-analysis
---

# Effect Size Extraction Tactic

Systematically extract quantitative effect sizes, study conditions, and precision metrics from included studies.

## Stages

### Stage 1: Paper Identification

Identify the specific sections of each paper containing quantitative results.

- Locate results tables, figures, and statistical reporting sections
- Identify primary and secondary outcomes
- Flag studies reporting insufficient statistics for effect size calculation

**Tools**: dare-scholar (paper_content, paper_reading), alphaxiv (answer_pdf_queries)

### Stage 2: Data Point Location

For each study, locate the exact data points needed for effect size calculation.

- Sample sizes per group (N treatment, N control)
- Central tendency (means, proportions, hazard ratios)
- Variability (SD, SE, CI, IQR)
- Test statistics (t, F, chi-square, z) when direct data unavailable
- p-values as last resort for back-calculation

**SOPs**: effect-size-planning (determine what to extract)

### Stage 3: Effect Size Calculation Planning

Plan the calculation method for each study based on available data.

- Direct calculation from means + SDs
- Conversion from test statistics (t → d, F → d, r → z)
- Conversion between effect size families (OR ↔ d, r ↔ d)
- Handling of multi-arm studies (shared control correction)
- Cluster-adjusted effect sizes (design effect)

**SOPs**: effect-size-planning

### Stage 4: Condition Recording

Record all study-level conditions and moderator variables.

- Population characteristics (N, demographics, baseline severity)
- Intervention details (dose, duration, delivery mode)
- Comparison conditions (active control, placebo, waitlist)
- Outcome measurement (tool, timing, blinding)
- Study design features (randomization, allocation concealment)

**SOPs**: data-extraction-form

### Stage 5: Quality Annotation

Annotate each extracted effect size with quality indicators.

- Intention-to-treat vs per-protocol
- Handling of missing data (complete case, imputation)
- Outcome measurement reliability
- Potential for selective reporting (registered vs reported)
- Confidence in the extracted value (high/medium/low)

**SOPs**: risk-of-bias-assessment

## Minimum Yield

Per execution of this tactic:
- At least 5 studies processed
- At least 5 effect sizes extracted or calculation planned
- All moderator variables recorded for extracted studies
- Quality annotation complete for all extractions

## Output Format

```yaml
extractions:
  - study_id: [identifier]
    effect_size_type: [SMD/OR/RR/MD/r]
    point_estimate: [value or calculation formula]
    precision: [SE/CI/variance]
    sample_size: [N_treatment, N_control]
    conditions: [moderator variables]
    quality: [high/medium/low confidence]
    notes: [calculation method, assumptions]
```
