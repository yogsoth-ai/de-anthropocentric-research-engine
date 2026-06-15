"""Stage-2: parse the stage-1-fixed all-graphs.html (the single source of truth)
into refactory_source.json. NEVER recompute names — copy ids/labels/desc/tip
verbatim from the rendered DataSets. <pkg>/ prefix is stripped to a bare `name`
plus a `package` field; REF nodes (research-catalog/ref/<pkg>) keep ref/<pkg>.
`update` is filled "none" here; the 3 update classes are injected by later steps
(rename = merge_updates.py --rename-only, scan = merge_updates.py)."""
import argparse, json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent

def parse_html(html_path):
    h = Path(html_path).read_text(encoding="utf-8")
    nodes = json.loads(re.search(r'nodes = new vis.DataSet\((\[.*?\])\);', h, re.S).group(1))
    edges = json.loads(re.search(r'edges = new vis.DataSet\((\[.*?\])\);', h, re.S).group(1))
    return nodes, edges

def split_id(nid):
    """`<pkg>/<skill>` -> (pkg, bare). REF `research-catalog/ref/<pkg>` ->
    ('research-catalog', 'ref/<pkg>')."""
    if "/ref/" in nid:
        pkg = nid.split("/", 1)[0]
        return pkg, nid.split("/", 1)[1]   # 'ref/<pkg>'
    pkg, bare = nid.split("/", 1)
    return pkg, bare

def build(html_path):
    vnodes, vedges = parse_html(html_path)
    nodes = []
    for n in vnodes:
        pkg, bare = split_id(str(n["id"]))
        # description: prefer the HTML title (hover), strip the RENAME directive we
        # appended (everything from the first '<hr><b>RENAME' on) so description is
        # the original desc only; rename info goes into `update` instead.
        title = n.get("title") or ""
        title = re.split(r'<hr><b>RENAME', title)[0]
        nodes.append({"name": bare, "layer": n.get("group",""),
                      "package": pkg, "description": title, "update": "none"})
    edges = [{"from": split_id(str(e["from"]))[1], "to": split_id(str(e["to"]))[1],
              "description": e.get("title",""), "update": "none"} for e in vedges]
    return {"meta": {"source": "all-graphs.html",
                     "generated_from": "render_combined.py",
                     "node_count": len(nodes), "edge_count": len(edges),
                     "note": "DARE 正确形态;refactory 唯一信息源"},
            "nodes": nodes, "edges": edges}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--html", default=str(HERE / "all-graphs.html"))
    ap.add_argument("--out", default=str(HERE / "refactory_source.json"))
    a = ap.parse_args()
    data = build(a.html)
    Path(a.out).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"refactory_source: {data['meta']['node_count']} nodes, "
          f"{data['meta']['edge_count']} edges -> {Path(a.out).name}")

if __name__ == "__main__":
    main()
