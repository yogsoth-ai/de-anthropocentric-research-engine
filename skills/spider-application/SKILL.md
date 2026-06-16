---
name: spider-application
description: 'SOP: Apply the SPIDER framework to structure a qualitative research question'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: Research intent (qualitative research direction)
output: Complete SPIDER fill-in + RQ statement
dependencies:
  skills:
  - subagent-spawning
---

# SPIDER Application

Apply the SPIDER framework — suitable for qualitative research.

## HARD-GATE

<HARD-GATE>
Input must contain: a clear qualitative research intent (exploratory, interpretive, explanatory).
</HARD-GATE>

## Pipeline

1. **Precheck**: Confirm the research is suitable for the SPIDER framework
2. **S (Sample)**: Define the sample / research subjects
3. **PI (Phenomenon of Interest)**: Define the phenomenon of interest
4. **D (Design)**: Define the research design (interview / observation / case study, etc.)
5. **E (Evaluation)**: Define the evaluation approach (thematic analysis / grounded theory, etc.)
6. **R (Research type)**: Define the research type (exploratory / descriptive / explanatory)
7. **Assembly**: Assemble the components into a complete RQ sentence
8. **Output**: SPIDER fill-in table + RQ statement

## Output Format

```
S: [sample description]
PI: [phenomenon of interest]
D: [research design]
E: [evaluation approach]
R: [research type]

RQ: "How do [S] experience [PI], as explored through [D] and evaluated via [E]?"
```
