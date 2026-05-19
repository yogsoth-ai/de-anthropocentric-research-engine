---
name: socratic-probing
description: Apply 6 types of Socratic questions to test claims and assumptions. Exposes weaknesses and strengthens reasoning.
execution: subagent
prompt: ./prompt.md
input: claim_or_assumption (string), context (string)
used-by: question-reformulation
---

# Socratic Probing

Test claims via systematic Socratic questioning.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one Socratic probing pass.
