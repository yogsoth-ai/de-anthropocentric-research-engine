---
name: dialectical-escalation
description: Double-loop learning escalation — surface governing variables, generate
  counter-assumptions, test if problem dissolves under alternatives, score wickedness
  if it persists.
execution: tactic
dependencies:
  sops:
  - counter-assumption-generation
  - deep-insight-assumption-surfacing
  - governing-variable-surfacing
  - wickedness-scoring
---

# Dialectical Escalation

Escalate from single-loop to double-loop learning.

## Operations

governing-variable-surfacing → counter-assumption-generation → wickedness-scoring

## Available SOPs

**Subagent:** governing-variable-surfacing, counter-assumption-generation, wickedness-scoring
**Shared:** assumption-surfacing

## Execution Guidance

Surface the governing variables (Argyris: the unstated rules everyone follows), generate the opposite assumption for each, test whether the problem still exists under the alternative. If it persists regardless, assess wickedness level.

Single-loop: "How do we solve this problem better?" Double-loop: "Should we be solving this problem at all?"

## Minimum Yield

```
<HARD-GATE>
- Governing variables surfaced: >= 3
- Counter-assumptions generated: >= 3
- Problem dissolution tests: >= 2
- Wickedness assessment: completed if problem persists
</HARD-GATE>
```

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| counter-assumption-generation | Generate dialectical opposites for governing variables — coherent alternative worldviews where the opposite is true. |
| deep-insight-assumption-surfacing | Systematically extract implicit assumptions from methods, frameworks, or arguments. Identifies what is taken for granted without explicit justification. |
| governing-variable-surfacing | Apply Argyris framework to identify governing variables — the unstated rules driving behavior in a research field. |
| wickedness-scoring | Score a problem against Rittel's 10 criteria to determine if it is tame, complex, or wicked. |

<!-- END available-tables (generated) -->
