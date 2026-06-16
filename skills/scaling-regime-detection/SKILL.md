---
name: scaling-regime-detection
description: Detect regime changes in scaling behavior — breakpoints where behavior
  qualitatively shifts, mechanisms behind transitions.
execution: subagent
prompt: ./prompt.md
input: performance_data (string), scale_dimensions (string)
dependencies:
  sops:
  - spawn-agent
---

# Scaling Regime Detection

Detect where scaling behavior qualitatively changes.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one scaling regime analysis.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
