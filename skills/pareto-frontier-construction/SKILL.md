---
name: pareto-frontier-construction
description: Build the Pareto frontier from multi-objective optimization, visualize
  trade-offs, and select a portfolio from non-dominated solutions.
execution: tactic
dependencies:
  sops:
  - objective-definition
  - optimization-run
  - pareto-visualization
  - selection-from-frontier
---

# Pareto Frontier Construction

Systematically construct the set of non-dominated solutions across multiple objectives, visualize the trade-off surface, and guide selection of a final portfolio from the frontier.

## Stages

| Stage | SOP | Purpose |
|-------|-----|---------|
| 1 | objective-definition | Define objectives, constraints, and trade-off preferences |
| 2 | optimization-run | Run multi-objective optimization to generate Pareto front |
| 3 | pareto-visualization | Visualize the frontier and trade-off relationships |
| 4 | selection-from-frontier | Select final portfolio based on preferences |

## Available SOPs

- **objective-definition** — Translate context into formal objectives and constraints
- **optimization-run** — Execute optimization producing non-dominated solution set
- **pareto-visualization** — Create visual representation of trade-off surface
- **selection-from-frontier** — Apply preference model to select from frontier

## Execution Guidance

1. Start with objective-definition to formalize what is being optimized
2. Ensure at least 2 competing objectives exist (otherwise no frontier needed)
3. Run optimization-run to generate >=5 non-dominated points
4. Visualize to help stakeholders understand trade-offs
5. Apply stated preferences to select final portfolio
6. If preferences are unclear, present 3 representative points (extremes + balanced)

## Minimum Yield

- Pareto front with >=5 non-dominated points
- Trade-off visualization showing objective tensions
- Selected portfolio with explicit justification referencing frontier position

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| objective-definition | Define optimization objectives, constraints, and trade-off preferences from context and candidate information. |
| optimization-run | Execute multi-objective optimization on candidates to produce a Pareto front of non-dominated solutions. |
| pareto-visualization | Create visual representation of the Pareto frontier showing trade-offs between objectives with narrative explanation. |
| selection-from-frontier | Select the final portfolio from the Pareto front by applying stakeholder preferences and decision criteria. |

<!-- END available-tables (generated) -->
