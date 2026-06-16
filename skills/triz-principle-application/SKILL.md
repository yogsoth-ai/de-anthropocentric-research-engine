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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
