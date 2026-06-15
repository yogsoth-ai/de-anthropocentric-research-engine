---
name: niche-coverage-analysis
description: Define niches within the solution space, map candidates to niches, score
  coverage completeness, and identify gaps requiring attention.
execution: tactic
dependencies:
  sops:
  - coverage-scoring
  - niche-definition
  - niche-mapping
---

# Niche Coverage Analysis

Systematically define the niches or capability areas that a portfolio should cover, map candidates to those niches, and score how well the current selection covers the space.

## Stages

| Stage | SOP | Purpose |
|-------|-----|---------|
| 1 | niche-definition | Define niches and capability areas to cover |
| 2 | niche-mapping | Map each candidate to its covered niches |
| 3 | coverage-scoring | Score coverage, redundancy, and gap severity |

## Available SOPs

- **niche-definition** — Identify and describe the niches the portfolio should span
- **niche-mapping** — Assign candidates to niches, noting partial vs full coverage
- **coverage-scoring** — Compute coverage metrics and prioritize gaps

## Execution Guidance

1. Define niches based on domain structure, user needs, or capability taxonomy
2. Aim for 4-10 niches that are mutually distinct and collectively exhaustive
3. Map candidates honestly — a candidate may cover multiple niches partially
4. Score coverage as fraction of niches with at least one strong candidate
5. Flag gaps (uncovered niches) with severity based on importance
6. Identify redundancy where multiple candidates cover the same niche

## Minimum Yield

- Coverage map showing candidate-to-niche assignments
- Gap analysis identifying uncovered or under-covered niches with severity ratings
- Diversity score (0-1) summarizing overall portfolio coverage
