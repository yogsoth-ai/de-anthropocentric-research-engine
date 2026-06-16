---
name: negation-definition
description: Define strongest plausible alternatives (negations) for each assumption
  to enable perturbation analysis.
execution: subagent
prompt: ./prompt.md
input: assumption_list
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete negation definition pass over an assumption list.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
