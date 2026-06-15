import subprocess, re
from pathlib import Path

HERE = Path(__file__).resolve().parent

def test_render_adds_898_edges_9_nodes():
    out = subprocess.run(["python","render_combined.py","--out","_t.html"],
                          cwd=HERE, capture_output=True, text=True)
    assert out.returncode == 0, out.stderr
    # printed summary line: "combined+collapsed: N nodes, E edges, P packages"
    m = re.search(r"(\d+) nodes, (\d+) edges, (\d+) packages", out.stdout)
    nodes, edges = int(m.group(1)), int(m.group(2))
    assert nodes == 878, f"nodes={nodes} (want 869+9)"
    assert edges == 3335, f"edges={edges} (want 2437+898)"

def test_every_ref_node_present():
    html = (HERE / "_t.html").read_text(encoding="utf-8")
    for pkg in ["north-star-crystallization","knowledge-acquisition","deep-insight",
                "hypothesis-formation","creative-ideation","convergence","stress-test",
                "experiment-execution","knowledge-structuring"]:
        assert f"research-catalog/ref/{pkg}" in html, pkg
