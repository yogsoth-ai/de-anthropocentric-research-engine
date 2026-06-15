---
name: execution-monitoring
description: Monitor execution progress, detect anomalies, and report status
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: running subagent handle and task specification
output: execution status (DONE/BLOCKED/NEEDS_CONTEXT/TIMEOUT) with anomaly report
---

# SOP: Execution Monitoring

Monitor a running subagent for progress, anomalies, and completion status.

Subagent — spawned via subagent-spawning/spawn-agent skill.
