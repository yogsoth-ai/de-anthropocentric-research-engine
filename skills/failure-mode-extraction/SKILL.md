---
name: failure-mode-extraction
description: Extract structured failure mode list from raw scenarios or artifact analysis. Produces standardized failure mode records.
execution: subagent
prompt: ./prompt.md
input: scenarios (string), artifact (string)
used-by: [failure-anticipation]
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
