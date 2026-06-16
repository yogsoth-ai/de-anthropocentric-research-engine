---
name: parameter-screening
description: Quick Morris method screening to identify which parameters have large
  effects and which can be safely ignored.
dependencies:
  tactics:
  - screening-then-decomposition
  sops:
  - morris-screening
---

# Parameter Screening

Quickly identify important vs unimportant parameters.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 20 | 18–22 |
| web-research | 5 | 4–6 |
| paper-overview | 30 | 27–33 |
| paper-search | 20 | 18–22 |
| paper-research | 10 | 9–11 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 20 | ? |
| web-research | ? | 5 | ? |
| paper-overview | ? | 30 | ? |
| paper-search | ? | 20 | ? |
| paper-research | ? | 10 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available Tactics

- screening-then-decomposition

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** morris-screening

## Execution Guidance

Use Morris method (one-at-a-time with random trajectories) to quickly identify which parameters have large effects (high mu*) and which have nonlinear/interaction effects (high sigma). Eliminate clearly unimportant parameters.

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| screening-then-decomposition | Two-phase sensitivity — Morris quick screening to eliminate unimportant factors, then Sobol precise decomposition on survivors. Efficient allocation of analytical effort. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| morris-screening | Morris method screening — compute elementary effects to quickly identify important vs unimportant parameters. |

<!-- END available-tables (generated) -->
