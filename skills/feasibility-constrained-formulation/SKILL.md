---
name: feasibility-constrained-formulation
description: 'Strategy: reshape a research question under resource constraints — pragmatic adjustment that preserves core value'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: research-question
tactics:
- question-refinement-loop
sops:
- scope-assessment
- finer-criteria-check
- success-criteria-definition
dependencies:
  tactics:
  - question-refinement-loop
---

# Feasibility-Constrained Formulation

Reshape a research question under constraints — when the ideal question exceeds available resources, pragmatically adjust it to be feasible while preserving core research value.

## When to Use

- The ideal research question exceeds available resources (time/data/compute/manpower)
- A trade-off between ambition and feasibility is needed
- There are explicit constraints (deadline, budget, data availability)

## Thinking Framework

Core logic: constraints are not the enemy, they are design parameters. Good reshaping under constraints = finding "the most valuable question answerable within these constraints."

### Constraint Types

| Constraint | Adjustment strategy | Example |
|------|---------|------|
| Insufficient time | narrow scope / use proxy metrics | 3 months → pilot study only |
| Data unavailable | switch data source / switch study object | cannot obtain X → use public dataset Y |
| Insufficient compute | simplify method / reduce scale | cannot train a large model → use fine-tuning |
| Insufficient expertise | narrow the domain / collaborate | no biology background → focus on the computational part |

### Adjustment Principles

- **Preserve the core**: adjust scope and method, but keep the essence of the core research question
- **Use proxies**: if direct measurement is infeasible, find a reasonable proxy metric
- **Phase it**: split a big problem into pilot → full study
- **Make trade-offs explicit**: explicitly state what was given up due to constraints

## Budget Gate

| Tier | Constraint analysis | Adjustment options | Output |
|------|---------|---------|------|
| S | list main constraints | 1 adjustment option | a feasible RQ |
| M | constraint classification + impact assessment | 2-3 adjustment options + comparison | best feasible RQ + trade-off statement |
| L | full constraint map + priorities | multiple options + Pareto analysis | best RQ under constraints + phased plan |

## Default Reference Flow

1. List all constraints (resources, time, data, capability)
2. Assess each constraint's impact on the ideal RQ
3. Design adjustment options (narrow/proxy/phase)
4. Assess whether the adjusted RQ still has value
5. FINER check (paying special attention to F = Feasible)
6. Define success criteria
7. Explicitly state trade-offs

## context-checkpoint

After the Strategy completes, you must call context-checkpoint and record:
- The list of constraints
- Ideal RQ vs adjusted RQ
- The adjustment strategy and rationale
- The trade-off statement
- The final feasible RQ

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| question-refinement-loop | Tactic: 迭代精化研究问题直到通过 FINER 5 项标准 |

<!-- END available-tables (generated) -->
