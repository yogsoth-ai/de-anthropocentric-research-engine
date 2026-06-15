---
name: source-gathering
description: SOP for gathering source material relevant to the ontology domain — fetch
  papers and web pages into source pages.
execution: sop
dependencies:
  sops:
  - wiki-ingest-source
---

# Source Gathering

Gather source material (papers, web pages) relevant to the ontology domain and ingest as source pages.

## Tool

`wiki-ingest-source` (SOP) + web/paper search tools

## Protocol

1. Search for relevant sources using brave-search, apify, semantic-scholar
2. For each relevant source, call wiki-ingest-source SOP to create a source page
3. Return list of ingested source paths

## HARD-GATE

<HARD-GATE>
Must ingest ≥2 source pages per invocation.
</HARD-GATE>

## Yield

Returns: `{ sources_ingested: number, paths: string[] }`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| wiki-ingest-source | SOP for source page creation — write immutable source page capturing raw material, then update search index. |

<!-- END available-tables (generated) -->
