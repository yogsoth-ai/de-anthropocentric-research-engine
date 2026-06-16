---
name: success-criteria-definition
description: 'SOP: Define measurable success criteria for a research question'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: Research question (RQ)
output: Measurable success criteria + thresholds
dependencies:
  skills:
  - subagent-spawning
---

# Success Criteria Definition

Define measurable success criteria for a research question — what counts as "having answered this question".

## HARD-GATE

<HARD-GATE>
Input must contain: 1 research question that has passed the FINER check.
</HARD-GATE>

## Pipeline

1. **Precheck**: Has the RQ passed FINER
2. **Result type identification**: Quantitative result / qualitative result / mixed
3. **Metric definition**: What metric measures "the question was answered"
4. **Threshold setting**: What degree counts as "successfully answered"
5. **Partial success definition**: What counts as "partially answered"
6. **Failure definition**: What outcome means "the question cannot be answered"
7. **Output**: Success criteria + thresholds + partial success + failure conditions

## Output Format

```
RQ: [research question]
Success criteria:
  - Full success: [concrete conditions + thresholds]
  - Partial success: [concrete conditions]
  - Failure/inconclusive: [concrete conditions]
Measurement: [how to measure]
Timeline: [expected duration]
```
