---
name: sub-question-generation
description: 'SOP: Decompose a main research question into independently answerable sub-questions'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: Main research question (RQ)
output: Sub-question list + independence argument
dependencies:
  skills:
  - subagent-spawning
---

# Sub-Question Generation

Decompose a main research question into independently answerable sub-questions.

## HARD-GATE

<HARD-GATE>
Input must contain: 1 main research question that is confirmed appropriately scoped but high in complexity.
</HARD-GATE>

## Pipeline

1. **Precheck**: Does the main RQ truly need decomposition (complexity judgment)
2. **Dimension identification**: Identify the independent dimensions within the main RQ
3. **Decomposition strategy selection**: By causality / variable / condition / hierarchy / temporal order
4. **Sub-question generation**: Generate a sub-question for each dimension
5. **MECE check**: Mutually exclusive and collectively exhaustive
6. **Independence argument**: Each sub-question can be studied independently
7. **Coverage check**: Combined sub-question answers = main question answer
8. **Output**: Sub-question list + independence argument + coverage argument

## Output Format

```
Main RQ: [main question]
Decomposition strategy: [selected decomposition strategy]
Sub-questions:
  1. [sub-question 1] — Independence: [argument]
  2. [sub-question 2] — Independence: [argument]
  ...
MECE check: PASS/FAIL
Coverage check: PASS/FAIL
```
