---
name: assess-goal-feasibility
description: "Cross-check goal branches against resources, obstacles, and timeline; label feasible/stretch/infeasible and propose OR alternatives."
---

# assess-goal-feasibility

## Purpose
Cross-check goal branches against resources, obstacles, and timeline; label each feasible, stretch, or infeasible and propose OR alternatives.

## Input contract
```yaml
required: [goal_branches, resource_profile, obstacle_register, timeline]
optional: [capability_evidence, dependency_graph, alternative_constraints]
constraints: [each branch must have explicit resource, obstacle, and deadline checks]
```

## Procedure
1. Decompose each branch into deliverables, dependencies, and required capabilities.
2. Compare requirements with resources and obstacle severity.
3. Test schedule against dependencies and deadline; assign feasible/stretch/infeasible.
4. For infeasible branches, construct OR alternatives that relax a declared constraint.

## Output contract
```yaml
produces: [feasibility_matrix, blocking_obstacles, alternative_branches, timeline_rationale]
delta_fields: [findings, decisions, open_questions, recommended_jumps]
```

## Quality gates
- Every branch receives all three labels checks: resource, obstacle, timeline.
- Infeasible labels identify a blocking condition and evidence.
- Each OR alternative states the relaxed constraint and residual risk.

## Parameterization
Caller supplies branch schema, resource dimensions, obstacle scale, timeline units, feasibility labels, and OR-generation policy.

## Failure and counterexamples
Do not label a branch feasible when an unbounded dependency or missing capability is unexamined.

## Provenance map
- resolved: feasibility-check

