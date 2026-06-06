from optimizer.loop import pretrain


def test_pretrain_stops_on_convergence():
    # fake: every batch all 8 topics pass -> 3 consecutive batches converge
    def fake_batch(batch_id, weights):
        ratios = [True] * 8
        return {"topic_pass_flags": ratios, "samples": [{"id": f"{batch_id}-s"}],
                "any_rigor_floor": False}

    history = pretrain(fake_batch_fn=fake_batch, max_safety=10)
    assert history["converged"] is True
    assert history["num_batches"] == 3  # stops at 3 consecutive


def test_pretrain_keeps_looping_until_gate():
    seq = [[True] * 6 + [False] * 2,  # 0.75 fails
           [True] * 7 + [False],      # 0.875
           [True] * 7 + [False],      # 0.875
           [True] * 8]                # 1.0 -> last 3 = 0.875,0.875,1.0 all >= 0.8
    calls = {"i": 0}

    def fake_batch(batch_id, weights):
        flags = seq[min(calls["i"], len(seq) - 1)]
        calls["i"] += 1
        return {"topic_pass_flags": flags, "samples": [], "any_rigor_floor": False}

    history = pretrain(fake_batch_fn=fake_batch, max_safety=20)
    assert history["converged"] is True
    assert history["num_batches"] == 4
