"""Render infrastructure-package use-dependency graphs as self-contained
interactive HTML (pyvis / vis-network), same lineage as the empirical-floor
skill_graph.html: vis-network inlined, external bootstrap CDN stripped, so the
file opens fully offline.

5 vertex types (campaign / strategy / tactic / sop / references), single edge
type `use`. One graph per infra repo; data is the cleaned dependency reconstruction
confirmed per-repo. Output HTML embeds only node names + layer. No filesystem paths.
"""
import argparse, re
from pathlib import Path

LAYER_COLORS = {
    "campaign":   "#ff3864",
    "strategy":   "#00f0ff",
    "tactic":     "#f9c80e",
    "sop":        "#9d7bff",
    "references": "#5a6988",
}
LAYER_SIZE = {"campaign": 40, "strategy": 30, "tactic": 22, "sop": 16, "references": 12}

# Cleaned use-dependency data per infra repo.
# nodes: {id: (layer, desc)}   edges: [(from, to, tip)]  — edge type is always `use`.
GRAPHS = {
    "literature-engine": {
        "nodes": {
            "literature-overview": ("sop",
                "<b>最浅一档:landscape 扫描定位。</b> 用 alphaxiv.discover_papers + "
                "ss.relevanceSearch 快速扫一个主题上<b>有哪些论文、谁是关键作者、引用量大致多少</b>。"
                "<b>只读摘要和元数据,不读全文。</b> 作用是 orientation —— 在投入深读之前先拿到鸟瞰图,"
                "判断哪些论文值得往下挖。HARD-GATE:禁止基于摘要对方法 / 结果 / 贡献下任何结论。"),
            "literature-search": ("sop",
                "<b>中等深度:读 AI 摘要报告。</b> 用 alphaxiv.get_paper_content(fullText: false)读每篇选中论文的"
                "<b>结构化 AI 摘要报告</b>,理解方法、贡献、发现以及彼此如何比较。适合做 literature survey、"
                "gap 分析、背景知识构建。HARD-GATE:每篇待分析论文都必须真正拉取摘要报告;但仍<b>不是</b>原始全文。"),
            "literature-research": ("sop",
                "<b>最深一档:读原始全文。</b> 用 alphaxiv.get_paper_content(fullText: true)+ answer_pdf_queries "
                "读<b>论文原文</b>,做精确方法细节(方程 / 算法 / 架构)、实验设置(超参 / 数据集 / baseline)、"
                "技术级比较、实验设计、精确引用。这是<b>深度天花板</b> —— AI 摘要在这一档不可接受,必须读原文。"),
        },
        "edges": [
            ("literature-overview", "literature-search",
                "overview 完成 landscape 扫描、已识别出值得细读的论文,但 HARD-GATE 禁止基于摘要下方法 / 结果 / "
                "贡献结论时,转交 search 去读这些论文的 <b>AI 摘要报告</b>(中等深度),做综述 / gap 分析 / 背景构建。"),
            ("literature-overview", "literature-research",
                "overview 定位到的论文需要<b>最高深度</b>的严谨分析(精确方法细节、实验设置、技术级比较),"
                "摘要远不够时,<b>越过中间层</b>直接转交 research 去读原始全文。"),
            ("literature-search",   "literature-research",
                "search 读的 AI 摘要报告<b>不足以支撑严谨分析</b>(需要方程 / 算法 / 超参 / 数据集 / baseline 等"
                "只有原文才有的细节,用于实验设计或精确引用)时,转交 research 去读原始全文。"),
        ],
    },
    "web-browsing": {
        "nodes": {
            "web-search": ("sop",
                "<b>快速定向搜索。</b> 理解一个主题上<b>存在哪些页面和来源</b>,适合快速事实核查、landscape 概览、"
                "为深入研究发现 URL。<b>只返回片段(snippets)</b>,不读整页。需要全文内容分析时升级到 web-research。"),
            "web-research": ("sop",
                "<b>深度网页研究。</b> Step 1 用配置的 web-search MCP 发现 URL,Step 3 用 apify/rag-web-browser "
                "<b>抓取整页内容</b>做分析。读完整页面而非片段,用于需要实际页面内容的研究。"),
        },
        "edges": [
            ("web-search", "web-research",
                "web-search 只返回片段;当需要对<b>完整页面内容</b>做分析(而非快速概览)时,"
                "升级转交 web-research 抓取整页全文。"),
        ],
    },
    "context-management": {
        "nodes": {
            "context-checkpoint": ("sop",
                "<b>研究阶段中追加落盘。</b> 把发现、模式、重要论文、技术细节追加写入当前 Phase 的 context 文件。"
                "Step 1 先 import context-init 确保文件存在(幂等),并调用 timestamp.py 更新 Last Updated 时间戳。"),
            "context-init": ("sop",
                "<b>Phase 开始时创建 context 文件。</b> 每个研究 Phase 开始调用一次,初始化后续 context-checkpoint "
                "追加写入的文件。调用 timestamp.py 取当前时间,生成文件名 context/&lt;timestamp&gt;-&lt;slug&gt;.md。"),
            "timestamp.py": ("references",
                "scripts/ 下的小型时间戳辅助脚本,返回当前时间。供 context-init 命名文件、"
                "context-checkpoint 更新时间戳调用。"),
        },
        "edges": [
            ("context-checkpoint", "context-init",
                "context-checkpoint Step 1 import context-init,确保当前 Phase 的 context 文件已存在"
                "(幂等:已存在则跳过创建,返回现有路径)。"),
            ("context-checkpoint", "timestamp.py",
                "context-checkpoint 调用 timestamp.py 获取当前时间,更新文件的 Last Updated 时间戳。"),
            ("context-init", "timestamp.py",
                "context-init 运行 timestamp.py 取当前时间,用于生成 context 文件名 &lt;timestamp&gt;-&lt;topic-slug&gt;.md。"),
        ],
    },
    "subagent-spawning": {
        "nodes": {
            "spawn-agent": ("sop",
                "<b>派生隔离的 subagent 执行任务并回收结构化输出。</b> DARE 体系里<b>被依赖最广</b>"
                "(blast-radius 最高)的基础设施 SOP —— 任何需要嵌套子代理编排的 skill 都依赖它。"),
        },
        "edges": [],
    },
}


