---
name: activity-listing
description: Enumerate all implementation activities from an experiment design
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: experiment design document
output: complete list of implementation activities with descriptions
dependencies:
  sops:
  - spawn-agent
---

# SOP: Activity Listing

Enumerate all discrete implementation activities required to execute an experiment design.

Subagent — spawned via subagent-spawning/spawn-agent skill.
