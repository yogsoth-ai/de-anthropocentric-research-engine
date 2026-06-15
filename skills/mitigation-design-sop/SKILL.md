---
name: mitigation-design-sop
description: Design prevention, detection, and response measures for high-priority
  failure modes. Produces actionable countermeasure specifications.
execution: subagent
prompt: ./prompt.md
input: high_priority_modes (string), chains (string), function_tree (string)
dependencies:
  sops:
  - spawn-agent
---

# Mitigation Design SOP

Designs three-layer countermeasures (prevention, detection, response) for high-priority failure modes.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Mitigation design requires creative problem-solving focused on solutions, isolated from the analytical mindset of failure identification.

## Input

- **high_priority_modes**: H-priority failure modes with chains
- **chains**: Full cause-mode-effect chains for context
- **function_tree**: Function structure for integration points

## Output

- **mitigations**: For each H-priority mode: prevention, detection, and response measures
- **implementation_notes**: Feasibility and resource requirements
- **residual_risk**: Expected risk remaining after mitigation
