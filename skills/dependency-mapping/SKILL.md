---
name: dependency-mapping
description: 'SOP: map dependency relationships among sub-questions'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: 'List of sub-questions'
output: 'Dependency graph + critical path + suggested answering order'
dependencies:
  skills:
  - subagent-spawning
---

# Dependency Mapping

Map dependency relationships among sub-questions — determine which sub-questions must be answered first.

## HARD-GATE

<HARD-GATE>
Input must contain: ≥2 already-generated sub-questions.
</HARD-GATE>

## Pipeline

1. **Pre-check**: is the sub-question list complete
2. **Dependency identification**: for each pair of sub-questions, judge whether a dependency exists
3. **Dependency-type tagging**: strong dependency (must be completed first) / weak dependency (helpful but not required)
4. **Cycle detection**: check whether circular dependencies exist
5. **Critical-path identification**: find the longest dependency chain
6. **Parallelization-opportunity identification**: find groups of sub-questions that can proceed simultaneously
7. **Output**: dependency graph + critical path + parallelization opportunities

## Output Format

```
Dependencies:
  SQ1 → SQ2 (strong: SQ2 needs SQ1's result as input)
  SQ1 → SQ3 (weak: SQ3 benefits from SQ1 but can proceed independently)
  SQ2 → SQ4 (strong)

Circular dependencies: NONE / [list]
Critical path: SQ1 → SQ2 → SQ4 (length: 3)
Parallel groups: [SQ1, SQ3] can run simultaneously
```
