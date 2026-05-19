---
name: undesirable-effect-listing
description: "List current Undesirable Effects (UDEs) — observable symptoms of system underperformance"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by: bottleneck-identification
input: system description, observed problems, stakeholder complaints
output: numbered UDE list with evidence and severity ratings
---

# SOP: Undesirable Effect Listing

List all observable Undesirable Effects (UDEs) in the system — symptoms that indicate the system is not performing as desired.

Subagent — spawned via subagent-spawning/spawn-agent skill.
