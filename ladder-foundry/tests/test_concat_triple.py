import json, subprocess, sys


def _setup(tmp_path, md):
    rd = tmp_path / "run"
    for sub in ("configs", "transcripts", "triples"):
        (rd / sub).mkdir(parents=True)
    (rd / "configs" / "s1.json").write_text(json.dumps({"F0": "cfg"}), encoding="utf-8")
    (rd / "transcripts" / "s1.md").write_text(md, encoding="utf-8")
    return rd


def test_concat_takes_last_fenced_block(tmp_path):
    md = "\n".join([
        "```research-graph", '{"nodes": [], "edges": []}', "```",
        "```research-result", '{"title": "old"}', "```",
        "```research-result", '{"title": "final"}', "```",   # accepted draft after pushback
    ])
    rd = _setup(tmp_path, md)
    subprocess.check_call([sys.executable, "scripts/concat_triple.py",
        "--run-dir", str(rd), "--sample", "s1"])
    tri = json.loads((rd / "triples" / "s1.json").read_text(encoding="utf-8"))
    assert tri["research_config"]["F0"] == "cfg"
    assert tri["research_result"]["title"] == "final"     # LAST research-result block
    assert "nodes" in tri["research_graph"]               # graph block also cut


def test_missing_fence_raises(tmp_path):
    rd = _setup(tmp_path, "```research-graph\n{\"nodes\": []}\n```\n")  # no research-result
    r = subprocess.run([sys.executable, "scripts/concat_triple.py",
        "--run-dir", str(rd), "--sample", "s1"])
    assert r.returncode != 0                              # missing required fence -> non-zero
