---
name: data-extraction-form
description: Design structured data extraction form for systematic meta-analysis data
  collection
execution: subagent
prompt: ./prompt.md
input: pico_framework, effect_size_type, moderator_variables
dependencies:
  sops:
  - spawn-agent
---

# Data Extraction Form SOP

Design a structured, comprehensive data extraction form tailored to the specific meta-analysis, ensuring all necessary data points are captured systematically.

## When to Use

- After PICO, inclusion criteria, and effect size type are determined
- Before beginning full data extraction from included studies
- When standardizing extraction across multiple reviewers

## Input

- `pico_framework`: The structured PICO/PECO framework
- `effect_size_type`: The chosen effect size metric and calculation methods
- `moderator_variables`: Pre-specified moderator variables for heterogeneity investigation

## Output

A complete data extraction form with field definitions, coding instructions, and examples for each variable.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
