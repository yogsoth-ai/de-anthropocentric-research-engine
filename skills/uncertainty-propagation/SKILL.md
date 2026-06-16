---
name: uncertainty-propagation
description: Propagate input uncertainties through the model via Monte Carlo sampling.
  Identifies which input uncertainties contribute most to output uncertainty.
dependencies:
  tactics:
  - uncertainty-cascade
  sops:
  - critical-path-identification
  - distribution-assignment
  - monte-carlo-sampling
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

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| uncertainty-cascade | Uncertainty cascade propagation — assign input distributions, sample via Monte Carlo, propagate through model, analyze output distribution, identify critical paths. Maps how input uncertainty flows to output uncertainty. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| critical-path-identification | Identify which input uncertainties contribute most to output uncertainty and compute EVPI for research prioritization. |
| distribution-assignment | Assign probability distributions to uncertain parameters based on available evidence and domain knowledge. |
| monte-carlo-sampling | Design and execute Monte Carlo sampling strategy for uncertainty propagation through a model. |

<!-- END available-tables (generated) -->
