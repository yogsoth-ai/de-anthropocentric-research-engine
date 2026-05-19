---
name: subagent-execution-loop
description: "Orchestrate task execution via fresh subagents with dispatch, monitoring, and result collection"
version: 1.0.0
category: experiment-execution
type: tactic
used-by: implementation-planning
orchestrates:
  - implementer-dispatch
  - execution-monitoring
  - result-collection
---

# Tactic: Subagent Execution Loop

## Orchestration Pattern

```pseudocode
FUNCTION subagent_execution_loop(plan):
    execution_log = []
    results = {}
    pending = plan.tasks.copy()
    
    WHILE pending.not_empty AND budget.remaining > 0:
        // Find ready tasks (all dependencies satisfied)
        ready = [t FOR t IN pending IF t.dependencies ALL IN results]
        
        IF ready.is_empty AND pending.not_empty:
            // Deadlock — all remaining tasks are blocked
            BREAK
        END
        
        FOR each task IN ready:
            // Checkpoint before execution
            checkpoint = save_state()
            
            // Dispatch
            model = select_model(task.complexity)
            prompt = construct_prompt(task, results)
            agent = SPAWN implementer-dispatch(model, prompt)
            
            // Monitor
            status = SPAWN execution-monitoring(agent)
            
            // Handle status
            SWITCH status:
                CASE DONE:
                    output = agent.output
                    validated = validate_output(output, task.success_criterion)
                    IF validated:
                        results[task.id] = SPAWN result-collection(output)
                        pending.remove(task)
                        execution_log.append({task, DONE, duration})
                    ELSE:
                        // Output doesn't meet success criterion
                        IF task.retries < 2:
                            task.retries += 1
                            // Will retry next iteration
                        ELSE:
                            execution_log.append({task, BLOCKED, "failed validation"})
                            pending.remove(task)
                        END
                    END
                    
                CASE BLOCKED:
                    execution_log.append({task, BLOCKED, status.reason})
                    IF task.retries < 2:
                        task.retries += 1
                    ELSE:
                        pending.remove(task)
                    END
                    
                CASE NEEDS_CONTEXT:
                    context = gather_context(status.request)
                    task.additional_context = context
                    task.retries += 1
                    // Will retry with context next iteration
                    
                CASE TIMEOUT:
                    restore_state(checkpoint)
                    execution_log.append({task, BLOCKED, "timeout"})
                    pending.remove(task)
            END
        END
    END
    
    RETURN {execution_log, results, blocked: pending}
END
```

## Decision Criteria

| Condition | Action |
|-----------|--------|
| Task complexity = low | Use Haiku model |
| Task complexity = medium | Use Sonnet model |
| Task complexity = high | Use Opus model |
| Task fails validation | Retry with feedback (max 2) |
| Task returns NEEDS_CONTEXT | Provide context from results/plan |
| Task times out | Restore checkpoint, mark BLOCKED |
| All ready tasks exhausted but pending remain | Report deadlock |
| Budget < 10% remaining | Stop, report partial results |
| >50% critical path BLOCKED | Abort execution |

## Error Recovery

- Timeout: Restore from checkpoint, mark task BLOCKED
- Validation failure: Provide failure reason in retry prompt
- Deadlock: Analyze dependency graph for unresolvable cycles
- Budget exhaustion: Produce partial report with remaining task list
