---
name: implementation-planning
description: Plan execution path, produce executable plan, dispatch subagents, collect
  and analyze results
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
dependencies:
  strategies:
  - critical-path-planning
  - experiment-running
  - plan-writing
  - prerequisite-planning
  - result-analysis
  tactics:
  - checkpoint-and-recover
  - result-validation-loop
  - subagent-execution-loop
  - task-decomposition
  sops:
  - context-checkpoint
  - context-init
  - execution-synthesis
  - experiment-execution-paper-overview
  - experiment-execution-paper-research
  - experiment-execution-paper-search
  - experiment-execution-quality-gate-check
  - experiment-execution-saturation-detection
  - experiment-execution-web-research
  - experiment-execution-web-search
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

<!-- BEGIN available-tables (generated) -->

## Available Strategies

Optional, no fixed order; the final leaf is always a sop.

| Strategy | When to use |
| --- | --- |
| critical-path-planning | Identify the shortest execution path via CPM forward/backward pass, resource leveling, and buffer insertion |
| experiment-running | Execute the plan by dispatching fresh subagents per task, monitoring status, and collecting results |
| plan-writing | Format critical path and prerequisites into bite-sized executable plan following superpowers:writing-plans conventions |
| prerequisite-planning | Identify obstacles blocking direct achievement and design intermediate objectives to overcome each |
| result-analysis | Statistically analyze collected results, verify reproducibility, and synthesize findings |

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| checkpoint-and-recover | Checkpoint state before risky operations, detect anomalies, and recover gracefully |
| result-validation-loop | Validate results through statistical testing, ROPE judgment, reproducibility re-runs, and final synthesis |
| subagent-execution-loop | Orchestrate task execution via fresh subagents with dispatch, monitoring, and result collection |
| task-decomposition | Orchestrate the breakdown of experiment design into sequenced, estimated, and formatted task plan |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| context-checkpoint | Append research process and results to the current Phase's context file. Each append MUST contain >=500 lines of markdown covering both process and results. Use this skill at plan-designated checkpoint points — typically after each strategy completes or at key decision nodes within a research Phase. |
| context-init | Create a new context file for a research Phase. Called once at Phase start to initialize the file that subsequent context-checkpoint calls will append to. Use this skill whenever a new research Phase begins and a fresh context file is needed. |
| execution-synthesis | Synthesize complete execution report from all results, tests, and reproducibility data |
| experiment-execution-paper-overview | Import SOP: paper landscape scan (from literature-engine skill) |
| experiment-execution-paper-research | Import SOP: paper full-text reading (from literature-engine skill) |
| experiment-execution-paper-search | Import SOP: paper AI summary reading (from literature-engine skill) |
| experiment-execution-quality-gate-check | Shared SOP: verify quality gate criteria are met before proceeding |
| experiment-execution-saturation-detection | Shared SOP: detect information saturation — know when to stop searching/analyzing |
| experiment-execution-web-research | Import SOP: deep full-page content analysis (from web-browsing skill) |
| experiment-execution-web-search | Import SOP: quick web scan discovery (from web-browsing skill) |

<!-- END available-tables (generated) -->
