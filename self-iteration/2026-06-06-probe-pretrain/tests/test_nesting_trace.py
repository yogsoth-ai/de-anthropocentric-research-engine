from optimizer.nesting import run_dialogue


class FakeEmitter:
    def __init__(self):
        self.events = []
        self.transcripts = {}

    def emit(self, event, **fields):
        self.events.append((event, fields))

    def save_transcript(self, sample_id, text):
        self.transcripts[sample_id] = text
        return f"transcripts/{sample_id}.md"


def test_dialogue_emits_turn_events_and_saves_transcript():
    em = FakeEmitter()

    def fake_sim(history, phase):
        return f"demand-{phase}"

    def fake_exec(history):
        return "design-step"

    res = run_dialogue(card={"f8_pressure_turns": 2, "f8_closing_turns": 1},
                       topic="t", sim_fn=fake_sim, exec_fn=fake_exec,
                       emitter=em, sample_id="b0-t01-id0")
    turn_events = [e for e in em.events if e[0] == "dialogue_turn"]
    # 2 pressure + 1 closing = 3 turns, each turn user+assistant = 2 events
    assert len(turn_events) == 6
    phases = [f["phase"] for _, f in turn_events]
    assert phases.count("pressure") == 4 and phases.count("closing") == 2
    # transcript reconnected and saved
    assert "b0-t01-id0" in em.transcripts
    assert res.transcript_path == "transcripts/b0-t01-id0.md"
