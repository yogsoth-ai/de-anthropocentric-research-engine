---
name: prioritization-scoring
description: Multi-dimensional gap scoring and ranking — define criteria, score, weight,
  rank, sensitivity-check. Combines multi-criteria-scoring, stakeholder-confirmation,
  and feasibility assessment.
execution: tactic
dependencies:
  sops:
  - deep-insight-multi-criteria-scoring
  - deep-insight-web-research
  - evidence-synthesis
  - stakeholder-confirmation
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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| deep-insight-multi-criteria-scoring | Score gaps on multiple dimensions (importance, feasibility, novelty, urgency, impact) using weighted multi-criteria decision analysis. |
| deep-insight-web-research | Deep web research with full page fetching via Apify. Import of web-browsing/web-research skill. Must fetch full page — no conclusions from previews. |
| evidence-synthesis | Synthesize multi-source evidence into structured argumentation. Weaves findings from literature, web, and analysis into coherent evidence maps with explicit strength ratings. |
| stakeholder-confirmation | Simulate stakeholder perspectives to validate gap priorities. Assesses gap value from researcher, practitioner, funder, and end-user viewpoints. |

<!-- END available-tables (generated) -->
