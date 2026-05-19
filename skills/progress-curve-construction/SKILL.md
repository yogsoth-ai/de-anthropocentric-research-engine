---
name: progress-curve-construction
description: Build performance-over-time progress curves with inflection detection
execution: tactic
used-by: baseline-establishment
---

# Progress Curve Construction


## Purpose

Transform historical performance data into temporal progress curves that reveal the rate of improvement, paradigm shifts, and saturation trends. Enables quantitative headroom analysis and identifies where the field needs breakthroughs vs. incremental refinement.

## Stages

### Stage 1: Time-Series Arrangement

Organize all historical scores into chronological sequences:
- Group by (dataset, metric) pairs
- Assign dates from paper publication or submission
- Track the SOTA frontier (envelope of best scores over time)
- Identify the method responsible for each SOTA advance

**Yield**: Chronological score sequences per benchmark.

### Stage 2: Curve Fitting

Fit parametric models to the SOTA frontier:
- Logarithmic: diminishing returns pattern
- Linear: steady improvement
- Sigmoid: approaching saturation
- Stepped: punctuated equilibrium (paradigm shifts)
- Compute goodness-of-fit metrics for model selection

**Yield**: Fitted curves with parameters and confidence bands.

### Stage 3: Inflection Point Detection

Identify moments where progress rate changed significantly:
- Sudden jumps (new method family introduced)
- Slowdowns (approaching ceiling)
- Acceleration (new paradigm unlocking faster progress)
- Correlate inflection points with methodological innovations

**Yield**: Annotated inflection points with causal attribution.

### Stage 4: Headroom Estimation

Quantify remaining improvement potential:
- Human performance ceiling (where applicable)
- Theoretical bounds (information-theoretic, Bayes-optimal)
- Practical ceiling (best possible with current paradigm)
- Rate-based extrapolation (when will SOTA reach X?)

**Yield**: Headroom estimates with confidence intervals.

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Progress curves constructed | 2 |
| Years of history covered | 3 |
| Inflection points identified | 1 |
| Headroom estimates produced | 2 |

## SOPs Used

- progress-curve-fitting (for Stages 2-3)
- headroom-estimation (for Stage 4)
- baseline-synthesis (for final integration)
