"""Render the layered skill graph as a self-contained interactive HTML
(pyvis / vis-network). Nodes colored by 4-layer level; inferred-layer nodes get
a dashed border so refactoring can tell declared from inferred. `reference`
nodes (e.g. research-catalog) are NOT skills and are excluded from the graph.

Output HTML embeds only node names + layer + phase. No filesystem paths.
"""
import argparse, json
from pathlib import Path

# Layers excluded from the graph entirely (not executable skills).
EXCLUDE_LAYERS = {"reference"}

LAYER_COLORS = {
    "campaign": "#e6194B",   # red    — top orchestration
    "strategy": "#f58231",   # orange
    "tactic":   "#3cb44b",   # green
    "sop":      "#4363d8",   # blue   — leaf execution
    "meta":     "#911eb4",   # purple — engine, outside the 4 layers
}
LAYER_SIZE = {"campaign": 40, "strategy": 28, "tactic": 20, "sop": 12, "meta": 36}
DECLARED_SOURCES = {"declared-type", "index-desc", "override"}

def build_nodes_edges(graph, layered):
    excluded = {n for n, v in layered.items()
                if (v.get("layer") in EXCLUDE_LAYERS)}
    nodes = []
    for n in graph["nodes"]:
        info = layered.get(n, {})
        layer = info.get("layer")
        if layer in EXCLUDE_LAYERS or layer is None:
            continue
        inferred = info.get("source") not in DECLARED_SOURCES
        phase = info.get("phase") or "—"
        nodes.append({
            "id": n,
            "label": n,
            "color": LAYER_COLORS.get(layer, "#999999"),
            "size": LAYER_SIZE.get(layer, 12),
            "title": f"{n}\nlayer: {layer} ({info.get('source')})\nphase: {phase}",
            "group": layer,
            "shapeProperties": {"borderDashes": inferred},
        })
    edges = []
    for a, b, src in graph["edges"]:
        if a in excluded or b in excluded:
            continue
        edges.append({"from": a, "to": b, "title": src, "arrows": "to"})
    return nodes, edges

def strip_external_cdn(html):
    """Remove pyvis's external bootstrap CDN <link>/<script> so the file is
    fully offline-openable. The graph uses inlined vis-network; bootstrap is
    only cosmetic chrome and is not needed."""
    import re
    html = re.sub(r'<link[^>]*https://cdn\.jsdelivr\.net[^>]*>', "", html)
    html = re.sub(r'<script[^>]*src="https://cdn\.jsdelivr\.net[^"]*"[^>]*>\s*</script>',
                  "", html)
    return html

def render_html(nodes, edges, out_path):
    from pyvis.network import Network
    net = Network(height="900px", width="100%", directed=True,
                  bgcolor="#1a1a1a", font_color="#eaeaea",
                  notebook=False, cdn_resources="in_line")
    net.barnes_hut(gravity=-8000, central_gravity=0.3, spring_length=120,
                   spring_strength=0.04, damping=0.5)
    for n in nodes:
        net.add_node(n["id"], label=n["label"], color=n["color"], size=n["size"],
                     title=n["title"], group=n["group"],
                     shapeProperties=n["shapeProperties"])
    ids = {n["id"] for n in nodes}
    for e in edges:
        if e["from"] in ids and e["to"] in ids:
            net.add_edge(e["from"], e["to"], title=e["title"], arrows=e["arrows"])
    net.set_options('{"physics":{"stabilization":{"iterations":200}},'
                    '"interaction":{"hover":true,"tooltipDelay":80,'
                    '"navigationButtons":true,"keyboard":true}}')
    html = net.generate_html()
    html = strip_external_cdn(html)
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text(html, encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--graph", required=True)
    ap.add_argument("--layers", required=True, help="layered_nodes.json")
    ap.add_argument("--out", required=True, help="output .html")
    a = ap.parse_args()
    graph = json.loads(Path(a.graph).read_text(encoding="utf-8"))
    layered = json.loads(Path(a.layers).read_text(encoding="utf-8"))
    nodes, edges = build_nodes_edges(graph, layered)
    render_html(nodes, edges, a.out)
    from collections import Counter
    print(f"rendered {len(nodes)} nodes, {len(edges)} edges -> {Path(a.out).name}")
    print("layers:", dict(Counter(n["group"] for n in nodes)))

if __name__ == "__main__":
    main()
