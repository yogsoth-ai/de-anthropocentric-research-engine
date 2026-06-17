import json
import build_refs


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
