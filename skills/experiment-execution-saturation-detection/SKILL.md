---
name: saturation-detection
description: 'Shared SOP: detect information saturation — know when to stop searching/analyzing'
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: Current information set + last N rounds of new additions
output: Saturation verdict (saturated/not-saturated) + evidence
dependencies:
  sops:
  - spawn-agent
---

# Saturation Detection

Detect information saturation — know when to stop searching or analyzing.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Saturation assessment requires independent evaluation of marginal information gain, avoiding confirmation bias from the main flow.

## Saturation Criteria

- New information no longer changes conclusions
- New sources repeat existing findings
- Coverage reaches preset threshold
- Marginal information gain falls below threshold

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
