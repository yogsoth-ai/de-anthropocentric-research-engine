---
name: patent-query-formulation
description: Construct keyword + IPC/CPC + assignee combination search strategies
  for patent databases
execution: subagent
prompt: ./prompt.md
input: research_question, target_technology, known_assignees
dependencies:
  sops:
  - spawn-agent
---

# Patent Query Formulation

Generates multi-faceted patent search strategies combining keywords, classification codes, and assignee names to maximize recall across patent databases.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
