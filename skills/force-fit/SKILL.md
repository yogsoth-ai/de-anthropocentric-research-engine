---
name: force-fit
description: Force-fit excursion discoveries back to the original problem. Deliberately
  create connections between unrelated findings and the challenge.
execution: subagent
prompt: ./prompt.md
input: excursion_discoveries (string), original_problem (string)
dependencies:
  sops:
  - spawn-agent
---

# Force-Fit

Force-fit excursion discoveries back to the original problem.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Force-fitting requires holding two unrelated domains in mind simultaneously and deliberately creating connections that don't naturally exist. Benefits from focused creative tension without premature judgment.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
