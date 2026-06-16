---
name: claim-refinement
description: Propose a refined claim that survives counterexamples while preserving
  maximum explanatory power (Lakatos lemma-incorporation).
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Claim Refinement

Subagent that refines claims to survive counterexamples using lemma incorporation, scope narrowing, or claim splitting.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
