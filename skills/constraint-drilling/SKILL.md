---
name: constraint-drilling
description: Identify constraints, classify them by type and severity, assess removability,
  and design removal paths for removable constraints.
execution: tactic
dependencies:
  sops:
  - constraint-classification
  - constraint-identification-sop
  - removability-assessment
  - removal-path
---

# Constraint Drilling

Systematically discover all constraints blocking a candidate, classify them into actionable categories, assess which can be removed, and design concrete removal paths for those that can.

## Stages

1. **Constraint Identification** — Use TOC current-reality-tree, TRIZ contradiction analysis, and Pre-mortem to surface all constraints. Deploy `constraint-identification-sop` SOP.

2. **Constraint Classification** — Sort identified constraints into hard constraints (immovable), soft constraints (workable), and assumptions (unvalidated). Deploy `constraint-classification` SOP.

3. **Removability Assessment** — For each non-trivial constraint, score how removable it is given available resources and context. Deploy `removability-assessment` SOP for each constraint (parallelizable).

4. **Removal Path Design** — For constraints with removability > 0.3, design concrete steps to remove or mitigate them. Deploy `removal-path` SOP for each removable constraint.

## Available SOPs

| SOP | Stage | Purpose |
|-----|-------|---------|
| constraint-identification-sop | 1 | Discover constraints using structured methods |
| constraint-classification | 2 | Categorize constraints by type |
| removability-assessment | 3 | Score removability of each constraint |
| removal-path | 4 | Design removal steps and timeline |

## Execution Guidance

- Stage 1 should apply all three methods (TOC, TRIZ, Pre-mortem) for completeness
- Stage 2 requires Stage 1 output
- Stage 3 can run assessments in parallel for each constraint
- Stage 4 only runs for constraints with removability score > 0.3
- If a hard constraint is a true showstopper, flag immediately — do not wait for full tactic completion

## Minimum Yield

- Classified constraint list with >= 3 constraints identified
- Removability assessment for each non-trivial constraint
- Removal paths for all constraints scoring removability > 0.3
