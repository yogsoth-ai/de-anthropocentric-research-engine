---
name: prioritization-scoring
description: Multi-dimensional gap scoring and ranking — define criteria, score, weight, rank, sensitivity-check. Combines multi-criteria-scoring, stakeholder-confirmation, and feasibility assessment.
execution: tactic
used-by: gap-prioritization
---

# Prioritization Scoring

Multi-dimensional gap scoring and ranking.

## Operations

- multi-criteria-scoring — score gaps on multiple dimensions
- stakeholder-confirmation — validate priorities across perspectives
- evidence-grading — assess evidence quality supporting each gap

## Available SOPs

**Subagent:** multi-criteria-scoring, stakeholder-confirmation
**Shared:** evidence-synthesis
**Import:** web-research

## Execution Guidance

Define scoring dimensions (importance, feasibility, novelty, urgency, impact). Score each gap 1-10 per dimension. Weight by stakeholder priorities. Rank. Check sensitivity of ranking to weight changes — are top gaps robust to ±20% weight shifts?

## Minimum Yield

```
<HARD-GATE>
- gaps scored: >= 5
- dimensions used: >= 4
- stakeholder perspectives: >= 3
- sensitivity check: performed
</HARD-GATE>
```
