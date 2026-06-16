---
name: failure-mode-analysis
description: Systematically catalog failure modes — generate edge cases, observe failures,
  cluster by mechanism, identify triggers and frequency.
dependencies:
  tactics:
  - deep-insight-failure-mode-cataloging
  sops:
  - edge-case-generation
  - failure-clustering
  - scaling-regime-detection
---

# Failure Mode Analysis

Build a comprehensive failure taxonomy for a method.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 40 | 36–44 |
| web-research | 15 | 13–17 |
| paper-overview | 40 | 36–44 |
| paper-search | 25 | 22–28 |
| paper-research | 10 | 9–11 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 40 | ? |
| web-research | ? | 15 | ? |
| paper-overview | ? | 40 | ? |
| paper-search | ? | 25 | ? |
| paper-research | ? | 10 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available Tactics

- failure-mode-cataloging

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** edge-case-generation, failure-clustering, scaling-regime-detection

## Execution Guidance

Generate systematic edge cases, observe failure patterns, cluster into failure modes, identify triggering conditions and frequency estimates.

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| deep-insight-failure-mode-cataloging | Systematic failure mode cataloging — generate boundary inputs, observe failures, cluster by mechanism, identify triggers, estimate frequency. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| edge-case-generation | Systematically generate boundary inputs — boundary values, adversarial constructions, distribution shifts, rare combinations, scale extremes. |
| failure-clustering | Group observed failures by mechanism (not symptom), identify common triggers per cluster, estimate frequency and severity. |
| scaling-regime-detection | Detect regime changes in scaling behavior — breakpoints where behavior qualitatively shifts, mechanisms behind transitions. |

<!-- END available-tables (generated) -->