def strip_external_cdn(html: str) -> str:
    """Remove pyvis's external bootstrap CDN <link>/<script> so the file is
    fully offline-openable. vis-network is inlined; bootstrap is cosmetic only."""
    html = re.sub(r'<link[^>]*https://cdn\.jsdelivr\.net[^>]*>', "", html)
    html = re.sub(
        r'<script[^>]*src="https://cdn\.jsdelivr\.net[^"]*"[^>]*>\s*</script>',
        "", html)
    return html


_CHROME_CSS = """
<style>
  html, body { margin:0; padding:0; height:100%; background:#191a1f; overflow:hidden; }
  .card { border:0 !important; background:#191a1f !important; box-shadow:none !important;
          border-radius:0 !important; }
  .card-body { padding:0 !important; }
  #mynetwork { width:100vw !important; height:100vh !important; border:0 !important;
               background:#191a1f !important; }
  div.vis-tooltip {
    background:rgba(13,13,18,0.97) !important; border:1px solid #00f0ff !important;
    border-radius:10px !important; padding:12px 14px !important; max-width:380px !important;
    white-space:normal !important; color:#e8eaf2 !important; font-size:13px !important;
    line-height:1.7 !important; box-shadow:0 8px 28px rgba(0,0,0,0.6) !important;
    font-family:"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif !important;
  }
  div.vis-tooltip b { color:#00f0ff; }
  div.vis-tooltip hr { border:0; border-top:1px solid #2c2f3a; margin:7px 0; }
</style>
"""


def strip_chrome(html: str) -> str:
    """Remove pyvis's bootstrap card frame and make the network fill the viewport;
    inject controllable dark tooltip styling (vis .vis-tooltip, not bootstrap)."""
    html = html.replace("</head>", _CHROME_CSS + "</head>", 1)
    return html


def render(name: str, spec: dict, out_path: Path) -> tuple[int, int]:
    from pyvis.network import Network
    net = Network(height="100vh", width="100%", directed=True,
                  bgcolor="#191a1f", font_color="#eaeaea",
                  notebook=False, cdn_resources="in_line")
    net.barnes_hut(gravity=-6000, central_gravity=0.3, spring_length=130,
                   spring_strength=0.04, damping=0.5)
    for nid, (layer, desc) in spec["nodes"].items():
        net.add_node(nid, label=nid, group=layer,
                     color=LAYER_COLORS.get(layer, "#999999"),
                     size=LAYER_SIZE.get(layer, 16),
                     borderWidth=2,
                     shapeProperties={"borderDashes": layer == "references"},
                     title=f"<b>{nid}</b> [{layer}]<hr>{desc}")
    for a, b, tip in spec["edges"]:
        net.add_edge(a, b, title=tip, arrows="to", color="#5b6172")
    net.set_options('{"physics":{"stabilization":{"iterations":200}},'
                    '"nodes":{"font":{"size":16,"strokeWidth":4,"strokeColor":"#191a1f"}},'
                    '"edges":{"width":1.5,"selectionWidth":2.5,'
                    '"smooth":{"type":"continuous","roundness":0.25},'
                    '"color":{"highlight":"#00f0ff","hover":"#00f0ff"}},'
                    '"interaction":{"hover":true,"tooltipDelay":80,'
                    '"navigationButtons":false,"keyboard":false}}')
    html = strip_external_cdn(net.generate_html())
    html = strip_chrome(html)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    return len(spec["nodes"]), len(spec["edges"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True, help="output directory for .html files")
    ap.add_argument("--only", default=None, help="render only this repo (optional)")
    a = ap.parse_args()
    out_dir = Path(a.out_dir)
    targets = {a.only: GRAPHS[a.only]} if a.only else GRAPHS
    for name, spec in targets.items():
        n, e = render(name, spec, out_dir / f"{name}.html")
        print(f"{name}: {n} nodes, {e} edges -> {name}.html")


if __name__ == "__main__":
    main()
