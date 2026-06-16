---
name: systematic-perturbation
description: Multi-axis systematic perturbation — define variation axes, perturb along
  each, measure degradation, construct validity envelope.
execution: tactic
dependencies:
  sops:
  - controlled-perturbation
  - deep-insight-paper-search
  - deep-insight-validity-envelope-construction
  - variation-axis-definition
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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| controlled-perturbation | Systematically vary parameters along defined axes, recording performance at each point to identify degradation thresholds. |
| deep-insight-paper-search | AI-powered paper summary and search. Import of literature-engine/literature-search skill. AI summary level — cite as "AI-extracted" not "paper states". |
| deep-insight-validity-envelope-construction | Combine multi-axis perturbation data into a multi-dimensional validity description with boundary conditions and interaction effects. |
| variation-axis-definition | Identify orthogonal axes along which a method's validity might vary. Ensures axes are independent, measurable, and span the relevant parameter space. |

<!-- END available-tables (generated) -->
