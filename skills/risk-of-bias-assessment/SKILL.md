---
name: risk-of-bias-assessment
description: Assess methodological bias using RoB2, PROBAST, or QUADAS-2 validated
  tools
execution: subagent
prompt: ./prompt.md
input: study_metadata, study_design
dependencies:
  sops:
  - spawn-agent
---

# Risk of Bias Assessment SOP

Conduct structured risk-of-bias assessment for individual studies using the appropriate validated tool (RoB 2.0, ROBINS-I, QUADAS-2, PROBAST, or Newcastle-Ottawa Scale).

## When to Use

- During quality assessment of each included study
- When deciding sensitivity analysis groupings
- When assessing GRADE certainty (risk of bias domain)

## Input

- `study_metadata`: Study characteristics, methods description, and results
- `study_design`: The study design (RCT, non-randomized, diagnostic, prediction model, observational)

## Output

Domain-level risk-of-bias judgments with supporting rationale for each signaling question.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
