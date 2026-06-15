"""Render a skill repo's use-dependency graph as a self-contained interactive
HTML (pyvis / vis-network). Offline-openable (vis-network inlined, external CDN
stripped), Obsidian-style force-directed, draggable, with a self-managed HTML
hover tooltip.

Input is a graph JSON file (see references/graph-schema.md):
  {
    "name": "literature-engine",
    "nodes": [ {"id": "...", "layer": "sop", "desc": "<b>...</b> 中英混合"} , ... ],
    "edges": [ {"from": "...", "to": "...", "tip": "触发情景文案"} , ... ]
  }

5 vertex types (campaign / strategy / tactic / sop / references); single edge
type `use`. Output HTML embeds only node names + layer + the desc/tip you supply.
No filesystem paths are emitted.

Usage:
  python render_graph.py --data graph.json --out graph.html
  python render_graph.py --data-dir ./data --out-dir ./graphs   # batch: every *.json
"""
import argparse, json
from pathlib import Path

LAYER_COLORS = {
    "entry":      "#39ff14",
    "campaign":   "#ff3864",
    "strategy":   "#00f0ff",
    "tactic":     "#f9c80e",
    "sop":        "#9d7bff",
    "references": "#5a6988",
}
LAYER_SIZE = {"entry": 48, "campaign": 40, "strategy": 30, "tactic": 22, "sop": 16, "references": 12}

# Layer hierarchy used to sanity-check edges. use-edge legality:
#   campaign -> {strategy, tactic, sop, references}
#   strategy -> {tactic, sop, references}
#   tactic   -> {sop, references}
#   sop      -> {references}   (+ same-layer sop->sop allowed: escalation handoff)
#   any      -> references
RANK = {"campaign": 4, "strategy": 3, "tactic": 2, "sop": 1, "references": 0}


def check_edges(spec):
    """Return a list of human-readable legality warnings (does not raise).
    sop->sop is allowed (escalation handoff per design); higher->lower and
    any->references are allowed; lower->higher (except ->references) is flagged."""
    layer = {n["id"]: n["layer"] for n in spec["nodes"]}
    warns = []
    for e in spec["edges"]:
        a, b = layer.get(e["from"]), layer.get(e["to"])
        if a is None or b is None:
            warns.append(f"edge {e['from']}->{e['to']}: endpoint not in nodes")
            continue
        if b == "references":
            continue
        if a == "sop" and b == "sop":
            continue  # escalation handoff
        if RANK[a] <= RANK[b]:
            warns.append(f"edge {e['from']}({a})->{e['to']}({b}): "
                         f"non-orchestration direction (lower/equal rank)")
    return warns


def strip_external_cdn(html: str) -> str:
    """Remove pyvis's external bootstrap CDN <link>/<script> so the file opens
    fully offline. vis-network is inlined; bootstrap is cosmetic only."""
    import re
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
  div.vis-tooltip { display:none !important; }
  #dare-tip {
    position:fixed; z-index:9999; pointer-events:none; opacity:0;
    transition:opacity .12s; max-width:380px;
    background:rgba(13,13,18,0.97); border:1px solid #00f0ff; border-radius:10px;
    padding:12px 14px; color:#e8eaf2; font-size:13px; line-height:1.7;
    box-shadow:0 8px 28px rgba(0,0,0,0.6); white-space:normal;
    font-family:"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;
  }
  #dare-tip.show { opacity:1; }
  #dare-tip b { color:#00f0ff; }
  #dare-tip hr { border:0; border-top:1px solid #2c2f3a; margin:7px 0; }
