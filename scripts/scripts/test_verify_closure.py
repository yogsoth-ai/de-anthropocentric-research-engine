from pathlib import Path
import lib_refactory as lib
import verify_closure as vc


def test_target_is_skill_to_skill_only():
    # target set excludes ref fan-out, catalog->ref, timestamp.py
    tgt = vc.target_edges()
    assert ("ref/convergence", "convergence-saturation-detection") not in tgt
    assert all(b != "timestamp.py" for _, b in tgt)
    # 1519 missing + 957 none skill->skill = 2476
    assert len(tgt) == 2476, f"target={len(tgt)}"


def test_scan_reads_new_subkeys(tmp_path):
    # a SKILL.md with new dependencies sub-keys yields the right edges
    sk = tmp_path / "skills" / "foo"
    sk.mkdir(parents=True)
    (sk / "SKILL.md").write_text(
        "---\nname: foo\ndependencies:\n  sops:\n    - bar\n  tactics:\n    - baz\n---\nbody\n",
        encoding="utf-8")
    edges = vc.scan_dir(tmp_path / "skills")
    assert ("foo", "bar") in edges and ("foo", "baz") in edges


def test_scan_ignores_used_by(tmp_path):
    sk = tmp_path / "skills" / "foo"
    sk.mkdir(parents=True)
    (sk / "SKILL.md").write_text(
        "---\nname: foo\nused-by:\n  - parent\n---\nbody\n", encoding="utf-8")
    edges = vc.scan_dir(tmp_path / "skills")
    assert ("parent", "foo") not in edges and ("foo", "parent") not in edges
