---
name: seed-concept-search
description: SOP for finding seed concepts in existing vault and web sources to anchor
  ontology construction.
execution: sop
---

# Seed Concept Search

Find seed concepts that anchor the ontology's center of gravity.

## Tool

`vault_search` + web search (brave-search)

## Protocol

1. Search vault for existing concepts in the target domain
2. If vault coverage is thin, search web for authoritative concept lists (textbooks, surveys)
3. Return ranked list of candidate seed concepts with source references

## HARD-GATE

<HARD-GATE>
Must return ≥3 candidate seed concepts with source attribution.
</HARD-GATE>

## Yield

Returns: `{ candidates: string[], sources: string[] }`
