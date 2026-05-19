---
name: scenario-narrative-construction
description: "Build rich narratives for surviving morphological configurations using Shell method"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - narrative-scenario
  - cross-consistency-filtering
input: parameter configuration, consistency context, research approach description
output: rich scenario narrative with causal logic, signposts, and implications
---

# SOP: Scenario Narrative Construction

Build a rich, internally consistent narrative for a given parameter configuration. The narrative should tell a coherent story of how this future comes to be, what it looks like, and what it means for the research approach.

Subagent — spawned via subagent-spawning/spawn-agent skill.
