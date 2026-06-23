---
name: repo-dependency-graph
description: >-
  Reconstruct a DARE skill repo's true use-dependency relations and render them
  as a self-contained, offline, Obsidian-style interactive HTML graph (pyvis /
  vis-network). Use this whenever the user wants to graph / map / visualize the
  skill dependencies of a repo or package, "画依赖图 / graph 化这个 repo / 把 skill
  连边画出来 / 用 pyvis 出个图 / skill 关系图", or to audit how campaign→strategy→
  tactic→sop skills connect. Trigger even if the user just says "给这个 package
  做个图" without naming pyvis or HTML. Goes straight to HTML — never write an
  intermediate mermaid markdown first.
---

# repo-dependency-graph

Turn a skill repo (or a whole campaign package) into a clean, interactive
**use-dependency graph**: read the original `SKILL.md` + design docs, reconstruct
the real `use` edges, and render one offline HTML per repo that looks and behaves
like an Obsidian graph (force-directed, draggable, neighbourhood-highlight, HTML
hover tooltips).

This skill exists because a repo's frontmatter alone gives a broken graph — real
routing lives in prose, in `references/*-index.md`, and in same-layer escalation
handoffs. Reconstructing the true graph takes a careful read of each repo, then a
deterministic render. This skill captures both halves so the result is consistent
every time and reusable across all repos.

## The model (read `references/layer-rules.md` for the full rules)

- **5 vertex types**: `campaign` (red) · `strategy` (cyan) · `tactic` (yellow) ·
  `sop` (purple) · `references` (gray dashed, = a `.py`/`.md` helper file).
- **One edge type `use`**: `A -->|use| B` = A invokes/orchestrates B (caller → callee).
- **Layer comes from frontmatter `type:` / `layer:`** (NOT `execution:`). Infer
  from body+README only if absent, and record the reasoning.
- **Escalation = same-layer `sop → sop` use edge** (locked decision): "escalate to
  X" / "for deeper analysis use X" / "import X" are all drawn as `use` edges. Do
  NOT promote a skill's layer just to make the edge look legal — same-layer
  handoff is a first-class edge here.

## Workflow

### 1. Read the repo and reconstruct the dependencies

For each `skills/*/SKILL.md`: read the **full body + frontmatter** (layer field,
and any prose that invokes/escalates to another skill or points at a
`references/` helper). Also read `README.md`, `docs/`, `assets/`, and any
`*-index.md` — real routing often lives there, not in frontmatter.

Only draw an edge the design files actually justify. If two skills are
independent siblings, leave them unconnected — do not invent edges. A pointer to
an external MCP tool (`alphaxiv`, `brave`) is a tool, not a vertex. A broken /
never-used file pointer does not justify a `references` vertex — verify the live
reference.

**For a large package (50+ skills), dispatch one subagent per package** to read
its `skills/` + `docs/` and return the reconstructed nodes/edges — they are
independent and parallelize cleanly. Give each subagent `references/layer-rules.md`
and `references/graph-schema.md` so its output is consistent and directly usable.

### 2. Write the graph JSON

Emit one JSON file per repo following `references/graph-schema.md`:

```json
{
  "name": "<repo-name>",
  "nodes": [ {"id": "<full-skill-name>", "layer": "sop", "desc": "<bilingual hover>"} ],
  "edges": [ {"from": "...", "to": "...", "tip": "<trigger scenario hover>"} ]
}
```

- **Node IDs are full skill names — never abbreviate.**
- `desc` (中英混合) = what the SKILL does + its depth / HARD-GATE. HTML allowed.
- `tip` = the condition under which the caller hands off to the callee; quote the
  source skill's own escalation language where possible. HTML allowed.
- Both `desc` and `tip` are optional — omit and the tooltip falls back to
  `name [layer]` / `use`.

### 3. Render the HTML

```
python scripts/render_graph.py --data <repo>.json --out <repo>.html
# or batch a whole directory of graph JSONs:
python scripts/render_graph.py --data-dir ./data --out-dir ./graphs
```

The script prints a `[warn]` for any edge that breaks layer legality
(`sop → sop` escalation never warns). It produces a fully offline HTML
(vis-network inlined, external CDN stripped) with:

- 5 vertex-type colors, dashed border for `references`.
- Force-directed, draggable, scroll-zoom, click-to-highlight neighbourhood.
- A self-managed `#dare-tip` hover layer that renders the HTML in `desc`/`tip`
  (vis's native tooltip shows a string title as plain text, leaking `<b>` tags —
  the script bypasses it with an event-driven layer; this is why HTML renders).
- No navigation buttons, no bootstrap card frame — just the graph on a dark canvas.

### 4. Verify

Open the HTML in a browser and confirm: nodes colored by layer, edges arrow
caller→callee, hovering a node/edge shows the bilingual tooltip with HTML
rendered (bold + `<hr>` divider, not raw tags). Requires `pyvis` (>=0.3.2).

## Key constraints

- **HTML directly, no intermediate mermaid `.md`.** The HTML is the deliverable.
- **Full skill names** as node IDs and labels — no abbreviations.
- Privacy: the HTML embeds only node names + layer + the desc/tip you write. Never
  emit filesystem paths, log paths, or session IDs into the graph data or output.
- Read-only on the source repo — reconstructing a graph never edits skills.

See `examples/literature-engine.json` for a complete, working graph JSON.
