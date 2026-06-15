---
name: edge-case-generation
description: Systematically generate boundary inputs — boundary values, adversarial
  constructions, distribution shifts, rare combinations, scale extremes.
execution: subagent
prompt: ./prompt.md
input: method_description (string), domain (string)
dependencies:
  sops:
  - spawn-agent
---

# Edge Case Generation

Generate systematic edge cases to probe failures.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one edge case generation pass (minimum 20 cases).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
