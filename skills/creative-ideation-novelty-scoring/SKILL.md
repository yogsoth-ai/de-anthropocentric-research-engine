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
