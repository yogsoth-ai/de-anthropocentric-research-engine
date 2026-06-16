---
name: cross-validation
description: Multi-source cross-validation of gap authenticity — cross-database search,
  temporal sensitivity testing, false-gap filtering, stakeholder confirmation.
execution: tactic
dependencies:
  sops:
  - cross-database-verification
  - deep-insight-paper-search
  - deep-insight-web-search
  - false-gap-filtering
  - stakeholder-confirmation
  - temporal-sensitivity-testing
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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| cross-database-verification | Verify gap existence across multiple databases (Semantic Scholar, Google Scholar, arXiv, domain-specific). Distinguishes database-specific gaps from universal gaps. |
| deep-insight-paper-search | AI-powered paper summary and search. Import of literature-engine/literature-search skill. AI summary level — cite as "AI-extracted" not "paper states". |
| deep-insight-web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
| false-gap-filtering | Detect false gaps — search failures, already-solved gaps, and inherently unanswerable questions masquerading as research gaps. |
| stakeholder-confirmation | Simulate stakeholder perspectives to validate gap priorities. Assesses gap value from researcher, practitioner, funder, and end-user viewpoints. |
| temporal-sensitivity-testing | Test whether a gap persists across different time windows (2/5/10 years). Determines if gap is narrowing, widening, or stable over time. |

<!-- END available-tables (generated) -->
