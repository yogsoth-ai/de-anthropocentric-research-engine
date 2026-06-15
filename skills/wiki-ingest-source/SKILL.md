---
name: wiki-ingest-source
description: SOP for source page creation — write immutable source page capturing
  raw material, then update search index.
execution: sop
---

# Wiki Ingest Source

Create an immutable source page capturing raw research material (paper notes, web content, experimental data). Sources are never edited after creation — they preserve the original material.

## HARD-GATE

<HARD-GATE>
Before creating a source page, search the vault for existing sources covering the same material.
If vault_search returns a match with score > 8.0 for the source title, STOP and report the duplicate.
</HARD-GATE>

## Tools

- `vault_search` (deduplication check)
- `vault_index` (post-creation index update)
- CC file write (page creation)

## Protocol

1. Search vault for existing source with similar title/content
2. If duplicate found → report and abort
3. Write source page to `sources/<slug>.md` with frontmatter:
   ```yaml
   ---
   type: source
   title: "<descriptive title>"
   created: <YYYY-MM-DD>
   origin: <url or citation>
   tags: [<relevant tags>]
   ---
   ```
4. Body contains raw material (quotes, data, notes) — no synthesis
5. Call `vault_index` (incremental) to make the page searchable
6. Return path of created source

## Source Page Rules

- **Immutable after creation.** Never edit source pages.
- **Verbatim content.** Preserve original wording, data, structure.
- **Attribution required.** Origin field must trace back to the original.
- **No interpretation.** Synthesis belongs in wiki pages, not sources.

## Yield

Returns: `{ created: string, indexed: boolean }`
