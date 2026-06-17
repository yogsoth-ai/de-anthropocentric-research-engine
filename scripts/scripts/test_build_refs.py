import json, importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("build_refs", HERE / "build_refs.py")
br = importlib.util.module_from_spec(spec); spec.loader.exec_module(br)
# Also make build_refs available as direct import for new tests
import build_refs

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
        nodes = json.loads((HERE.parent/"data"/f"{pkg}.json").read_text(encoding="utf-8"))["nodes"]
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


def _write_pkg(tmp_path, pkg, nodes):
    data_dir = tmp_path / "data"
    data_dir.mkdir(exist_ok=True)
    (data_dir / f"{pkg}.json").write_text(
        json.dumps({"name": pkg, "nodes": nodes}, ensure_ascii=False),
        encoding="utf-8")


def test_only_writes_just_that_package(tmp_path, monkeypatch):
    # two data files exist; --only must touch exactly one output
    monkeypatch.setattr(build_refs, "DATA", tmp_path / "data")
    monkeypatch.setattr(build_refs, "SKILL_INDEX", tmp_path / "gone.md")
    _write_pkg(tmp_path, "ara-from-context",
               [{"id": "ara-from-context", "layer": "campaign", "desc": "Compile a context/ record into an ARA"}])
    _write_pkg(tmp_path, "convergence",
               [{"id": "convergence", "layer": "campaign", "desc": "should not be written"}])
    out = tmp_path / "refs"
    build_refs.main(["--only", "ara-from-context", "--allow-degraded",
                     "--out-dir", str(out)])
    assert (out / "ara-from-context.md").exists()
    assert not (out / "convergence.md").exists()


def test_only_unknown_package_still_renders_from_json(tmp_path, monkeypatch):
    # a package not in NINE is allowed when its data json exists
    monkeypatch.setattr(build_refs, "DATA", tmp_path / "data")
    monkeypatch.setattr(build_refs, "SKILL_INDEX", tmp_path / "gone.md")
    _write_pkg(tmp_path, "ara-from-context",
               [{"id": "ara-compile", "layer": "sop", "desc": "Run the compiler"}])
    out = tmp_path / "refs"
    build_refs.main(["--only", "ara-from-context", "--allow-degraded",
                     "--out-dir", str(out)])
    text = (out / "ara-from-context.md").read_text(encoding="utf-8")
    assert "ara-compile" in text and "Run the compiler" in text
    assert "1 skills." in text
