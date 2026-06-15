---
name: risk-balancing
description: Balance portfolio risk and return using Markowitz mean-variance, CVaR,
  Risk parity, and Kelly criterion methods.
dependencies:
  tactics:
  - pareto-frontier-construction
  - scenario-stress-testing
  sops:
  - objective-definition
  - optimization-run
  - pareto-visualization
  - portfolio-evaluation-per-scenario
  - scenario-construction
  - selection-from-frontier
---

# Risk Balancing

## Purpose

Construct a portfolio that achieves acceptable returns while managing downside risk, correlation between failures, and tail events. Applies Markowitz-style thinking beyond finance to any domain with uncertain outcomes.

## When to use

- Candidates have uncertain outcomes with estimable distributions
- Correlation between candidate failures matters
- Downside protection is as important as upside
- Stakeholders have explicit risk tolerance levels

## Budget

| Dimension | Target |
|-----------|--------|
| Candidates evaluated | 8-20 |
| Risk factors modeled | 2-5 |
| Correlation pairs assessed | key pairs |
| Efficient frontier points | >=5 |

## State Ledger

| Field | Type | Description |
|-------|------|-------------|
| candidates | list | Candidates with expected return and risk estimates |
| correlation_matrix | matrix | Pairwise correlation of candidate outcomes |
| risk_tolerance | number | Stakeholder risk appetite parameter |
| efficient_frontier | list | Risk-return trade-off curve |
| selected_portfolio | list | Final allocation balancing risk and return |

## Available Tactics

| Tactic | When |
|--------|------|
| pareto-frontier-construction | Building the efficient frontier (risk vs return) |
| scenario-stress-testing | Testing portfolio under adverse scenarios |

## Available SOPs

| SOP | Purpose |
|-----|---------|
| objective-definition | Define risk and return metrics |
| optimization-run | Compute efficient frontier |
| pareto-visualization | Visualize risk-return trade-off |
| selection-from-frontier | Select portfolio matching risk tolerance |
| scenario-construction | Define stress scenarios |
| portfolio-evaluation-per-scenario | Test portfolio under stress |

## Execution Guidance

1. Define risk and return metrics via objective-definition
2. Estimate expected returns, variances, and correlations for candidates
3. Construct efficient frontier via optimization-run
4. Visualize risk-return trade-off via pareto-visualization
5. Select portfolio matching risk tolerance via selection-from-frontier
6. Optionally stress-test via scenario-stress-testing tactic

## Output Format

```yaml
strategy: risk-balancing
selected_portfolio:
  - candidate: <name>
    allocation_weight: <0-1>
    expected_return: <value>
    risk_contribution: <value>
portfolio_expected_return: <aggregate>
portfolio_risk: <variance or CVaR>
sharpe_ratio: <risk-adjusted return>
method_used: <mean-variance|CVaR|risk-parity|Kelly>
```
