---
name: convergence-saturation-detection
description: Determines when to stop iterating — coverage threshold met or marginal
  returns diminishing. Shared across all campaigns.
execution: subagent
prompt: ./prompt.md
input: iteration_data[], threshold (float)
dependencies:
  sops:
  - spawn-agent
---

# Saturation Detection

Determines when an iterative convergence process has reached diminishing returns and should stop.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Saturation detection requires analyzing trends across multiple iterations with fresh analytical perspective. Dedicated context prevents anchoring to earlier iterations.

## HARD-GATE

Must have ≥3 data points before declaring saturation. A single iteration cannot trigger a stop decision.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
