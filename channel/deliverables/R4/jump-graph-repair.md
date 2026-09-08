# Tactic jump 图修复

v3 `refactory_source.json` 中，`patent-mining` campaign 路由到 `landscape-survey`、`prior-art-search`、`white-space-analysis`；三者都处理已知覆盖、空白或 novelty 判断。v4 中对应的三个 tactic 原先只互连成孤岛，因此补到已有的 `validate-research-gap`。

| 节点 ID | 应连到的 tactic | v3 推导路径 | 新增的 jump 边 |
|---|---|---|---|
| `mine-patent-landscape` | `validate-research-gap` | `patent-mining → landscape-survey`; landscape 的 uncovered-area 结果进入 gap validation | `["mine-patent-landscape", "validate-research-gap"]` |
| `assess-prior-art-and-claims` | `validate-research-gap` | `patent-mining → prior-art-search`; novelty / prior-art 判断检验候选 gap 是否已被覆盖 | `["assess-prior-art-and-claims", "validate-research-gap"]` |
| `map-patent-white-space` | `validate-research-gap` | `patent-mining → white-space-analysis`; v3 明确处理 gaps / uncovered areas | `["map-patent-white-space", "validate-research-gap"]` |

未新增节点。修复后 tactic jump 图为单一连通分量。
