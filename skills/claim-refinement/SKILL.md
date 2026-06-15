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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
