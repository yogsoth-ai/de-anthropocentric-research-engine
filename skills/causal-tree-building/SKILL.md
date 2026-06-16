---
name: causal-tree-building
description: Build logical causal trees from symptoms to root causes — list UDEs,
  connect causal chains, validate logic, locate root causes. Combines ishikawa-decomposition,
  current-reality-tree, and clr-validation SOPs.
execution: tactic
dependencies:
  sops:
  - clr-validation
  - current-reality-tree
  - deep-insight-paper-search
  - five-whys-drilling
  - ishikawa-decomposition
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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| clr-validation | Apply Goldratt's 8 Categories of Legitimate Reservation to validate causal claims. Tests clarity, existence, sufficiency, and logical integrity. |
| current-reality-tree | Build TOC Current Reality Trees — connect Undesirable Effects via sufficient-cause logic to identify 1-3 root causes. |
| deep-insight-paper-search | AI-powered paper summary and search. Import of literature-engine/literature-search skill. AI summary level — cite as "AI-extracted" not "paper states". |
| five-whys-drilling | Iterative "Why?" questioning (5+ levels) to drill from surface phenomenon to actionable root cause. Each level verified against evidence. |
| ishikawa-decomposition | Decompose problems into 6M categories (Methodology, Data, Theory, Measurement, Researchers, Environment) via fishbone diagram analysis. |

<!-- END available-tables (generated) -->
