---
name: mitigation-proposal
description: Proposes concrete mitigation strategies for identified weaknesses. Generates prevention, detection, and response measures with feasibility assessment.
execution: subagent
prompt: ./prompt.md
input: classified_weakness (string), artifact_context (string)
used-by: failure-anticipation, red-teaming, adversarial-stress-testing
---

# Mitigation Proposal

Proposes concrete mitigation strategies for identified weaknesses.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Mitigation design requires creative problem-solving in dedicated context, separate from the attack/discovery mindset.

## Input

- **classified_weakness**: The weakness with severity classification
- **artifact_context**: The original artifact context

## Output

- **prevention_measures**: What changes prevent this weakness
- **detection_mechanisms**: What checks catch this earlier
- **response_actions**: What contingency limits damage
- **feasibility_assessment**: How practical are these mitigations
- **residual_risk**: What risk remains after mitigation

## Constraint

Stop at proposal — do NOT modify the original artifact. Suggestions only.

## Budget

One unit = one mitigation proposal per weakness. Focus on fatal and major findings.
