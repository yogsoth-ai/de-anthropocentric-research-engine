---
name: collective-adjudication
description: Strategy for multi-judge ranking aggregation using Condorcet, Schulze,
  Borda, Kemeny-Young, and Copeland methods to produce consensus rankings from diverse
  perspectives.
dependencies:
  tactics:
  - consistency-audit-loop
  - multi-judge-aggregation
  sops:
  - ranking-synthesis
---

# Collective Adjudication

## Purpose

Aggregate rankings from multiple independent judges into a single consensus ranking. Handles disagreement detection, voting paradoxes, and produces transparent aggregation with disagreement maps.

## When to use

- Multiple judges/evaluators available (≥3)
- LLM-as-judge with multiple prompting perspectives
- Committee decision-making requiring formal aggregation
- Need to identify and characterize disagreement patterns

## Budget

| Resource | Allocation |
|----------|-----------|
| Judges/Perspectives | ≥3 independent evaluators |
| Comparisons per judge | Complete or near-complete per judge |
| Aggregation methods | ≥2 methods for robustness check |
| Disagreement threshold | Flag pairs where judges disagree >40% |

## State Ledger

```yaml
candidates: []
perspectives: []        # judge identities/prompts
ballots: []             # [{judge, ranking: [...]}]
aggregation_results: {} # method → consensus_ranking
disagreement_map: {}    # pair → {agreement_rate, split}
cycles: []              # Condorcet cycles if any
method: ""              # schulze | borda | kemeny-young | copeland
```

## Available Tactics

- **multi-judge-aggregation** — collect ballots, aggregate, identify disagreement
- **consistency-audit-loop** — detect cycles in aggregated preferences

## Available SOPs

- ballot-collection
- aggregation-method
- cycle-detection
- inconsistency-localization
- ranking-synthesis

## Execution Guidance

1. Define perspectives (judge roles, prompting strategies)
2. Run ballot-collection to gather independent rankings
3. Run aggregation-method with primary method (Schulze recommended)
4. Run cycle-detection on aggregated pairwise matrix
5. If cycles exist, run inconsistency-localization
6. Cross-validate with secondary method (Borda or Copeland)
7. Produce final ranking with disagreement heatmap

## Output Format

```yaml
consensus_ranking:
  - {rank: 1, candidate: "...", wins: 8, copeland_score: 0.95}
  - {rank: 2, candidate: "...", wins: 7, copeland_score: 0.88}
method: schulze
judges: 5
condorcet_winner: "candidate_a"  # or null if cycle
disagreement_hotspots:
  - {pair: ["c", "d"], agreement: 0.4, split: "3:2"}
cross_validation: {borda_agreement: 0.92, copeland_agreement: 0.96}
```

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| consistency-audit-loop | Detect preference cycles, localize inconsistent judgments, request corrections, and recompute ratings until consistency threshold is met. |
| multi-judge-aggregation | Collect independent rankings from multiple judges, aggregate using social choice methods, and identify disagreement hotspots. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| ranking-synthesis | Produce the final ranking artifact from converged ratings and consistency report. |

<!-- END available-tables (generated) -->
