import subprocess, json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def _export():
    out = subprocess.run(["python","export_structured.py","--out","_t_rs.json"],
                         cwd=HERE, capture_output=True, text=True)
    assert out.returncode == 0, out.stderr
    return json.loads((HERE / "_t_rs.json").read_text(encoding="utf-8"))

def test_schema_valid():
    d = _export()
    assert set(d.keys()) >= {"meta","nodes","edges"}
    assert d["meta"]["node_count"] == len(d["nodes"]) == 915
    for n in d["nodes"]:
        assert set(n.keys()) == {"name","layer","package","description","update"}, n
    for e in d["edges"]:
        assert set(e.keys()) == {"from","to","description","update"}, e

def test_names_are_bare():
    d = _export()
    for n in d["nodes"]:
        if n["package"] == "research-catalog":   # REF nodes keep ref/<pkg>
            assert n["name"].startswith("ref/")
        else:
            assert "/" not in n["name"], f"name not bare: {n['name']}"

def test_update_all_none_before_injection():
    d = _export()
    # 本任务阶段 update 全是 none(三类 update 由后续 task 注入)
    assert all(n["update"] == "none" for n in d["nodes"])
    assert all(e["update"] == "none" for e in d["edges"])


def _wrappers_and_collisions():
    links = json.loads((HERE/"infra-links.json").read_text(encoding="utf-8"))
    wr = [(c["pkg"], c["wrapper"], "wrapper", f'{c["infra"]}/{c["skill"]}') for c in links["collapse"]]
    col = [(c["pkg"], c["old"], "collision", None)
           for c in json.loads((HERE/"collision-links.json").read_text(encoding="utf-8"))["groups"]]
    return wr + col

def test_rename_updates_injected():
    # run full pipeline: export then merge rename
    subprocess.run(["python","export_structured.py"], cwd=HERE, check=True)
    subprocess.run(["python","merge_updates.py","--rename-only"], cwd=HERE, check=True)
    d = json.loads((HERE/"refactory_source.json").read_text(encoding="utf-8"))
    by = {(n["package"], n["name"]): n for n in d["nodes"]}
    for pkg, old, kind, tgt in _wrappers_and_collisions():
        n = by[(pkg, f"{pkg}-{old}")]
        assert n["update"].startswith("skill rename:"), f"{pkg}-{old}: {n['update']}"
        if kind == "wrapper":
            assert "source:" in n["update"], f"wrapper {pkg}-{old} missing source: fix"

def test_rename_count():
    d = json.loads((HERE/"refactory_source.json").read_text(encoding="utf-8"))
    renames = [n for n in d["nodes"] if n["update"].startswith("skill rename:")]
    assert len(renames) == 64 + 37, f"rename updates={len(renames)} (want 101)"


def test_missing_edges_computed():
    subprocess.run(["python","compute_missing_edges.py"], cwd=HERE, check=True)
    mu = json.loads((HERE/"missing-updates.json").read_text(encoding="utf-8"))
    eu = mu["edge_updates"]
    # every missing edge endpoint must be a real correct-graph node name
    d = json.loads((HERE/"refactory_source.json").read_text(encoding="utf-8"))
    names = {n["name"] for n in d["nodes"]}
    for e in eu:
        assert e["from"] in names and e["to"] in names, f"ghost: {e['from']}->{e['to']}"
        assert e["update"].startswith("缺失依赖 edge:"), e["update"][:40]
        assert e["confidence"] == "high"
    assert len(eu) > 0, "expected non-empty missing-edge set"


def test_update_values_classified():
    d = json.loads((HERE/"refactory_source.json").read_text(encoding="utf-8"))
    TAGS = ("skill rename:", "缺失依赖 edge:")   # 2 classes (缺失 skill node dropped)
    for n in d["nodes"]:
        assert n["update"] == "none" or n["update"].startswith(TAGS), n["update"][:40]
    for e in d["edges"]:
        assert e["update"] == "none" or e["update"].startswith(TAGS), e["update"][:40]

def test_missing_edges_subset():
    d = json.loads((HERE/"refactory_source.json").read_text(encoding="utf-8"))
    names = {n["name"] for n in d["nodes"]}
    for e in d["edges"]:
        if e["update"].startswith("缺失依赖 edge:"):
            assert e["from"] in names and e["to"] in names, f"ghost edge {e['from']}->{e['to']}"

def test_no_low_confidence_in_output():
    # low-confidence.json items must NOT appear as updates unless user-approved.
    # (This round low is empty — user elected to add all missing edges.)
    lc_path = HERE / "low-confidence.json"
    if not lc_path.exists():
        return
    lc = json.loads(lc_path.read_text(encoding="utf-8"))
    d = json.loads((HERE/"refactory_source.json").read_text(encoding="utf-8"))
    approved = {(i.get("from"), i.get("to")) for i in lc.get("approved", [])}
    out_edges = {(e["from"], e["to"]) for e in d["edges"]
                 if e["update"].startswith("缺失依赖 edge:")}
    for item in lc.get("edge_updates", []):
        key = (item["from"], item["to"])
        if key in out_edges:
            assert key in approved, f"unapproved low-confidence edge in output: {key}"

def test_injected_edge_count_matches_missing_updates():
    # self-contained: run the full pipeline so injection state is deterministic
    # regardless of test order (other tests re-export and reset update fields).
    subprocess.run(["python","export_structured.py"], cwd=HERE, check=True)
    subprocess.run(["python","compute_missing_edges.py"], cwd=HERE, check=True)
    subprocess.run(["python","merge_updates.py"], cwd=HERE, check=True)
    mu = json.loads((HERE/"missing-updates.json").read_text(encoding="utf-8"))["edge_updates"]
    d = json.loads((HERE/"refactory_source.json").read_text(encoding="utf-8"))
    injected = [e for e in d["edges"] if e["update"].startswith("缺失依赖 edge:")]
    assert len(injected) == len(mu), f"injected={len(injected)} vs missing-updates={len(mu)}"
