---
name: deep-insight-assumption-perturbation
description: One-at-a-time assumption perturbation — extract assumptions, define negations,
  re-derive conclusions under each negation, measure sensitivity. Identifies which
  assumptions are load-bearing.
execution: tactic
dependencies:
  sops:
  - conclusion-sensitivity-measurement
  - deep-insight-assumption-extraction
  - deep-insight-assumption-surfacing
  - deep-insight-paper-research
  - negation-definition
  - re-derivation
---

# Assumption Perturbation

Systematically perturb assumptions to identify which are load-bearing.

## Operations

assumption-extraction → negation-definition → re-derivation → conclusion-sensitivity-measurement

## Available SOPs

**Subagent:** assumption-extraction, negation-definition, re-derivation, conclusion-sensitivity-measurement
**Shared:** assumption-surfacing
**Import:** paper-research

## Execution Guidance

Extract all assumptions (use shared SOP for initial surfacing), define weakest plausible alternative for each, re-derive the conclusion under each alternative, measure change magnitude and direction. Rank by sensitivity.

Key principle: negation is not logical NOT — it is the strongest plausible alternative. "Data is normally distributed" negates to "data follows a heavy-tailed distribution" not "data is not normally distributed."

## Minimum Yield

```
<HARD-GATE>
- Assumptions extracted: >= 5
- Negations defined: >= 5
- Re-derivations completed: >= 4
- Sensitivity rankings produced: >= 1 complete ranking
</HARD-GATE>
```

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| conclusion-sensitivity-measurement | Quantify how much conclusions change across all assumption negations and produce a sensitivity ranking. |
| deep-insight-assumption-extraction | Systematically extract all assumptions (stated, implicit, boundary, mathematical, practical) from a method or model. |
| deep-insight-assumption-surfacing | Systematically extract implicit assumptions from methods, frameworks, or arguments. Identifies what is taken for granted without explicit justification. |
| deep-insight-paper-research | Full-text paper reading via three-pass Keshav method. Import of literature-engine/literature-research skill. Authoritative source for claims about paper content. |
| negation-definition | Define strongest plausible alternatives (negations) for each assumption to enable perturbation analysis. |
| re-derivation | Re-derive conclusions under a negated assumption, tracking where the derivation diverges from the original. |

<!-- END available-tables (generated) -->
