---
name: ishikawa-decomposition
description: Decompose problems into 6M categories (Methodology, Data, Theory, Measurement,
  Researchers, Environment) via fishbone diagram analysis.
execution: subagent
prompt: ./prompt.md
input: problem_statement (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Ishikawa Decomposition

Multi-factor causal decomposition via fishbone diagram.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one Ishikawa decomposition pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
