---
name: reversal-generation
description: Systematically reverse positive statements to generate creative inversions.
  Produces reversed statements with initial associations.
execution: subagent
prompt: ./prompt.md
input: statement_list (array), reversal_depth (string)
dependencies:
  sops:
  - spawn-agent
---

# Reversal Generation

Systematically reverse positive statements.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Reversal generation requires creative linguistic and conceptual inversion across multiple dimensions. Benefits from dedicated attention to produce both obvious negations and surprising creative reversals.
