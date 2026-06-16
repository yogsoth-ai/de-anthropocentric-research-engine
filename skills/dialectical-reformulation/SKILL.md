---
name: dialectical-reformulation
description: Surface Argyris governing variables and test whether the problem dissolves
  under alternative governing variables (double-loop learning).
dependencies:
  tactics:
  - deep-insight-dialectical-escalation
  sops:
  - counter-assumption-generation
  - governing-variable-surfacing
---

# Dialectical Reformulation

Apply double-loop learning to question the problem's governing variables.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 20 | 18–22 |
| web-research | 10 | 9–11 |
| paper-overview | 30 | 27–33 |
| paper-search | 20 | 18–22 |
| paper-research | 10 | 9–11 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 20 | ? |
| web-research | ? | 10 | ? |
| paper-overview | ? | 30 | ? |
| paper-search | ? | 20 | ? |
| paper-research | ? | 10 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available Tactics

- dialectical-escalation

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** governing-variable-surfacing, counter-assumption-generation

## Execution Guidance

Surface Argyris governing variables (the unstated rules driving behavior), generate counter-assumptions for each, test whether the problem dissolves under alternative governing variables (double-loop learning).

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| deep-insight-dialectical-escalation | Double-loop learning escalation — surface governing variables, generate counter-assumptions, test if problem dissolves under alternatives, score wickedness if it persists. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| counter-assumption-generation | Generate dialectical opposites for governing variables — coherent alternative worldviews where the opposite is true. |
| governing-variable-surfacing | Apply Argyris framework to identify governing variables — the unstated rules driving behavior in a research field. |

<!-- END available-tables (generated) -->
