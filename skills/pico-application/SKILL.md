---
name: pico-application
description: 'SOP: apply the PICO/PICOTS framework to structure a research question'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: 'Research intent + hypothesis'
output: 'Complete PICO fill-in + RQ statement'
dependencies:
  skills:
  - subagent-spawning
---

# PICO Application

Apply the PICO/PICOTS framework — suited to quantitative/interventional research.

## HARD-GATE

<HARD-GATE>
Input must contain: a clear research intent (involving an intervention or quantitative comparison).
</HARD-GATE>

## Pipeline

1. **Precondition check**: confirm the research is suited to the PICO framework
2. **P (Population)**: define the target population/subjects (specific characteristics)
3. **I (Intervention)**: define the intervention/exposure/method
4. **C (Comparison)**: define the control group/alternative
5. **O (Outcome)**: define the expected outcome/measurement indicator
6. **T (Timeframe)**: optional — define the time range
7. **S (Setting)**: optional — define the research setting
8. **Assembly**: assemble the components into a complete RQ sentence
9. **Output**: PICO fill-in table + RQ statement

## Output Format

```
P: [Specific population description]
I: [Specific intervention description]
C: [Specific comparison description]
O: [Specific outcome indicator]
T: [Time range] (optional)
S: [Research setting] (optional)

RQ: "In [P], does [I] compared to [C] improve [O] (within [T], in [S])?"
```
