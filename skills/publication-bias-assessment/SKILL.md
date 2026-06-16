---
name: publication-bias-assessment
description: Plan funnel plots, Egger's test, trim-and-fill, p-curve, and selection
  model analyses for publication bias
execution: subagent
prompt: ./prompt.md
input: effect_size_distribution, study_count
dependencies:
  sops:
  - spawn-agent
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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
