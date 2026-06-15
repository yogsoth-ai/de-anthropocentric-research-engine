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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
