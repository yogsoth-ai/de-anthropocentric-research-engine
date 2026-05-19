---
name: domain-scanning
description: Scan distant domains for transferable principles. Uses web-search and paper-overview to identify analogous solutions in unrelated fields.
execution: subagent
prompt: ./prompt.md
input: problem_description (string), excluded_domains (string)
used-by: cross-domain-discovery, biomimicry, synectics, combinatorial-creativity
---

# Domain Scanning

Scan distant domains for transferable principles.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Domain scanning requires creative lateral search across multiple unrelated fields, evaluating each for structural similarity to the target problem. Benefits from dedicated exploratory attention.
