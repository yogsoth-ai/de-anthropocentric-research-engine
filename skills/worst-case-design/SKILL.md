---
name: worst-case-design
description: Design the worst possible solution. Deliberate failure engineering to
  reveal hidden constraints and inversion opportunities.
execution: subagent
prompt: ./prompt.md
input: problem (string), constraints (string)
dependencies:
  sops:
  - spawn-agent
---

# Worst-Case Design

Design the worst possible solution.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Worst-case design requires creative perversity — deliberately optimizing for failure across multiple dimensions. Benefits from dedicated focus to produce genuinely terrible solutions (not just mediocre ones) that yield rich inversion material.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
