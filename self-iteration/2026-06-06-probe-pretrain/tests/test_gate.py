from optimizer.gate import topic_passes, batch_pass_ratio, converged


def test_topic_passes_requires_all_three():
    assert topic_passes(fidelity_rate=0.95, monotonicity_pass=True, endpoint_separation_pass=True)
    assert not topic_passes(fidelity_rate=0.80, monotonicity_pass=True, endpoint_separation_pass=True)
    assert not topic_passes(fidelity_rate=0.95, monotonicity_pass=False, endpoint_separation_pass=True)


def test_batch_pass_ratio_threshold():
    # 8 topic, 7 过 → 0.875 ≥ 0.8
    assert batch_pass_ratio([True] * 7 + [False]) >= 0.8


def test_converged_needs_3_consecutive():
    # 每 batch 的 pass ratio ≥0.8 连续 3 个
    assert converged([0.875, 0.875, 1.0])
    assert not converged([0.875, 0.75, 1.0])
    assert not converged([0.875, 0.875])  # 只有 2 个
