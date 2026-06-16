---
name: threshold-setting
description: Define minimum acceptable thresholds for each criterion based on context
  and constraints.
execution: subagent
prompt: ./prompt.md
input: criteria (string[]), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Threshold Setting

Set minimum acceptable threshold values for each evaluation criterion, used for non-compensatory screening.

## Execution

Subagent receives criteria list and decision context, determines reasonable minimum thresholds for each criterion.

## Why Subagent

Threshold setting requires reasoning that combines domain knowledge and contextual constraints; independent execution ensures threshold reasonableness and consistency.

## HARD-GATE

Each threshold must include a rationale for its setting, and threshold values must be within the actual value range of that criterion.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
