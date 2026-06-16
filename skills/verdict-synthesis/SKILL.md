---
name: verdict-synthesis
description: Synthesizes findings from a completed campaign into typed verdict reports.
  Produces DebateVerdict, RedTeamReport, FailureAnticipationReport, CounterfactualMap,
  or AdversarialStressReport depending on campaign. Also supports cross-campaign StressTestSummary.
execution: subagent
prompt: ./prompt.md
input: campaign_name (string), strategy_outputs (string), weakness_classifications
  (string)
dependencies:
  sops:
  - spawn-agent
---

# Verdict Synthesis

Synthesizes campaign findings into typed verdict reports.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Synthesis requires processing all strategy/tactic outputs from a campaign in dedicated context to produce coherent final report.

## Input

- **campaign_name**: Which campaign produced these findings
- **strategy_outputs**: All strategy and tactic outputs from the campaign
- **weakness_classifications**: Classified weaknesses (from weakness-classification)

## Output

Typed report matching campaign:
- `DebateVerdict` (multiagent-debate)
- `RedTeamReport` (red-teaming)
- `FailureAnticipationReport` (failure-anticipation)
- `CounterfactualMap` (counterfactual-probing)
- `AdversarialStressReport` (adversarial-stress-testing)
- `StressTestSummary` (cross-campaign aggregation)

## Budget

One unit = one synthesis pass producing a complete typed report.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
