"""Combine all data/*.json package graphs into ONE offline interactive HTML.

Connection model (driven by infra-links.json, derived from source frontmatter):
  - import-SOP wrappers (web-search/web-research + the resolvable paper->literature
    ones) are RE-MATERIALIZED as their own nodes, RENAMED to `<pkg>/<pkg>-<wrapper>`
    (the on-disk target name), each wired by ONE import edge to the real underlying
    infra skill (`literature-engine/literature-overview`, `web-browsing/web-search`,
    …). The old collapse-onto-a-hub behavior is gone.
  - each `execution: subagent` SOP gets an edge to `subagent-spawning/spawn-agent`.
  - each campaign gets edges to `context-management/context-init` and
    `.../context-checkpoint`.
  - the 4 infra packages (literature-engine, web-browsing, subagent-spawning,
    context-management) render as ordinary `<pkg>/<skill>` SOP nodes — no `infra/`
    prefix, no hub enlargement, no special styling.

Each renamed wrapper node carries a RENAME directive in its hover desc: this graph
is the executable spec for a LATER on-disk refactoring round that renames the skill
directories and fixes their `source:` pointers. THIS module touches only the graph.

Deferred (NOT connected here): 12 paper-* wrappers whose source: pointers are
broken (hypothesis-formation / convergence / experiment-execution / stress-test).
They stay as package-local nodes until the recovery pass confirms their targets.

Styling reused from the repo-dependency-graph skill renderer (LAYER_COLORS, sizes,
#dare-tip hover layer, offline CDN strip) for visual consistency.

Usage:
  python render_combined.py                 # -> all-graphs.html
  python render_combined.py --out foo.html
"""
import argparse, json, importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
_RG = HERE / "repo-dependency-graph" / "scripts" / "render_graph.py"
_spec = importlib.util.spec_from_file_location("rg", _RG)
rg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rg)
from pyvis.network import Network

# infra packages: still processed FIRST (so their real skills exist before any
# import edge points at them) but no longer prefixed/enlarged — they render as
# ordinary SOPs like every other package.
INFRA_PKGS = {"literature-engine", "web-browsing", "subagent-spawning", "context-management"}
SPAWN_HUB = "subagent-spawning/spawn-agent"
CTX_INIT  = "context-management/context-init"
CTX_CKPT  = "context-management/context-checkpoint"
# super-connected skills kept OUT of the physics solver so the layout settles
# (decoupled from the now-removed infra/ concept).
SUPERCONNECTED = {SPAWN_HUB, CTX_INIT, CTX_CKPT}

# research-catalog ref structure (U4): the catalog node lives in engine-core, so
# canon() prefixes it "engine-core/". Its 9 ref nodes + skill fan-out are injected
# programmatically (static json would be mangled by canon()).
RESEARCH_CATALOG = "engine-core/research-catalog"
NINE_PKGS = ["north-star-crystallization","knowledge-acquisition","deep-insight",
             "hypothesis-formation","creative-ideation","convergence","stress-test",
             "experiment-execution","knowledge-structuring"]


def load_links():
    return json.loads((HERE / "infra-links.json").read_text(encoding="utf-8"))


def build_rename(links):
    """wrapper `<pkg>/<wrapper>` -> renamed canonical id `<pkg>/<pkg>-<wrapper>`."""
    return {f"{c['pkg']}/{c['wrapper']}": f"{c['pkg']}/{c['pkg']}-{c['wrapper']}"
            for c in links["collapse"]}


def build_target(links):
    """wrapper `<pkg>/<wrapper>` -> real infra skill `<infra>/<skill>` it imports."""
    return {f"{c['pkg']}/{c['wrapper']}": f"{c['infra']}/{c['skill']}"
            for c in links["collapse"]}


def canon(pkg, nid, rename):
    """Canonical id after de-collapse. Infra repos keep their plain <pkg>/<skill>
    id (no infra/ prefix); a collapse wrapper is RENAMED to <pkg>/<pkg>-<wrapper>;
    everything else stays <pkg>/<nid>."""
    key = f"{pkg}/{nid}"
    return rename.get(key, key)


