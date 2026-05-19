---
name: probe-execution
description: Execute a single attack probe against an artifact, record the result with evidence and severity classification.
execution: subagent
prompt: ./prompt.md
input: vector (string), artifact (string), persona (string)
used-by: [red-teaming]
---

# Probe Execution

Executes a single attack vector and records the detailed result.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Probe execution requires committed adversarial stance. The prober must genuinely attempt to break the artifact without pulling punches or rationalizing away findings.

## Input

- **vector**: The specific attack vector to execute (from attack-vector-generation)
- **artifact**: The artifact being probed
- **persona**: Optional adversarial persona to adopt during probing

## Output

- **result**: success/failure/partial (did the attack find a vulnerability?)
- **evidence**: Specific evidence supporting the result
- **severity**: critical/major/minor (if vulnerability found)
- **follow_up**: Whether deeper probing is warranted
