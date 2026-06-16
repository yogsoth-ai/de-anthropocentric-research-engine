---
name: distribution-assignment
description: Assign probability distributions to uncertain parameters based on available
  evidence and domain knowledge.
execution: subagent
prompt: ./prompt.md
input: parameter_list, available_evidence
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete distribution assignment pass over a parameter list.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
