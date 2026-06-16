---
name: root-cause-drilling
description: Drill from surface symptoms to root causes via 5 Whys, Ishikawa decomposition,
  and Current Reality Trees. Validates each causal link with literature evidence.
dependencies:
  tactics:
  - causal-tree-building
  sops:
  - current-reality-tree
  - five-whys-drilling
  - ishikawa-decomposition
---

# Root-Cause Drilling

Drill from surface phenomena to actionable root causes.

## When to Use

A gap or problem has been identified but the underlying cause is unclear — need to understand WHY it exists.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 30 | 27–33 |
| web-research | 10 | 9–11 |
| paper-overview | 40 | 36–44 |
| paper-search | 25 | 22–28 |
| paper-research | 10 | 9–11 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 30 | ? |
| web-research | ? | 10 | ? |
| paper-overview | ? | 40 | ? |
| paper-search | ? | 25 | ? |
| paper-research | ? | 10 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available Tactics

- causal-tree-building

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** five-whys-drilling, ishikawa-decomposition, current-reality-tree

## Execution Guidance

Start with 5 Whys to drill from surface to root. Use Ishikawa for multi-factor decomposition. Build CRT for formal causal logic. Validate each causal link with literature evidence.

## Output Format

Root Cause Report — causal chain, Ishikawa diagram, CRT, validated root causes with evidence.

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| causal-tree-building | Build logical causal trees from symptoms to root causes — list UDEs, connect causal chains, validate logic, locate root causes. Combines ishikawa-decomposition, current-reality-tree, and clr-validation SOPs. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| current-reality-tree | Build TOC Current Reality Trees — connect Undesirable Effects via sufficient-cause logic to identify 1-3 root causes. |
| five-whys-drilling | Iterative "Why?" questioning (5+ levels) to drill from surface phenomenon to actionable root cause. Each level verified against evidence. |
| ishikawa-decomposition | Decompose problems into 6M categories (Methodology, Data, Theory, Measurement, Researchers, Environment) via fishbone diagram analysis. |

<!-- END available-tables (generated) -->
