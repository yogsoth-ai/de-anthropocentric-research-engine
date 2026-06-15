---
name: breakpoint-detection
description: Test a claim at extreme parameter values and detect the precise point
  where it breaks down.
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Breakpoint Detection

Subagent that evaluates a claim at extreme values to find the precise breakpoint where validity fails.
