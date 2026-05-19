---
name: screening-then-decomposition
description: Two-phase sensitivity — Morris quick screening to eliminate unimportant factors, then Sobol precise decomposition on survivors. Efficient allocation of analytical effort.
execution: tactic
used-by: parameter-screening, variance-decomposition
---

# Screening Then Decomposition

Two-phase approach: quick screening followed by precise decomposition.

## Operations

morris-screening → sobol-decomposition → interaction-detection

## Available SOPs

**Subagent:** morris-screening, sobol-decomposition, interaction-detection
**Import:** paper-search

## Execution Guidance

Phase 1 (Morris): Screen all parameters, eliminate those with low mu* and low sigma. These are unimportant and can be safely fixed at nominal values.

Phase 2 (Sobol): For surviving parameters, compute precise variance decomposition. First-order indices (Si) measure direct effects, total-order indices (STi) measure direct + all interactions.

Phase 3: Detect significant interaction pairs (STi - Si > threshold). Characterize interaction types and implications.

## Minimum Yield

```
<HARD-GATE>
- Parameters screened: >= 5
- Parameters eliminated (low mu*): >= 1
- Sobol indices computed: >= 3 parameters
- Interaction pairs identified: >= 1
</HARD-GATE>
```
