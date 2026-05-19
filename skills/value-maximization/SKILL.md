---
name: value-maximization
description: Maximize total portfolio value within constraints using Knapsack, Linear programming, Cost-benefit analysis, and NPV ranking methods.
used-by: portfolio-optimization
---

# Value Maximization

## Purpose

Select the portfolio subset that maximizes aggregate value (ROI, impact, utility) subject to resource constraints. Applies when the primary goal is getting the most out of a limited budget.

## When to use

- Fixed budget with many candidate investments
- Clear value metrics exist for each candidate
- Constraints are well-defined (cost, time, capacity)
- Goal is maximum total return, not diversity or risk management

## Budget

| Dimension | Target |
|-----------|--------|
| Candidates evaluated | 8-20 |
| Constraints modeled | 1-5 |
| Value metrics | 1-3 per candidate |
| Solutions compared | >=5 |

## State Ledger

| Field | Type | Description |
|-------|------|-------------|
| candidates | list | All candidate items with value and cost attributes |
| constraints | list | Budget, capacity, or other binding constraints |
| objective_function | string | How value is aggregated (sum, weighted sum, etc.) |
| optimal_solution | list | Selected portfolio maximizing value |
| value_achieved | number | Total value of selected portfolio |

## Available Tactics

| Tactic | When |
|--------|------|
| pareto-frontier-construction | Multiple value dimensions to trade off |

## Available SOPs

| SOP | Purpose |
|-----|---------|
| objective-definition | Define what "value" means and what constraints bind |
| optimization-run | Run the optimization to find best portfolios |
| pareto-visualization | Visualize value trade-offs if multi-objective |
| selection-from-frontier | Pick final portfolio from candidates |

## Execution Guidance

1. Define value metric(s) and constraints via objective-definition
2. If single objective: solve as knapsack/LP directly
3. If multiple objectives: use pareto-frontier-construction tactic
4. Select from frontier based on stakeholder preferences
5. Validate selected portfolio against all constraints

## Output Format

```yaml
strategy: value-maximization
selected_portfolio:
  - candidate: <name>
    value: <score>
    cost: <cost>
total_value: <aggregate>
total_cost: <aggregate>
constraint_slack: <remaining budget>
method_used: <knapsack|LP|NPV>
confidence: <high|medium|low>
```
