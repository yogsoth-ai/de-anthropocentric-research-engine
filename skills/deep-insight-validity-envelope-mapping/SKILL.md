---
name: deep-insight-validity-envelope-mapping
description: Map multi-dimensional validity envelopes — define variation axes, perturb
  systematically, measure degradation, construct boundary surface.
dependencies:
  tactics:
  - systematic-perturbation
  sops:
  - controlled-perturbation
  - deep-insight-validity-envelope-construction
  - variation-axis-definition
---

# Validity Envelope Mapping

Map the conditions under which a method remains valid.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 30 | 27–33 |
| web-research | 10 | 9–11 |
| paper-overview | 40 | 36–44 |
| paper-search | 30 | 27–33 |
| paper-research | 15 | 13–17 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 30 | ? |
| web-research | ? | 10 | ? |
| paper-overview | ? | 40 | ? |
| paper-search | ? | 30 | ? |
| paper-research | ? | 15 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available Tactics

- systematic-perturbation

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** variation-axis-definition, controlled-perturbation, validity-envelope-construction

## Execution Guidance

Define orthogonal variation axes (data size, noise level, distribution type, etc.), systematically perturb along each axis, measure performance degradation, construct multi-dimensional validity envelope.

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| systematic-perturbation | Multi-axis systematic perturbation — define variation axes, perturb along each, measure degradation, construct validity envelope. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| controlled-perturbation | Systematically vary parameters along defined axes, recording performance at each point to identify degradation thresholds. |
| deep-insight-validity-envelope-construction | Combine multi-axis perturbation data into a multi-dimensional validity description with boundary conditions and interaction effects. |
| variation-axis-definition | Identify orthogonal axes along which a method's validity might vary. Ensures axes are independent, measurable, and span the relevant parameter space. |

<!-- END available-tables (generated) -->
