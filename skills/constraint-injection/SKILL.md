---
name: constraint-injection
description: Inject artificial constraints to force creative divergence. Generates
  and applies constraints (resource, time, material, audience, scale) to existing
  ideas to produce variants.
execution: subagent
prompt: ./prompt.md
input: problem_or_idea (string), constraint_type (string)
dependencies:
  sops:
  - spawn-agent
---

# Constraint Injection

Inject artificial constraints to force creative divergence.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Constraint injection requires generating appropriate constraints AND then reasoning about how to satisfy the problem under those constraints. The two-phase process benefits from dedicated attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
