---
name: evidence-synthesis-planning
description: Plan the statistical synthesis approach — model selection, heterogeneity strategy, and reporting
execution: tactic
used-by: meta-analysis
---

# Evidence Synthesis Planning Tactic

Plan the complete statistical synthesis approach: effect size standardization, model selection, heterogeneity quantification, sensitivity analyses, and PRISMA-compliant reporting.

## Stages

### Stage 1: Effect Size Type Determination

Determine the appropriate effect size metric for the synthesis.

| Outcome Type | Effect Size | When |
|--------------|-------------|------|
| Continuous (same scale) | Mean Difference (MD) | All studies use same measurement |
| Continuous (different scales) | Standardized Mean Difference (SMD) | Studies use different instruments |
| Binary | Odds Ratio (OR) / Risk Ratio (RR) | Dichotomous outcomes |
| Time-to-event | Hazard Ratio (HR) | Survival data |
| Correlation | Fisher's z (transformed r) | Association studies |
| Count/rate | Incidence Rate Ratio (IRR) | Event rate data |

**SOPs**: effect-size-planning

### Stage 2: Model Selection

Choose between fixed-effect and random-effects models.

- **Fixed-effect** (Mantel-Haenszel, Inverse Variance): assumes one true effect, studies estimate same parameter
- **Random-effects** (DerSimonian-Laird, REML, Paule-Mandel, Knapp-Hartung): assumes distribution of true effects
- **Decision criteria**: clinical/methodological diversity, number of studies, intended inference scope
- **Knapp-Hartung adjustment**: recommended when k < 20 studies

**Decision tree**: If studies are clinically homogeneous AND methodologically identical → fixed-effect. Otherwise → random-effects with REML + Knapp-Hartung.

### Stage 3: Heterogeneity Strategy

Plan heterogeneity quantification and investigation.

- **Quantification**: I2 (proportion), tau2 (absolute), H2, prediction interval
- **Testing**: Cochran's Q (detection), confidence intervals for I2
- **Investigation**: pre-specified subgroups, meta-regression (if k >= 10)
- **Thresholds**: I2 interpretation (0-40% low, 30-60% moderate, 50-90% substantial, 75-100% considerable)

**SOPs**: heterogeneity-source-analysis

### Stage 4: Sensitivity Design

Design robustness checks for the primary analysis.

- Leave-one-out analysis (influence of individual studies)
- Influence diagnostics (Cook's distance, DFFITS, hat values)
- Subgroup analyses (pre-specified moderators only)
- Alternative model (fixed vs random comparison)
- Alternative effect size (OR vs RR, SMD vs MD)
- Excluding high risk-of-bias studies

**SOPs**: sensitivity-analysis-design

### Stage 5: Reporting Plan

Design PRISMA-2020 compliant reporting.

- PRISMA flow diagram (identification, screening, eligibility, inclusion)
- Forest plot specifications (study labels, weights, diamonds)
- Summary of findings table (GRADE certainty)
- Heterogeneity reporting (I2, tau2, prediction interval)
- Sensitivity analysis presentation
- Protocol registration (PROSPERO)

## Minimum Yield

Per execution of this tactic:
- Effect size type justified and documented
- Model selection with explicit rationale
- Heterogeneity quantification plan complete
- At least 3 sensitivity analyses designed
- PRISMA reporting checklist addressed

## Output Format

```yaml
synthesis_plan:
  effect_size:
    type: [SMD/OR/RR/MD/HR/z]
    justification: [why this metric]
    conversions_needed: [any transformations]
  model:
    type: [fixed-effect/random-effects]
    estimator: [IV/MH/REML/DL/PM]
    adjustment: [Knapp-Hartung/none]
    justification: [rationale]
  heterogeneity:
    metrics: [I2, tau2, Q, prediction interval]
    investigation:
      subgroups: [list of categorical moderators]
      meta_regression: [list of continuous moderators]
      minimum_k_per_subgroup: [threshold]
  sensitivity:
    - leave_one_out
    - influence_diagnostics
    - alternative_model
    - rob_exclusion
    - [additional pre-specified]
  reporting:
    standard: PRISMA-2020
    registration: [PROSPERO ID or plan]
    grade_domains: [risk_of_bias, inconsistency, indirectness, imprecision, publication_bias]
```
