from optimizer.topic_run import run_topic_ladder


class FakeEmitter:
    def __init__(self):
        self.events = []

    def emit(self, event, **fields):
        self.events.append(event)

    def save_transcript(self, sample_id, text):
        return f"transcripts/{sample_id}.md"


def test_topic_run_emits_rung_and_topic_events():
    cards = [{"label": f"id{i}", "f8_pressure_turns": 1, "f8_closing_turns": 1,
              "axis_levels": {"A1": f"L{min(i,4)}"}} for i in range(2)]

    def fake_dialogue(card, topic, emitter=None, sample_id=""):
        class R:
            spec_text = ('```json graph\n{"nodes":[],"edges":[]}\n```\n'
                         '```json result\n{"document":"d"}\n```')
            transcript = [{"speaker": "user", "text": "x"}]
            completability = "ok"
            transcript_path = "transcripts/x.md"
        return R()

    def fake_loss1(t, c):
        return {"fidelity": True, "drift_flag": False, "per_axis_evidence": {}}

    def fake_loss2(s, o):
        return {"tau": 0.9, "monotonicity_pass": True, "endpoint_separation_pass": True,
                "rigor_floor_flag": False, "pairwise_log": []}

    em = FakeEmitter()
    run_topic_ladder(cards, topic_id="topic-01", dialogue_fn=fake_dialogue,
                     loss1_fn=fake_loss1, loss2_fn=fake_loss2, emitter=em)
    assert em.events.count("rung_start") == 2
    assert em.events.count("rung_done") == 2
    assert em.events.count("topic_start") == 1
    assert em.events.count("topic_done") == 1
