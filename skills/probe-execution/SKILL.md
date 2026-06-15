---
name: probe-execution
description: Execute a single attack probe against an artifact, record the result
  with evidence and severity classification.
execution: subagent
prompt: ./prompt.md
input: vector (string), artifact (string), persona (string)
dependencies:
  sops:
  - spawn-agent
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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
