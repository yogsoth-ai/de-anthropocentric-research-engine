---
name: ballot-collection
description: Gather independent ranking ballots from multiple judges or perspectives
  for a given candidate set.
execution: subagent
prompt: ./prompt.md
input: candidates(array), perspectives(array)
dependencies:
  sops:
  - spawn-agent
---

# Ballot Collection

Collects independent ranking ballots from multiple judges or evaluation perspectives. Each judge produces a complete or partial ranking of the candidates without seeing other judges' rankings.

## Execution

Runs as a subagent. Receives candidates and perspective definitions, returns structured ballots.

## Why Subagent

Each ballot must be generated independently to prevent anchoring. The subagent evaluates from a single perspective without access to other judges' outputs, ensuring genuine independence.

## HARD-GATE

Output MUST contain one ballot per perspective. Each ballot MUST rank all candidates (complete ranking) or explicitly mark unranked candidates. No two ballots may be identical unless perspectives are genuinely indistinguishable.
