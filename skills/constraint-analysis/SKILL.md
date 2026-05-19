---
name: constraint-analysis
description: "What limits us — identify bottlenecks, quantify constraints, analyze dependencies, resolve conflicts before experiment execution"
version: 1.0.0
category: experiment-execution
type: campaign
strategies:
  - bottleneck-identification
  - resource-constraint
  - assumption-constraint
  - dependency-constraint
  - conflict-resolution
tactics:
  - constraint-tree-building
  - sensitivity-ranking
  - constraint-breaking
---

# Campaign 2: Constraint Analysis

## HARD-GATE

Before entering this campaign, the following must be true:

| Gate | Condition |
|------|-----------|
| Research direction exists | North star or research question is crystallized |
| Scope is bounded | Problem space has defined boundaries |
| Resources are enumerable | Can list available compute, data, time, people, budget |
| Stakeholders identified | Know who cares about the outcome |

If any gate fails, return to Campaign 1 (research-direction) or pre-campaign intake.

## Campaign Goal

Produce a comprehensive constraint profile that identifies:
1. The system bottleneck (TOC focusing)
2. Resource gaps (demand vs supply)
3. Fragile assumptions (vulnerability ranked)
4. Dependency chains (critical path)
5. Conflicts between constraints (with resolution injections)

## Strategy Selection

| Situation | Strategy | When to Use |
|-----------|----------|-------------|
| Unknown bottleneck | bottleneck-identification | System performance is limited but cause unclear |
| Resource uncertainty | resource-constraint | Need to verify feasibility of resource plan |
| Assumption risk | assumption-constraint | Key assumptions untested or fragile |
| Sequencing unclear | dependency-constraint | Task ordering and prerequisites unknown |
| Conflicting demands | conflict-resolution | Two or more constraints oppose each other |

Default execution order: bottleneck-identification → resource-constraint → assumption-constraint → dependency-constraint → conflict-resolution

## Budget Gate

| Resource | Budget | Escalation |
|----------|--------|------------|
| Subagent calls | ≤15 per strategy | Pause and report partial |
| Wall-clock time | ≤30 min per strategy | Checkpoint and continue |
| Context tokens | ≤80k per strategy | Summarize and spawn fresh |
| Total campaign | ≤5 strategies | Skip if constraint already resolved |

## Context Management

- Each strategy produces a structured artifact (table/tree/graph)
- Artifacts are passed forward as compressed summaries
- Full details stored in vault pages for later retrieval
- Campaign synthesis merges all strategy outputs

## Minimum Yield

Campaign is complete when:
- At least 1 binding constraint identified and characterized
- Resource feasibility assessed (go/no-go)
- Critical dependency chain mapped
- No unresolved conflicts between top-3 constraints
- Constraint synthesis report produced
