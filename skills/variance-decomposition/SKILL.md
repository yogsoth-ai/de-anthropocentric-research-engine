---
name: variance-decomposition
description: Sobol variance decomposition — compute first-order and total-order sensitivity indices to quantify each parameter's contribution to output variance.
used-by: sensitivity-analysis
---

# Variance Decomposition

Quantify each parameter's contribution to output variance.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 20 | 18–22 |
| web-research | 10 | 9–11 |
| paper-overview | 30 | 27–33 |
| paper-search | 25 | 22–28 |
| paper-research | 15 | 13–17 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 20 | ? |
| web-research | ? | 10 | ? |
| paper-overview | ? | 30 | ? |
| paper-search | ? | 25 | ? |
| paper-research | ? | 15 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available Tactics

- screening-then-decomposition

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** sobol-decomposition, interaction-detection

## Execution Guidance

For parameters surviving screening, compute Sobol first-order (Si) and total-order (STi) indices. Si measures direct effect, STi-Si measures interaction contribution. Focus on parameters with high STi.
