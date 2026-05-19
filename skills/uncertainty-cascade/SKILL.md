---
name: uncertainty-cascade
description: Uncertainty cascade propagation — assign input distributions, sample via Monte Carlo, propagate through model, analyze output distribution, identify critical paths. Maps how input uncertainty flows to output uncertainty.
execution: tactic
used-by: uncertainty-propagation
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
