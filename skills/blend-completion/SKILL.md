---
name: blend-completion
description: Complete blend with background knowledge
execution: subagent
prompt: ./prompt.md
input: initial_blend (object)
used-by: combinatorial-creativity, concept-blending
---

# Blend Completion

Complete blend with background knowledge — recruit additional structure from long-term memory and world knowledge to fill out the blend.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Blend completion requires broad knowledge recruitment — bringing in patterns, frames, and schemas from background knowledge that weren't in either input but are triggered by the blend's emergent structure. Benefits from exploratory breadth.
