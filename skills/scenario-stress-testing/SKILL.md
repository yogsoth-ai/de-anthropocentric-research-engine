---
name: scenario-stress-testing
description: Construct distinct future scenarios, evaluate portfolio performance under
  each, and identify vulnerabilities and robustness characteristics.
execution: tactic
dependencies:
  sops:
  - portfolio-evaluation-per-scenario
  - portfolio-synthesis
  - scenario-construction
---

# Scenario Stress Testing

Evaluate how a portfolio performs across multiple plausible future scenarios to identify vulnerabilities, assess robustness, and inform portfolio adjustments.

## Stages

| Stage | SOP | Purpose |
|-------|-----|---------|
| 1 | scenario-construction | Construct >=3 distinct future scenarios |
| 2 | portfolio-evaluation-per-scenario | Evaluate portfolio under each scenario |
| 3 | portfolio-synthesis | Synthesize findings into robustness verdict |

## Available SOPs

- **scenario-construction** — Build diverse, plausible scenarios spanning uncertainty space
- **portfolio-evaluation-per-scenario** — Assess portfolio metrics under a specific scenario
- **portfolio-synthesis** — Aggregate per-scenario results into final recommendation

## Execution Guidance

1. Construct at least 3 scenarios that are distinct and span key uncertainties
2. Include at least one optimistic, one pessimistic, and one surprising scenario
3. Evaluate the same portfolio under each scenario using consistent metrics
4. Look for scenarios where portfolio performance drops below acceptable thresholds
5. Identify which candidates are vulnerable vs resilient across scenarios
6. Synthesize into robustness score and actionable recommendations

## Minimum Yield

- Performance assessment across >=3 distinct scenarios
- Vulnerability list identifying which portfolio elements fail under which conditions
- Robustness verdict (robust / conditionally robust / fragile) with supporting evidence

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| portfolio-evaluation-per-scenario | Evaluate a specific portfolio's performance metrics and vulnerabilities under a given scenario. |
| portfolio-synthesis | Synthesize all per-scenario evaluations into a final portfolio recommendation with robustness score and actionable guidance. |
| scenario-construction | Construct distinct future scenarios spanning key uncertainties for portfolio stress testing. |

<!-- END available-tables (generated) -->
