from optimizer.topic_run import run_topic_ladder


def test_run_topic_ladder_emits_n_samples():
    cards = [{"label": f"id{i}", "f8_pressure_turns": 1, "f8_closing_turns": 1,
              "axis_levels": {"A1": f"L{min(i, 4)}"}} for i in range(6)]

    def fake_dialogue(card, topic):
        class R:
            spec_text = ('```json graph\n{"nodes":[],"edges":[]}\n```\n'
                         '```json result\n{"document":"d"}\n```')
            transcript = [{"speaker": "user", "text": "x"}]
            completability = "ok"
        return R()

    def fake_loss1(transcript, card):
        return {"fidelity": True, "drift_flag": False, "per_axis_evidence": {}}

    def fake_loss2(samples, order):
        return {"tau": 0.9, "monotonicity_pass": True, "endpoint_separation_pass": True,
                "rigor_floor_flag": False, "pairwise_log": []}

    result = run_topic_ladder(cards, topic_id="topic-01",
                              dialogue_fn=fake_dialogue, loss1_fn=fake_loss1, loss2_fn=fake_loss2)
    assert len(result["samples"]) == 6
    assert result["topic_pass"] is True
    assert result["fidelity_rate"] == 1.0
