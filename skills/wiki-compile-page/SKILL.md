---
name: wiki-compile-page
description: SOP for wiki page creation/update — create or update a synthesized wiki
  page with edges and index update.
execution: sop
---

# Wiki Compile Page

Create or update a synthesized wiki page. Wiki pages are living documents that evolve as understanding deepens. They link to sources (evidence) and connect to other concepts via edges.

## HARD-GATE

<HARD-GATE>
Before writing, determine whether this is a CREATE or UPDATE operation.
- CREATE: vault_search must confirm no existing page covers this topic (score < 5.0)
- UPDATE: read the existing page first, then apply changes
Never blindly overwrite an existing page.
</HARD-GATE>

## Tools

- `vault_search` (existence check)
- `vault_add_edge` (relationship creation)
- `vault_index` (post-write index update)
- CC file write/edit (page creation or modification)

## Protocol

### Create Flow

1. Search vault to confirm topic is not already covered
2. Determine entity type (concept, claim, entity, relation, question, evidence, failure, topic)
3. Write page to `<type>s/<slug>.md` with appropriate frontmatter:
   ```yaml
   ---
   type: <entity_type>
   title: "<descriptive title>"
   created: <YYYY-MM-DD>
   confidence: <0.0-1.0>  # required for claim/evidence types
   tags: [<relevant tags>]
   ---
   ```
4. Body contains synthesized content with `[[wikilinks]]` to related pages
5. Add edges connecting this page to related pages
6. **Inline wikilinks:** For each edge created, ensure the page body contains `[[dir/slug]]` pointing to the target (dir/slug = target path minus `.md`). Place inline at semantically relevant location. Skip if already present.
7. Call `vault_index` (incremental)

### Update Flow

1. Read existing page content
2. Apply changes (add information, update confidence, add wikilinks)
3. Add new edges if new relationships discovered
4. **Inline wikilinks:** For each new edge, ensure the page body contains `[[dir/slug]]` pointing to the target (dir/slug = target path minus `.md`). Place inline at semantically relevant location. Skip if already present.
5. Call `vault_index` (incremental)

## Yield

Returns: `{ operation: "create" | "update", path: string, edges_added: number }`
