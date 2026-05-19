---
name: assumption-audit
description: Surface all assumptions, classify by vulnerability (load-bearing × likely-false), validate causal logic. Focus on dangerous assumptions — high load-bearing + non-explicit.
used-by: insight
---

# Assumption Audit

Systematically audit assumptions underlying a method, theory, or gap.

## When to Use

Need to identify which hidden assumptions are most dangerous — load-bearing yet unexamined.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 30 | 27–33 |
| web-research | 10 | 9–11 |
| paper-overview | 30 | 27–33 |
| paper-search | 20 | 18–22 |
| paper-research | 10 | 9–11 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 30 | ? |
| web-research | ? | 10 | ? |
| paper-overview | ? | 30 | ? |
| paper-search | ? | 20 | ? |
| paper-research | ? | 10 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available Tactics

- assumption-stress-test

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** abp-vulnerability-classification, clr-validation
**Shared:** assumption-surfacing

## Execution Guidance

Surface all assumptions (shared SOP), classify by vulnerability (ABP), validate causal logic (CLR 8-check). Focus on load-bearing + non-explicit assumptions.

## Output Format

Assumption Audit Report — assumption inventory, vulnerability matrix, CLR validation results, priority list for challenging.
