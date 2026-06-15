---
name: sacred-cow-identification
description: Find domain's unquestioned beliefs. Systematic identification of dogma
  that constrains innovation.
execution: subagent
prompt: ./prompt.md
input: domain_description (string), known_practices (string)
dependencies:
  sops:
  - spawn-agent
---

# Sacred Cow Identification

Find domain's unquestioned beliefs.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Sacred cow identification requires deep domain analysis and the ability to distinguish between well-justified constraints and mere tradition. Benefits from dedicated critical thinking without solution-generation pressure.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
