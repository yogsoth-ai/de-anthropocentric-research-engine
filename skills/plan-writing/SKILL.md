---
name: plan-writing
description: "Format critical path and prerequisites into bite-sized executable plan following superpowers:writing-plans conventions"
version: 1.0.0
category: experiment-execution
type: strategy
used-by: implementation-planning
sops:
  - plan-formatting
tactics:
  - task-decomposition
---

# Strategy: Plan Writing

**Key Question**: How to write it as an executable plan?

## Methodology

Adaptation of superpowers:writing-plans pattern — transforms abstract task graphs into concrete, executable task specifications that a subagent can complete without ambiguity.

### Core Principles (from superpowers:writing-plans)
1. **Bite-sized tasks**: Each task = one clear action with one clear output
2. **Exact paths**: Every file reference is absolute, every command is copy-pasteable
3. **TDD where applicable**: Test specification before implementation
4. **No placeholders**: No TBD, TODO, "figure out later" — everything resolved NOW
5. **Context-minimal**: Each task carries only the context needed to execute it

## Execution Flow

```
[Critical path + IO sequence from strategies 1-2]
    → plan-formatting (transform into executable task specs)
        → HARD-GATE: scan for TBD/TODO/placeholders → REJECT if found
            → OUTPUT: executable plan document
```

## Budget Gate

| Step | Max Budget | Output |
|------|-----------|--------|
| Plan formatting | 5% | Complete task plan |
| Validation pass | 2% | Confirmed no placeholders |

## Quality Criteria

A valid plan has:
- [ ] Every task has: ID, description, inputs, expected output, success criterion
- [ ] Every file path is absolute
- [ ] Every task is independently executable (no hidden dependencies)
- [ ] Critical path tasks are marked
- [ ] Buffer tasks (non-critical) are identified with float values
- [ ] No TBD/TODO/placeholder text anywhere
- [ ] Estimated duration per task (from PERT)