def build(files, links, a_data_dir):
    net = Network(height="100vh", width="100%", directed=True,
                  bgcolor="#f8f9fa", font_color="#2b2f36",
                  notebook=False, cdn_resources="in_line")
    net.barnes_hut(gravity=-6000, central_gravity=0.12, spring_length=130,
                   spring_strength=0.04, damping=0.5)
    rename = build_rename(links)
    target = build_target(links)
    added = set()          # node ids already added
    edgeset = set()        # (from,to) already added, dedup after rename
    n_cnt = e_cnt = 0

    def ensure(nid, label, layer, title):
        nonlocal n_cnt
        if nid in added:
            return
        net.add_node(nid, label=label, group=layer,
                     color=rg.LAYER_COLORS.get(layer, "#999999"),
                     size=rg.LAYER_SIZE.get(layer, 16),
                     borderWidth=2,
                     shapeProperties={"borderDashes": layer == "references"},
                     title=title)
        added.add(nid); n_cnt += 1

    def link(a, b, tip):
        nonlocal e_cnt
        if a == b or (a, b) in edgeset:
            return
        # Any edge touching a super-connected skill OR the research-catalog ref
        # structure is drawn but EXCLUDED from the physics solver (physics=false).
        # These nodes are super-connected (spawn-agent + context-* fan in from
        # every package; a ref node fans to its whole package); letting their
        # springs act makes total kinetic energy never decay, so the layout never
        # settles. Excluding them lets each package cluster lay out by its own
        # internal edges while the hub/ref links stay visible as star spokes.
        hub_edge = (a in SUPERCONNECTED or b in SUPERCONNECTED
                    or a.startswith("research-catalog/ref/") or b.startswith("research-catalog/ref/")
                    or a == RESEARCH_CATALOG or b == RESEARCH_CATALOG)
        net.add_edge(a, b, title=tip, arrows="to", color="#7D8E9E",
                     physics=not hub_edge)
        edgeset.add((a, b)); e_cnt += 1

    subagent_sops = links["subagent_sops"]
    # process infra packages FIRST so the real skill nodes (spawn-agent, context-*,
    # literature-*, web-*) exist before any import edge points at them.
    ordered = sorted(files, key=lambda p: (Path(p).stem not in INFRA_PKGS, Path(p).stem))
    for f in ordered:
        s = json.loads(Path(f).read_text(encoding="utf-8"))
        pkg = s["name"]
        layer_of = {n["id"]: n["layer"] for n in s["nodes"]}
        for n in s["nodes"]:
            key = f'{pkg}/{n["id"]}'
            cid = canon(pkg, n["id"], rename)
            layer = n["layer"]
            label = cid.split("/")[-1]
            title = f'<b>{label}</b> [{layer}] &middot; <i>{pkg}</i>'
            if n.get("desc"):
                title += f"<hr>{n['desc']}"
            if key in rename:  # a renamed import wrapper
                tgt = target[key]
                title += (f'<hr><b>RENAME 计划:</b> 本地 wrapper <code>{key}</code> → '
                          f'重命名为 <code>{cid.split("/")[-1]}</code>;import 自 '
                          f'<code>{tgt}</code>。后续 refactory 轮据此重命名磁盘 skill '
                          f'目录并修正其 <code>source:</code> 指针。')
            ensure(cid, label, layer, title)
        for e in s["edges"]:
            a = canon(pkg, e["from"], rename)
            b = canon(pkg, e["to"], rename)
            link(a, b, e.get("tip", "use"))
        # spawn-agent fan-in: each subagent SOP -> spawn hub
        if pkg not in INFRA_PKGS:
            for sop in subagent_sops.get(pkg, []):
                src = canon(pkg, sop, rename)
                if src in added:
                    link(src, SPAWN_HUB, "execution: subagent &mdash; spawned via <b>subagent-spawning/spawn-agent</b>")
            # campaign -> context-management
            for c in links["campaigns"]:
                if c["pkg"] == pkg:
                    cc = canon(pkg, c["campaign"], rename)
                    if cc in added:
                        link(cc, CTX_INIT, "campaign 启动时调 <b>context-init</b>（加载/创建 campaign context file）")
                        link(cc, CTX_CKPT, "每个 strategy 完成后调 <b>context-checkpoint</b>（硬性约束）")
    # --- import-SOP edges: each renamed wrapper -> the real infra skill ---
    # (de-collapse replacement: the wrapper is now its own node; this edge is the
    # import-forward the collapse used to imply. Target nodes already exist because
    # the 4 infra packages are processed first.)
    for key, nid in rename.items():
        tgt = target[key]
        if nid in added and tgt in added:
            link(nid, tgt, f"import-SOP 转发:<b>{nid.split('/')[-1]}</b> 调用真实 skill <b>{tgt}</b>")
    # --- research-catalog ref structure (U4) ---
    # research-catalog already added (engine-core). Add 9 ref nodes + fan-out.
    for pkg in NINE_PKGS:
        ref = f"research-catalog/ref/{pkg}"
        ensure(ref, f"ref:{pkg}", "references",
               f'<b>{pkg}</b> [references] &middot; <i>research-catalog ref table</i>'
               f'<hr>该 package 的完整 skill 表(layer→name 排序)。catalog 选中此 package 后读它。')
        # catalog -> ref
        link(RESEARCH_CATALOG, ref,
             f"读 research-catalog 后选中 <b>{pkg}</b>,打开其 skill 表")
        # ref -> every skill node of this package (canon'd ids)
        s = json.loads((Path(a_data_dir) / f"{pkg}.json").read_text(encoding="utf-8"))
        for n in s["nodes"]:
            cid = canon(pkg, n["id"], rename)
            if cid in added:
                link(ref, cid, f"<b>{pkg}</b> 表中的一项:{n['id']}")
    net.set_options('{"physics":{"stabilization":{"enabled":true,"iterations":1000,'
                    '"updateInterval":50,"fit":true},"minVelocity":0.75,'
                    '"barnesHut":{"avoidOverlap":0.2}},'
                    '"nodes":{"font":{"size":16,"color":"#2b2f36","strokeWidth":4,"strokeColor":"#f8f9fa"}},'
                    '"groups":{'
                    '"entry":{"color":{"background":"#ffb7b2","border":"#e8857e",'
                    '"highlight":{"background":"#ffc9c5","border":"#e8857e"},'
                    '"hover":{"background":"#ffc9c5","border":"#e8857e"}}},'
                    '"campaign":{"color":{"background":"#ffdac1","border":"#e6a878",'
                    '"highlight":{"background":"#ffe7d6","border":"#e6a878"},'
                    '"hover":{"background":"#ffe7d6","border":"#e6a878"}}},'
                    '"strategy":{"color":{"background":"#e2f0cb","border":"#a8c878",'
                    '"highlight":{"background":"#eef6e0","border":"#a8c878"},'
                    '"hover":{"background":"#eef6e0","border":"#a8c878"}}},'
                    '"tactic":{"color":{"background":"#b5ead7","border":"#6cc4a1",'
                    '"highlight":{"background":"#cdf2e4","border":"#6cc4a1"},'
                    '"hover":{"background":"#cdf2e4","border":"#6cc4a1"}}},'
                    '"sop":{"color":{"background":"#c7ceea","border":"#8b97cf",'
                    '"highlight":{"background":"#dadff2","border":"#8b97cf"},'
                    '"hover":{"background":"#dadff2","border":"#8b97cf"}}},'
                    '"references":{"color":{"background":"#FFFFBA","border":"#d6c84e",'
                    '"highlight":{"background":"#ffffd6","border":"#d6c84e"},'
                    '"hover":{"background":"#ffffd6","border":"#d6c84e"}}}},'
                    '"edges":{"width":1.5,"selectionWidth":2.5,'
                    '"smooth":{"type":"continuous","roundness":0.25},'
                    '"color":{"highlight":"#8b97cf","hover":"#8b97cf"}},'
                    '"interaction":{"hover":true,"tooltipDelay":80,'
                    '"navigationButtons":false,"keyboard":false}}')
    return net, n_cnt, e_cnt


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", default=str(HERE / "data"))
    ap.add_argument("--out", default=str(HERE / "all-graphs.html"))
    a = ap.parse_args()
    files = sorted(Path(a.data_dir).glob("*.json"))
    links = load_links()
    net, nodes, edges = build(files, links, a.data_dir)
    html = rg.strip_chrome(rg.strip_external_cdn(net.generate_html()))
    # Light-theme patch (combined file only — leaves the shared _CHROME_CSS and the
    # per-package single graphs on their dark theme). Swap the dark canvas/tooltip
    # tokens for the pastel palette: #f8f9fa background, dark tooltip -> light card.
    html = html.replace("#191a1f", "#f8f9fa")          # canvas + card + body bg
    html = (html
            .replace("background:rgba(13,13,18,0.97)", "background:rgba(255,255,255,0.98)")
            .replace("color:#e8eaf2", "color:#2b2f36")          # tooltip text
            .replace("border:1px solid #00f0ff", "border:1px solid #8b97cf")  # tooltip border
            .replace("#dare-tip b { color:#00f0ff; }", "#dare-tip b { color:#5b6aa8; }")
            .replace("border-top:1px solid #2c2f3a", "border-top:1px solid #d4d8df"))
    # Freeze fallback: once the solver reports stabilization done, turn physics
    # off so the canvas is guaranteed to come to rest even if residual jitter
    # remains. Dragging a node still works; it just won't re-simulate the world.
    freeze = ("""
                  network.on('stabilizationIterationsDone', function(){
                    network.setOptions({physics:false});
                  });""")
    html = html.replace(
        "                  network.on('blurEdge', _hide);",
        "                  network.on('blurEdge', _hide);" + freeze, 1)
    Path(a.out).write_text(html, encoding="utf-8")
    print(f"combined+collapsed: {nodes} nodes, {edges} edges, {len(files)} packages -> {Path(a.out).name}")


if __name__ == "__main__":
    main()
