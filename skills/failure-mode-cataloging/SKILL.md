---
name: failure-mode-cataloging
description: Systematic failure mode cataloging — generate boundary inputs, observe failures, cluster by mechanism, identify triggers, estimate frequency.
execution: tactic
used-by: failure-mode-analysis
---

# Failure Mode Cataloging

Build a comprehensive failure taxonomy.

## Operations

- edge-case-generation → failure-clustering → scaling-regime-detection

## Available SOPs

**Subagent:** edge-case-generation, failure-clustering, scaling-regime-detection
**Import:** web-search

## Execution Guidance

Generate edge cases systematically (boundary values, adversarial inputs, distribution shifts, scale extremes), observe which cause failures, cluster failures by mechanism, identify common triggers.

## Minimum Yield

```
<HARD-GATE>
- edge cases generated: >= 20
- failure clusters identified: >= 3
- triggers per cluster: >= 1
</HARD-GATE>
```
