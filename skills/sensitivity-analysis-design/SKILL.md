---
name: sensitivity-analysis-design
description: Design leave-one-out, influence diagnostics, subgroup analyses, and robustness checks
execution: subagent
prompt: ./prompt.md
input: included_studies, potential_outliers, subgroup_variables
used-by: meta-analysis
---

# Sensitivity Analysis Design SOP

Design comprehensive sensitivity analyses to test the robustness of meta-analytic conclusions under different assumptions and exclusion criteria.

## When to Use

- After primary analysis plan is established
- When outliers or influential studies are identified
- When methodological decisions could affect conclusions

## Input

- `included_studies`: List of included studies with characteristics
- `potential_outliers`: Studies flagged as potential outliers or influential cases
- `subgroup_variables`: Variables for pre-specified subgroup analyses

## Output

Complete sensitivity analysis plan specifying each analysis, its rationale, and interpretation framework.
