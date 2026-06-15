import json, importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("build_refs", HERE / "build_refs.py")
br = importlib.util.module_from_spec(spec); spec.loader.exec_module(br)

NINE = ["north-star-crystallization","knowledge-acquisition","deep-insight",
        "hypothesis-formation","creative-ideation","convergence","stress-test",
        "experiment-execution","knowledge-structuring"]

def test_parse_descriptions_nonempty():
    d = br.parse_descriptions(HERE.parent.parent / "skills/research-catalog/skill-index.md")
    assert d["actor-profiling"].startswith("Understand who the user is")

def test_rows_for_package_count_matches_json():
    for pkg in NINE:
        nodes = json.loads((HERE/"data"/f"{pkg}.json").read_text(encoding="utf-8"))["nodes"]
        rows = br.rows_for_package(pkg)
        assert len(rows) == len(nodes), f"{pkg}: {len(rows)} != {len(nodes)}"

def test_rows_sorted_layer_then_name():
    rows = br.rows_for_package("convergence")
    keys = [(br.LAYER_RANK[r["layer"]], r["name"]) for r in rows]
    assert keys == sorted(keys)

def test_render_table_has_header_and_all_rows():
    md = br.render_table("north-star-crystallization")
    assert "| Layer | Skill | Description |" in md
    assert md.count("\n|") >= 33  # 33 skills + header rows
