import json
import subprocess
import sys
from pathlib import Path

LF = Path(__file__).resolve().parents[1]          # ladder-foundry/
SPECS = LF / "skills" / "formated-specs" / "SKILL.md"
RESULTS = LF / "skills" / "formated-results" / "SKILL.md"

sys.path.insert(0, str(LF))
from generator.leak_audit import leak_audit, LeakHit


def test_both_skill_md_exist():
    assert SPECS.exists() and RESULTS.exists()


def test_skill_md_are_leak_clean():
    leak_audit(SPECS.read_text(encoding="utf-8"))      # raises LeakHit on any check vocab
    leak_audit(RESULTS.read_text(encoding="utf-8"))


def test_frontmatter_names_are_plural():
    assert "name: formated-specs" in SPECS.read_text(encoding="utf-8")
    assert "name: formated-results" in RESULTS.read_text(encoding="utf-8")


def _make_run(tmp_path, graph_blocks, result_blocks):
    rd = tmp_path / "runs" / "r0"
    for sub in ("configs", "transcripts", "triples"):
        (rd / sub).mkdir(parents=True)
    (rd / "configs" / "s.json").write_text('{"rung_id": 0}', encoding="utf-8")
    md = "# transcript\n\n"
    for g in graph_blocks:
        md += "```research-graph\n" + json.dumps(g) + "\n```\n\n"
    for r in result_blocks:
        md += "```research-result\n" + json.dumps(r) + "\n```\n\n"
    (rd / "transcripts" / "s.md").write_text(md, encoding="utf-8")
    return rd


def _run_concat(rd):
    return subprocess.run([sys.executable, "scripts/concat_triple.py",
                           "--run-dir", str(rd), "--sample", "s"],
                          cwd=str(LF), capture_output=True, text=True)


def test_fence_contract_green(tmp_path):
    rd = _make_run(tmp_path, [{"nodes": []}], [{"title": "only"}])
    r = _run_concat(rd)
    assert r.returncode == 0, r.stderr
    tri = json.loads((rd / "triples" / "s.json").read_text(encoding="utf-8"))
    assert set(tri) == {"research_config", "research_graph", "research_result"}
    assert tri["research_result"]["title"] == "only"


def test_takes_last_result_block(tmp_path):
    rd = _make_run(tmp_path, [{"nodes": []}],
                   [{"title": "draft"}, {"title": "final"}])
    assert _run_concat(rd).returncode == 0
    tri = json.loads((rd / "triples" / "s.json").read_text(encoding="utf-8"))
    assert tri["research_result"]["title"] == "final"


def test_missing_result_fence_nonzero(tmp_path):
    rd = _make_run(tmp_path, [{"nodes": []}], [])     # no research-result fence
    assert _run_concat(rd).returncode != 0


def test_wrong_info_string_drift_nonzero(tmp_path):
    rd = tmp_path / "runs" / "r0"
    for sub in ("configs", "transcripts", "triples"):
        (rd / sub).mkdir(parents=True)
    (rd / "configs" / "s.json").write_text("{}", encoding="utf-8")
    # ```json drift instead of ```research-graph -> concat findall empties -> ValueError
    (rd / "transcripts" / "s.md").write_text(
        '```json\n{"nodes": []}\n```\n\n```research-result\n{"title":"x"}\n```\n',
        encoding="utf-8")
    assert _run_concat(rd).returncode != 0
