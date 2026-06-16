---
name: futures-calibration
description: Aggregate probability judgments across perspectives using Real-Time Delphi
  or prediction market mechanisms.
dependencies:
  tactics:
  - iterative-convergence-round
  - threshold-calibration
  sops:
  - consensus-synthesis
---

# Futures Calibration

**Purpose:** Aggregate probabilistic forecasts from multiple perspectives into calibrated predictions. Uses Real-Time Delphi continuous updating or prediction market scoring to produce well-calibrated probability estimates for future events.

**When to use:**
- Technology timeline estimation
- Market forecasts requiring multiple expert inputs
- Risk probability assessment
- Any question framed as "what is the probability that X by time T?"

## Budget

| Parameter | Constraint |
|-----------|-----------|
| Rounds | 2–3 (continuous updating preferred) |
| Perspectives | ≥4 independent forecasters |
| Calibration target | Brier score improvement across rounds |

## State Ledger

| Key | Type | Description |
|-----|------|-------------|
| question | string | The forecasting question |
| time_horizon | string | When the event would resolve |
| perspectives | array | List of forecaster perspectives |
| rounds | array | History of probability estimates |
| current_aggregate | float | Current aggregated probability |
| calibration_metrics | object | Brier score, log score tracking |

## Available Tactics

- **iterative-convergence-round** — Adapted for probability estimates
- **threshold-calibration** — Determine confidence bands

## Available SOPs

- judgment-collection
- feedback-distribution
- consensus-measurement
- round-decision
- threshold-sweep
- consensus-synthesis

## Execution Guidance

1. Frame question with clear resolution criteria and time horizon
2. Collect initial probability estimates with reasoning
3. Share aggregate and reasoning (anonymized) each round
4. Track whether estimates are converging or polarizing
5. Report final calibrated estimate with confidence interval

## Output Format

```yaml
forecast_question: <question>
time_horizon: <date/period>
calibrated_probability: <float 0-1>
confidence_interval: [lower, upper]
rounds_completed: <int>
convergence_pattern: converging/stable/polarizing
key_considerations: [...]
```

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| iterative-convergence-round | Execute one full Delphi round — collect judgments, distribute anonymous feedback, measure consensus, decide whether to continue. |
| threshold-calibration | Systematically sweep consensus thresholds to observe which items achieve consensus at what level, producing a threshold-consensus curve. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| consensus-synthesis | Synthesize all rounds into a final consensus report documenting agreements, dissent, and process. |

<!-- END available-tables (generated) -->
