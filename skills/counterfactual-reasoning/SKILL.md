---
name: counterfactual-reasoning
description: Tactic for reasoning about what would happen if variables were different
  — supports causal identification and intervention analysis.
execution: tactic
dependencies:
  sops:
  - causal-chain-query
  - confidence-scoring
  - contradiction-flagging
---

# Counterfactual Reasoning

Reason about what would happen if a variable were different. "If X had not occurred, would Y still have happened?" This is the gold standard for causal identification.

## Available SOPs

- causal-chain-query — trace causal paths to identify dependencies
- contradiction-flagging — flag when counterfactual contradicts observed evidence
- confidence-scoring — assess confidence in counterfactual conclusions

## Guiding Principles

- **Minimal change.** Counterfactuals should change only the target variable, holding all else constant.
- **Mechanism required.** A counterfactual without a mechanism is speculation, not reasoning.
- **Multiple paths.** If Y can be caused by X through multiple paths, removing X may not remove Y.
- **Temporal ordering.** Causes precede effects. Counterfactuals that violate temporal order are invalid.

## Minimum Yield

<HARD-GATE>
≥1 counterfactual assessment with explicit mechanism and confidence score per invocation.
</HARD-GATE>

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| causal-chain-query | SOP for tracing causal chains — follow edges from cause to effect through intermediate variables. |
| confidence-scoring | SOP for assigning calibrated confidence scores to causal claims based on evidence quality and quantity. |
| contradiction-flagging | SOP for flagging contradictions in the causal model — identify conflicting evidence or mechanism claims. |

<!-- END available-tables (generated) -->
