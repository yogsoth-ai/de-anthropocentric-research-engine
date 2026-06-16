---
name: effect-size-planning
description: Determine effect size types and calculation methods for meta-analytic
  synthesis
execution: subagent
prompt: ./prompt.md
input: outcome_measures, study_designs
dependencies:
  sops:
  - spawn-agent
---

# Effect Size Planning SOP

Determine the appropriate effect size metric, calculation methods, and conversion formulas for the meta-analysis.

## When to Use

- After inclusion criteria are defined
- Before data extraction begins
- When studies report outcomes in different metrics

## Input

- `outcome_measures`: Types of outcome measures across included studies
- `study_designs`: Study designs present in the evidence base

## Output

Complete effect size specification including primary metric, calculation formulas for each reporting format, and conversion procedures.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
