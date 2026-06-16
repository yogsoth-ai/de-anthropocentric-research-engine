---
name: evidence-collection
description: Gather evidence for causal claims
execution: strategy
dependencies:
  tactics:
  - counterfactual-reasoning
  - evidence-weighing
  - feedback-loop-detection
  sops:
  - evidence-linking
---

# Evidence Collection

Systematically gather and attach evidence pages to the causal claims in the model, creating supported_by edges for confirming evidence and contradicts edges for disconfirming evidence. A causal model without evidence provenance is speculation; this strategy converts it into a structured, auditable knowledge artifact.

## Guiding Focus

CC should treat evidence collection as adversarial by default: for every supported_by edge added, actively search for contradicting evidence before moving on. The contradicts edges are as important as the supported_by edges — a model that only records confirming evidence is biased. Evidence pages must record the source, study design (where applicable), and a brief assessment of quality. Quantity matters less than coverage across independent sources.

## Available Tactics

- evidence-weighing — score each evidence page by study design strength, sample size, and independence from other sources
- counterfactual-reasoning — use "what evidence would change this claim?" to direct the search toward the most informative gaps
- feedback-loop-detection — flag evidence patterns that suggest bidirectional causation rather than clean one-way support

## Budget Slice

| Metric | S | M | L |
|--------|---|---|---|
| Evidence pages created | 8 | 20 | 45 |
| supported_by edges | 10 | 25 | 50 |
| contradicts edges flagged | 2 | 5 | 10 |

## State Ledger Template

```
| Metric                   | Target | Current | Status |
|--------------------------|--------|---------|--------|
| Evidence pages created   | S:8 / M:20 / L:45  | 0 | ⬜ |
| supported_by edges       | S:10 / M:25 / L:50 | 0 | ⬜ |
| contradicts edges flagged | S:2 / M:5 / L:10  | 0 | ⬜ |
```

<HARD-GATE>
Cannot exit until 80% of budget met. Print state ledger before each iteration decision.
</HARD-GATE>

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| counterfactual-reasoning | Tactic for reasoning about what would happen if variables were different — supports causal identification and intervention analysis. |
| evidence-weighing | Tactic for assessing the strength and relevance of evidence for causal claims — distinguishes correlation from causation. |
| feedback-loop-detection | Tactic for identifying circular causation — detect feedback loops, classify as reinforcing or balancing, document loop structure. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| evidence-linking | SOP for linking evidence pages to causal claims — creates supported_by or contradicts edges. |

<!-- END available-tables (generated) -->
