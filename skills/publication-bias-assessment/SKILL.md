---
name: publication-bias-assessment
description: Plan funnel plots, Egger's test, trim-and-fill, p-curve, and selection model analyses for publication bias
execution: subagent
prompt: ./prompt.md
input: effect_size_distribution, study_count
used-by: meta-analysis
---

# Publication Bias Assessment SOP

Design the complete publication bias detection and adjustment protocol using visual, statistical, and model-based methods.

## When to Use

- After effect sizes are extracted (need precision estimates)
- When assessing GRADE certainty (publication bias domain)
- When deciding whether pooled estimate may be inflated

## Input

- `effect_size_distribution`: Summary of extracted effect sizes and their precision
- `study_count`: Number of included studies (determines which methods are feasible)

## Output

Complete publication bias assessment protocol with method selection justified by study count and data characteristics.
