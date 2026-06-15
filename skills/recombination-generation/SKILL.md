---
name: recombination-generation
description: Reassemble decomposed system fragments into novel structural arrangements
  that create emergent value.
execution: subagent
prompt: ./prompt.md
input: component_set (string)
dependencies:
  sops:
  - spawn-agent
---

# Recombination Generation

Reassemble decomposed fragments into novel structures.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Recombination requires creative exploration of arrangement possibilities while tracking interface compatibility. Benefits from dedicated context that can systematically explore the combination space without premature convergence.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
