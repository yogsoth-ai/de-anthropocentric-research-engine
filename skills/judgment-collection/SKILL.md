---
name: judgment-collection
description: Collect independent judgments from all perspectives on a given question.
execution: subagent
prompt: ./prompt.md
input: question, perspectives[]
used-by: structured-consensus
---

# Judgment Collection

Collect independent judgments from each perspective on the focal question. Each perspective provides its rating/estimate and supporting reasoning without seeing others' responses.

## Execution

Spawn a subagent that takes the question and list of perspectives, then generates an independent judgment from each perspective's viewpoint. Judgments include both a structured response (rating, probability, or position) and free-text reasoning.

## Why Subagent

- Each perspective must be generated independently without cross-contamination
- The collection task is well-bounded and parallelizable
- Keeps the parent context clean for orchestration logic

## HARD-GATE

Output MUST contain: one judgment object per perspective, each with `perspective_id`, `response`, and `reasoning` fields. Missing any perspective fails the gate.
