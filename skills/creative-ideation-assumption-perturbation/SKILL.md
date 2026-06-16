---
name: creative-ideation-assumption-perturbation
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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
