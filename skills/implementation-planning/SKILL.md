---
name: implementation-planning
description: "Plan execution path, produce executable plan, dispatch subagents, collect and analyze results"
version: 1.0.0
category: experiment-execution
type: campaign
strategies:
  - critical-path-planning
  - prerequisite-planning
  - plan-writing
  - experiment-running
  - result-analysis
tactics:
  - task-decomposition
  - subagent-execution-loop
  - checkpoint-and-recover
  - result-validation-loop
---

# Campaign 4: Implementation Planning

**Positioning**: "How to do it + do it" — from validated experiment design to executed results.

## HARD-GATE

Before entering this campaign, the following must be true:

- [ ] Experiment design exists (output of Campaign 3: experiment-design)
- [ ] Variables are operationalized with concrete measures
- [ ] Success criteria are defined with statistical thresholds
- [ ] Resource budget is allocated (tokens, time, compute)

If any gate fails, STOP and return to the appropriate upstream campaign.

## Campaign Goal

Transform a validated experiment design into:
1. An executable task plan (critical path identified, obstacles resolved)
2. Dispatched execution via subagents
3. Collected, validated, and statistically analyzed results
4. A comprehensive execution report with reproducibility verification

## Strategy Selection

| Situation | Strategy | Key Question |
|-----------|----------|--------------|
| Need shortest execution path | critical-path-planning | What is the shortest path? |
| Obstacles block direct execution | prerequisite-planning | What obstacles are in the way? |
| Ready to format executable plan | plan-writing | How to write it as an executable plan? |
| Plan ready, execute tasks | experiment-running | How to execute? |
| Results collected, need analysis | result-analysis | What do the results tell us? |

Typical flow: critical-path-planning → prerequisite-planning → plan-writing → experiment-running → result-analysis

## Budget Gate

| Phase | Max Budget | Checkpoint |
|-------|-----------|------------|
| Planning (strategies 1-3) | 20% of total | Plan document produced |
| Execution (strategy 4) | 60% of total | All tasks DONE or BLOCKED |
| Analysis (strategy 5) | 20% of total | Statistical report produced |

If any phase exceeds budget, STOP and report partial results.

## Superpowers Adaptation

This campaign internalizes two superpowers patterns:

### From superpowers:writing-plans
- Tasks are bite-sized (one clear action each)
- Every task specifies exact file paths (no placeholders)
- TDD where applicable (test first, implement second)
- No TBD/TODO in final plan — everything resolved or explicitly deferred

### From superpowers:subagent-driven-development
- Fresh subagent per task (clean context)
- Three-stage review: implementer → reviewer → integration
- Status codes: DONE / BLOCKED / NEEDS_CONTEXT
- Continuous execution until all tasks complete or budget exhausted

## Minimum Yield

Even if execution is partial, this campaign MUST produce:
- Task dependency graph (from planning phase)
- Execution log with status per task
- Whatever results were collected before budget/failure
- Clear statement of what remains undone and why
