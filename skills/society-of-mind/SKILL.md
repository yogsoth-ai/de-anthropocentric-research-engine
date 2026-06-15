---
name: society-of-mind
description: 'Strategy: Multi-agent collaborative debate based on Du et al. Society
  of Mind. Agents share perspectives iteratively until convergence or divergence is
  detected.'
type: strategy
tactics:
- perspective-rotation
dependencies:
  tactics:
  - stress-test-perspective-rotation
  sops:
  - confidence-calibration
  - debate-architect
  - divergence-detection
  - perspective-critic
---

# Society of Mind Strategy

Multiple agents evaluate independently, then share and revise through iterative rounds.

## Method

1. **debate-architect** assigns N distinct perspectives to agents
2. Each **perspective-critic** evaluates artifact from assigned viewpoint
3. All perspectives shared — agents revise positions given others' arguments
4. **divergence-detection** identifies agreement clusters and persistent disagreements
5. Repeat sharing rounds until convergence or saturation

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Debate rounds | 4 | 8 | 12 |
| Participating agents | 3 | 5 | 8 |
| Coverage dimensions | 3 | 5 | 7 |
| External evidence searches | 2 | 5 | 10 |

## Orchestration

```
debate-architect → [assign perspectives]
→ [parallel]: perspective-critic × N
→ [for each sharing round]:
    share all outputs → perspective-critic revises
    → divergence-detection → (converge or continue)
→ debate-transcript-analysis → verdict-synthesis
```

## Subagents

- debate-architect (perspective assignment)
- perspective-critic × N (perspective evaluation)
- divergence-detection (convergence tracking)
- confidence-calibration (termination decision)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| stress-test-perspective-rotation | Tactic: Sequential perspective evaluation with divergence aggregation. Each agent evaluates from a distinct viewpoint, then disagreements are surfaced and resolved. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| confidence-calibration | Calibrates confidence scores based on debate progression. Determines whether to escalate, continue, or terminate based on cumulative evidence. |
| debate-architect | Designs debate structure based on artifact type — selects attack vectors, assigns perspectives, determines escalation ladder, and configures round parameters. |
| divergence-detection | Identifies agreement and disagreement patterns across multiple perspective evaluations. Maps consensus clusters and persistent divergence points. |
| perspective-critic | Evaluates artifact from a specific assigned perspective. Produces assessment grounded in that viewpoint's values, priorities, and expertise. |

<!-- END available-tables (generated) -->
