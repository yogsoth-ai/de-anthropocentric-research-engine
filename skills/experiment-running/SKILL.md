---
name: experiment-running
description: "Execute the plan by dispatching fresh subagents per task, monitoring status, and collecting results"
version: 1.0.0
category: experiment-execution
type: strategy
used-by: implementation-planning
sops:
  - implementer-dispatch
  - execution-monitoring
  - result-collection
tactics:
  - subagent-execution-loop
  - checkpoint-and-recover
---

# Strategy: Experiment Running

**Key Question**: How to execute?

## Methodology

Adaptation of superpowers:subagent-driven-development pattern — systematic execution via fresh subagents with three-stage review and continuous progress.

### Core Principles (from superpowers:subagent-driven-development)
1. **Fresh subagent per task**: Clean context prevents cross-contamination
2. **Three-stage review**: Implementer → Reviewer → Integration check
3. **Status codes**: DONE / BLOCKED / NEEDS_CONTEXT
4. **Continuous execution**: Don't stop at first failure — continue with independent tasks
5. **Checkpoint before risk**: Save state before destructive or irreversible operations

## Execution Flow

```
FOR each task in plan (topological order):
    IF dependencies not met:
        SKIP (will revisit)
    ELSE:
        checkpoint current state
        implementer-dispatch (select model, construct prompt, spawn)
        execution-monitoring (poll status, detect anomalies)
        IF status == DONE:
            result-collection (gather, validate, structure)
            mark task complete
        ELIF status == BLOCKED:
            log blocker, continue with next independent task
        ELIF status == NEEDS_CONTEXT:
            provide context, retry (max 2 retries)
        END
    END
END

IF any tasks BLOCKED:
    attempt unblock (resolve dependencies, provide missing context)
    retry blocked tasks
END
```

## Budget Gate

| Step | Max Budget | Output |
|------|-----------|--------|
| Per-task execution | 50% of execution budget / N tasks | Task result |
| Monitoring overhead | 5% of execution budget | Status log |
| Retry budget | 10% of execution budget | Unblocked tasks |

## Key Decisions

- **Model selection**: Simple tasks → Haiku; Complex tasks → Sonnet; Critical/creative → Opus
- **Retry policy**: Max 2 retries per task, then mark BLOCKED
- **Parallel execution**: Independent tasks can run in parallel (respect resource limits)
- **Abort condition**: If >50% of critical path tasks are BLOCKED, abort and report
