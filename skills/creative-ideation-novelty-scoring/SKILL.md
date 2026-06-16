---
name: creative-ideation-novelty-scoring
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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
