---
name: screening-then-scoring
description: First eliminate non-qualifying candidates with non-compensatory rules, then score survivors with full MCDA methods.
execution: tactic
used-by: multi-criteria-scoring
---

# Screening Then Scoring

First eliminate non-qualifying alternatives using non-compensatory rules, then perform fine-grained scoring and ranking of survivors. Suitable for scenarios with large candidate sets or hard constraints.

## Stages

1. **Threshold Setting** — Set minimum thresholds for critical criteria
2. **Conjunctive Filtering** — Eliminate non-qualifying alternatives based on thresholds
3. **Dominance Check** — Identify dominated alternatives among survivors (optional further reduction)
4. **Full Scoring** — Execute scoring-matrix-construction workflow on survivors

## Available SOPs

- threshold-setting — Set criteria thresholds
- conjunctive-filter — Conjunctive rule elimination
- dominance-check — Dominance relationship check
- criterion-definition — Fine-grained scoring criteria (Stage 4)
- weight-elicitation-sop — Weight computation (Stage 4)
- alternative-scoring — Alternative scoring (Stage 4)
- normalization — Normalization (Stage 4)
- scoring-synthesis — Comprehensive recommendation (Stage 4)

## Execution Guidance

- Stages 1-3 are the screening phase, rapidly reducing the candidate set
- Screening criteria should focus on hard constraints (safety, compliance, budget caps, etc.)
- Survivor count should ideally be 3-8 before entering fine-grained scoring
- If too few survivors after screening (<3), consider relaxing thresholds
- If too many survivors (>10), add screening criteria or tighten thresholds
- Stage 4 reuses the complete scoring-matrix-construction tactic workflow

## Minimum Yield

Elimination rationale + survivor ranking
