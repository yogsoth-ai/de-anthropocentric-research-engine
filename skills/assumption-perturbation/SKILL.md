---
name: assumption-perturbation
description: One-at-a-time assumption perturbation — extract assumptions, define negations, re-derive conclusions under each negation, measure sensitivity. Identifies which assumptions are load-bearing.
execution: tactic
used-by: assumption-criticality
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
