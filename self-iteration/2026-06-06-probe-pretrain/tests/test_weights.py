from optimizer.weights import Weights


def test_weights_roundtrip(tmp_path):
    w = Weights.default()
    p = tmp_path / "w.json"
    w.save(p)
    w2 = Weights.load(p)
    assert w2.axis_prose == w.axis_prose
    assert w2.interp_params == w.interp_params


def test_revise_axis_prose_records_reason():
    w = Weights.default()
    w.revise(target="axis_prose", key="A1.L4", new_value="完全不追问", reason="loss-1 低: A1=L4 未演出")
    assert w.axis_prose["A1.L4"] == "完全不追问"
    assert w.revision_log[-1]["target"] == "axis_prose"
    # W5: 修改理由不得引用 check
    assert "check" not in w.revision_log[-1]["reason"].lower()


def test_revise_rejects_check_reference():
    w = Weights.default()
    import pytest
    with pytest.raises(ValueError, match="W5"):
        w.revise(target="interp_params", key="step", new_value=2, reason="R13 check fired")
