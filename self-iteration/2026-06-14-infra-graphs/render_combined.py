"""Combine all data/*.json package graphs into ONE offline interactive HTML,
COLLAPSING shared infrastructure skills into single hub nodes so the 13 repos
connect through them instead of staying disconnected.

Connection model (driven by infra-links.json, derived from source frontmatter):
  - import-SOP wrappers (web-search/web-research + the resolvable paper->literature
    ones) are COLLAPSED onto one canonical `infra/<infra-pkg>/<skill>` hub node;
    every edge that touched a package-local wrapper is redirected to the hub.
  - each `execution: subagent` SOP gets an edge to `infra/subagent-spawning/spawn-agent`.
  - each campaign gets edges to `infra/context-management/context-init` and
    `.../context-checkpoint`.
  - the 4 infra packages' OWN graphs (literature-engine, web-browsing,
    subagent-spawning, context-management) are mapped onto the SAME hub ids, so a
    package's wrapper and the infra repo's real skill become the one shared node.

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

# infra packages whose own graph nodes map directly onto the shared hub ids
INFRA_PKGS = {"literature-engine", "web-browsing", "subagent-spawning", "context-management"}
SPAWN_HUB = "infra/subagent-spawning/spawn-agent"
CTX_INIT  = "infra/context-management/context-init"
CTX_CKPT  = "infra/context-management/context-checkpoint"

# research-catalog ref structure (U4): the catalog node lives in engine-core, so
# canon() prefixes it "engine-core/". Its 9 ref nodes + skill fan-out are injected
# programmatically (static json would be mangled by canon()).
RESEARCH_CATALOG = "engine-core/research-catalog"
NINE_PKGS = ["north-star-crystallization","knowledge-acquisition","deep-insight",
             "hypothesis-formation","creative-ideation","convergence","stress-test",
             "experiment-execution","knowledge-structuring"]


def load_links():
    return json.loads((HERE / "infra-links.json").read_text(encoding="utf-8"))


def hub_id(infra_pkg, skill):
    return f"infra/{infra_pkg}/{skill}"


def build_remap(links):
    """Map each package-local node id `<pkg>/<wrapper>` to its canonical hub id.
    Also map the infra packages' own `<infra>/<skill>` nodes onto the same hub."""
    remap = {}
    for c in links["collapse"]:
        remap[f"{c['pkg']}/{c['wrapper']}"] = hub_id(c["infra"], c["skill"])
    # infra repos' own skills -> same hub id (so wrapper + real skill merge)
    for ip in INFRA_PKGS:
        # handled generically at node-add time (see build())
        pass
    return remap


def canon(pkg, nid, remap):
    """Canonical id for a node/edge endpoint after collapse."""
    # infra repo's own skill -> hub id
    if pkg in INFRA_PKGS:
        return hub_id(pkg, nid)
    # package-local wrapper that collapses onto a hub
    return remap.get(f"{pkg}/{nid}", f"{pkg}/{nid}")


