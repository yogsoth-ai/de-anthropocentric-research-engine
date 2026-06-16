---
name: sensitivity-analysis-design
description: Design leave-one-out, influence diagnostics, subgroup analyses, and robustness
  checks
execution: subagent
prompt: ./prompt.md
input: included_studies, potential_outliers, subgroup_variables
dependencies:
  sops:
  - spawn-agent
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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
