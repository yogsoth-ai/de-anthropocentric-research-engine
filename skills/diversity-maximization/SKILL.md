---
name: diversity-maximization
description: Maximize portfolio diversity and coverage using MAP-Elites, Niche coverage, Maximum dispersion, and Anti-clustering methods.
used-by: portfolio-optimization
---

# Diversity Maximization

## Purpose

Select a portfolio that maximizes coverage across the solution space, avoiding redundancy and ensuring representation of distinct approaches, domains, or capabilities.

## When to use

- Redundancy between candidates is a concern
- Coverage of different niches or capabilities matters
- Innovation portfolio needs variety of approaches
- Hedging through diversity rather than risk modeling

## Budget

| Dimension | Target |
|-----------|--------|
| Candidates evaluated | 8-20 |
| Niches defined | 4-10 |
| Diversity dimensions | 2-5 |
| Coverage threshold | >=80% of defined niches |

## State Ledger

| Field | Type | Description |
|-------|------|-------------|
| candidates | list | All candidates with feature vectors |
| niches | list | Defined niches or capability areas |
| coverage_map | matrix | Which candidates cover which niches |
| diversity_score | number | Aggregate diversity metric |
| gaps | list | Uncovered or under-covered niches |

## Available Tactics

| Tactic | When |
|--------|------|
| niche-coverage-analysis | Need to map and score coverage systematically |
| pareto-frontier-construction | Trading off diversity against cost or value |

## Available SOPs

| SOP | Purpose |
|-----|---------|
| niche-definition | Define the niches to cover |
| niche-mapping | Map candidates to niches |
| coverage-scoring | Score how well portfolio covers space |
| objective-definition | Define diversity objectives formally |

## Execution Guidance

1. Define the diversity dimensions and niches via niche-definition
2. Map all candidates to niches via niche-mapping
3. Score current coverage and identify gaps via coverage-scoring
4. Select portfolio that maximizes coverage while respecting constraints
5. If value also matters, use pareto-frontier-construction to trade off

## Output Format

```yaml
strategy: diversity-maximization
selected_portfolio:
  - candidate: <name>
    niches_covered: [<niche1>, <niche2>]
coverage_score: <0-1>
redundancy_score: <0-1>
gaps_remaining:
  - niche: <name>
    severity: <high|medium|low>
method_used: <MAP-Elites|niche-coverage|max-dispersion>
```
