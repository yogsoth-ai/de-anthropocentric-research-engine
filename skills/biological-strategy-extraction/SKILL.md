---
name: biological-strategy-extraction
description: "Extract strategy principles from organisms. Identify mechanism-level details of how biological systems achieve their function."
execution: subagent
prompt: ./prompt.md
input: organism (string)
used-by: biologize-and-discover, functional-analogy, biotriz-resolution
---

# Biological Strategy Extraction

Extract strategy principles from organisms.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Strategy extraction requires deep dive into biological mechanisms, understanding multi-scale interactions, and identifying the transferable principle beneath species-specific details. Benefits from focused analytical attention.
