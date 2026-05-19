---
name: result-validation-loop
description: "Validate results through statistical testing, ROPE judgment, reproducibility re-runs, and final synthesis"
version: 1.0.0
category: experiment-execution
type: tactic
used-by: implementation-planning
orchestrates:
  - result-collection
  - statistical-testing
  - reproducibility-verification
  - execution-synthesis
---

# Tactic: Result Validation Loop

## Orchestration Pattern

```pseudocode
FUNCTION result_validation_loop(raw_results, experiment_design):
    // Phase 1: Collect and structure
    structured = SPAWN result-collection(raw_results)
    VALIDATE structured.complete
    
    // Phase 2: Statistical testing
    stats = SPAWN statistical-testing(structured, experiment_design.hypotheses)
    
    // Phase 3: ROPE Judgment
    rope = experiment_design.rope  // pre-registered ROPE bounds
    
    IF stats.posterior_in_rope > 0.95:
        judgment = "ACCEPT_NULL"  // practically equivalent
    ELIF stats.posterior_above_rope > 0.95:
        judgment = "REJECT_NULL"  // meaningful effect detected
    ELSE:
        judgment = "UNDECIDED"  // need more data
    END
    
    // Phase 4: Reproducibility verification
    IF judgment != "UNDECIDED":
        repro = SPAWN reproducibility-verification(
            experiment_design,
            n_reruns = 3,
            seeds = [42, 123, 7]
        )
        
        IF repro.icc < 0.5:
            judgment = "NOT_REPRODUCIBLE"
        ELIF repro.icc < 0.75:
            judgment = judgment + "_PARTIAL_REPRO"
        ELSE:
            judgment = judgment + "_REPRODUCIBLE"
        END
    ELSE:
        // Undecided — still run reproducibility to check if issue is noise
        repro = SPAWN reproducibility-verification(
            experiment_design,
            n_reruns = 5,  // more runs for undecided cases
            seeds = [42, 123, 7, 256, 999]
        )
        
        IF repro.variance_explained_by_seed > 0.5:
            judgment = "HIGH_VARIANCE_ACROSS_SEEDS"
        END
    END
    
    // Phase 5: Synthesis
    report = SPAWN execution-synthesis({
        structured_results: structured,
        statistical_tests: stats,
        judgment: judgment,
        reproducibility: repro,
        experiment_design: experiment_design
    })
    
    RETURN report
END
```

## Decision Criteria

| Condition | Action |
|-----------|--------|
| Results incomplete (missing tasks) | Report gaps, analyze available data |
| P(in ROPE) > 95% | Accept null (no practical difference) |
| P(above ROPE) > 95% | Reject null (meaningful effect) |
| Neither threshold met | Undecided — recommend more data |
| ICC > 0.75 | Results reproducible |
| ICC 0.5-0.75 | Partially reproducible — flag |
| ICC < 0.5 | Not reproducible — investigate sources of variance |
| High seed-dependent variance | Report instability, recommend investigation |

## Quality Gates

Before producing final synthesis:
- [ ] All statistical tests report effect sizes (not just p-values)
- [ ] Confidence intervals are provided for all estimates
- [ ] ROPE was defined before analysis (not post-hoc)
- [ ] At least 3 reproducibility re-runs completed
- [ ] Limitations are explicitly stated
- [ ] Next steps are actionable
