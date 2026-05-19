---
name: clr-validation
description: Apply Goldratt's 8 Categories of Legitimate Reservation to validate causal claims. Tests clarity, existence, sufficiency, and logical integrity.
execution: subagent
prompt: ./prompt.md
input: causal_claim (string), context (string)
used-by: root-cause-drilling, assumption-audit
---

# CLR Validation

Validate causal logic via Categories of Legitimate Reservation.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one CLR validation pass.
