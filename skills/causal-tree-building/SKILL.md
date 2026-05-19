---
name: causal-tree-building
description: Build logical causal trees from symptoms to root causes — list UDEs, connect causal chains, validate logic, locate root causes. Combines ishikawa-decomposition, current-reality-tree, and clr-validation SOPs.
execution: tactic
used-by: root-cause-drilling
---

# Causal Tree Building

Build formal causal trees from symptoms to root causes.

## Operations

- ishikawa-decomposition — multi-factor decomposition (6M categories)
- current-reality-tree — sufficient-cause logic tree
- clr-validation — validate every causal link

## Available SOPs

**Subagent:** five-whys-drilling, ishikawa-decomposition, current-reality-tree, clr-validation
**Import:** paper-search

## Execution Guidance

Decompose via Ishikawa (6M categories adapted for research: Methodology, Data, Theory, Measurement, Researchers, Environment). Build formal CRT with sufficient-cause logic. Validate every causal link with CLR 8-check.

## Minimum Yield

```
<HARD-GATE>
- ishikawa diagrams: >= 1
- CRT constructed: >= 1
- CLR validations: >= 3 links validated
- root causes identified: >= 1
</HARD-GATE>
```
