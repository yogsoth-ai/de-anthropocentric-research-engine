---
name: prerequisite-planning
description: Identify obstacles blocking direct achievement and design intermediate
  objectives to overcome each
version: 1.0.0
category: experiment-execution
type: strategy
sops:
- obstacle-identification
- intermediate-objective-design
tactics:
- task-decomposition
dependencies:
  sops:
  - intermediate-objective-design
  - obstacle-identification
  tactics:
  - task-decomposition
---

# Strategy: Prerequisite Planning

**Key Question**: What obstacles are in the way?

## Methodology

Theory of Constraints (TOC) Prerequisite Tree + Transition Tree:

1. **Prerequisite Tree (PRT)** — identify obstacles preventing direct achievement of the objective
2. **Intermediate Objectives (IOs)** — design actions that overcome each obstacle
3. **Transition Tree** — sequence IOs into executable steps with cause-effect logic

## Execution Flow

```
[Objective from experiment design]
    → obstacle-identification (PRT)
        → intermediate-objective-design (IOs for each obstacle)
            → [sequence IOs by dependency]
                → OUTPUT: ordered list of IOs with obstacle-IO mapping
```

## Budget Gate

| Step | Max Budget | Output |
|------|-----------|--------|
| Obstacle identification | 10% | Complete obstacle list |
| IO design | 10% | IO for each obstacle |

## Key Decisions

- If an obstacle cannot be overcome: escalate to experiment redesign (return to Campaign 3)
- If multiple IOs address same obstacle: choose simplest (Occam's razor)
- If IOs create new obstacles: recurse (but limit depth to 3 levels)

## Integration with Critical Path

Obstacles identified here feed back into the critical path:
- Each IO becomes an activity in the network
- IO dependencies become edges in the activity graph
- This ensures the plan accounts for real-world blockers, not just ideal-path tasks

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
| intermediate-objective-design | Design intermediate objectives to overcome each identified obstacle |
| obstacle-identification | TOC Prerequisite Tree — list obstacles preventing direct achievement of the objective |

<!-- END available-tables (generated) -->
