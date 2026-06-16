# Graph JSON schema

`render_graph.py` consumes one JSON file per repo. Shape:

```json
{
  "name": "literature-engine",
  "nodes": [
    {
      "id": "literature-overview",
      "layer": "sop",
      "desc": "<b>最浅一档:landscape 扫描定位。</b> 中英混合说明,可含 <b> 加粗。"
    }
  ],
  "edges": [
    {
      "from": "literature-overview",
      "to": "literature-search",
      "tip": "触发情景:在什么情况下走这条 use 通路。可含 <b> 与 &lt;转义&gt;。"
    }
  ]
}
```

## Fields

| field | required | notes |
| --- | --- | --- |
| `name` | yes | output file stem (`<name>.html`) and graph title |
| `nodes[].id` | yes | the skill slug, **full name, no abbreviation** — also the node label |
| `nodes[].layer` | yes | one of `campaign` / `strategy` / `tactic` / `sop` / `references` |
| `nodes[].desc` | optional | bilingual (中英混合) hover text; HTML allowed (`<b>`, `<hr>` auto-added after the title line). Omit → tooltip shows just `name [layer]` |
| `edges[].from` / `to` | yes | must match a node `id` |
| `edges[].tip` | optional | hover text = the trigger scenario for this `use` path; HTML allowed. Omit → shows `use` |

## Conventions

- **Node IDs are full skill names** — never abbreviate (`literature-overview`, not `litov`).
- HTML in `desc`/`tip` is rendered (not escaped) by the self-managed tooltip layer.
  To show literal `<` / `>` (e.g. `<timestamp>`), write `&lt;` / `&gt;`.
- Keep `desc` to what the SKILL.md actually says it does + its depth/HARD-GATE.
- Keep `tip` to the condition under which the caller hands off to the callee —
  quote the source skill's own escalation language where possible.
- `render_graph.py` prints a `[warn]` for any edge that violates layer legality
  (see `layer-rules.md`); `sop → sop` escalation is allowed and never warns.
