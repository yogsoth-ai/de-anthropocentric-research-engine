---
name: cross-database-verification
description: Verify gap existence across multiple databases (Semantic Scholar, Google Scholar, arXiv, domain-specific). Distinguishes database-specific gaps from universal gaps.
execution: subagent
prompt: ./prompt.md
input: gap_description (string), databases_to_check (string)
used-by: gap-validation
---

# Cross-Database Verification

Verify gap authenticity by searching across multiple databases.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one cross-database verification pass for a single gap.
