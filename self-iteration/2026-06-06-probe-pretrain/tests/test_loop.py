from optimizer.loop import pretrain


def test_pretrain_stops_on_convergence():
    # fake: 每个 batch 8 topic 全过 → 连续 3 batch 收敛
    def fake_batch(batch_id, weights):
        ratios = [True] * 8
        return {"topic_pass_flags": ratios, "samples": [{"id": f"{batch_id}-s"}],
                "any_rigor_floor": False}

    history = pretrain(fake_batch_fn=fake_batch, max_safety=10)
    assert history["converged"] is True
    assert history["num_batches"] == 3  # 连续 3 个即停


def test_pretrain_keeps_looping_until_gate():
    seq = [[True] * 6 + [False] * 2,  # 0.75 不过
           [True] * 7 + [False],      # 0.875
           [True] * 7 + [False],      # 0.875
           [True] * 8]                # 1.0 → 此时最近3个=0.875,0.875,1.0 全≥0.8
    calls = {"i": 0}

    def fake_batch(batch_id, weights):
        flags = seq[min(calls["i"], len(seq) - 1)]
        calls["i"] += 1
        return {"topic_pass_flags": flags, "samples": [], "any_rigor_floor": False}

    history = pretrain(fake_batch_fn=fake_batch, max_safety=20)
    assert history["converged"] is True
    assert history["num_batches"] == 4
