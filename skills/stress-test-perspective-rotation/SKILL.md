---
name: perspective-rotation
description: 'Tactic: Sequential perspective evaluation with divergence aggregation.
  Each agent evaluates from a distinct viewpoint, then disagreements are surfaced
  and resolved.'
type: tactic
strategies:
- society-of-mind
- multi-perspective-panel
dependencies:
  sops:
  - confidence-calibration
  - debate-architect
  - divergence-detection
  - perspective-critic
---

# Perspective Rotation Tactic

Sequential multi-perspective evaluation followed by divergence analysis and deliberation.

## Orchestration

1. **debate-architect** assigns N perspectives (domain expert, skeptic, practitioner, theorist, etc.)
2. [Parallel] Each **perspective-critic** evaluates artifact from assigned viewpoint
3. **divergence-detection** compares all evaluations:
   - Identifies consensus points (agreement across >70% of perspectives)
   - Identifies divergence points (disagreement across >50% of perspectives)
4. [Deliberation] Perspective-critics respond to divergence points
5. **divergence-detection** re-evaluates — tracks convergence trend
6. **confidence-calibration** determines if further rounds needed

## Perspective Types

- Domain Expert (technical validity)
- Methodological Skeptic (rigor and reproducibility)
- Practitioner (real-world applicability)
- Theorist (conceptual coherence)
- Adversary (strongest possible objection)
- Novice (clarity and accessibility)

## Subagents Dispatched

- debate-architect (perspective assignment)
- perspective-critic × N (evaluation from viewpoint)
- divergence-detection (agreement/disagreement mapping)
- confidence-calibration (convergence assessment)

## Termination Conditions

- Convergence reached (divergence points < 2)
- Max deliberation rounds exhausted
- Saturation detected (no position changes between rounds)
- Irreconcilable disagreement identified (flagged for human review)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| confidence-calibration | Calibrates confidence scores based on debate progression. Determines whether to escalate, continue, or terminate based on cumulative evidence. |
| debate-architect | Designs debate structure based on artifact type — selects attack vectors, assigns perspectives, determines escalation ladder, and configures round parameters. |
| divergence-detection | Identifies agreement and disagreement patterns across multiple perspective evaluations. Maps consensus clusters and persistent divergence points. |
| perspective-critic | Evaluates artifact from a specific assigned perspective. Produces assessment grounded in that viewpoint's values, priorities, and expertise. |

<!-- END available-tables (generated) -->
