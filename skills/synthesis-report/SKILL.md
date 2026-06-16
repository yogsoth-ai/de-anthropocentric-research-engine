---
name: synthesis-report
description: SOP for producing argument synthesis reports — aggregate evidence, resolve
  contradictions, identify surviving claims, write structured summary.
execution: sop
---

# Synthesis Report

Produce a synthesis report that identifies which claims survive scrutiny.

## Tool

`vault_query_graph` + `vault_graph_stats` + CC file write

## Protocol

1. Query graph for all claims and evidence in the target domain
2. Classify claims by survival status:
   - **Survived**: strength ≥ 7, no undefeated contradictions
   - **Contested**: strength 4-6, active contradictions with comparable evidence
   - **Undermined**: strength ≤ 3, or defeated by stronger contradicting evidence
3. For each contested claim, summarize the state of the debate
4. Write `wiki/topics/<topic-slug>-synthesis.md` with sections:
   - Surviving claims (high confidence)
   - Contested claims (ongoing debate)
   - Undermined claims (low confidence / refuted)
   - Remaining gaps (claims lacking sufficient evidence either way)
5. Add `addresses` edges from synthesis page to relevant question pages

## HARD-GATE

<HARD-GATE>
Must categorize ALL claims for the topic — no claim left unclassified. Synthesis is comprehensive or it is not synthesis.
</HARD-GATE>

## Yield

Returns: `{ topic: string, survived: number, contested: number, undermined: number, gaps: number }`
