---
name: gap-validation
description: Validate gap authenticity via cross-database verification, temporal sensitivity testing, and false-gap filtering. Ensures gaps are genuine absences, not search artifacts.
used-by: gap-analysis
---

# Gap Validation

Verify that identified gaps are genuine research absences, not artifacts of search failure.

## When to Use

Classified gaps need validation before prioritization — confirm they represent real absences across multiple sources and time windows.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 40 | 36–44 |
| web-research | 15 | 13–17 |
| paper-overview | 40 | 36–44 |
| paper-search | 25 | 22–28 |
| paper-research | 15 | 13–17 |

## State Ledger

Print before every iteration:

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 40 | ? |
| web-research | ? | 15 | ? |
| paper-overview | ? | 40 | ? |
| paper-search | ? | 25 | ? |
| paper-research | ? | 15 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available Tactics

- cross-validation

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** cross-database-verification, false-gap-filtering, temporal-sensitivity-testing

## Execution Guidance

For each classified gap: verify across multiple databases (Semantic Scholar, Google Scholar, arXiv, domain-specific), test temporal stability (does gap persist across 2/5/10 year windows?), filter false gaps (search failure vs genuine absence vs already solved).

## Output Format

Validated Gap List — each gap with: validation status (confirmed/partial/refuted), cross-database results, temporal trend, false-gap assessment.
