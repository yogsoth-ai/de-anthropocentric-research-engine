---
name: experiment-execution-bottleneck-identification
description: Where is the system bottleneck? — TOC 5 Focusing Steps + Current Reality
  Tree to find the binding constraint
version: 1.0.0
category: experiment-execution
type: strategy
sops:
- undesirable-effect-listing
- causal-chain-tracing
- core-conflict-extraction
tactics:
- constraint-tree-building
dependencies:
  sops:
  - causal-chain-tracing
  - core-conflict-extraction
  - undesirable-effect-listing
  tactics:
  - constraint-tree-building
---

# Strategy: Bottleneck Identification

## Methodology

Based on Goldratt's Theory of Constraints (TOC) 5 Focusing Steps:
1. **IDENTIFY** the constraint (Current Reality Tree)
2. **EXPLOIT** the constraint (maximize throughput at bottleneck)
3. **SUBORDINATE** everything else to the constraint
4. **ELEVATE** the constraint (invest to remove it)
5. **REPEAT** (check if constraint has shifted)

Combined with Current Reality Tree (CRT) construction:
- List Undesirable Effects (UDEs) observed in the system
- Trace causal chains using IF...THEN...BECAUSE logic
- Converge chains to identify root causes / core conflicts

## Execution Flow

1. **List UDEs** → call `undesirable-effect-listing` SOP
   - Input: system description, observed problems
   - Output: numbered UDE list with evidence

2. **Trace Causal Chains** → call `causal-chain-tracing` SOP
   - Input: UDE list
   - Output: IF-THEN causal tree

3. **Extract Core Conflict** → call `core-conflict-extraction` SOP
   - Input: causal tree root causes
   - Output: Evaporating Cloud (A-B-C-D-D') format

4. **Build Constraint Tree** → invoke `constraint-tree-building` tactic
   - Orchestrates steps 1-3 into a coherent tree structure

5. **Rank & Report** → synthesize findings
   - Identify the single binding constraint
   - Assess exploitation potential
   - Recommend elevation path

## Budget Gate

| Resource | Budget | Notes |
|----------|--------|-------|
| Subagent calls | ≤6 | 3 SOPs + synthesis |
| Iterations | ≤2 | Re-trace if tree is incomplete |
| Output size | ≤3000 tokens | Compressed tree + recommendation |

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| constraint-tree-building | Build Current Reality Tree from UDEs through causal chains to core conflicts |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| causal-chain-tracing | Trace UDE to root cause via IF...THEN...BECAUSE logic chains |
| core-conflict-extraction | Extract core conflict in Evaporating Cloud format (A-B-C-D-D') |
| undesirable-effect-listing | List current Undesirable Effects (UDEs) — observable symptoms of system underperformance |

<!-- END available-tables (generated) -->
