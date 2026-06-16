---
name: assumption-stress-test
description: Systematic stress testing of assumptions — surface, classify by vulnerability,
  attack, assess fragility. Combines assumption-surfacing (shared), abp-vulnerability-classification,
  and clr-validation SOPs.
execution: tactic
dependencies:
  sops:
  - abp-vulnerability-classification
  - clr-validation
  - deep-insight-assumption-surfacing
  - deep-insight-paper-research
---

# Assumption Stress Test

Systematically stress-test assumptions to find dangerous ones.

## Operations

- assumption-surfacing (shared) — extract all implicit assumptions
- abp-vulnerability-classification — classify by load-bearing × vulnerable
- clr-validation — validate causal logic of critical assumptions

## Available SOPs

**Shared:** assumption-surfacing
**Subagent:** abp-vulnerability-classification, clr-validation
**Import:** paper-research

## Execution Guidance

Surface all assumptions (shared SOP). Classify each by load-bearing × vulnerable matrix. Validate causal logic of most critical assumptions (High-Load × High-Vulnerable quadrant).

## Minimum Yield

```
<HARD-GATE>
- assumptions surfaced: >= 5
- vulnerability classifications: >= 5
- CLR validations on critical assumptions: >= 2
- dangerous assumptions identified: >= 1
</HARD-GATE>
```

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| abp-vulnerability-classification | Classify assumptions on 2 axes — load-bearing (how much conclusion depends on it) × vulnerable (how likely to be false). Focuses attention on High-Load × High-Vulnerable quadrant. |
| clr-validation | Apply Goldratt's 8 Categories of Legitimate Reservation to validate causal claims. Tests clarity, existence, sufficiency, and logical integrity. |
| deep-insight-assumption-surfacing | Systematically extract implicit assumptions from methods, frameworks, or arguments. Identifies what is taken for granted without explicit justification. |
| deep-insight-paper-research | Full-text paper reading via three-pass Keshav method. Import of literature-engine/literature-research skill. Authoritative source for claims about paper content. |

<!-- END available-tables (generated) -->
