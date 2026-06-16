---
name: uncertainty-cascade
description: Uncertainty cascade propagation — assign input distributions, sample
  via Monte Carlo, propagate through model, analyze output distribution, identify
  critical paths. Maps how input uncertainty flows to output uncertainty.
execution: tactic
dependencies:
  sops:
  - critical-path-identification
  - deep-insight-paper-search
  - distribution-assignment
  - monte-carlo-sampling
---

# Uncertainty Cascade

Map how input uncertainty flows through to output uncertainty.

## Operations

distribution-assignment → monte-carlo-sampling → critical-path-identification

## Available SOPs

**Subagent:** distribution-assignment, monte-carlo-sampling, critical-path-identification
**Import:** paper-search

## Execution Guidance

Assign distributions to all uncertain inputs (use literature for informed priors), sample (Latin Hypercube for efficiency), propagate, analyze output distribution shape and spread, identify which inputs contribute most to output variance (critical path).

Focus on: which inputs, if resolved, would most reduce output uncertainty? This directly informs research prioritization.

## Minimum Yield

```
<HARD-GATE>
- Input distributions assigned: >= 4
- Propagation completed: yes
- Output distribution characterized: yes
- Critical path identified: >= 1 path with ranked inputs
</HARD-GATE>
```

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| critical-path-identification | Identify which input uncertainties contribute most to output uncertainty and compute EVPI for research prioritization. |
| deep-insight-paper-search | AI-powered paper summary and search. Import of literature-engine/literature-search skill. AI summary level — cite as "AI-extracted" not "paper states". |
| distribution-assignment | Assign probability distributions to uncertain parameters based on available evidence and domain knowledge. |
| monte-carlo-sampling | Design and execute Monte Carlo sampling strategy for uncertainty propagation through a model. |

<!-- END available-tables (generated) -->
