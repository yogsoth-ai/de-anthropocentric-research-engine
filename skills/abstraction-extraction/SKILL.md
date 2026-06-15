---
name: abstraction-extraction
description: Extract abstract principles from concrete domain cases. Strips domain-specific
  details to reveal transferable mechanisms.
execution: subagent
prompt: ./prompt.md
input: source_domain_case (string)
dependencies:
  sops:
  - spawn-agent
---

# Abstraction Extraction

Extract abstract principles from concrete domain cases.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Abstraction requires careful layered reasoning — moving from concrete details through functional description to pure relational structure. Benefits from dedicated attention to avoid premature abstraction or under-abstraction.
