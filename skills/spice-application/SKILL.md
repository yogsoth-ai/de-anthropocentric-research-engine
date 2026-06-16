---
name: spice-application
description: 'SOP: Apply the SPICE framework to structure an evaluation research question'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: Research intent (evaluation research direction)
output: Complete SPICE fill-in + RQ statement
dependencies:
  skills:
  - subagent-spawning
---

# SPICE Application

Apply the SPICE framework — suitable for evaluation research.

## HARD-GATE

<HARD-GATE>
Input must contain: a clear evaluation research intent (assessing the effect of an intervention / program / service).
</HARD-GATE>

## Pipeline

1. **Precheck**: Confirm the research is suitable for the SPICE framework
2. **S (Setting)**: Define the research setting
3. **P (Perspective)**: Define the evaluation perspective (whose perspective?)
4. **I (Intervention)**: Define the intervention / program being evaluated
5. **C (Comparison)**: Define the comparison object
6. **E (Evaluation)**: Define the evaluation metrics and methods
7. **Assembly**: Assemble the components into a complete RQ sentence
8. **Output**: SPICE fill-in table + RQ statement

## Output Format

```
S: [research setting]
P: [evaluation perspective]
I: [intervention being evaluated]
C: [comparison object]
E: [evaluation metrics and methods]

RQ: "In [S], from [P]'s perspective, how does [I] compare to [C] in terms of [E]?"
```
