---
name: idea-synthesis
description: Synthesize diverse ideas into coherent solution concepts. Combines fragments from multiple ideation passes into structured, actionable ideas with clear mechanism descriptions.
execution: subagent
prompt: ./prompt.md
input: raw_ideas (string), campaign_context (string)
used-by: structural-deconstruction, cross-domain-discovery, assumption-destruction, biomimicry, synectics, morphological-exploration, lateral-thinking, combinatorial-creativity, perspective-forcing, systematic-enumeration
---

# Idea Synthesis

Synthesize diverse ideas into coherent solution concepts.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires holding all intermediate outputs in context simultaneously and identifying connections, redundancies, and complementary fragments across multiple ideation passes.
