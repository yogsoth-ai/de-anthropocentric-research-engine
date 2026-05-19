---
name: cross-validation
description: Multi-source cross-validation of gap authenticity — cross-database search, temporal sensitivity testing, false-gap filtering, stakeholder confirmation.
execution: tactic
used-by: gap-validation
---

# Cross-Validation

Multi-source verification of gap authenticity.

## Operations

- cross-database-verification — search gap across 3+ databases
- temporal-sensitivity-testing — test persistence across time windows
- false-gap-filtering — detect search failures vs genuine absences
- stakeholder-confirmation — validate from multiple perspectives

## Available SOPs

**Subagent:** cross-database-verification, temporal-sensitivity-testing, false-gap-filtering, stakeholder-confirmation
**Import:** web-search, paper-search

## Execution Guidance

For each gap candidate: verify across 3+ databases (Semantic Scholar, Google Scholar, arXiv, domain-specific), test if gap persists across 2/5/10 year windows, apply false-gap heuristics (wrong search terms? already solved? inherently unanswerable?), confirm with stakeholder simulation.

## Minimum Yield

```
<HARD-GATE>
- cross-database checks: >= 3 per gap
- temporal windows tested: >= 2 per gap
- false-gap filter applied: >= 1 per gap
</HARD-GATE>
```
