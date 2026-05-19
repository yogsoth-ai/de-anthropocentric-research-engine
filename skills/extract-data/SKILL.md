---
name: extract-data
description: Structured data extraction from deep-read papers — produces comparison tables (method, dataset, metrics, results, limitations). Used by systematic-survey and deep-survey.
execution: subagent
prompt: ./prompt.md
input: paper_contents (string)
used-by: literature-survey
---

# Extract Data

Pull structured facts from paper full text into comparison tables.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Data extraction requires careful, systematic reading of multiple full papers simultaneously to ensure consistent extraction across all entries. Dedicated context prevents extraction drift.
