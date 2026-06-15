---
name: inclusion-criteria-design
description: Define inclusion/exclusion criteria for systematic study selection in
  meta-analysis
execution: subagent
prompt: ./prompt.md
input: pico_framework, study_types
dependencies:
  sops:
  - spawn-agent
---

# Inclusion Criteria Design SOP

Define rigorous inclusion and exclusion criteria for study selection, ensuring reproducibility and minimizing selection bias.

## When to Use

- After PICO formulation is complete
- Before beginning systematic search
- When refining scope after pilot search reveals too many/few results

## Input

- `pico_framework`: The structured PICO/PECO output from pico-formulation
- `study_types`: Acceptable study designs (RCT, cohort, case-control, cross-sectional, etc.)

## Output

Complete eligibility criteria document with decision rules for borderline cases, suitable for independent screening by multiple reviewers.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
