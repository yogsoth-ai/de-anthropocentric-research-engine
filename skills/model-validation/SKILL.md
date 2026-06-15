---
name: model-validation
description: Validate causal model consistency
execution: strategy
dependencies:
  tactics:
  - counterfactual-reasoning
  - evidence-weighing
  - feedback-loop-detection
  sops:
  - model-gap-detection
  - validation-report
---

# Model Validation

Audit the completed causal model for internal consistency: detect and resolve cycles that should not exist, surface contradictions between evidence and claimed edges, and recalibrate confidence scores where the evidence base has shifted. This strategy is the final quality gate before the model is used for inference or reporting.

## Guiding Focus

CC must approach validation as a skeptic, not a defender. The goal is to find problems, not confirm that the model is fine. Cycles in a directed acyclic graph (DAG) are structural errors unless explicitly modeled as feedback loops with documentation. Contradictions between evidence pages and mechanism edges indicate that either the edge or the evidence assessment is wrong — both must be re-examined. Confidence recalibrations should propagate: if a key mechanism edge loses confidence, all downstream claims that depend on it should be flagged for review as well.

## Available Tactics

- feedback-loop-detection — distinguish legitimate documented feedback loops from accidental cycles introduced by inconsistent edge direction
- evidence-weighing — re-score confidence on edges where new contradicting evidence was added during evidence-collection
- counterfactual-reasoning — use "if this edge were removed, which predictions would change?" to identify which edges are load-bearing and deserve the most scrutiny

## Budget Slice

| Metric | S | M | L |
|--------|---|---|---|
| Cycles checked | 3 | 8 | 15 |
| Contradictions resolved | 1 | 3 | 6 |
| Confidence recalibrations | 3 | 8 | 15 |

## State Ledger Template

```
| Metric                    | Target | Current | Status |
|---------------------------|--------|---------|--------|
| Cycles checked            | S:3 / M:8 / L:15  | 0 | ⬜ |
| Contradictions resolved   | S:1 / M:3 / L:6   | 0 | ⬜ |
| Confidence recalibrations | S:3 / M:8 / L:15  | 0 | ⬜ |
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
| feedback-loop-detection | Tactic for identifying circular causation — detect feedback loops, classify as reinforcing or balancing, document loop structure. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| model-gap-detection | SOP for finding gaps in the causal model — missing variables, unexplained effects, weak links. |
| validation-report | SOP for generating a causal model validation report — summarize coverage, confidence, gaps, contradictions. |

<!-- END available-tables (generated) -->
