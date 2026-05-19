---
name: uncertainty-propagation
description: Propagate input uncertainties through the model via Monte Carlo sampling. Identifies which input uncertainties contribute most to output uncertainty.
used-by: sensitivity-analysis
---

# Uncertainty Propagation

Map how input uncertainty flows to output uncertainty.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 20 | 18–22 |
| web-research | 10 | 9–11 |
| paper-overview | 25 | 22–28 |
| paper-search | 20 | 18–22 |
| paper-research | 10 | 9–11 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 20 | ? |
| web-research | ? | 10 | ? |
| paper-overview | ? | 25 | ? |
| paper-search | ? | 20 | ? |
| paper-research | ? | 10 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available Tactics

- uncertainty-cascade

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** distribution-assignment, monte-carlo-sampling, critical-path-identification

## Execution Guidance

Assign probability distributions to uncertain inputs, propagate through the model via Monte Carlo sampling, analyze output distribution, identify which input uncertainties contribute most.