def build(files, links, a_data_dir):
    net = Network(height="100vh", width="100%", directed=True,
                  bgcolor="#191a1f", font_color="#eaeaea",
                  notebook=False, cdn_resources="in_line")
    net.barnes_hut(gravity=-6000, central_gravity=0.12, spring_length=130,
                   spring_strength=0.04, damping=0.5)
    remap = build_remap(links)
    added = set()          # node ids already added
    edgeset = set()        # (from,to) already added, dedup after collapse
    n_cnt = e_cnt = 0

    def ensure(nid, label, layer, title):
        nonlocal n_cnt
        if nid in added:
            return
        net.add_node(nid, label=label, group=layer,
                     color=rg.LAYER_COLORS.get(layer, "#999999"),
                     size=rg.LAYER_SIZE.get(layer, 16) + (8 if nid.startswith("infra/") else 0),
                     borderWidth=2,
                     shapeProperties={"borderDashes": layer == "references"},
                     title=title)
        added.add(nid); n_cnt += 1

    def link(a, b, tip):
        nonlocal e_cnt
        if a == b or (a, b) in edgeset:
            return
        # Any edge touching an infra hub OR the research-catalog ref structure is
        # drawn but EXCLUDED from the physics solver (physics=false). The infra
        # hubs and the catalog ref nodes are super-connected (a ref node fans to
        # its whole package); letting their springs act makes total kinetic energy
        # never decay, so the layout never settles. Excluding them lets each
        # package cluster lay out by its own internal edges while the hub/ref links
        # stay visible as star spokes.
        hub_edge = (a.startswith("infra/") or b.startswith("infra/")
                    or a.startswith("research-catalog/ref/") or b.startswith("research-catalog/ref/")
                    or a == RESEARCH_CATALOG or b == RESEARCH_CATALOG)
        net.add_edge(a, b, title=tip, arrows="to", color="#5b6172",
                     physics=not hub_edge)
        edgeset.add((a, b)); e_cnt += 1

    subagent_sops = links["subagent_sops"]
    # process infra packages FIRST so the hub nodes (spawn-agent, context-*,
    # literature-*, web-*) exist before any package edge redirects onto them.
    ordered = sorted(files, key=lambda p: (Path(p).stem not in INFRA_PKGS, Path(p).stem))
    for f in ordered:
        s = json.loads(Path(f).read_text(encoding="utf-8"))
        pkg = s["name"]
        layer_of = {n["id"]: n["layer"] for n in s["nodes"]}
        for n in s["nodes"]:
            cid = canon(pkg, n["id"], remap)
            layer = n["layer"]
            if cid.startswith("infra/"):
                label = cid.split("/")[-1]
                title = f'<b>{label}</b> [{layer}] &middot; <i>infra hub</i>'
                if n.get("desc"):
                    title += f"<hr>{n['desc']}"
                ensure(cid, label, layer, title)
            else:
                title = f'<b>{n["id"]}</b> [{layer}] &middot; <i>{pkg}</i>'
                if n.get("desc"):
                    title += f"<hr>{n['desc']}"
                ensure(cid, n["id"], layer, title)
        for e in s["edges"]:
            a = canon(pkg, e["from"], remap)
            b = canon(pkg, e["to"], remap)
            link(a, b, e.get("tip", "use"))
        # spawn-agent fan-in: each subagent SOP -> spawn hub
        if pkg not in INFRA_PKGS:
            for sop in subagent_sops.get(pkg, []):
                src = canon(pkg, sop, remap)
                if src in added:
                    link(src, SPAWN_HUB, "execution: subagent &mdash; spawned via <b>subagent-spawning/spawn-agent</b>")
            # campaign -> context-management
            for c in links["campaigns"]:
                if c["pkg"] == pkg:
                    cc = canon(pkg, c["campaign"], remap)
                    if cc in added:
                        link(cc, CTX_INIT, "campaign 启动时调 <b>context-init</b>（加载/创建 campaign context file）")
                        link(cc, CTX_CKPT, "每个 strategy 完成后调 <b>context-checkpoint</b>（硬性约束）")
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
            cid = canon(pkg, n["id"], remap)
            if cid in added:
                link(ref, cid, f"<b>{pkg}</b> 表中的一项:{n['id']}")
    net.set_options('{"physics":{"stabilization":{"enabled":true,"iterations":1000,'
                    '"updateInterval":50,"fit":true},"minVelocity":0.75,'
                    '"barnesHut":{"avoidOverlap":0.2}},'
                    '"nodes":{"font":{"size":16,"strokeWidth":4,"strokeColor":"#191a1f"}},'
                    '"groups":{"entry":{"color":{"background":"#39ff14","border":"#0fae00",'
                    '"highlight":{"background":"#7dff5e","border":"#39ff14"},'
                    '"hover":{"background":"#7dff5e","border":"#39ff14"}}}},'
                    '"edges":{"width":1.5,"selectionWidth":2.5,'
                    '"smooth":{"type":"continuous","roundness":0.25},'
                    '"color":{"highlight":"#00f0ff","hover":"#00f0ff"}},'
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
