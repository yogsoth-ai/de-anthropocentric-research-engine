---
name: dependency-constraint
description: "What must be completed first? — Dependency chain analysis + prerequisite graph construction"
version: 1.0.0
category: experiment-execution
type: strategy
used-by: constraint-analysis
sops:
  - dependency-graph-construction
  - critical-chain-identification
tactics:
  - sensitivity-ranking
---

# Strategy: Dependency Constraint

## Methodology

Systematic dependency analysis:
- **Task decomposition**: Break experiment into atomic tasks
- **Dependency typing**: Finish-to-Start, Start-to-Start, Finish-to-Finish, Start-to-Finish
- **Graph construction**: Build directed acyclic graph (DAG)
- **Critical path**: Longest path through the DAG
- **Critical chain**: Critical path + resource contention
- **Prerequisite identification**: External dependencies, approvals, data availability

Dependency categories:
| Category | Examples |
|----------|----------|
| Technical | Code A needs library B, model needs data |
| Sequential | Train before evaluate, design before implement |
| Resource | Same GPU needed by two tasks |
| External | API access, dataset release, paper review |
| Knowledge | Need result X to decide approach Y |

## Execution Flow

1. **Build Dependency Graph** → call `dependency-graph-construction` SOP
   - Input: task list, known dependencies
   - Output: DAG with typed edges

2. **Identify Critical Chain** → call `critical-chain-identification` SOP
   - Input: DAG + resource assignments
   - Output: critical chain with contention points

3. **Rank Sensitivity** → invoke `sensitivity-ranking` tactic
   - Determine which dependencies are most binding

4. **Report** → synthesize dependency assessment
   - Critical path length
   - Binding dependency constraints
   - Parallelization opportunities

## Budget Gate

| Resource | Budget | Notes |
|----------|--------|-------|
| Subagent calls | ≤5 | 2 SOPs + synthesis |
| Iterations | ≤2 | Re-build if tasks change |
| Output size | ≤3000 tokens | Graph summary + critical chain |
