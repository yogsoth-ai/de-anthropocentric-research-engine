---
name: assumption-stress-test
description: Systematic stress testing of assumptions — surface, classify by vulnerability, attack, assess fragility. Combines assumption-surfacing (shared), abp-vulnerability-classification, and clr-validation SOPs.
execution: tactic
used-by: assumption-audit
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
