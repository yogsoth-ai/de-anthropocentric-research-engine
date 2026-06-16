---
name: failure-taxonomy
description: Catalog all failure modes in a domain, classify them systematically,
  and generate targeted solutions for each failure type.
execution: strategy
dependencies:
  sops:
  - coverage-gap-detection
  - creative-ideation-failure-mode-cataloging
  - enumeration-synthesis
  - failure-driven-generation
  tactics:
  - gap-driven-generation
---

# Failure Taxonomy

Catalog all failure modes, classify them into a taxonomy, and generate targeted solutions that address each specific failure type.

## State Ledger

| Resource | Target | Current | % |
|----------|--------|---------|---|
| web-search | 25 | 0 | 0% |
| web-research | 10 | 0 | 0% |
| paper-overview | 25 | 0 | 0% |
| paper-search | 15 | 0 | 0% |
| paper-research | 5 | 0 | 0% |

## HARD-GATE

Cannot exit strategy until ≥80% of each budget line is consumed OR yield targets are met with justification for remaining budget.

## Available Tactics

| Tactic | Role |
|--------|------|
| gap-driven-generation | Generate solutions from identified failure gaps |
| evaluation-filtering | Score and filter failure-targeted ideas |

## Available SOPs

| SOP | Role |
|-----|------|
| failure-mode-cataloging | Systematically catalog all failure modes |
| failure-driven-generation | Generate targeted solution per failure mode |
| coverage-gap-detection | Detect failure modes without existing solutions |
| enumeration-synthesis | Synthesize failure analysis into idea report |

## Execution Guidance

1. **Catalog**: Run failure-mode-cataloging to enumerate all failure modes
2. **Classify**: Organize failures into taxonomy (type, severity, frequency)
3. **Gap-check**: Run coverage-gap-detection to find unaddressed failures
4. **Generate**: Run failure-driven-generation for each unaddressed failure
5. **Filter**: Apply evaluation-filtering to rank solutions
6. **Synthesize**: Produce structured report via enumeration-synthesis

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| gap-driven-generation | Generate solutions targeting specific coverage gaps — detect gaps, generate failure-driven solutions, and design factor-level experiments. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| coverage-gap-detection | Detect uncovered regions in the solution space, producing a prioritized gap list. |
| creative-ideation-failure-mode-cataloging | Systematically catalog all failure modes in a domain or method, producing a classified failure taxonomy. |
| enumeration-synthesis | Synthesize all systematic enumeration outputs into a structured idea report with prioritized recommendations. |
| failure-driven-generation | Generate targeted solutions for each identified failure mode, ensuring every failure has at least one proposed mitigation. |

<!-- END available-tables (generated) -->
