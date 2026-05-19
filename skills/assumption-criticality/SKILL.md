---
name: assumption-criticality
description: Measure how much conclusions change when each assumption is negated. Ranks assumptions by their impact on the final result.
used-by: sensitivity-analysis
---

# Assumption Criticality

Rank assumptions by their impact on conclusions.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 30 | 27–33 |
| web-research | 10 | 9–11 |
| paper-overview | 30 | 27–33 |
| paper-search | 20 | 18–22 |
| paper-research | 10 | 9–11 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 30 | ? |
| web-research | ? | 10 | ? |
| paper-overview | ? | 30 | ? |
| paper-search | ? | 20 | ? |
| paper-research | ? | 10 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available Tactics

- assumption-perturbation

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** assumption-extraction, negation-definition, re-derivation, conclusion-sensitivity-measurement

## Execution Guidance

Extract assumptions, define negation for each, re-derive conclusions under negated assumption, measure how much the conclusion changes. Rank by conclusion sensitivity.
