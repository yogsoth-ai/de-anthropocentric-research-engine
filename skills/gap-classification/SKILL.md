---
name: gap-classification
description: Classify identified gaps using Miles 7-type taxonomy and AHRQ 4-reason framework. Determines gap type (theoretical, methodological, empirical, etc.) and root cause of gap existence.
used-by: gap-analysis
---

# Gap Classification

Classify identified gaps by type and root cause.

## When to Use

Gap candidates have been identified and need systematic categorization to inform prioritization and resolution strategy.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 20 | 18–22 |
| web-research | 5 | 4–6 |
| paper-overview | 30 | 27–33 |
| paper-search | 20 | 18–22 |
| paper-research | 10 | 9–11 |

## State Ledger

Print before every iteration:

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 20 | ? |
| web-research | ? | 5 | ? |
| paper-overview | ? | 30 | ? |
| paper-search | ? | 20 | ? |
| paper-research | ? | 10 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** gap-typology-classification, ahrq-reason-classification

## Execution Guidance

For each gap candidate, apply Miles 7-type taxonomy (theoretical, methodological, empirical, population, practical, knowledge void, evidence gap), then AHRQ 4-reason classification for root cause of gap existence (insufficient info, biased info, inconsistent info, not yet integrated).

## Output Format

Classified Gap Table — each gap with: type label, AHRQ reason, confidence, supporting evidence.
