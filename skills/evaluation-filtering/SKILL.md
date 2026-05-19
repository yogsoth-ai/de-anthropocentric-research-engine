---
name: evaluation-filtering
description: Multi-dimensional evaluation and tiered filtering of generated ideas. Orchestrates novelty assessment → feasibility check → ranking → selection.
execution: tactic
used-by: structural-deconstruction, cross-domain-discovery, assumption-destruction, biomimicry, synectics, morphological-exploration, lateral-thinking, combinatorial-creativity, perspective-forcing, systematic-enumeration
---

# Evaluation Filtering

Multi-dimensional evaluation and tiered filtering of generated ideas.

## Stages

### Stage 1: Novelty Assessment

Score all ideas on novelty dimensions using novelty-scoring SOP. Assign tier: BREAKTHROUGH / HIGH / MODERATE / INCREMENTAL.

### Stage 2: Feasibility Signal

For HIGH and BREAKTHROUGH tier ideas, assess initial feasibility:
- Technical feasibility (can it be built with known methods?)
- Resource feasibility (reasonable cost/time/expertise?)
- Constraint satisfaction (does it meet stated requirements?)

This is a signal, not a deep validation — that's the convergence repo's job.

### Stage 3: Ranking

Rank ideas by composite score: novelty (0.6) × feasibility signal (0.2) × completeness (0.2).

### Stage 4: Selection

Select top ideas for output. All BREAKTHROUGH ideas pass regardless of feasibility. HIGH ideas pass if feasibility ≥ MEDIUM. MODERATE ideas pass only if they fill a coverage gap.

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Ideas evaluated | all generated ideas |
| Ideas scored on all dimensions | 100% |
| Tier distribution reported | yes |
| Top ideas selected | ≥5 (or all BREAKTHROUGH + HIGH) |

## Available SOPs

| SOP | Role |
|-----|------|
| novelty-scoring | Stage 1 — multi-dimensional novelty assessment |
| constraint-injection | Stage 2 — test feasibility under constraints |
| idea-synthesis | Stage 3 — refine top ideas into complete descriptions |
| saturation-detection | Pre — determine if enough ideas exist to evaluate |
