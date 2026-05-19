---
name: evidence-grading
description: Assess evidence quality using GRADE/SOE framework. Rates certainty level and identifies downgrade reasons.
execution: subagent
prompt: ./prompt.md
input: evidence_collection (string), grading_context (string)
used-by: gap-identification, gap-prioritization
---

# Evidence Grading

Assess the quality and certainty of evidence supporting or surrounding a gap.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one evidence grading assessment.
