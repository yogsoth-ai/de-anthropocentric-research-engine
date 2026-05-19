---
name: causal-chain-tracing
description: "Trace UDE to root cause via IF...THEN...BECAUSE logic chains"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by: bottleneck-identification
input: numbered UDE list with evidence
output: causal tree with IF-THEN-BECAUSE chains converging to root causes
---

# SOP: Causal Chain Tracing

Trace each Undesirable Effect backward through causal chains using IF...THEN...BECAUSE logic to find root causes and convergence points.

Subagent — spawned via subagent-spawning/spawn-agent skill.
