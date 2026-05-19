---
name: systematic-perturbation
description: Multi-axis systematic perturbation — define variation axes, perturb along each, measure degradation, construct validity envelope.
execution: tactic
used-by: validity-envelope-mapping
---

# Systematic Perturbation

Map validity by perturbing along defined axes.

## Operations

- variation-axis-definition → controlled-perturbation → validity-envelope-construction

## Available SOPs

**Subagent:** variation-axis-definition, controlled-perturbation, validity-envelope-construction
**Import:** paper-search

## Execution Guidance

Define orthogonal axes of variation (at least 3), perturb one axis at a time while holding others constant, record performance at each point, construct envelope from degradation thresholds.

## Minimum Yield

```
<HARD-GATE>
- variation axes defined: >= 3
- perturbation curves: >= 3
- validity envelope: >= 1 constructed
</HARD-GATE>
```
