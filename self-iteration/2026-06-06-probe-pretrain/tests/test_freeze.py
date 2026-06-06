from optimizer.freeze import coverage_report, freeze_weights


def test_coverage_report_counts_axis_cells():
    samples = [
        {"label": {"A4": "C-", "A5": "G0"}}, {"label": {"A4": "C0", "A5": "G+"}},
        {"label": {"A4": "C0", "A5": "G0"}},
    ]
    rep = coverage_report(samples)
    assert rep["A4"]["C-"] == 1 and rep["A5"]["G+"] == 1


def test_freeze_marks_immutable(tmp_path):
    p = tmp_path / "frozen.json"
    freeze_weights({"axis_prose": {}}, p)
    import json
    assert json.loads(p.read_text())["_frozen"] is True
