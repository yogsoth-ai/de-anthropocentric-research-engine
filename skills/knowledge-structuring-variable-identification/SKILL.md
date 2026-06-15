---
name: variable-identification
description: Identify key variables in the causal system
execution: strategy
dependencies:
  tactics:
  - counterfactual-reasoning
  - evidence-weighing
  sops:
  - variable-page-creation
---

# Variable Identification

Systematically surface all variables that participate in the causal system under study. This strategy drives CC to read source material, extract candidate variables, create variable pages, and flag potential confounders before any mechanism edges are drawn.

## Guiding Focus

CC must resist the urge to jump straight to causal edges. The quality of the entire causal model depends on having a complete, well-scoped variable inventory first. Every variable should be grounded in at least one source page, typed (exposure, outcome, mediator, moderator, confounder, or instrument), and given a plain-language description. Confounders deserve explicit flagging because they are the most common source of spurious causal claims.

## Available Tactics

- counterfactual-reasoning — use "what if this variable were absent?" to test whether a candidate is truly load-bearing
- evidence-weighing — prioritize variables that appear across multiple independent sources over single-mention candidates

## Budget Slice

| Metric | S | M | L |
|--------|---|---|---|
| Variables identified | 6 | 15 | 30 |
| Source pages analyzed | 5 | 15 | 30 |
| Confounders flagged | 2 | 5 | 10 |

## State Ledger Template

```
| Metric              | Target | Current | Status |
|---------------------|--------|---------|--------|
| Variables identified | S:6 / M:15 / L:30 | 0 | ⬜ |
| Source pages analyzed | S:5 / M:15 / L:30 | 0 | ⬜ |
| Confounders flagged | S:2 / M:5 / L:10 | 0 | ⬜ |
```

<HARD-GATE>
Cannot exit until 80% of budget met. Print state ledger before each iteration decision.
</HARD-GATE>

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| counterfactual-reasoning | Tactic for reasoning about what would happen if variables were different — supports causal identification and intervention analysis. |
| evidence-weighing | Tactic for assessing the strength and relevance of evidence for causal claims — distinguishes correlation from causation. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| variable-page-creation | SOP for creating a variable page in the causal model — documents a measurable quantity with its properties. |

<!-- END available-tables (generated) -->
