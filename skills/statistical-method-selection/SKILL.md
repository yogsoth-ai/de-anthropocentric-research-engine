---
name: statistical-method-selection
description: "Select appropriate statistical methods for experiment analysis"
version: 1.0.0
category: experiment-execution
type: tactic
used-by: experiment-design
orchestrates:
  - metric-specification
  - sample-size-estimation
---

# Tactic: Statistical Method Selection

## Orchestration Pattern

1. **Assess Data Characteristics** → Determine distribution type, sample size, pairing structure
2. **metric-specification** → Ensure metrics are well-defined and measurable
3. **Select Test Family** → Choose between parametric, non-parametric, or Bayesian
4. **sample-size-estimation** → Power analysis for the selected test
5. **Define Analysis Pipeline** → Pre-register the complete analysis plan

## Decision Criteria

| Condition | Recommended Method |
|-----------|-------------------|
| Normal data, 2 groups, paired | Paired t-test |
| Normal data, 2 groups, unpaired | Welch's t-test |
| Normal data, 3+ groups | ANOVA + post-hoc (Tukey HSD) |
| Non-normal, 2 groups | Wilcoxon signed-rank / Mann-Whitney U |
| Non-normal, 3+ groups | Kruskal-Wallis + Dunn's test |
| Multiple datasets, multiple methods | Friedman + Nemenyi / critical difference |
| Want probability of superiority | Bayesian comparison (Benavoli 2017) |
| Small sample, no distributional assumptions | Permutation test |
| Variance estimation needed | Bootstrap confidence intervals |
| Multiple comparisons | Apply Holm-Bonferroni correction |

## Quality Checks

- Is the test appropriate for the data type (continuous, ordinal, categorical)?
- Are independence assumptions met? (If not, use paired/repeated-measures variants)
- Is the sample size sufficient for the chosen test's power requirements?
- Are multiple comparison corrections applied when testing multiple hypotheses?
- Is the effect size reported alongside p-values?
- Is the significance threshold pre-registered (not chosen post-hoc)?
