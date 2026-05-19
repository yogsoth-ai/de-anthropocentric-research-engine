---
name: checkpoint-and-recover
description: "Checkpoint state before risky operations, detect anomalies, and recover gracefully"
version: 1.0.0
category: experiment-execution
type: tactic
used-by: implementation-planning
orchestrates:
  - execution-monitoring
  - result-collection
---

# Tactic: Checkpoint and Recover

## Orchestration Pattern

```pseudocode
FUNCTION checkpoint_and_recover(task, execute_fn):
    // Pre-execution checkpoint
    checkpoint = {
        timestamp: now(),
        task_id: task.id,
        state: capture_current_state(),
        files_modified: [],
        outputs_produced: []
    }
    save_checkpoint(checkpoint)
    
    TRY:
        // Execute with monitoring
        monitor = SPAWN execution-monitoring(task)
        result = execute_fn(task)
        
        // Post-execution validation
        IF monitor.anomalies_detected:
            RAISE AnomalyError(monitor.anomalies)
        END
        
        // Validate result integrity
        validated = SPAWN result-collection(result, task.success_criterion)
        
        IF validated.complete AND validated.consistent:
            // Success — archive checkpoint (keep for audit trail)
            archive_checkpoint(checkpoint)
            RETURN {status: DONE, result: validated}
        ELSE:
            // Partial success — decide whether to keep or rollback
            IF validated.partial_value > threshold:
                archive_checkpoint(checkpoint)
                RETURN {status: PARTIAL, result: validated, missing: validated.gaps}
            ELSE:
                restore_state(checkpoint)
                RETURN {status: ROLLED_BACK, reason: validated.failure_reason}
            END
        END
        
    CATCH error:
        // Failure — diagnose and recover
        diagnosis = diagnose_failure(error, checkpoint, task)
        
        SWITCH diagnosis.severity:
            CASE TRANSIENT:
                // Retry without rollback (e.g., network timeout)
                RETURN {status: RETRY, reason: diagnosis}
                
            CASE CORRUPTING:
                // Rollback to checkpoint
                restore_state(checkpoint)
                RETURN {status: ROLLED_BACK, reason: diagnosis}
                
            CASE FATAL:
                // Rollback and escalate
                restore_state(checkpoint)
                RETURN {status: FATAL, reason: diagnosis, escalate: true}
        END
    END
END
```

## Decision Criteria

| Condition | Action |
|-----------|--------|
| Task modifies existing files | MUST checkpoint before |
| Task is read-only/analysis | Checkpoint optional |
| Anomaly detected during execution | Pause, diagnose, decide |
| Result partially valid | Keep if value > threshold |
| Result invalid | Rollback to checkpoint |
| Transient error (timeout, rate limit) | Retry without rollback |
| Corrupting error (bad state) | Rollback then retry |
| Fatal error (impossible task) | Rollback and escalate |

## Checkpoint Contents

A checkpoint captures:
- Timestamp and task ID
- File system state (modified files' contents before modification)
- Execution context (variables, intermediate results)
- Dependencies state (which tasks were complete)

## Recovery Strategies

1. **Retry**: Same task, same parameters (for transient failures)
2. **Retry with modification**: Same task, adjusted parameters (for NEEDS_CONTEXT)
3. **Rollback and skip**: Restore state, mark task BLOCKED, continue
4. **Rollback and escalate**: Restore state, report to orchestrator for human decision
