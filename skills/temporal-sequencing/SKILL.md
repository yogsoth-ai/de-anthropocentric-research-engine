---
name: temporal-sequencing
description: Determine optimal ordering and phasing of portfolio investments using Real Options, Critical path, Dependency graph, and Staged investment methods.
used-by: portfolio-optimization
---

# Temporal Sequencing

## Purpose

Determine the optimal order, timing, and phasing of portfolio elements when dependencies, learning effects, and option value make sequencing matter as much as selection.

## When to use

- Candidates have dependencies (A must precede B)
- Early investments create options for later ones
- Information gained from early bets informs later decisions
- Budget is released in phases over time
- Timing affects value (first-mover advantage, market windows)

## Budget

| Dimension | Target |
|-----------|--------|
| Candidates sequenced | 8-20 |
| Time periods modeled | 3-6 phases |
| Dependencies mapped | all critical |
| Decision points identified | >=2 stage-gates |

## State Ledger

| Field | Type | Description |
|-------|------|-------------|
| candidates | list | Candidates with timing attributes |
| dependencies | graph | Precedence relationships between candidates |
| phases | list | Time periods with budget allocations |
| option_values | list | Value of information/flexibility from early bets |
| sequence | list | Ordered plan with stage-gates |

## Available Tactics

| Tactic | When |
|--------|------|
| pareto-frontier-construction | Trading off speed vs cost vs risk in sequencing |
| scenario-stress-testing | Testing sequence robustness under timeline uncertainty |

## Available SOPs

| SOP | Purpose |
|-----|---------|
| objective-definition | Define sequencing objectives and constraints |
| optimization-run | Find optimal sequences |
| scenario-construction | Model timeline uncertainties |
| portfolio-evaluation-per-scenario | Test sequence under delays/accelerations |
| portfolio-synthesis | Synthesize robust sequence recommendation |

## Execution Guidance

1. Map dependencies and precedence constraints
2. Identify option value — which early investments create future flexibility
3. Define phase budgets and stage-gate criteria
4. Optimize sequence considering dependencies, option value, and constraints
5. Stress-test sequence against timeline uncertainties
6. Build staged investment plan with decision points

## Output Format

```yaml
strategy: temporal-sequencing
sequence:
  - phase: 1
    candidates: [<name1>, <name2>]
    budget: <amount>
    stage_gate: <criteria for proceeding>
  - phase: 2
    candidates: [<name3>]
    budget: <amount>
    depends_on: [<phase 1 outcomes>]
critical_path: [<ordered candidates>]
option_values:
  - candidate: <name>
    options_created: [<future possibilities>]
method_used: <real-options|critical-path|staged-investment>
```
