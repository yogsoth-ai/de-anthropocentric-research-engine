---
name: knowledge-compilation
description: Tactic for compiling research findings into vault pages — orchestrates
  page creation, updates, edge linking, and index maintenance. Minimum yield ≥3 page
  operations per invocation.
execution: tactic
dependencies:
  sops:
  - wiki-add-edge
  - wiki-compile-page
  - wiki-edge-audit
  - wiki-graph-query
  - wiki-ingest-source
  - wiki-lint-fix
  - wiki-search
---

# Knowledge Compilation

Compile research findings into structured vault pages. Triggered after each strategy completes, or when CC judges accumulated information density warrants compilation.

## Available SOPs

- `wiki-search` — check for existing pages before creating duplicates
- `wiki-ingest-source` — write immutable source pages
- `wiki-compile-page` — create/update wiki pages with edges
- `wiki-add-edge` — create typed relationships between pages
- `wiki-lint-fix` — run lint in report mode at end

## Guiding Principles

- **Assess before acting.** Scan incoming material. Identify what's new vs what updates existing pages.
- **Deduplication first.** Always search before creating. Near-duplicates should be merged, not added.
- **Edges are first-class.** Every new page should have at least one edge connecting it to the existing graph. Orphans are failures.
- **Source immutability.** Source pages capture raw material verbatim. Wiki pages synthesize and evolve.
- **Batch efficiency.** Group related operations. Create all pages for a concept cluster, then wire edges, then index once.

## Minimum Yield

<HARD-GATE>
≥3 page operations per invocation (any combination of: create page, update page, add edge).
If incoming material cannot produce 3 operations, accumulate and defer.
</HARD-GATE>

## Execution Guidance

CC has full autonomy over:
- Which SOPs to invoke and in what order
- Whether to spawn a subagent for complex ingest decisions
- How to partition material across pages
- When to create new pages vs update existing ones

Typical flow (reference, not prescription):
1. Search vault for existing coverage of incoming topics
2. Decide page operations: new sources, new wiki pages, updates, edges
3. Execute operations via SOPs
4. Run vault_lint (report mode) to verify no broken links introduced

## Context-Management Integration

After compilation completes, trigger `context-checkpoint` to persist vault state changes to the context layer.
