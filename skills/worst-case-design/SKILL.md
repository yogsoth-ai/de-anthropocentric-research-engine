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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
