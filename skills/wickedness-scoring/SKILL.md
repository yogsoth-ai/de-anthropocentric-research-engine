---
name: wickedness-scoring
description: Score a problem against Rittel's 10 criteria to determine if it is tame,
  complex, or wicked.
execution: subagent
prompt: ./prompt.md
input: problem_description, context
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete wickedness assessment (10-criterion scoring + classification).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
