---
name: saturation-detection
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
