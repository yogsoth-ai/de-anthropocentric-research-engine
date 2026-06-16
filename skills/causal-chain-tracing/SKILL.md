---
name: causal-chain-tracing
description: Trace UDE to root cause via IF...THEN...BECAUSE logic chains
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: numbered UDE list with evidence
output: causal tree with IF-THEN-BECAUSE chains converging to root causes
dependencies:
  sops:
  - spawn-agent
---

# SOP: Causal Chain Tracing

Trace each Undesirable Effect backward through causal chains using IF...THEN...BECAUSE logic to find root causes and convergence points.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
