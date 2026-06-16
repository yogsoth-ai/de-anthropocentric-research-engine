---
name: finer-criteria-check
description: 'SOP: check research-question quality against each of the 5 FINER criteria'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: 'Research question (RQ)'
output: '5 per-criterion verdicts + revision suggestions for failed items'
dependencies:
  skills:
  - subagent-spawning
---

# FINER Criteria Check

FINER 5-criteria per-item check — the standardized test of research-question quality.

## HARD-GATE

<HARD-GATE>
Input must contain: at least 1 fully stated research question.
</HARD-GATE>

## Pipeline

1. **Pre-check**: is the RQ a complete sentence
2. **F (Feasible)**: is it feasible under the available resources/time/data
3. **I (Interesting)**: is it interesting to scholars and practitioners in the field
4. **N (Novel)**: does it provide new knowledge/new perspective/new method
5. **E (Ethical)**: does it comply with research ethics
6. **R (Relevant)**: is it relevant to the field/society/practice
7. **Overall verdict**: all pass / partial pass
8. **Revision suggestions**: give specific revision directions for failed items
9. **Output**: the 5 verdicts + revision suggestions (if any)

## Output Format

```
F: PASS/FAIL — [rationale]
I: PASS/FAIL — [rationale]
N: PASS/FAIL — [rationale]
E: PASS/FAIL — [rationale]
R: PASS/FAIL — [rationale]

Overall: PASS (5/5) / PARTIAL (X/5)
Suggestions: [specific revision suggestions for FAIL items]
```
