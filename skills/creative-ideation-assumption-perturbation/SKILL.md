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
