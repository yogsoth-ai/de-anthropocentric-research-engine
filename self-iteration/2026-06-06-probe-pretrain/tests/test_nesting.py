from optimizer.nesting import run_dialogue, DialogueResult  # noqa: F401


def test_two_phase_f8_turn_budget():
    # fake: 模拟器每轮回 "demand", 执行器每轮回 "design v{n}"
    sim_turns, exec_turns = [], []

    def fake_sim(history, phase):
        sim_turns.append(phase)
        return f"demand-{phase}"

    def fake_exec(history):
        exec_turns.append(1)
        return f"design-{len(exec_turns)}"

    res = run_dialogue(card={"f8_pressure_turns": 3, "f8_closing_turns": 2},
                       topic="t", sim_fn=fake_sim, exec_fn=fake_exec)
    # 施压 3 轮 + 收尾 2 轮 = 5 个模拟器轮次
    assert sim_turns.count("pressure") == 3
    assert sim_turns.count("closing") == 2
    assert res.completability in ("ok", "failed")
    assert res.spec_text is not None
