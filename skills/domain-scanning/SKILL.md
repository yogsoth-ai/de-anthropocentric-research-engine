---
name: domain-scanning
description: Scan distant domains for transferable principles. Uses web-search and
  paper-overview to identify analogous solutions in unrelated fields.
execution: subagent
prompt: ./prompt.md
input: problem_description (string), excluded_domains (string)
dependencies:
  sops:
  - spawn-agent
---

# Domain Scanning

Scan distant domains for transferable principles.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Domain scanning requires creative lateral search across multiple unrelated fields, evaluating each for structural similarity to the target problem. Benefits from dedicated exploratory attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
