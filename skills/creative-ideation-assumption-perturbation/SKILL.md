---
name: assumption-perturbation
description: Perturb each assumption, observe system response. Systematic stress-testing
  of assumptions to reveal fragility and opportunity.
execution: subagent
prompt: ./prompt.md
input: assumption_list (array), system_context (string)
dependencies:
  sops:
  - spawn-agent
---

# Assumption Perturbation

Perturb each assumption, observe system response.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Assumption perturbation requires systematic, methodical testing of each assumption under various perturbation types (negate, weaken, strengthen, delay, reverse). Benefits from dedicated analytical focus to track cascading effects.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
