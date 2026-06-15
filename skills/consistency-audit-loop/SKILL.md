---
name: consistency-audit-loop
description: Detect preference cycles, localize inconsistent judgments, request corrections,
  and recompute ratings until consistency threshold is met.
execution: tactic
dependencies:
  sops:
  - comparison-executor
  - cycle-detection
  - inconsistency-localization
---

# Consistency Audit Loop

Audit a comparison matrix for transitivity violations, pinpoint the most problematic judgments, request re-evaluation of those pairs, and recompute until the consistency threshold is satisfied.

## Stages

1. **Detect** — cycle-detection scans the comparison matrix for cycles and computes transitivity score
2. **Localize** — inconsistency-localization identifies which pairs participate in the most cycles
3. **Repair** — comparison-executor re-evaluates the problematic pairs with explicit context about the inconsistency

Loop stages 1-3 until consistency threshold met or repair budget exhausted.

## Available SOPs

| Stage | SOP | Input | Output |
|-------|-----|-------|--------|
| Detect | cycle-detection | comparison_matrix | cycles[], transitivity_score |
| Localize | inconsistency-localization | comparison_matrix, cycles[] | problematic_pairs[] |
| Repair | comparison-executor | pair, context | judgment |

## Execution Guidance

- Run detection first — if no cycles and CR < 0.1, exit immediately (no repair needed)
- Localization should rank pairs by cycle participation count
- When re-comparing, provide the judge with context: "A>B and B>C but you said C>A — please reconsider"
- Limit repairs to top 20% most problematic pairs per iteration
- After repair, recompute full ratings before next detection pass
- Maximum 3 audit iterations to prevent infinite loops
- Document all changes in repair log for transparency

## Minimum Yield

- Consistency report + correction recommendations
- Consistency report: CR value, transitivity score, cycle count
- List of all cycles found (before and after repair)
- Repair log: which pairs were re-evaluated, old vs new judgment
- Final consistency status: pass/fail with metrics
