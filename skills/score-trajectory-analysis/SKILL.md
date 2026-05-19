---
name: score-trajectory-analysis
description: Collect historical scores, fit saturation curves, detect inflection points
execution: tactic
used-by: benchmark-archaeology
---

# Score Trajectory Analysis Tactic

Collect historical SOTA scores for a benchmark, arrange as time-series, fit saturation curves, and detect inflection points indicating phase transitions in benchmark difficulty.

## Stages

### Stage 1: Multi-Source Score Collection

Gather historical scores from multiple sources to build comprehensive timeline.

**Sources** (search in order):
1. Papers With Code leaderboards (primary)
2. Official benchmark leaderboards/websites
3. Individual papers reporting SOTA (via dare-ss, dare-scholar)
4. Blog posts and technical reports (via brave-search, dare-web)

**Per data point, collect**:
- Model name and family
- Score (primary metric)
- Date (publication/release date)
- Paper/source reference
- Model size (parameters) if available
- Training data scale if available

**Minimum**: 10 data points spanning at least 2 years.

### Stage 2: Time-Series Arrangement

- Sort by date
- Compute SOTA envelope (monotonically non-decreasing maximum)
- Identify score jumps > 2 standard deviations
- Note human baseline and theoretical ceiling positions
- Flag suspicious entries (unreplicated claims, withdrawn papers)

### Stage 3: Curve Fitting

Fit multiple saturation models to the SOTA envelope:
- **Logistic**: S(t) = L / (1 + e^(-k(t-t0)))
- **Exponential decay to ceiling**: S(t) = C - (C-S0) * e^(-lambda*t)
- **Linear** (for pre-saturation benchmarks)
- **Piecewise** (for benchmarks with phase transitions)

Report goodness-of-fit (R-squared) for each model. Select best-fit.

### Stage 4: Saturation/Inflection Detection

Classify benchmark status:
- **Pre-saturation**: Linear or early logistic, >20% headroom remaining
- **Approaching**: Mid-logistic, 5-20% headroom, decelerating gains
- **Saturated**: <5% headroom, gains < noise level
- **Supersaturated**: Multiple models at ceiling, benchmark no longer discriminative

Detect inflection points:
- Acceleration phases (new paradigm unlocks rapid progress)
- Deceleration phases (diminishing returns begin)
- Step functions (single breakthrough causes discontinuous jump)

## Output

```yaml
trajectory:
  benchmark: string
  metric: string
  data_points: int
  time_span: string
  sota_envelope:
    - {date, score, model, source}
  best_fit_model: logistic|exponential|linear|piecewise
  fit_r_squared: float
  saturation_status: pre-saturation|approaching|saturated|supersaturated
  headroom: float
  inflection_points:
    - {date, type: acceleration|deceleration|step, cause: string}
  estimated_ceiling: float
  time_to_ceiling: string
```

## Yield Report

| Metric | Minimum |
|--------|---------|
| Data points collected | 10 |
| Sources consulted | 3 |
| Curve models fitted | 3 |
| Saturation classification produced | 1 |
