---
name: failure-mode-extraction
description: Extract structured failure mode list from raw scenarios or artifact analysis.
  Produces standardized failure mode records.
execution: subagent
prompt: ./prompt.md
input: scenarios (string), artifact (string)
dependencies:
  sops:
  - spawn-agent
---

# Failure Mode Extraction

Converts raw failure scenarios or artifact analysis into structured failure mode records.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Extraction requires systematic decomposition without creative bias. Isolated context ensures consistent structuring.

## Input

- **scenarios**: Raw failure scenarios from pre-mortem or analysis
- **artifact**: Original artifact for reference

## Output

- **failure_modes**: List of structured failure mode records (ID, name, description, category)
- **deduplication_notes**: Merged or related modes flagged

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
