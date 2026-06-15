---
name: triz-principle-application
description: Select inventive principles from the contradiction matrix and generate
  concrete solutions for identified contradictions.
execution: subagent
prompt: ./prompt.md
input: contradiction_description (string)
dependencies:
  sops:
  - spawn-agent
---

# TRIZ Principle Application

Apply selected TRIZ inventive principles to generate concrete solutions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Principle application requires deep analogical reasoning — translating abstract TRIZ principles into domain-specific solutions. Benefits from dedicated context that can fully explore each principle's implications.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
