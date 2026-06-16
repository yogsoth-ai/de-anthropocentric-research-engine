---
name: scenario-construction
description: Construct distinct future scenarios spanning key uncertainties for portfolio
  stress testing.
execution: subagent
prompt: ./prompt.md
input: context, uncertainties
dependencies:
  sops:
  - spawn-agent
---

# Scenario Construction

Build a set of distinct, plausible future scenarios that span the key uncertainties relevant to portfolio performance.

## Execution

Spawns a subagent that identifies key uncertainties and constructs diverse scenarios for stress testing.

## Why Subagent

Scenario construction requires creative yet disciplined thinking to produce scenarios that are distinct, plausible, and collectively span the uncertainty space. This generative-analytical work benefits from focused attention.

## HARD-GATE

Output must contain at least 3 distinct scenarios that span different combinations of key uncertainties. Each scenario must include a narrative, key assumptions, and probability estimate.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
