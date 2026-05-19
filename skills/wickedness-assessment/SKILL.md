---
name: wickedness-assessment
description: Apply Rittel's 10 criteria to determine if the problem is tame, complex, or wicked, and adjust research strategy accordingly.
used-by: problem-reformulation
---

# Wickedness Assessment

Determine the problem's nature — tame, complex, or wicked.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 25 | 22–28 |
| web-research | 10 | 9–11 |
| paper-overview | 25 | 22–28 |
| paper-search | 15 | 13–17 |
| paper-research | 10 | 9–11 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 25 | ? |
| web-research | ? | 10 | ? |
| paper-overview | ? | 25 | ? |
| paper-search | ? | 15 | ? |
| paper-research | ? | 10 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** wickedness-scoring

## Execution Guidance

Apply Rittel's 10 criteria for wicked problems, score the research problem on each, determine if the problem is tame (solvable with standard methods), complex (requires systems thinking), or wicked (requires ongoing management, not solution). Adjust research strategy accordingly.
