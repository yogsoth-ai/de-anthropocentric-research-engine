---
name: optimization-run
description: Execute multi-objective optimization on candidates to produce a Pareto front of non-dominated solutions.
execution: subagent
prompt: ./prompt.md
input: candidates, objectives, constraints
used-by: portfolio-optimization
---

# Optimization Run

Execute multi-objective optimization over the candidate set given defined objectives and constraints, producing a Pareto front of non-dominated solutions.

## Execution

Spawns a subagent that applies optimization logic to enumerate, evaluate, and filter candidate portfolios, returning the non-dominated set.

## Why Subagent

Optimization requires systematic enumeration or heuristic search across the combinatorial space of possible portfolios. This computational work is self-contained and produces a well-defined output structure.

## HARD-GATE

Output must contain at least 5 non-dominated solutions on the Pareto front. If the candidate set is too small or constraints too tight, report the maximum achievable frontier size with explanation.
