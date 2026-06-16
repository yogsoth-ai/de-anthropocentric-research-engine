---
name: assumption-audit
description: Surface all assumptions, classify by vulnerability (load-bearing × likely-false),
  validate causal logic. Focus on dangerous assumptions — high load-bearing + non-explicit.
dependencies:
  tactics:
  - assumption-stress-test
  sops:
  - abp-vulnerability-classification
  - clr-validation
  - deep-insight-assumption-surfacing
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

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| assumption-stress-test | Systematic stress testing of assumptions — surface, classify by vulnerability, attack, assess fragility. Combines assumption-surfacing (shared), abp-vulnerability-classification, and clr-validation SOPs. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| abp-vulnerability-classification | Classify assumptions on 2 axes — load-bearing (how much conclusion depends on it) × vulnerable (how likely to be false). Focuses attention on High-Load × High-Vulnerable quadrant. |
| clr-validation | Apply Goldratt's 8 Categories of Legitimate Reservation to validate causal claims. Tests clarity, existence, sufficiency, and logical integrity. |
| deep-insight-assumption-surfacing | Systematically extract implicit assumptions from methods, frameworks, or arguments. Identifies what is taken for granted without explicit justification. |

<!-- END available-tables (generated) -->
