---
name: argument-crystallization
description: Distill the strongest arguments from each perspective through Argument
  Delphi or Dialectical Delphi methods.
dependencies:
  tactics:
  - disagreement-mapping
  - iterative-convergence-round
  sops:
  - consensus-synthesis
---

# Argument Crystallization

**Purpose:** Rather than converging on a single answer, crystallize the strongest possible arguments for each position. Uses Argument Delphi (focus on argument quality over agreement) and Dialectical Delphi (thesis-antithesis-synthesis) to produce the most rigorous version of each stance.

**When to use:**
- Policy deliberation requiring clear pro/con articulation
- Interdisciplinary disputes where each field has valid concerns
- Pre-decision analysis where decision-makers need best arguments
- Situations where the goal is argument quality, not agreement

## Budget

| Parameter | Constraint |
|-----------|-----------|
| Rounds | 2–3 (refine arguments, not opinions) |
| Perspectives | ≥4 independent |
| Argument quality gate | Each argument must be steel-manned |

## State Ledger

| Key | Type | Description |
|-----|------|-------------|
| question | string | The deliberation question |
| perspectives | array | Contributing perspectives |
| initial_arguments | array | First-round arguments |
| critiques | array | Cross-perspective critiques |
| refined_arguments | array | Steel-manned final arguments |
| synthesis | object | Points of agreement and irreducible tensions |

## Available Tactics

- **disagreement-mapping** — Identify argument clusters
- **iterative-convergence-round** — Refine arguments across rounds

## Available SOPs

- judgment-collection
- cluster-analysis
- argument-extraction
- feedback-distribution
- consensus-measurement
- consensus-synthesis

## Execution Guidance

1. Collect initial positions with supporting arguments
2. Cross-distribute: each perspective critiques and steel-mans others
3. Authors refine arguments incorporating strongest critiques
4. Identify points of genuine agreement vs. irreducible tensions
5. Produce crystallized argument map with quality ratings

## Output Format

```yaml
positions:
  - label: <position name>
    strongest_arguments: [...]
    acknowledged_weaknesses: [...]
    steel_man_version: <best possible formulation>
agreements:
  - point: <shared conclusion>
    strength: <how robust>
irreducible_tensions:
  - between: [position_a, position_b]
    nature: <empirical/value/priority>
    why_irreducible: <explanation>
```

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| disagreement-mapping | Map disagreement structure by collecting judgments, clustering opinions, extracting arguments per cluster, and visualizing fault lines. |
| iterative-convergence-round | Execute one full Delphi round — collect judgments, distribute anonymous feedback, measure consensus, decide whether to continue. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| consensus-synthesis | Synthesize all rounds into a final consensus report documenting agreements, dissent, and process. |

<!-- END available-tables (generated) -->
