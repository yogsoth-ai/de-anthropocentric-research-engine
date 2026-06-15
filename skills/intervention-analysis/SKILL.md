---
name: intervention-analysis
description: Analyze interventions and manipulations on the causal system
execution: strategy
dependencies:
  tactics:
  - counterfactual-reasoning
  - evidence-weighing
  - feedback-loop-detection
  sops:
  - intervention-page-creation
---

# Intervention Analysis

Identify and analyze interventions — deliberate manipulations of variables in the causal system — and predict their downstream outcomes given the current causal graph. This strategy operationalizes the model by showing what would happen if a practitioner or researcher actually pulled a lever.

## Guiding Focus

CC must distinguish clearly between observational associations and interventional effects. An intervention severs the incoming edges to the manipulated variable (do-calculus style), so the predicted outcome may differ substantially from what correlation alone would suggest. For each intervention analyzed, CC should trace the causal path forward through the graph, note moderating variables that could dampen or amplify the effect, and flag any feedback loops that make the outcome path-dependent. Predicted outcomes should be directional claims (increases, decreases, no expected change) with explicit uncertainty where the graph is incomplete.

## Available Tactics

- counterfactual-reasoning — for each intervention, construct the counterfactual scenario (do(X=x) vs do(X=x')) and trace diverging outcomes
- feedback-loop-detection — identify whether the intervention triggers a feedback loop that partially reverses or amplifies the initial effect
- evidence-weighing — prioritize interventions that have existing experimental or quasi-experimental evidence over purely theoretical ones

## Budget Slice

| Metric | S | M | L |
|--------|---|---|---|
| Interventions analyzed | 2 | 5 | 10 |
| Intervention pages created | 2 | 5 | 10 |
| Predicted outcomes | 3 | 8 | 15 |

## State Ledger Template

```
| Metric                    | Target | Current | Status |
|---------------------------|--------|---------|--------|
| Interventions analyzed    | S:2 / M:5 / L:10  | 0 | ⬜ |
| Intervention pages created | S:2 / M:5 / L:10 | 0 | ⬜ |
| Predicted outcomes        | S:3 / M:8 / L:15  | 0 | ⬜ |
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
| intervention-page-creation | SOP for documenting an intervention — what happens when a causal variable is manipulated. |

<!-- END available-tables (generated) -->
