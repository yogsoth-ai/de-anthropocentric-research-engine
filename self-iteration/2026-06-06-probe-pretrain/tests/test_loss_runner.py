from optimizer.loss_runner import run_loss1, run_loss2, parse_loss1, parse_loss2


def test_parse_loss1():
    out = '{"fidelity": true, "per_axis_evidence": {}, "drift_flag": false}'
    r = parse_loss1(out)
    assert r["fidelity"] is True and r["drift_flag"] is False


def test_parse_loss2():
    out = '{"tau": 0.85, "monotonicity_pass": true, "endpoint_separation_pass": true, "rigor_floor_flag": false, "pairwise_log": []}'
    r = parse_loss2(out)
    assert r["tau"] == 0.85 and r["monotonicity_pass"] is True


def test_run_loss1_uses_injected_codex(monkeypatch):
    calls = {}

    def fake_codex(skill, payload):
        calls["skill"] = skill
        return '{"fidelity": true, "per_axis_evidence": {}, "drift_flag": false}'

    r = run_loss1(transcript=[{"speaker": "user", "text": "why?"}], card={"label": "id0"},
                  codex_fn=fake_codex)
    assert calls["skill"] == "injection-fidelity"
    assert r["fidelity"] is True
