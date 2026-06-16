---
name: portfolio-optimization
description: 'Strategy: Treat the gap set as an investment portfolio — use risk/return/diversity
  optimization to select the optimal gap portfolio'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: gap-prioritization
tactics:
- scoring-matrix-construction
- priority-sensitivity-testing
sops:
- importance-scoring
- feasibility-scoring
- novelty-scoring
- impact-scoring
- ahp-weighting
- priority-synthesis
dependencies:
  tactics:
  - hypothesis-formation-scoring-matrix-construction
  - priority-sensitivity-testing
  sops:
  - gap-normalization
---

# Portfolio Optimization

Treat the set of research gaps as an investment portfolio: not only assess the value of each individual gap, but also analyze the correlation and complementarity among gaps, selecting the portfolio with the greatest overall return and the most diversified risk.

## When to Use

- The number of gaps is large (20+) and not all can be attacked
- The research team has multiple parallel tracks (can advance several gaps simultaneously)
- A balance between "high risk, high reward" and "robust, deliverable" is needed
- Resources are limited and overall research output must be maximized

## Thinking Framework

**Core principle**: The value of an individual gap is not equal to its marginal contribution within the portfolio.

Draw an analogy between gap portfolio optimization and Markowitz portfolio theory:

**Return**: the expected academic/applied value of the gap (importance × impact)

**Risk**: the uncertainty of the gap (reciprocal of feasibility + reciprocal of technical maturity)

**Correlation**: Do two gaps depend on the same methods, data, or prerequisite work? Highly correlated gaps have a higher probability of failing simultaneously and should receive lower portfolio weight.

**Diversity**: The portfolio should span different subfields, different methodologies, and different time horizons (short-term deliverable + long-term breakthrough).

**Efficient Frontier**: At a given risk level, find the gap portfolio with the greatest return; or at a given return target, find the portfolio with the least risk.

**Key insight**: A medium-value gap with low correlation to other gaps may be more worth including in the portfolio than a high-value but highly correlated gap — because it provides genuine diversification.

## Budget Gate

| Tier | Number of gaps | Correlation analysis | Portfolio size | Final output |
|------|---------|-----------|---------|---------|
| S | 20–30 | Qualitative (high/medium/low) | Select 3–5 | Recommended portfolio + rationale |
| M | 31–50 | Semi-quantitative (correlation matrix) | Select 5–8 | Recommended portfolio + efficient frontier chart + alternative portfolios |
| L | 50+ | Quantitative (method/data overlap) | Select 8–12 | Full portfolio analysis + efficient frontier + risk decomposition |

## Default Reference Flow

1. Call the `gap-normalization` SOP: unify gap format, extract methodology labels and data dependencies
2. Call the four-dimension scoring SOPs in parallel (`importance-scoring`, `feasibility-scoring`, `novelty-scoring`, `impact-scoring`)
3. Call the `scoring-matrix-construction` tactic: build the scoring matrix
4. Build the correlation matrix: analyze the method/data/prerequisite-dependency overlap between gap pairs
5. Compute each gap's return (importance × impact) and risk (1/feasibility)
6. Enumerate candidate portfolios, computing portfolio return and portfolio risk (accounting for correlation)
7. Call the `priority-sensitivity-testing` tactic: test portfolio robustness under different risk preferences
8. Call the `priority-synthesis` SOP: output the recommended portfolio + efficient frontier analysis

## context-checkpoint

Record after each round:
- Each gap's return/risk score
- The correlation matrix (gap pairs × overlap)
- The candidate portfolio list and their portfolio scores
- The recommended portfolio (with selection rationale)
- The efficient frontier description (text or table)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| hypothesis-formation-scoring-matrix-construction | Tactic: orchestrate multi-dimensional scoring SOPs to build a comprehensive assessment matrix for all gaps |
| priority-sensitivity-testing | Tactic: perturb scoring weights to test the robustness of the gap ranking against weight choice |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| gap-normalization | SOP: Unify gaps from different sources into the standard GapRecord format |

<!-- END available-tables (generated) -->
