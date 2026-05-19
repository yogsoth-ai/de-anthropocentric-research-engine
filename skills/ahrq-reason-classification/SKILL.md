---
name: ahrq-reason-classification
description: Classify gap root causes using AHRQ 4-reason framework (insufficient info, biased info, inconsistent info, not yet integrated).
execution: subagent
prompt: ./prompt.md
input: gap_description (string), surrounding_evidence (string)
used-by: gap-classification
---

# AHRQ Reason Classification

Classify why a research gap exists using the AHRQ framework.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one AHRQ reason classification pass.
