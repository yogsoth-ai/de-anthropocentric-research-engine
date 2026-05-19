---
name: resource-constraint
description: "Are resources sufficient? — Quantify compute, data, time, human, and financial resource constraints"
version: 1.0.0
category: experiment-execution
type: strategy
used-by: constraint-analysis
sops:
  - resource-quantification
  - critical-chain-identification
  - buffer-sizing
tactics:
  - sensitivity-ranking
---

# Strategy: Resource Constraint

## Methodology

Systematic resource feasibility assessment:
- **Demand modeling**: What does the experiment need?
- **Supply inventory**: What do we actually have?
- **Gap analysis**: Where does demand exceed supply?
- **Critical chain**: Which resource constraints lie on the critical path?
- **Buffer sizing**: How much slack do we need?

Resource categories:
| Category | Examples |
|----------|----------|
| Compute | GPU hours, CPU cores, memory, storage |
| Data | Training samples, labeled data, access rights |
| Time | Calendar time, researcher hours, review cycles |
| Human | Expertise, headcount, availability |
| Financial | Budget, cost per experiment, opportunity cost |

## Execution Flow

1. **Quantify Resources** → call `resource-quantification` SOP
   - Input: experiment plan, resource inventory
   - Output: demand/supply/gap table per category

2. **Identify Critical Chain** → call `critical-chain-identification` SOP
   - Input: task list with resource assignments
   - Output: critical chain with resource contention points

3. **Size Buffers** → call `buffer-sizing` SOP
   - Input: critical chain, task duration estimates
   - Output: project/feeding/resource buffer recommendations

4. **Rank Sensitivity** → invoke `sensitivity-ranking` tactic
   - Determine which resource gap is most binding

5. **Report** → synthesize feasibility assessment
   - Go/No-Go/Conditional recommendation

## Budget Gate

| Resource | Budget | Notes |
|----------|--------|-------|
| Subagent calls | ≤6 | 3 SOPs + synthesis |
| Iterations | ≤2 | Re-quantify if estimates change |
| Output size | ≤3000 tokens | Gap table + recommendation |
