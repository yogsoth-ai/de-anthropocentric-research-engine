import subprocess, re, json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def _render():
    out = subprocess.run(["python","render_combined.py","--out","_t_dc.html"],
                         cwd=HERE, capture_output=True, text=True)
    assert out.returncode == 0, out.stderr
    h = (HERE / "_t_dc.html").read_text(encoding="utf-8")
    nodes = json.loads(re.search(r'nodes = new vis.DataSet\((\[.*?\])\);', h, re.S).group(1))
    edges = json.loads(re.search(r'edges = new vis.DataSet\((\[.*?\])\);', h, re.S).group(1))
    return out.stdout, nodes, edges

# the 37 wrappers, derived from infra-links.json collapse array
def _wrappers():
    links = json.loads((HERE/"infra-links.json").read_text(encoding="utf-8"))
    return [(c["pkg"], c["wrapper"], f'{c["infra"]}/{c["skill"]}') for c in links["collapse"]]

def test_node_count_915():
    _, nodes, _ = _render()
    assert len(nodes) == 915, f"nodes={len(nodes)} (want 878+37)"

def test_no_infra_prefix_anywhere():
    _, nodes, edges = _render()
    bad_n = [n["id"] for n in nodes if str(n["id"]).startswith("infra/")]
    bad_e = [(e["from"],e["to"]) for e in edges
             if str(e["from"]).startswith("infra/") or str(e["to"]).startswith("infra/")]
    assert not bad_n, f"infra/ nodes remain: {bad_n[:3]}"
    assert not bad_e, f"infra/ edge endpoints remain: {bad_e[:3]}"

def test_wrappers_renamed_with_label_and_directive():
    _, nodes, _ = _render()
    by_id = {n["id"]: n for n in nodes}
    for pkg, w, _tgt in _wrappers():
        nid = f"{pkg}/{pkg}-{w}"
        assert nid in by_id, f"missing renamed node {nid}"
        assert by_id[nid]["label"] == f"{pkg}-{w}", f"label wrong for {nid}: {by_id[nid]['label']}"
        assert "RENAME" in (by_id[nid].get("title") or ""), f"no RENAME directive in {nid}"

def test_superconnected_edges_physics_false():
    _, _, edges = _render()
    SC = {"subagent-spawning/spawn-agent","context-management/context-init",
          "context-management/context-checkpoint"}
    for e in edges:
        if e["from"] in SC or e["to"] in SC:
            assert e.get("physics") is False, f"physics not false: {e['from']}->{e['to']}"
