---
name: design-matrix-construction
description: Build the experiment design matrix with proper orthogonality and balance
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: factors with levels, design type, budget constraint
output: complete design matrix with run order
dependencies:
  sops:
  - spawn-agent
---

# SOP: Design Matrix Construction

Build the actual design matrix specifying all experimental runs, including proper orthogonality, balance, and randomized run order.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
