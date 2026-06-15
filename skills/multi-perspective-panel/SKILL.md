---
name: multi-perspective-panel
description: 'Strategy: Multi-stakeholder review panel — diverse expert perspectives
  evaluate artifact simultaneously, then synthesize through structured deliberation.'
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

# Multi-Perspective Panel Strategy

Diverse expert panel evaluates artifact from multiple stakeholder viewpoints.

## Method

1. **debate-architect** selects relevant perspectives based on artifact domain
2. Each **perspective-critic** evaluates from assigned stakeholder viewpoint
3. **divergence-detection** maps agreement/disagreement landscape
4. Panel deliberation: agents respond to each other's concerns
5. **confidence-calibration** determines if consensus reached or irreconcilable

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Debate rounds | 4 | 8 | 12 |
| Participating agents | 3 | 5 | 8 |
| Coverage dimensions | 3 | 5 | 7 |
| External evidence searches | 2 | 5 | 10 |

## Orchestration

```
debate-architect → [select panel perspectives]
→ [parallel]: perspective-critic × N (independent evaluation)
→ divergence-detection (map landscape)
→ [deliberation rounds]:
    perspective-critic responds to disagreements
    → divergence-detection → confidence-calibration
→ debate-transcript-analysis → verdict-synthesis
```

## Subagents

- debate-architect (panel composition)
- perspective-critic × N (stakeholder evaluation)
- divergence-detection (agreement mapping)
- confidence-calibration (consensus detection)

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
