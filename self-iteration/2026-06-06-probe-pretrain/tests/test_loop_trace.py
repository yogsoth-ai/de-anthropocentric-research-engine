from optimizer.loop import pretrain


class FakeEmitter:
    def __init__(self):
        self.events = []

    def emit(self, event, **fields):
        self.events.append(event)

    def save_transcript(self, sample_id, text):
        return f"transcripts/{sample_id}.md"


def test_loop_emits_run_and_batch_events():
    def fake_batch(batch_id, weights):
        return {"topic_pass_flags": [True] * 8, "samples": [], "any_rigor_floor": False}

    em = FakeEmitter()
    pretrain(fake_batch_fn=fake_batch, max_safety=10, emitter=em)
    assert em.events.count("run_start") == 1
    assert em.events.count("run_end") == 1
    assert em.events.count("batch_start") == 3
    assert em.events.count("batch_done") == 3
    assert em.events.count("converged") == 1
