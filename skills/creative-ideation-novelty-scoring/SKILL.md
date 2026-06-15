---
name: novelty-scoring
description: Score ideas on novelty dimensions — structural distance from known solutions,
  conceptual surprise, domain-crossing depth. Produces ranked novelty assessment.
execution: subagent
prompt: ./prompt.md
input: idea_set (string), domain_context (string)
dependencies:
  sops:
  - spawn-agent
---

# Novelty Scoring

Score ideas on multiple novelty dimensions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Novelty assessment requires comparing each idea against the known solution landscape and scoring across multiple dimensions. Benefits from focused analytical attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
