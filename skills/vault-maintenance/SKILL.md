---
name: vault-maintenance
description: Tactic for vault health upkeep — lint, orphan resolution, merge candidates,
  confidence updates. Minimum yield ≥1 issue resolved per invocation.
execution: tactic
dependencies:
  sops:
  - wiki-add-edge
  - wiki-edge-audit
  - wiki-graph-query
  - wiki-lint-fix
  - wiki-search
---

# Vault Maintenance

Vault health upkeep. Called when CC judges the vault has accumulated enough entropy to warrant cleanup, or periodically between research phases.

## Available SOPs

- `wiki-lint-fix` — run lint checks, identify issues, optionally auto-fix
- `wiki-search` — find near-duplicate candidates for merging
- `wiki-graph-query` — explore orphan neighborhoods for reconnection
- `wiki-add-edge` — reconnect orphans to the graph

## Guiding Principles

- **Lint first.** Start with vault_lint in report mode to assess current health.
- **Triage by severity.** Errors (broken links, missing frontmatter) before warnings (orphans, stale entries).
- **Conservative auto-fix.** Only auto-fix safe operations (duplicate edge removal, stale index pruning). Manual intervention for ambiguous cases.
- **Merge, don't delete.** Near-duplicate pages should be merged (consolidate content, redirect edges) rather than deleted.
- **Confidence decay.** Pages with evidence older than the research horizon may need confidence score updates.

## Minimum Yield

<HARD-GATE>
≥1 issue resolved per invocation.
If vault_lint returns zero issues, report clean state and exit.
</HARD-GATE>

## Execution Guidance

CC has full autonomy over:
- Which issues to address and in what order
- Whether to auto-fix or manually resolve
- How aggressively to merge near-duplicates
- When to update confidence scores

Typical flow (reference, not prescription):
1. Run vault_lint (report mode) — assess issue landscape
2. Categorize: auto-fixable vs manual
3. Auto-fix safe issues (duplicate edges, stale index)
4. For orphans: search for connection candidates, add edges
5. For near-duplicates: merge content into canonical page, update edges
6. Re-run vault_lint to confirm resolution

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| wiki-add-edge | SOP wrapping vault_add_edge — create a typed relationship between two vault pages. |
| wiki-edge-audit | SOP for auditing wikilink coverage — scans all edges and reports which source pages are missing [[dir/slug]] wikilinks to their targets. |
| wiki-graph-query | SOP wrapping vault_query_graph — traverse knowledge graph from a node to explore its neighborhood and context. |
| wiki-lint-fix | SOP wrapping vault_lint — run batch validation, report issues, optionally auto-fix safe problems. |
| wiki-search | SOP wrapping vault_search — BM25 full-text search across vault pages. Returns ranked results with snippets. |

<!-- END available-tables (generated) -->
