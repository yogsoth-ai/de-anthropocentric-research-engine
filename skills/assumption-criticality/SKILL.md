---
name: assumption-criticality
description: Measure how much conclusions change when each assumption is negated.
  Ranks assumptions by their impact on the final result.
dependencies:
  tactics:
  - deep-insight-assumption-perturbation
  sops:
  - conclusion-sensitivity-measurement
  - deep-insight-assumption-extraction
  - negation-definition
  - re-derivation
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

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| deep-insight-assumption-perturbation | One-at-a-time assumption perturbation — extract assumptions, define negations, re-derive conclusions under each negation, measure sensitivity. Identifies which assumptions are load-bearing. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| conclusion-sensitivity-measurement | Quantify how much conclusions change across all assumption negations and produce a sensitivity ranking. |
| deep-insight-assumption-extraction | Systematically extract all assumptions (stated, implicit, boundary, mathematical, practical) from a method or model. |
| negation-definition | Define strongest plausible alternatives (negations) for each assumption to enable perturbation analysis. |
| re-derivation | Re-derive conclusions under a negated assumption, tracking where the derivation diverges from the original. |

<!-- END available-tables (generated) -->
