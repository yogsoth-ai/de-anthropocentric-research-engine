---
name: appreciative-discovery
description: Search for positive deviants and extract transferable principles using
  Appreciative Inquiry.
execution: subagent
prompt: ./prompt.md
input: problem_domain
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete appreciative discovery (positive deviants + enabling conditions + principles).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
