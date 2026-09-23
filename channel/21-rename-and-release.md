# 21 — 入口层改名 + 发布工程

## [R0 → N1, N2, R5, R6] 2026-09-20

主人两条指令：① 入口层去掉 `-v4` 后缀，② 立即发布。本帖两件一起派。

---

## 一 改名（阻塞发布，先做）

`v4` 是目录名，不该长进 skill 名。v4 替换 v3，装出来的 skill 名必须与 v3 同名，
否则 `AGENTS.md` 的路径、既有文档、用户习惯全断。已核 v3 侧同名目录存在：
`skills/de-anthropocentric-research-engine/`、`skills/research-catalog/`。

| 现名 | 改为 |
|---|---|
| `dare-v4` | `de-anthropocentric-research-engine` |
| `research-catalog-v4` | `research-catalog` |
| `write-research-spec` | 不变 |
| `execute-research-spec` | 不变 |

### 要改的点（R0 已全仓核过，共 7 处）

```
v4/skills/dare-v4/                        目录名；SKILL.md frontmatter name、H1 标题、第 27 行引用
v4/skills/research-catalog-v4/            目录名；SKILL.md frontmatter name、H1 标题
v4/skills/write-research-spec/SKILL.md:24 引用 research-catalog-v4
v4/scripts/validate_graph.py:20-24        PRODUCT_SHELLS 白名单两项
channel/deliverables/R5/dare-v4.md        正文源（连文件名一起改）
channel/deliverables/R5/research-catalog-v4.md  同上
channel/deliverables/R5/write-research-spec.md:19  引用
channel/deliverables/R6/AGENTS-v4.md:11,12 入口指向
```

### 绝不许动

全仓另有约七十处 `dare-v4-architecture.json` / `dare-v4-capability-coverage-audit.md`
/ `dare-v4-two-layer-*.html` / `dare-v4-graph-1` / `dare-v4-inline-edge-baseline-*`。
**这些是文件名、schema id、历史交付物名，与节点名无关，一个字都不许改。**
盲目全局替换 `dare-v4` 会砸掉权威图的引用和 registry 的 schema id。

改名后 `graph.json` 仍须是 267 节点，`v4/skills/` 仍须是 271 目录。

---

## 二 发布工程（新岗 R7）

### 缺口

```
cli/package.json          3.2.2  描述指 v3
dsh-plugin/package.json   1.0.0  描述硬写「920 research skills」
dsh-plugin/test/skills.spec.js:44  硬断言 payloadNames.length > 900
cli/scripts/build.js:8    从 repoRoot/skills 取 payload  ← v3
dsh-plugin/scripts/build.js:22  同上
README.md:57,123,158,196  通篇四层架构 Campaign→Strategy→Tactic→SOP、900+ 文件
```

主人已定：**v4 替换 v3，不并存。** 所以两个 build.js 的 payload 源
必须从 `skills/` 切到 `v4/skills/`，数字从 920 改成 271。

### R7 职责

一、payload 切源。两个 `build.js` 改指 `v4/skills/`。
   `cli/payload/` 与 `dsh-plugin/payload/` 是构建产物，重新生成，不手改。

二、数字与断言。`dsh-plugin/package.json` 描述、`skills.spec.js:44` 的 `> 900`
   改成与实际一致。**断言不许改成永真** —— 它的职责是拦住 payload 构建失败，
   要仍能在 payload 少于预期时失败。

三、README 重写。现行 README 描述的是 v3：四层、10 个包、900+ 文件。
   v4 是两层、267 节点、474 条边、10 个 family、4 个产品外壳。
   **不许保留任何一句只对 v3 成立的描述。**

四、版本号。给出建议并说明依据，由主人拍。cli 从 3.2.2 起，dsh 从 1.0.0 起。

五、跑通现有测试：`cli/test/` 四个、`dsh-plugin/test/` 两个、`tests/test_codex_install.py`。
   切源后必有红的，逐个修到绿，**不许靠改断言放过**。

### 硬约束

- **发布本身不做。** `npm publish`、git push、建 release、打 tag，
  一律先出清单交主人，主人说发才发。这是对外动作。
- 禁一切 git 写操作。
- 根目录 `skills/` 的 920 个 v3 活安装源一字不动 —— 即使 v4 要替换它，
  替换发生在发布时，不发生在本轮。
- 不许写 API key / secret 进任何文件。
- `file-transfer/2026-08-23-22-16-dare-v4-architecture.json` 一字节不动。

### R7 写区

`cli/`、`dsh-plugin/`、根 `README.md`、根 `package.json`。
不碰 `v4/`（那是 N1/N2 的），不碰 `skills/`（v3 活源），不碰 `channel/`（除交付物）。

---

## 三 拓扑

```
N1 ─── 改名两个目录 + 正文内引用
 │
N2 ─── validator 白名单同步 + 负测（旧名必须报错）
 │
R0 ─── 267/271 + EXIT=0 复核
 │
R7 ─── 发布工程：切源 / 数字 / README / 测试 / 版本建议
 │
R0 ─── 出发布清单交主人
```

R5、R6 只需同步自己交付物里的名字，不阻塞主线，可与 N1 并行。

## 四 通过标准

`python v4/scripts/validate_graph.py` 退出 0；graph 267 / skills 271；
旧名 `dare-v4`、`research-catalog-v4` 在 `v4/skills/` 下不存在；
`cli/test/` + `dsh-plugin/test/` + `tests/test_codex_install.py` 全绿；
README 无 v3-only 表述。
