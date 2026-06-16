---
name: wiki-search
description: SOP wrapping vault_search — BM25 full-text search across vault pages.
  Returns ranked results with snippets.
execution: sop
---

# Wiki Search

Search the vault for existing pages matching a query. Used before creating new pages (deduplication) and for finding related content.

## HARD-GATE

<HARD-GATE>
Query must be non-empty and contain at least one meaningful term.
Do NOT search with single characters or pure stop words.
</HARD-GATE>

## Tool

`vault_search`

## Parameters

| Param | Required | Description |
|-------|----------|-------------|
| query | yes | Search query (natural language or keywords) |
| type | no | Filter by entity types (e.g., ["concept", "claim"]) |
| tags | no | Filter by tags |
| limit | no | Max results (default 20) |

## Protocol

1. Formulate query from the concept/topic you need to check
2. Call `vault_search` with query and optional filters
3. Examine results: score > 5.0 indicates strong match (potential duplicate)
4. Return results to calling tactic with match assessment

## Yield

Returns: `{ results_count: number, top_score: number, potential_duplicates: string[] }`
