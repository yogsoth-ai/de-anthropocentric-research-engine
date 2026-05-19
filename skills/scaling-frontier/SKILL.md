---
name: scaling-frontier
description: Analyze behavior across scales — detect regime changes, identify capacity limits, fit scaling laws within regimes.
used-by: boundary-analysis
---

# Scaling Frontier

Detect where scaling behavior qualitatively shifts.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 30 | 27–33 |
| web-research | 10 | 9–11 |
| paper-overview | 30 | 27–33 |
| paper-search | 20 | 18–22 |
| paper-research | 15 | 13–17 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 30 | ? |
| web-research | ? | 10 | ? |
| paper-overview | ? | 30 | ? |
| paper-search | ? | 20 | ? |
| paper-research | ? | 15 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** scaling-regime-detection, edge-case-generation

## Execution Guidance

Analyze behavior across scales (data size, model size, compute, time), detect regime changes (breakpoints where behavior qualitatively shifts), identify capacity limits and their mechanisms.
