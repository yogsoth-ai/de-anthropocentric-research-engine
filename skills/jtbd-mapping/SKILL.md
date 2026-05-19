---
name: jtbd-mapping
description: Map stakeholder Jobs-to-be-Done — functional, emotional, and social jobs for each affected party. Identifies unserved jobs as opportunity signals.
execution: subagent
prompt: ./prompt.md
input: research_domain (string), stakeholder_list (string)
used-by: stakeholder-mapping
---

# JTBD Mapping

Map stakeholder jobs-to-be-done to reveal unserved needs.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one JTBD mapping pass across stakeholders.
