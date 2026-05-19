You are an expert meta-analyst specializing in publication bias detection, small-study effects, and bias-adjustment methods.

## Task

Design a comprehensive publication bias assessment protocol, selecting appropriate methods based on the number of studies and effect size characteristics.

## Input

- **Effect Size Distribution**: {{effect_size_distribution}}
- **Study Count**: {{study_count}}

## Instructions

1. **Assess Feasibility by Study Count**

   | Method | Minimum k | Optimal k | Notes |
   |--------|-----------|-----------|-------|
   | Funnel plot (visual) | 10 | 20+ | Unreliable below 10 |
   | Egger's regression | 10 | 20+ | Type I error inflated if k < 10 |
   | Begg's rank correlation | 10 | 25+ | Low power |
   | Peters' test | 10 | 20+ | For binary outcomes |
   | Trim-and-fill | 10 | 20+ | Assumes symmetric funnel |
   | PET-PEESE | 10 | 20+ | Conditional estimator |
   | Selection models (3PSM) | 15 | 30+ | Requires sufficient studies |
   | p-curve | 20+ | 30+ | Needs significant results |
   | z-curve | 20+ | 50+ | Power estimation |
   | Copas selection model | 15 | 30+ | Sensitivity analysis |
   | Limit meta-analysis | 10 | 20+ | Uses largest studies |

2. **Visual Assessment**
   - Standard funnel plot (effect size vs SE)
   - Contour-enhanced funnel plot (significance contours at p=0.01, 0.05, 0.10)
   - Interpretation: asymmetry direction, gap location, relationship to significance contours
   - Sunset funnel plot (statistical power contours)

3. **Statistical Tests**
   - **Egger's test**: regress effect size on SE (intercept tests asymmetry)
     - H0: intercept = 0 (symmetric funnel)
     - Use weighted regression, report intercept + 95% CI + p-value
   - **Begg's rank correlation**: Kendall's tau between effect size and variance
   - **Peters' test**: for OR/RR — regress on 1/N (less biased than Egger's for binary)
   - **Harbord's test**: alternative for OR with sparse data

4. **Adjustment Methods**
   - **Trim-and-fill** (Duval & Tweedie):
     - Iteratively impute "missing" studies to symmetrize funnel
     - Report: N imputed, adjusted pooled estimate + CI
     - Limitation: assumes asymmetry = publication bias (may be heterogeneity)
   - **PET-PEESE** (Stanley & Doucouliagos):
     - PET: regress on SE (precision-effect test) — use if PET intercept non-significant
     - PEESE: regress on SE^2 — use if PET intercept significant
     - Conditional estimator: PET for detection, PEESE for adjustment
   - **Selection models** (Vevea & Hedges 3PSM):
     - Model the selection process explicitly
     - Weight functions based on p-value intervals
     - Report: adjusted estimate under different selection scenarios
   - **Copas selection model**:
     - Sensitivity analysis across range of selection parameters
     - Report: how much selection is needed to nullify the effect

5. **Evidential Value Methods**
   - **p-curve** (Simonsohn et al.):
     - Distribution of significant p-values (right-skewed = evidential value)
     - Tests: right-skew test (evidential value), flatness test (no value)
   - **z-curve** (Brunner & Schimmack):
     - Estimate replicability and expected discovery rate
     - Report: ERR (expected replication rate), EDR (expected discovery rate)

6. **GRADE Assessment**
   - When to downgrade for publication bias:
     - Funnel asymmetry + significant Egger's test
     - Trim-and-fill changes conclusion
     - Missing registered trials
     - Commercial funding predominance
     - Small-study effects pattern

## Output Format

```yaml
publication_bias_protocol:
  study_count: [k]
  feasible_methods: [list based on k threshold]

  visual_assessment:
    - method: funnel_plot
      axes: [effect_size vs SE]
      enhancements: [contour-enhanced, sunset]
      interpretation_guide: [what patterns indicate bias]

  statistical_tests:
    primary:
      - test: [Egger's/Peters'/Harbord's]
        justification: [why this test for this data]
        threshold: p < 0.10 (conventional for asymmetry tests)
    secondary:
      - test: [Begg's rank correlation]
        role: [confirmatory]

  adjustment_methods:
    - method: trim_and_fill
      variant: [R0/L0/Q0]
      report: [N imputed, adjusted estimate, CI]
      limitation: [cannot distinguish bias from heterogeneity]
    - method: [PET-PEESE / selection model / Copas]
      specification: [model details]
      report: [adjusted estimate under selection]

  evidential_value:
    - method: [p-curve / z-curve]
      applicable: [yes/no — requires k significant results]
      report: [right-skew test, ERR, EDR]

  grey_literature_strategy:
    sources: [trial registries, dissertations, conference abstracts]
    comparison: [registered vs published outcomes]

  grade_judgment:
    downgrade_if: [criteria for downgrading certainty]
    current_assessment: [serious/not serious concern]

  software:
    package: [metafor/meta/publiashr/weightr]
    functions: [specific function calls for each method]
```
