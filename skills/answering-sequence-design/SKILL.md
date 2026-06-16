---
name: answering-sequence-design
description: 'SOP: Design the optimal answering order for sub-questions'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: Sub-question list + dependency graph
output: Execution sequence + rationale + parallelization opportunities
dependencies:
  skills:
  - subagent-spawning
---

# Answering Sequence Design

Design the optimal answering order for sub-questions — based on dependency relationships and resource efficiency.

## HARD-GATE

<HARD-GATE>
Input must contain: sub-question list + dependency graph (from dependency-mapping).
</HARD-GATE>

## Pipeline

1. **Precondition check**: is the dependency graph acyclic
2. **Topological sort**: determine the basic order based on dependency relationships
3. **Parallel grouping**: identify sub-questions that can proceed simultaneously
4. **Resource optimization**: adjust the order considering resource constraints
5. **Risk ordering**: prioritize high-risk/high-uncertainty items (fail fast)
6. **Final sequence**: determine the optimal sequence by integrating the above factors
7. **Output**: execution sequence + phased plan + parallelization opportunities

## Output Format

```
Phase 1 (parallel): [SQ1, SQ3] — no mutual dependencies
Phase 2 (sequential): [SQ2] — depends on SQ1
Phase 3 (parallel): [SQ4, SQ5] — depend on SQ2
Rationale: [why this order is optimal]
Risk note: [which sub-questions, if they fail, will affect subsequent ones]
```
</output>
