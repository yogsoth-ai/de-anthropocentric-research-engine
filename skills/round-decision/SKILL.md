---
name: round-decision
description: Decide whether to continue iterating or stop based on consensus score,
  round number, and stability.
execution: subagent
prompt: ./prompt.md
input: consensus_score, round_n, stability
dependencies:
  sops:
  - spawn-agent
---

# Round Decision

Decide whether to run another Delphi round or stop the iteration. Uses consensus score, current round number, and stability (whether scores changed from prior round) to make the continue/stop decision.

## Execution

Spawn a subagent that evaluates the stopping criteria and returns a clear continue/stop decision with rationale.

## Why Subagent

- Decision logic is a pure function of three inputs
- Rationale documentation is important for audit trail
- Keeps orchestration logic clean

## HARD-GATE

Output MUST contain: `decision` (continue/stop), `reason` (string), and `next_action` (what to do next). Decision must be exactly one of "continue" or "stop".

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
