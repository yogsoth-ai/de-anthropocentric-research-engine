---
name: perspective-attack
description: Attack a decision from a specific assigned perspective, producing rated
  arguments and constructive alternatives.
execution: subagent
prompt: ./prompt.md
input: decision, perspective_brief
dependencies:
  sops:
  - spawn-agent
---

# Perspective Attack

Executes an attack on the decision from a specific assigned perspective. The attacker fully inhabits the perspective's values and concerns, finding every legitimate objection and proposing alternatives that would better serve that perspective's interests.

## Execution

Spawns a subagent that adopts the assigned perspective and attacks the decision from that viewpoint.

## Why Subagent

- Each perspective attack must be fully committed to its viewpoint
- Isolation prevents cross-contamination between perspectives
- The attacker must genuinely inhabit the role, not simulate it superficially

## HARD-GATE

Output must include:
- >= 2 distinct attacks grounded in the perspective's values
- Severity rating for each attack
- At least 1 constructive alternative (not just criticism)
- Attacks must be consistent with the assigned perspective (not generic)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
