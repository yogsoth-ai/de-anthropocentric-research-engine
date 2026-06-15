---
name: claim-negation
description: Formally negate the core claim, producing the logical complement for
  reductio testing.
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Claim Negation

Subagent that takes a claim P and produces its formal negation ~P, ensuring the negation is logically precise and preserves scope.
