"""Combine all data/*.json package graphs into ONE offline interactive HTML.

Each node id is namespaced as "<package>/<skill>" so the shared infra SOP names
that recur across packages (web-search, paper-search, ...) do not collide. The
node label stays the bare skill name; the hover tooltip names the owning
package. NO cross-package edges are invented — every package keeps exactly its
own edges, so the 13 repos appear as distinct clusters on one shared canvas.

Styling (LAYER_COLORS, sizes, the self-managed #dare-tip hover layer, offline
CDN strip) is imported from the repo-dependency-graph skill's render_graph.py,
so the combined view is pixel-consistent with the 13 per-repo HTMLs.

Usage:
  python render_combined.py                # -> all-graphs.html
  python render_combined.py --out foo.html
"""
import argparse, glob, json, importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
_RG = HERE / "repo-dependency-graph" / "scripts" / "render_graph.py"
_spec = importlib.util.spec_from_file_location("rg", _RG)
rg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rg)

from pyvis.network import Network


def build(files):
    net = Network(height="100vh", width="100%", directed=True,
                  bgcolor="#191a1f", font_color="#eaeaea",
                  notebook=False, cdn_resources="in_line")
    # lower central_gravity than the single-repo renderer so the many
    # disconnected clusters spread out instead of piling at the centre.
    net.barnes_hut(gravity=-6000, central_gravity=0.12, spring_length=130,
                   spring_strength=0.04, damping=0.5)
    nodes = edges = 0
    for f in sorted(files):
        s = json.loads(Path(f).read_text(encoding="utf-8"))
        pkg = s["name"]
        for n in s["nodes"]:
            layer = n["layer"]
            title = f'<b>{n["id"]}</b> [{layer}] &middot; <i>{pkg}</i>'
            if n.get("desc"):
                title += f"<hr>{n['desc']}"
            net.add_node(f"{pkg}/{n['id']}", label=n["id"], group=layer,
                         color=rg.LAYER_COLORS.get(layer, "#999999"),
                         size=rg.LAYER_SIZE.get(layer, 16), borderWidth=2,
                         shapeProperties={"borderDashes": layer == "references"},
                         title=title)
            nodes += 1
        for e in s["edges"]:
            net.add_edge(f"{pkg}/{e['from']}", f"{pkg}/{e['to']}",
                         title=e.get("tip", "use"), arrows="to", color="#5b6172")
            edges += 1
    net.set_options('{"physics":{"stabilization":{"iterations":150}},'
                    '"nodes":{"font":{"size":16,"strokeWidth":4,"strokeColor":"#191a1f"}},'
                    '"edges":{"width":1.5,"selectionWidth":2.5,'
                    '"smooth":{"type":"continuous","roundness":0.25},'
                    '"color":{"highlight":"#00f0ff","hover":"#00f0ff"}},'
                    '"interaction":{"hover":true,"tooltipDelay":80,'
                    '"navigationButtons":false,"keyboard":false}}')
    return net, nodes, edges


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", default=str(HERE / "data"))
    ap.add_argument("--out", default=str(HERE / "all-graphs.html"))
    a = ap.parse_args()
    files = sorted(Path(a.data_dir).glob("*.json"))
    net, nodes, edges = build(files)
    html = rg.strip_chrome(rg.strip_external_cdn(net.generate_html()))
    out = Path(a.out)
    out.write_text(html, encoding="utf-8")
    print(f"combined: {nodes} nodes, {edges} edges, {len(files)} packages -> {out.name}")


if __name__ == "__main__":
    main()
