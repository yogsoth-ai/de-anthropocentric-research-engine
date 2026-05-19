---
name: constraint-tree-building
description: "Build Current Reality Tree from UDEs through causal chains to core conflicts"
version: 1.0.0
category: experiment-execution
type: tactic
used-by: constraint-analysis
orchestrates:
  - undesirable-effect-listing
  - causal-chain-tracing
  - core-conflict-extraction
---

# Tactic: Constraint Tree Building

## Orchestration Pattern

1. **List UDEs** → spawn `undesirable-effect-listing`
   - Collect all observable symptoms of system underperformance
   - Ensure each UDE is specific, observable, and evidenced
   - Minimum 5 UDEs for a meaningful tree

2. **Trace Causal Chains** → spawn `causal-chain-tracing`
   - Input: UDE list from step 1
   - For each UDE, trace backward: IF [cause] THEN [effect] BECAUSE [assumption]
   - Connect UDEs that share common causes
   - Identify convergence points (multiple chains meeting at one cause)

3. **Extract Core Conflict** → spawn `core-conflict-extraction`
   - Input: convergence points from step 2
   - If root cause is a dilemma, express as Evaporating Cloud
   - If root cause is a single constraint, express as binding constraint statement

## Decision Criteria

- **When to iterate**: If the tree has disconnected components (UDEs not linked to any chain), return to step 2 with those UDEs
- **When to stop**: All UDEs connect to at most 3 root causes, and root causes are expressed as constraints or conflicts
- **When to escalate**: If >10 UDEs found, prioritize top-5 by severity before tracing
- **Quality gate**: Every causal link must have a BECAUSE clause (the underlying assumption)
