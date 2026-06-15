---
name: robustness-under-uncertainty
description: Select portfolios that perform well across multiple future scenarios
  using Minimax regret, Robust optimization, Scenario planning, and Info-gap methods.
dependencies:
  tactics:
  - pareto-frontier-construction
  - scenario-stress-testing
  sops:
  - objective-definition
  - optimization-run
  - portfolio-evaluation-per-scenario
  - portfolio-synthesis
  - scenario-construction
---

# Robustness Under Uncertainty

## Purpose

Select a portfolio that performs acceptably well across a range of plausible futures, rather than optimizing for a single expected scenario. Prioritizes resilience over peak performance.

## When to use

- Future conditions are highly uncertain
- Multiple plausible scenarios with different implications
- Catastrophic failure in any scenario is unacceptable
- Stakeholders prefer robustness over maximum expected value
- Cannot assign reliable probabilities to scenarios

## Budget

| Dimension | Target |
|-----------|--------|
| Candidates evaluated | 8-20 |
| Scenarios constructed | >=3 distinct futures |
| Performance metrics | 2-4 per scenario |
| Robustness threshold | acceptable in all scenarios |

## State Ledger

| Field | Type | Description |
|-------|------|-------------|
| candidates | list | All candidates with scenario-dependent performance |
| scenarios | list | Distinct future scenarios |
| performance_matrix | matrix | Candidate performance per scenario |
| regret_matrix | matrix | Regret vs best-in-scenario for each candidate |
| robust_portfolio | list | Portfolio minimizing worst-case regret |

## Available Tactics

| Tactic | When |
|--------|------|
| scenario-stress-testing | Core tactic — evaluate across scenarios |
| pareto-frontier-construction | Trade off robustness vs expected value |

## Available SOPs

| SOP | Purpose |
|-----|---------|
| scenario-construction | Build distinct future scenarios |
| portfolio-evaluation-per-scenario | Evaluate portfolio in each scenario |
| portfolio-synthesis | Synthesize robust recommendation |
| objective-definition | Define robustness criteria |
| optimization-run | Find minimax-regret or robust solutions |

## Execution Guidance

1. Construct diverse scenarios spanning the uncertainty space
2. Evaluate each candidate portfolio under each scenario
3. Compute regret matrix (gap vs best possible in each scenario)
4. Find portfolio minimizing maximum regret (minimax regret)
5. Alternatively: find portfolio meeting minimum threshold in all scenarios
6. Report robustness score and vulnerability analysis

## Output Format

```yaml
strategy: robustness-under-uncertainty
selected_portfolio:
  - candidate: <name>
    worst_case_performance: <value>
    best_case_performance: <value>
robustness_score: <0-1>
max_regret: <value>
vulnerable_scenarios:
  - scenario: <name>
    performance: <value>
    gap_to_best: <value>
method_used: <minimax-regret|robust-optimization|info-gap>
```
