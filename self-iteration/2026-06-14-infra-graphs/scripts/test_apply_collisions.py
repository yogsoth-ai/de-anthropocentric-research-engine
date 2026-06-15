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
