---
name: deep-insight-failure-mode-cataloging
description: Systematic failure mode cataloging — generate boundary inputs, observe
  failures, cluster by mechanism, identify triggers, estimate frequency.
execution: tactic
dependencies:
  sops:
  - deep-insight-web-search
  - edge-case-generation
  - failure-clustering
  - scaling-regime-detection
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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| deep-insight-web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
| edge-case-generation | Systematically generate boundary inputs — boundary values, adversarial constructions, distribution shifts, rare combinations, scale extremes. |
| failure-clustering | Group observed failures by mechanism (not symptom), identify common triggers per cluster, estimate frequency and severity. |
| scaling-regime-detection | Detect regime changes in scaling behavior — breakpoints where behavior qualitatively shifts, mechanisms behind transitions. |

<!-- END available-tables (generated) -->
