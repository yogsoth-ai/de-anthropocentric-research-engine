---
name: heterogeneity-source-analysis
description: Identify and classify sources of between-study heterogeneity (clinical,
  methodological, statistical)
execution: subagent
prompt: ./prompt.md
input: study_characteristics, effect_sizes, moderator_candidates
dependencies:
  sops:
  - spawn-agent
---

# Heterogeneity Source Analysis SOP

Systematically identify, classify, and prioritize potential sources of between-study heterogeneity for investigation via subgroup analysis and meta-regression.

## When to Use

- When meta-analysis reveals substantial heterogeneity (I2 > 50%)
- During planning of subgroup analyses and meta-regression
- When assessing the transitivity assumption in network meta-analysis

## Input

- `study_characteristics`: Study-level characteristics and covariates
- `effect_sizes`: Extracted effect sizes showing variation
- `moderator_candidates`: Pre-specified candidate moderator variables

## Output

Classified sources of heterogeneity with investigation priority and statistical analysis plan.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
