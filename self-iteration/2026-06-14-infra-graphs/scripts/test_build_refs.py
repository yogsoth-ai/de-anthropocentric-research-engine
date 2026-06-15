import json, importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("build_refs", HERE / "build_refs.py")
br = importlib.util.module_from_spec(spec); spec.loader.exec_module(br)

NINE = ["north-star-crystallization","knowledge-acquisition","deep-insight",
        "hypothesis-formation","creative-ideation","convergence","stress-test",
        "experiment-execution","knowledge-structuring"]

def test_parse_descriptions_parses_table_rows():
    # skill-index.md (the original 2-column description source) was split into the
    # 9 ref files and removed; parse_descriptions must still parse a
    # "| skill | description |" table. A small committed fixture preserves that
    # exact format so the test stays meaningful without the deleted file.
    d = br.parse_descriptions(HERE / "testdata_skill_table.md")
    assert d["actor-profiling"].startswith("Understand who the user is")

def test_parse_descriptions_missing_source_is_empty():
    # When the source file is gone, callers fall back to the json desc field, so
    # parse_descriptions must degrade gracefully to an empty dict (not raise).
    assert br.parse_descriptions(HERE / "does-not-exist.md") == {}

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
