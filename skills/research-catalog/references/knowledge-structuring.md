# knowledge-structuring — skill table

71 skills. Sorted by layer (campaign→strategy→tactic→sop), then name.

| Layer | Skill | Description |
| --- | --- | --- |
| campaign | argument-mapping | <b>论证结构映射 campaign。</b> 编排 3 条 strategy <b>claim-extraction → evidence-linking-arg → argument-synthesis</b>,抽 claim、挂证据、评强度、综合立场。每条 strategy 后 knowledge-compilation 落盘。synthesis≠averaging。 |
| campaign | causal-modeling | <b>因果建模 campaign。</b> 编排 5 条 strategy <b>variable-identification → mechanism-mapping → evidence-collection → intervention-analysis → model-validation</b> 构建有向因果图;每条 strategy 后 knowledge-compilation 落盘。核心戒律:correlation≠causation,每条 mechanism edge 必须有机制论证。 |
| campaign | dimensional-analysis | <b>维度/设计空间分析 campaign。</b> 编排 3 条 strategy <b>dimension-discovery → combination-mapping → gap-prioritization</b>,发现变化轴、枚举组合、定位未探索空白(novel opportunities)。每条 strategy 后 knowledge-compilation 落盘。 |
| campaign | ontology-building | <b>本体构建 campaign。</b> 为一个研究域系统化建本体:按 strategy 序列 <b>domain-scoping → concept-extraction → relation-typing → taxonomy-validation → ontology-refinement</b> 编排,每条 strategy 后强制 <b>knowledge-compilation</b> 落盘(HARD-GATE: context-init / context-checkpoint / knowledge-compilation)。produces 一个 wiki vault 里的 concept hierarchy。 |
| strategy | argument-synthesis | <b>argument strategy③。</b> 聚合证据、解矛盾、产出 synthesis(哪些 claim 经得起 scrutiny)。编排 claim-decomposition / strength-assessment,直列 argument-visualization / synthesis-report。HARD-GATE: ledger + 80% budget。 |
| strategy | claim-extraction | <b>argument strategy①。</b> 从 source 抽 claim、拆复合句、分类、建 claim 页。编排 tactic claim-decomposition,直列 sop claim-page-creation / rebuttal-documentation。HARD-GATE: ledger + 80% budget + adversarial completeness probe。 |
| strategy | knowledge-structuring-combination-mapping | Systematically enumerate parameter dimensions and generate viable combinations. Orchestrates parameter extraction → value enumeration → compatibility assessment → synthesis. |
| strategy | concept-extraction | <b>ontology strategy②。</b> 从 source 挖 concept(precision>recall),编排 concept-decomposition / consistency-checking,直调 source-gathering 取材。HARD-GATE: 80% budget + ledger。 |
| strategy | dimension-discovery | <b>dimensional strategy①。</b> 找设计空间里相互独立的根本变化轴。编排 tactic axis-extraction / matrix-generation。HARD-GATE: 80% budget + state ledger。 |
| strategy | domain-scoping | <b>ontology strategy①。</b> 定本体边界 + seed concepts + 分类 topic 规模。编排 tactic concept-decomposition / hierarchy-construction,直调 sop seed-concept-search。HARD-GATE: 80% budget 才能退出 + 打印 state ledger。 |
| strategy | evidence-collection | <b>causal strategy③。</b> 挂证据页,造 supported_by / contradicts 边,对抗式找反证。编排 evidence-weighing / counterfactual-reasoning / feedback-loop-detection,直调 evidence-linking。HARD-GATE: 80% budget。 |
| strategy | evidence-linking-arg | <b>argument strategy②。</b> 以 typed edge 把证据挂到 claim、评质量、找矛盾/gap。编排 strength-assessment,直列 evidence-attachment / strength-scoring。HARD-GATE: ledger + 80% budget + confirmation-bias self-check。 |
| strategy | knowledge-structuring-gap-prioritization | Score and rank validated gaps on importance, feasibility, novelty, and urgency. Multi-criteria decision analysis with stakeholder confirmation. |
| strategy | intervention-analysis | <b>causal strategy④。</b> do-calculus:切断入边、前向追踪、预测方向性结果。编排 counterfactual-reasoning / feedback-loop-detection / evidence-weighing,直调 intervention-page-creation。HARD-GATE: 80% budget。 |
| strategy | mechanism-mapping | <b>causal strategy②。</b> 构建有向因果图,每条 mechanism edge = 带 pathway+falsifier+citation 的假设。编排 counterfactual-reasoning / evidence-weighing / feedback-loop-detection,直调 mechanism-edge-creation。HARD-GATE: 80% budget。 |
| strategy | model-validation | <b>causal strategy⑤ (final quality gate)。</b> 以 skeptic 立场审环、解矛盾、重标定并传播 confidence。编排 feedback-loop-detection / evidence-weighing / counterfactual-reasoning,直调 model-gap-detection / validation-report。HARD-GATE: 80% budget。 |
| strategy | ontology-refinement | <b>ontology strategy⑤。</b> 迭代精修:merge 近重复、补 gap、更新 confidence、剪枝。编排 concept-decomposition / consistency-checking,直调 confidence-update / ontology-export / gap-detection 等。HARD-GATE: 80% budget。 |
| strategy | relation-typing | <b>ontology strategy③。</b> 识别并 type 概念间的边,要求每个 concept 至少连 2 个其它。编排 hierarchy-construction / consistency-checking,直调 edge-batch-creation。HARD-GATE: 80% budget。 |
| strategy | taxonomy-validation | <b>ontology strategy④ (quality gate)。</b> 校验结构完整性(环 / orphan / 类型违例)。编排 consistency-checking / hierarchy-construction,直调 gap-detection / hierarchy-visualization / ontology-export。HARD-GATE: 80% budget。 |
| strategy | knowledge-structuring-variable-identification | "SOP: 识别变量及其在假设中的角色" |
| tactic | axis-extraction | <b>dimensional tactic。</b> 从文献系统抽变化轴(对比/trade-off/taxonomy)。编排 sop dimension-page-creation / axis-validation(+域外 wiki-search)。HARD-GATE: 每次 ≥2 candidate axes 带 independence assessment。 |
| tactic | knowledge-structuring-claim-decomposition | Independent/dependent claim parsing, element extraction, and feature mapping to technical domains |
| tactic | concept-decomposition | <b>ontology tactic。</b> 把复合/过宽概念拆成原子子概念。编排 sop concept-page-creation / edge-batch-creation / alias-resolution(+域外 wiki-search)。HARD-GATE: 每次 ≥2 child concepts,否则报 atomic 并退出。 |
| tactic | knowledge-structuring-consistency-checking | Pairwise consistency evaluation to reduce solution space by identifying and removing inconsistent combinations. |
| tactic | counterfactual-reasoning | <b>causal tactic (因果识别金标准)。</b> 'if X had not occurred, would Y still happen?'。编排 sop causal-chain-query / contradiction-flagging / confidence-scoring。HARD-GATE: 每次 ≥1 counterfactual 带显式机制+confidence。 |
| tactic | evidence-weighing | <b>causal tactic。</b> 按证据层级(RCT>observational>theoretical>anecdote)+ effect size + replication 排序。编排 sop evidence-linking / confidence-scoring / contradiction-flagging。HARD-GATE: 每次 ≥2 assessments 带 strength rating。 |
| tactic | feedback-loop-detection | <b>causal tactic。</b> 找循环因果,分 reinforcing/balancing,记 delay/break point。编排 sop causal-chain-query / loop-documentation / mechanism-edge-creation。HARD-GATE: 每次 ≥1 loop 分类(或显式报无)。 |
| tactic | hierarchy-construction | <b>ontology tactic。</b> 用 component_of/instance_of 建无环、可传递、depth≤5 的层级。编排 sop edge-batch-creation / hierarchy-visualization / gap-detection,并 peer-调 consistency-checking 验环。HARD-GATE: 每次 ≥3 hierarchy edges。 |
| tactic | knowledge-compilation | <b>wiki-vault tactic (核心落盘)。</b> 把研究发现编译进 vault 页面;每条 strategy 结束后被 campaign 强制调用。编排 sop wiki-search / wiki-ingest-source / wiki-compile-page / wiki-add-edge / wiki-lint-fix / wiki-edge-audit。HARD-GATE: 每次调用 ≥3 page operations,否则 accumulate and defer。 |
| tactic | matrix-generation | <b>dimensional tactic。</b> 跨维度生成/填充组合矩阵。编排 sop combination-enumeration / novelty-scoring / question-generation / matrix-export。HARD-GATE: 每次 ≥1 matrix 且 ≥50% cell 已分类。 |
| tactic | strength-assessment | <b>argument tactic。</b> 按证据质量/独立性/defeater 评 claim 强度并给校准分。编排 sop strength-scoring / evidence-attachment。HARD-GATE: 每次 ≥3 claims 评分。 |
| tactic | vault-maintenance | <b>wiki-vault tactic (健康维护)。</b> vault 熵积累到一定程度时清理:lint / orphan 重连 / merge / confidence 更新。编排 sop wiki-lint-fix / wiki-search / wiki-graph-query / wiki-add-edge / wiki-edge-audit。HARD-GATE: 每次调用 ≥1 issue resolved。 |
| sop | alias-resolution | <b>ontology sop。</b> 检测同概念异名页并 merge 到 canonical。HARD-GATE: merge 前须确认确为同一概念。 |
| sop | argument-visualization | <b>argument sop。</b> 查图渲 mermaid 论证图(按强度着色)写入 wiki 页。HARD-GATE: ≥3 claims + relationships。 |
| sop | axis-validation | <b>dimensional sop。</b> 两两测维度独立性,合并共变者、删单值者。HARD-GATE: 对所有 candidate 做 pairwise independence test。 |
| sop | causal-chain-query | <b>causal sop。</b> 经 vault_query_graph(depth3, out)重建有序因果链、分支、环。HARD-GATE: 报含中间节点的完整链。 |
| sop | claim-page-creation | <b>argument sop。</b> 写原子命题 claim 页带 type/confidence/source + derived_from 边。HARD-GATE: claim 须原子(无 and/but/because)。 |
| sop | combination-enumeration | <b>dimensional sop。</b> 笛卡尔积枚举维度取值并逐格分类。HARD-GATE: 枚举全部组合而非抽样。 |
| sop | concept-page-creation | <b>ontology sop。</b> 建新 concept 页带 frontmatter + ≥1 edge。HARD-GATE: 不准造 orphan,至少 1 条边。 |
| sop | confidence-scoring | <b>causal sop。</b> net confidence = support_w/(support_w+contradict_w) ± 机制调整,写入 frontmatter。HARD-GATE: 0.0–1.0 且引证据。 |
| sop | confidence-update | <b>ontology sop。</b> 据新证据更新 confidence 分。HARD-GATE: 每次改动都引具体 evidence。 |
| sop | contradiction-flagging | <b>causal sop。</b> 检测同时存在的 support+contradict 证据,建 contradicts 边并记入 question 页。HARD-GATE: 必须记录、不可忽略。 |
| sop | dimension-page-creation | <b>dimensional sop。</b> 建 concepts/<slug>.md 维度页带 values + edges。HARD-GATE: ≥2 distinct values + 清晰 axis 定义。 |
| sop | edge-batch-creation | <b>ontology sop。</b> 批量建边 + inline wikilink。HARD-GATE: 整批先校验再写。 |
| sop | evidence-attachment | <b>argument sop。</b> 用 typed edge(supported_by/contradicts/related_to)把证据挂到 claim,带质量元数据。HARD-GATE: 须标 quality + directness。 |
| sop | evidence-linking | <b>causal sop。</b> 从 evidence 页向具体 claim 建 supported_by / contradicts 边。HARD-GATE: 须挂到 claim 而非 topic。 |
| sop | gap-detection | <b>ontology sop。</b> 找 orphan / 细枝 / 断簇,给可执行修补建议。HARD-GATE: 分析完整 orphan 列表。 |
| sop | hierarchy-visualization | <b>ontology sop。</b> 经 graph query 取层级,出缩进树。HARD-GATE: ≥top-3 roots 都查到。 |
| sop | intervention-page-creation | <b>causal sop。</b> 写 claims/<slug>.md(目标变量、操纵、预测/观测效应)+ addresses/derived_from 边。HARD-GATE: 须指明 target / direction / predicted effects。 |
| sop | loop-documentation | <b>causal sop。</b> 写 relations/<slug>.md 记反馈环(类型、变量、delay、break point)。HARD-GATE: 分类 reinforcing/balancing 并列全环变量。 |
| sop | matrix-export | <b>dimensional sop。</b> 把矩阵导出到 topics/dimensional-matrix.md 带 summary stats。HARD-GATE: 自包含、脱离 vault 也可读。 |
| sop | mechanism-edge-creation | <b>causal sop。</b> 建因果边(derived_from/component_of),weight=机制强度(1.0/0.5/0.2)。HARD-GATE: 每条边须陈述 HOW。 |
| sop | merge-candidates | <b>ontology sop。</b> 标近重复 concept(score>7.0)。HARD-GATE: 扫 ≥10 concepts(或全部)。 |
| sop | model-gap-detection | <b>causal sop。</b> 经 vault_graph_stats 找 orphan(度0)+ 弱链(<0.3)→ 可执行 gap。HARD-GATE: orphan 与 weak link 都查并给建议。 |
| sop | knowledge-structuring-novelty-scoring | "SOP: 评估研究 gap 的新颖性潜力，识别差异化方向并输出评分" |
| sop | ontology-export | <b>ontology sop。</b> 产出可读 ontology summary。HARD-GATE: 含定量计数 + 定性层级。 |
| sop | question-generation | <b>dimensional sop。</b> 从优先 gap 提可答研究问题,写 questions/<slug>.md。HARD-GATE: 问题须具体可答、不泛。 |
| sop | rebuttal-documentation | <b>argument sop。</b> 写 counter-claim 页带 contradicts + derived_from 边。HARD-GATE: 须点名被反驳 claim + 矛盾类型。 |
| sop | seed-concept-search | <b>ontology sop。</b> 在 vault + web 找 seed concept。HARD-GATE: ≥3 candidates 带 source attribution。 |
| sop | source-gathering | <b>ontology sop。</b> 用 web/paper 搜索找源,逐条转交 wiki-ingest-source 落 source 页。HARD-GATE: 每次 ≥2 source pages。 |
| sop | strength-scoring | <b>argument sop。</b> 据图中证据用 rubric 给 claim 打 0-10 校准强度分,写入 frontmatter。HARD-GATE: 须给显式 reasoning。 |
| sop | synthesis-report | <b>argument sop。</b> 把所有 claim 分类 survived/contested/undermined/gaps,写 synthesis 页。HARD-GATE: 全部 claim 都须分类。 |
| sop | validation-report | <b>causal sop。</b> vault_graph_stats + vault_lint → 写 topics/causal-model-report.md。HARD-GATE: 含变量/边/confidence 分布/未决矛盾/结构问题。 |
| sop | variable-page-creation | <b>causal sop。</b> 写 concepts/<slug>.md 描述一个可测变量 + ≥1 图边。HARD-GATE: 须有清晰 operational definition。 |
| sop | wiki-add-edge | <b>wiki-vault sop。</b> 包 vault_add_edge,在两页间建 10 类 typed edge 之一并补 inline wikilink。HARD-GATE: 两端文件都须存在、不连不存在的页。 |
| sop | wiki-compile-page | <b>wiki-vault sop。</b> 创建/更新 synthesized wiki 页 + edges + inline wikilink + 增量 index。HARD-GATE: 先判 CREATE(search 确认 score<5.0)vs UPDATE(先读原页),绝不盲目覆盖。 |
| sop | wiki-edge-audit | <b>wiki-vault sop。</b> 包 vault_edge_audit,扫所有 edge、补缺失的 [[dir/slug]] wikilink。HARD-GATE: 不可跳过 fix,重审须 missing_count==0。 |
| sop | wiki-graph-query | <b>wiki-vault sop。</b> 包 vault_query_graph,从某节点 BFS 探邻域、找 orphan / 缺连。HARD-GATE: node 文件须存在。 |
| sop | wiki-ingest-source | <b>wiki-vault sop。</b> 写 immutable source 页(原文 verbatim),再 vault_index。HARD-GATE: title score>8.0 即报重复并 abort;source 永不再编辑。 |
| sop | wiki-lint-fix | <b>wiki-vault sop。</b> 包 vault_lint 批量校验,先 report 后可 auto-fix(仅 dup edge / stale index)。HARD-GATE: 必先 report 模式、呈摘要后才 fix。 |
| sop | wiki-search | <b>wiki-vault sop。</b> 包 vault_search 做 BM25 全文检索,建页前去重(score>5.0 视为强匹配)。HARD-GATE: query 非空且含实义词。 |
