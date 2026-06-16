---
name: reframing-matrix
description: Reframe the problem from 4 professional perspectives to reveal what each
  discipline would focus on.
execution: subagent
prompt: ./prompt.md
input: problem_statement
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete reframing matrix (4 perspectives) for one problem.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
