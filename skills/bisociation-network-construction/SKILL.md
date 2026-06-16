---
name: bisociation-network-construction
description: Build multi-domain bridging concept network. Creates a network of collision
  points between multiple thinking matrices.
execution: subagent
prompt: ./prompt.md
input: multiple_source_domains (string)
dependencies:
  sops:
  - spawn-agent
---

# Bisociation Network Construction

Build multi-domain bridging concept network.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Network construction requires holding multiple domain logics in working memory simultaneously and systematically identifying collision points between all pairs. Benefits from dedicated context to manage the combinatorial complexity.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
