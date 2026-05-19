---
name: debate-transcript-analysis
description: Extracts key turning points, patterns, and insights from completed debate transcripts. Produces structured summary for verdict synthesis.
execution: subagent
prompt: ./prompt.md
input: full_transcript (string), round_verdicts (string), final_confidence (string)
used-by: [multiagent-debate]
---

# Debate Transcript Analysis

Extracts key turning points from completed debates.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Post-debate analysis requires reviewing the full transcript with fresh eyes — isolated context prevents anchoring to any single round's perspective.

## Input

- **full_transcript**: Complete debate transcript (all rounds)
- **round_verdicts**: All judge verdicts
- **final_confidence**: Final calibrated confidence score

## Output

- **turning_points**: Moments where the debate shifted significantly
- **key_vulnerabilities**: Most impactful weaknesses identified
- **strongest_defenses**: Most effective counter-arguments
- **unresolved_tensions**: Issues that remained contested
- **summary**: Concise narrative of the debate arc

## Budget

One unit = one transcript analysis per completed debate.
