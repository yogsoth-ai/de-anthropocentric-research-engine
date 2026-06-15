---
name: model-gap-detection
description: SOP for finding gaps in the causal model — missing variables, unexplained
  effects, weak links.
execution: sop
---

# Model Gap Detection

Find gaps in the causal model: effects without causes, causes without mechanisms, weak confidence links.

## Tool

`vault_graph_stats` + `vault_query_graph`

## Protocol

1. Run vault_graph_stats — identify orphans and low-connectivity nodes
2. For each variable with out_degree=0 (no downstream effects): is this truly a terminal variable?
3. For each variable with in_degree=0 (no upstream causes): is this truly exogenous?
4. Check for edges with weight < 0.3 — these are weak links needing more evidence
5. Report gaps with suggested actions

## HARD-GATE

<HARD-GATE>
Must check both orphans and weak links. Report must include actionable suggestions.
</HARD-GATE>

## Yield

Returns: `{ unexplained_effects: string[], missing_causes: string[], weak_links: string[] }`
