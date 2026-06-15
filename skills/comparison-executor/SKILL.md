---
name: comparison-executor
description: Execute a pairwise comparison between two candidates, producing a judgment
  with winner, confidence, and reasoning.
execution: subagent
prompt: ./prompt.md
input: pair(array), context(object)
dependencies:
  sops:
  - spawn-agent
---

# Comparison Executor

Executes a single pairwise comparison between two candidates. Produces a structured judgment indicating the winner, confidence level, and detailed reasoning supporting the decision.

## Execution

Runs as a subagent. Receives a pair of candidates and evaluation context, returns a judgment.

## Why Subagent

Each comparison requires focused deliberation on the specific pair without being influenced by prior ranking expectations. Isolation prevents anchoring bias from the current leaderboard.

## HARD-GATE

Output MUST declare exactly one winner from the pair (no ties unless context explicitly permits ties). Confidence MUST be a value in [0.5, 1.0]. Reasoning MUST reference specific attributes of both candidates.
