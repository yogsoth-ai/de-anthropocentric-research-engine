---
name: critical-path-planning
description: Identify the shortest execution path via CPM forward/backward pass, resource
  leveling, and buffer insertion
version: 1.0.0
category: experiment-execution
type: strategy
sops:
- activity-listing
- dependency-sequencing
- duration-estimation
- critical-path-calculation
tactics:
- task-decomposition
dependencies:
  sops:
  - activity-listing
  - critical-path-calculation
  - dependency-sequencing
  - duration-estimation
  tactics:
  - task-decomposition
---

# Strategy: Critical Path Planning

**Key Question**: What is the shortest path?

## Methodology

Critical Path Method (CPM) adapted for experiment execution:

1. **Activity Listing** — enumerate all implementation tasks
2. **Dependency Sequencing** — determine predecessor/successor relationships
3. **Duration Estimation** — three-point PERT (optimistic, most likely, pessimistic)
4. **Forward Pass** — calculate earliest start/finish for each activity
5. **Backward Pass** — calculate latest start/finish, identify zero-float path
6. **Resource Leveling** — resolve resource conflicts on parallel paths
7. **Buffer Insertion** — add project buffer (Critical Chain method) at convergence points

## Execution Flow

```
activity-listing
    → dependency-sequencing
        → duration-estimation
            → critical-path-calculation
                → [resource leveling if conflicts]
                    → [buffer insertion]
                        → OUTPUT: annotated task graph with critical path highlighted
```

## Budget Gate

| Step | Max Budget | Output |
|------|-----------|--------|
| Activity listing | 5% | Complete activity list |
| Dependency + Duration | 10% | Sequenced, estimated network |
| CPM calculation | 5% | Critical path + float table |

## Key Decisions

- If critical path is too long: look for fast-tracking (parallel execution) or crashing (more resources)
- If resource conflicts exist: prioritize critical path tasks over float tasks
- Buffer size: typically 50% of critical chain duration (Goldratt's recommendation)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| task-decomposition | Orchestrate the breakdown of experiment design into sequenced, estimated, and formatted task plan |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| activity-listing | Enumerate all implementation activities from an experiment design |
| critical-path-calculation | CPM forward/backward pass with float calculation to identify the critical path |
| dependency-sequencing | Determine task dependencies and execution order |
| duration-estimation | Three-point PERT estimation for implementation activities |

<!-- END available-tables (generated) -->
