---
name: validity-envelope-mapping
description: Map multi-dimensional validity envelopes — define variation axes, perturb systematically, measure degradation, construct boundary surface.
used-by: boundary-analysis
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
