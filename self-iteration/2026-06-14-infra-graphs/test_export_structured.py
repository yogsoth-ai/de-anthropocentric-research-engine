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
