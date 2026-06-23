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
    # Baseline updated by the infra de-collapse round (2026-06-15): the 37 import
    # wrappers re-materialize as their own nodes (+37 -> 915) and gain import edges
    # (+37) on top of a +4 dedup shift from un-collapsing (-> 3376). The ref
    # injection's own contribution (9 ref nodes + 898 edges) is unchanged and is
    # asserted structurally in test_decollapse.py.
    assert nodes == 915, f"nodes={nodes} (want 878 base + 37 re-materialized wrappers)"
    assert edges == 3376, f"edges={edges} (want 3339 de-collapsed base + 37 import edges)"

def test_every_ref_node_present():
    html = (HERE / "_t.html").read_text(encoding="utf-8")
    for pkg in ["north-star-crystallization","knowledge-acquisition","deep-insight",
                "hypothesis-formation","creative-ideation","convergence","stress-test",
                "experiment-execution","knowledge-structuring"]:
        assert f"research-catalog/ref/{pkg}" in html, pkg
