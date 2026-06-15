---
name: alternative-scoring
description: Score each candidate alternative against all criteria to produce a score
  matrix.
execution: subagent
prompt: ./prompt.md
input: candidates (string[]), criteria (string[]), weights (number[])
dependencies:
  sops:
  - spawn-agent
---

# Alternative Scoring

Score candidate alternatives against each criterion to produce a complete scoring matrix (alternatives x criteria).

## Execution

Subagent receives candidate list, criteria definitions, and weight vector, scores each alternative on each criterion, and outputs the scoring matrix.

## Why Subagent

Scoring requires analyzing each alternative individually, involves significant workload and needs consistent scoring standards; independent execution prevents score drift.

## HARD-GATE

Scoring matrix must have no empty values, each score must include a brief rationale (1 sentence), and quantitative criteria must use actual data.
