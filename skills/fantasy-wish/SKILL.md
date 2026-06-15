---
name: fantasy-wish
description: Unconstrained wish-fulfillment ideation. Ignore all physical laws to
  imagine the ideal solution, then identify realization directions.
execution: subagent
prompt: ./prompt.md
input: problem (string)
dependencies:
  sops:
  - spawn-agent
---

# Fantasy Wish

Unconstrained wish-fulfillment ideation.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Fantasy ideation requires complete suspension of critical judgment and physical constraints. Benefits from dedicated imaginative space without analytical interference pulling ideas back to feasibility prematurely.
