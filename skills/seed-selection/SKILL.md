---
name: seed-selection
description: Validate and prioritize starting papers for snowball surveys. Evaluates which seeds will yield the richest citation traces based on citation count, recency, and network position.
execution: subagent
prompt: ./prompt.md
input: seed_papers (string), context (string)
used-by: literature-survey
---

# Seed Selection

Validate and prioritize starting papers for snowball surveys.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Seed evaluation requires analyzing citation networks and making strategic judgments about which papers will yield the richest traces. Dedicated context for this analytical work.
