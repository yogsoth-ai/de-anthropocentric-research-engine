---
name: task-decomposition
description: "Orchestrate the breakdown of experiment design into sequenced, estimated, and formatted task plan"
version: 1.0.0
category: experiment-execution
type: tactic
used-by: implementation-planning
orchestrates:
  - activity-listing
  - dependency-sequencing
  - duration-estimation
  - plan-formatting
---

# Tactic: Task Decomposition

## Orchestration Pattern

```pseudocode
FUNCTION task_decomposition(experiment_design):
    // Phase 1: Enumerate
    activities = SPAWN activity-listing(experiment_design)
    VALIDATE activities.count > 0
    
    // Phase 2: Sequence
    sequenced = SPAWN dependency-sequencing(activities)
    VALIDATE no_circular_dependencies(sequenced)
    
    // Phase 3: Estimate
    estimated = SPAWN duration-estimation(sequenced)
    VALIDATE all_tasks_have_estimates(estimated)
    
    // Phase 4: Format
    plan = SPAWN plan-formatting(estimated)
    VALIDATE no_placeholders(plan)
    VALIDATE all_paths_absolute(plan)
    
    RETURN plan
END
```

## Decision Criteria

| Condition | Action |
|-----------|--------|
| Activity list is empty | ABORT — experiment design is incomplete |
| Circular dependency detected | Return to dependency-sequencing with conflict details |
| Duration estimate has high variance (σ > tM) | Flag as risky, add extra buffer |
| Plan contains TBD/TODO | REJECT — return to plan-formatting |
| Task count > 50 | Consider grouping into phases |
| Task count < 3 | Verify decomposition isn't too coarse |

## Error Recovery

- If activity-listing fails: check experiment design completeness, escalate to Campaign 3
- If dependency-sequencing finds cycles: present cycle to user, ask for resolution
- If duration-estimation lacks data: use conservative estimates (pessimistic × 1.5)
- If plan-formatting produces placeholders: iterate with specific missing information
