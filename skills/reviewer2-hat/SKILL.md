---
name: reviewer2-hat
description: Hostile reviewer perspective — find fatal flaws, logical gaps, and missing
  evidence in a solution.
execution: subagent
prompt: ./prompt.md
input: solution (string)
dependencies:
  sops:
  - spawn-agent
---

# Reviewer 2 Hat

Hostile reviewer perspective: find fatal flaws.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Hostile reviewing requires sustained adversarial reasoning that benefits from dedicated attention and prevents contamination of the constructive ideation context.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
