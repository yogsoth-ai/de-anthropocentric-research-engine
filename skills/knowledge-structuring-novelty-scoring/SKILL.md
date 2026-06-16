---
name: novelty-scoring
description: SOP for scoring empty cells by novelty potential — how surprising and
  valuable would this combination be?
execution: sop
---

# Novelty Scoring

Score empty cells (unexplored combinations) by their novelty potential.

## Tool

`vault_search` + CC reasoning

## Protocol

1. For each empty cell, assess:
   - Distance from nearest occupied cell (more distant = more novel)
   - Feasibility (are there physical/logical constraints?)
   - Potential impact (would this combination solve known problems?)
2. Score 0-10: novelty (0=obvious, 10=paradigm-shifting)
3. Flag top-scoring cells as priority research opportunities

## HARD-GATE

<HARD-GATE>
Must provide explicit reasoning for each score, not just a number.
</HARD-GATE>

## Yield

Returns: `{ scored: Array<{combination: string, score: number, reasoning: string}> }`
