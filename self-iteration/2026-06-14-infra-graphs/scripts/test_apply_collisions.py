import json, shutil
from pathlib import Path
import lib_refactory as lib
import apply_collisions as ac

HERE = Path(__file__).resolve().parent

# 5 stale flat-merge orphan wrapper folders (not graph nodes; 3 carry external source)
ORPHANS = ("broad-paper-search", "broad-web-search",
           "paper-overview", "paper-research", "paper-search")


def test_plan_counts():
    p = ac.build_plan()        # dry-run plan, no disk writes
    # 101 copy-rename targets (64 collision + 37 wrapper)
    assert len(p["copies"]) == 101
    # 29 collision bare + 5 stale orphan wrapper folders = 34
    assert len(p["deletes"]) == 34
    # timestamp.py copied into both context skills
    assert any("context-init" in str(t) for t in p["scripts"])
    assert any("context-checkpoint" in str(t) for t in p["scripts"])


def test_copy_sources_exist():
    p = ac.build_plan()
    for c in p["copies"]:
        assert Path(c["src"]).exists(), f"source missing: {c['src']}"


def test_wrapper_source_internal():
    # every wrapper's source: must point inside skills/, never an external repo
    p = ac.build_plan()
    for w in p["wrapper_source_fixes"]:
        assert w["source"].startswith("skills/"), w
    assert len(p["wrapper_source_fixes"]) == 37


def test_body_fixes_make_web_bodies_self_contained():
    # web-search / web-research flat folders are external-import wrappers on disk;
    # build_plan must replace them with the REAL bodies from the source repo.
    p = ac.build_plan()
    names = {b["name"] for b in p["body_fixes"]}
    assert names == {"web-search", "web-research"}
    for b in p["body_fixes"]:
        assert Path(b["src"]).exists(), f"body source missing: {b['src']}"


def test_orphans_are_deleted():
    p = ac.build_plan()
    deleted_names = {Path(d).name for d in p["deletes"]}
    for orphan in ORPHANS:
        assert orphan in deleted_names, f"orphan not scheduled for delete: {orphan}"
    # the kept infra bodies must NOT be deleted
    assert "web-search" not in deleted_names
    assert "web-research" not in deleted_names


def _expected_missing():
    """Graph skill nodes absent from the flat body and not rename targets — computed
    the same way the script does, so the test is independent of whether apply already
    ran (clean tree -> 68; post-apply -> 0; both correct)."""
    d = lib.load_source()
    on_disk = {p.name for p in lib.SKILL_DIR.iterdir() if (p / "SKILL.md").exists()}
    new_names = set(lib.rename_map().values())
    return {n["name"] for n in d["nodes"]
            if n["layer"] not in ("references", "entry")
            and n["name"] not in on_disk and n["name"] not in new_names}


def test_missing_nodes_match_graph_gap():
    # build_plan's missing_nodes must equal the graph-vs-disk gap (order/idempotent-safe)
    p = ac.build_plan()
    mn = p["missing_nodes"]
    got = {Path(m["dst"]).parent.name if m.get("is_entry") else Path(m["dst"]).name
           for m in mn}
    assert got == _expected_missing()
    # every planned source must exist; entry roots come from ENTRY.md
    for m in mn:
        assert Path(m["src"]).exists(), f"missing-node source absent: {m['src']}"
        if m.get("is_entry"):
            assert Path(m["src"]).name == "ENTRY.md"


def test_missing_nodes_cover_68_on_clean_tree():
    # On a pristine flat body (before any apply) the gap is exactly the 65
    # knowledge-structuring uniques + 3 package-root campaigns. Skip once applied.
    exp = _expected_missing()
    if not exp:
        import pytest
        pytest.skip("flat body already populated (apply has run); gap closed")
    assert len(exp) == 68, f"clean-tree gap={len(exp)}"
    roots = exp & {"creative-ideation", "deep-insight", "knowledge-acquisition"}
    assert roots == {"creative-ideation", "deep-insight", "knowledge-acquisition"}


def test_missing_node_dst_inside_skills():
    p = ac.build_plan()
    for m in p["missing_nodes"]:
        assert str(lib.SKILL_DIR) in str(Path(m["dst"]).resolve().parent)
