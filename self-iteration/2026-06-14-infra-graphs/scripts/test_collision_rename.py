import subprocess, re, json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def _collision():
    return json.loads((HERE / "collision-links.json").read_text(encoding="utf-8"))["groups"]

def test_collision_links_shape():
    g = _collision()
    assert len(g) == 64, f"collision nodes={len(g)} (want 64)"
    names = {c["old"] for c in g}
    assert len(names) == 29, f"collision names={len(names)} (want 29)"
    # no wrapper / no REF leaked in
    WRAP = {"web-search","web-research","paper-overview","paper-search","paper-research"}
    assert not (names & WRAP), f"wrapper leaked into collision set: {names & WRAP}"
    for c in g:
        assert "/" not in c["old"], f"old name should be bare: {c['old']}"


def _render():
    out = subprocess.run(["python","render_combined.py","--out","_t_cr.html"],
                         cwd=HERE, capture_output=True, text=True)
    assert out.returncode == 0, out.stderr
    h = (HERE / "_t_cr.html").read_text(encoding="utf-8")
    nodes = json.loads(re.search(r'nodes = new vis.DataSet\((\[.*?\])\);', h, re.S).group(1))
    edges = json.loads(re.search(r'edges = new vis.DataSet\((\[.*?\])\);', h, re.S).group(1))
    return out.stdout, nodes, edges

def test_no_bare_collision():
    _, nodes, _ = _render()
    bare = {}
    for n in nodes:
        nid = str(n["id"])
        if "/ref/" in nid:          # 4 REF nodes keep ref/ qualifier — exempt
            continue
        b = nid.split("/")[-1]
        bare.setdefault(b, []).append(nid)
    dups = {b: v for b, v in bare.items() if len(v) > 1}
    assert not dups, f"bare-name collisions remain: {dict(list(dups.items())[:5])}"

def test_64_collision_nodes_renamed():
    _, nodes, _ = _render()
    by_id = {n["id"]: n for n in nodes}
    for c in _collision():
        nid = f"{c['pkg']}/{c['pkg']}-{c['old']}"
        assert nid in by_id, f"missing renamed collision node {nid}"
        assert by_id[nid]["label"] == f"{c['pkg']}-{c['old']}", f"label wrong: {nid}"

def test_node_count_unchanged():
    _, nodes, _ = _render()
    assert len(nodes) == 915, f"nodes={len(nodes)} (rename must not add/drop)"

def test_ref_untouched():
    _, nodes, _ = _render()
    nids = {n["id"] for n in nodes}
    for p in ["creative-ideation","deep-insight","knowledge-acquisition","north-star-crystallization"]:
        assert f"research-catalog/ref/{p}" in nids, f"REF node lost: {p}"

def test_edge_count_locked_after_collision():
    out, _, edges = _render()
    EXPECT = 3376   # observed: collision rename is a pure relabel, no dedup shift
    assert len(edges) == EXPECT, f"edges={len(edges)}, expected {EXPECT}"
