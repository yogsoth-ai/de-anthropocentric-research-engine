---
name: question-synthesis
description: 'SOP: synthesize all intermediate products into a final research-question set'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: 'All intermediate products (framework application, FINER results, sub-questions, etc.)'
output: 'Final RQ document (fully structured)'
dependencies:
  skills:
  - subagent-spawning
---

# Question Synthesis

Synthesize all intermediate products into a final research-question set — the campaign's final output step.

## HARD-GATE

<HARD-GATE>
Input must contain: at least 1 RQ that has passed the FINER check + its corresponding framework-application result.
</HARD-GATE>

## Pipeline

1. **Precondition check**: have all RQs passed FINER?
2. **Collect intermediate products**: framework application, scope assessment, FINER results, sub-questions, dependency graph
3. **Consistency check**: are the products mutually consistent?
4. **Formatting**: assemble the final document in the standard format
5. **Completeness check**: does each RQ include all 6 required components?
6. **Output**: final RQ document

## Required Components (per RQ)

Each RQ must include:
1. Main question (one precise sentence)
2. Framework (the framework used and how each component is filled)
3. Scope (clear boundaries)
4. Success criteria (measurable success criteria)
5. Sub-questions (if any)
6. FINER assessment (5/5 pass)

## Output Format

```
# Research Question Set

## RQ1: [Main question]
- Framework: [framework name] — [components]
- Scope: In scope: [...] / Out of scope: [...]
- Success criteria: [measurable criteria]
- Sub-questions: [if any]
- FINER: F✓ I✓ N✓ E✓ R✓

## RQ2: [Main question]
...
```
