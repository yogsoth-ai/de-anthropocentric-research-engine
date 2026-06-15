---
name: resource-quantification
description: Quantify resource demand vs supply vs gap for each resource category
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: experiment plan, resource inventory, task estimates
output: demand/supply/gap table per resource category with severity ratings
dependencies:
  sops:
  - spawn-agent
---

# SOP: Resource Quantification

Quantify resource demand, supply, and gap for each resource category (compute, data, time, human, financial).

Subagent — spawned via subagent-spawning/spawn-agent skill.
