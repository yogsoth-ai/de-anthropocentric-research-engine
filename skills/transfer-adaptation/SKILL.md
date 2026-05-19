---
name: transfer-adaptation
description: Adapt transferred principle to target problem constraints. Produces concrete adapted solutions from abstract principles.
execution: subagent
prompt: ./prompt.md
input: abstract_principle (string), target_problem (string)
used-by: cross-domain-discovery, analogical-transfer, design-by-analogy, bridge-validation, forced-bridge-construction
---

# Transfer Adaptation

Adapt transferred principle to target problem constraints.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Transfer adaptation requires careful reasoning about how abstract mechanisms instantiate in a new domain. Benefits from dedicated attention to constraint satisfaction and risk identification without being distracted by the broader creative process.
