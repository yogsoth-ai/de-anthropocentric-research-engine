---
name: coverage-scoring
description: Compute coverage completeness, redundancy, and gap severity scores from a coverage map.
execution: subagent
prompt: ./prompt.md
input: coverage_map
used-by: portfolio-optimization
---

# Coverage Scoring

Compute quantitative scores for portfolio coverage completeness, redundancy levels, and gap severity from the candidate-to-niche coverage map.

## Execution

Spawns a subagent that applies scoring algorithms to the coverage map and produces actionable metrics.

## Why Subagent

Scoring requires consistent application of metrics across the full coverage map with attention to edge cases (partial coverage, weighted importance). Focused execution ensures no niches are overlooked.

## HARD-GATE

Output must include a numeric coverage score (0-1), redundancy score (0-1), and severity-ranked gap list. All scores must be justified with methodology.
