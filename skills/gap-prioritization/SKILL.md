---
name: gap-prioritization
description: Score and rank validated gaps on importance, feasibility, novelty, and urgency. Multi-criteria decision analysis with stakeholder confirmation.
used-by: gap-analysis
---

# Gap Prioritization

Score validated gaps and produce a ranked research priority list.

## When to Use

Gaps have been validated as genuine — now determine which are most worth pursuing based on multiple criteria and stakeholder perspectives.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 30 | 27–33 |
| web-research | 10 | 9–11 |
| paper-overview | 20 | 18–22 |
| paper-search | 15 | 13–17 |
| paper-research | 5 | 4–6 |

## State Ledger

Print before every iteration:

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 30 | ? |
| web-research | ? | 10 | ? |
| paper-overview | ? | 20 | ? |
| paper-search | ? | 15 | ? |
| paper-research | ? | 5 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available Tactics

- prioritization-scoring

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** multi-criteria-scoring, stakeholder-confirmation, evidence-grading
**Shared:** multi-stakeholder-simulation

## Execution Guidance

Score validated gaps on importance × feasibility × novelty × urgency. Confirm with multi-stakeholder simulation. Produce ranked list with sensitivity analysis (how stable is ranking under different weight schemes?).

## Output Format

Ranked Gap List — each gap with: composite score, per-dimension scores, stakeholder consensus level, sensitivity assessment.
