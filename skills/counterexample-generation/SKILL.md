---
name: counterexample-generation
description: "Systematically generate counterexamples (monsters) to a given claim using diverse heuristic strategies."
execution: subagent
prompt: ./prompt.md
used-by: [adversarial-stress-testing]
---

# Counterexample Generation

Subagent that produces counterexamples to a claim using boundary cases, degenerate cases, and domain-specific heuristics.
