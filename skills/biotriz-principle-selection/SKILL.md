---
name: biotriz-principle-selection
description: Select applicable BioTRIZ principles for a given contradiction. Map to
  biological cases.
execution: subagent
prompt: ./prompt.md
input: contradiction_description (string)
dependencies:
  sops:
  - spawn-agent
---

# BioTRIZ Principle Selection

Select applicable BioTRIZ principles for a given contradiction.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

BioTRIZ principle selection requires knowledge of the biological 40 principles, the bio contradiction matrix, and the ability to find relevant biological cases. Benefits from focused specialist attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