</style>
"""

# Injected JS: vis renders a *string* title as plain text (HTML tags leak), so we
# stash titles, clear the native title, and render the HTML on hover in our own
# #dare-tip layer. Event-driven => robust across vis versions.
_TIP_JS = """
  var _tip = document.createElement('div'); _tip.id = 'dare-tip'; document.body.appendChild(_tip);
  var _nt = {}, _et = {};
  nodes.forEach(function(n){ if(n.title){ _nt[n.id] = n.title; nodes.update({id:n.id, title:undefined}); } });
  edges.forEach(function(e){ if(e.title){ _et[e.id] = e.title; edges.update({id:e.id, title:undefined}); } });
  var _mx = 0, _my = 0;
  document.addEventListener('mousemove', function(ev){ _mx = ev.clientX; _my = ev.clientY;
    if(_tip.classList.contains('show')){ _place(); } });
  function _place(){ var pad=16, w=_tip.offsetWidth, h=_tip.offsetHeight;
    var x=_mx+pad, y=_my+pad;
    if(x+w>innerWidth) x=_mx-w-pad; if(y+h>innerHeight) y=_my-h-pad;
    _tip.style.left=x+'px'; _tip.style.top=y+'px'; }
  function _show(html){ _tip.innerHTML=html; _tip.classList.add('show'); _place(); }
  function _hide(){ _tip.classList.remove('show'); }
                  network = new vis.Network(container, data, options);
                  network.on('hoverNode', function(p){ if(_nt[p.node]) _show(_nt[p.node]); });
                  network.on('hoverEdge', function(p){ if(_et[p.edge]) _show(_et[p.edge]); });
                  network.on('blurNode', _hide);
                  network.on('blurEdge', _hide);"""


def strip_chrome(html: str) -> str:
    """Remove pyvis's bootstrap card frame, fill the viewport, and swap vis's
    native (plain-text) tooltip for the self-managed #dare-tip layer."""
    html = html.replace("</head>", _CHROME_CSS + "</head>", 1)
    html = html.replace(
        "                  network = new vis.Network(container, data, options);",
        _TIP_JS, 1)
    return html


def render(spec: dict, out_path: Path) -> tuple[int, int]:
    from pyvis.network import Network
    net = Network(height="100vh", width="100%", directed=True,
                  bgcolor="#191a1f", font_color="#eaeaea",
                  notebook=False, cdn_resources="in_line")
    net.barnes_hut(gravity=-6000, central_gravity=0.3, spring_length=130,
                   spring_strength=0.04, damping=0.5)
    for n in spec["nodes"]:
        layer = n["layer"]
        title = f"<b>{n['id']}</b> [{layer}]"
        if n.get("desc"):
            title += f"<hr>{n['desc']}"
        net.add_node(n["id"], label=n["id"], group=layer,
                     color=LAYER_COLORS.get(layer, "#999999"),
                     size=LAYER_SIZE.get(layer, 16), borderWidth=2,
                     shapeProperties={"borderDashes": layer == "references"},
                     title=title)
    for e in spec["edges"]:
        net.add_edge(e["from"], e["to"], title=e.get("tip", "use"),
                     arrows="to", color="#5b6172")
    net.set_options('{"physics":{"stabilization":{"iterations":200}},'
                    '"nodes":{"font":{"size":16,"strokeWidth":4,"strokeColor":"#191a1f"}},'
                    '"edges":{"width":1.5,"selectionWidth":2.5,'
                    '"smooth":{"type":"continuous","roundness":0.25},'
                    '"color":{"highlight":"#00f0ff","hover":"#00f0ff"}},'
                    '"interaction":{"hover":true,"tooltipDelay":80,'
                    '"navigationButtons":false,"keyboard":false}}')
    html = strip_chrome(strip_external_cdn(net.generate_html()))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    return len(spec["nodes"]), len(spec["edges"])


def _load(path: Path) -> dict:
    spec = json.loads(path.read_text(encoding="utf-8"))
    for w in check_edges(spec):
        print(f"  [warn] {spec.get('name', path.stem)}: {w}")
    return spec


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data", help="single graph JSON file")
    ap.add_argument("--out", help="output .html (for --data)")
    ap.add_argument("--data-dir", help="dir of *.json graphs (batch mode)")
    ap.add_argument("--out-dir", help="output dir (for --data-dir)")
    a = ap.parse_args()
    if a.data:
        spec = _load(Path(a.data))
        out = Path(a.out or Path(a.data).with_suffix(".html"))
        n, e = render(spec, out)
        print(f"{spec.get('name', out.stem)}: {n} nodes, {e} edges -> {out.name}")
    elif a.data_dir:
        out_dir = Path(a.out_dir or a.data_dir)
        for jf in sorted(Path(a.data_dir).glob("*.json")):
            spec = _load(jf)
            name = spec.get("name", jf.stem)
            n, e = render(spec, out_dir / f"{name}.html")
            print(f"{name}: {n} nodes, {e} edges -> {name}.html")
    else:
        ap.error("provide --data <file> or --data-dir <dir>")


if __name__ == "__main__":
    main()
