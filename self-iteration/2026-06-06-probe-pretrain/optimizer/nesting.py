from dataclasses import dataclass


@dataclass
class DialogueResult:
    spec_text: str
    transcript: list
    completability: str  # "ok" | "failed"
    transcript_path: str = ""  # observability relative path (empty when no emitter)


def _emit_turn(emitter, transcript, speaker, text, phase, turn_idx, sample_id):
    transcript.append({"speaker": speaker, "text": text})
    if emitter:
        emitter.emit("dialogue_turn", sample_id=sample_id, phase=phase,
                     turn_idx=turn_idx, speaker=speaker,
                     text_excerpt=text[:200])


def run_dialogue(card, topic, sim_fn, exec_fn, emitter=None, sample_id=""):
    """Middle layer of the 3-level nesting: drive the simulator<->executor dialogue. Two-phase F8.
    emitter optional: emit dialogue_turn per turn to the observability stream and save the full transcript."""
    history, transcript = [], []
    # Pressure phase
    for i in range(card["f8_pressure_turns"]):
        u = sim_fn(history, "pressure")
        _emit_turn(emitter, transcript, "user", u, "pressure", i, sample_id)
        a = exec_fn(history + [u])
        _emit_turn(emitter, transcript, "assistant", a, "pressure", i, sample_id)
        history += [u, a]
    # Closing phase: user stops adding new demands; executor runs formated-specs -> load formated-result
    for i in range(card["f8_closing_turns"]):
        u = sim_fn(history, "closing")
        _emit_turn(emitter, transcript, "user", u, "closing", i, sample_id)
        a = exec_fn(history + [u])
        _emit_turn(emitter, transcript, "assistant", a, "closing", i, sample_id)
        history += [u, a]
    spec_text = exec_fn(history + ["FINALIZE: load formated-result"])
    completability = "ok" if spec_text and "design" in spec_text else "failed"
    tpath = ""
    if emitter and sample_id:
        full = "\n".join(f'{t["speaker"]}: {t["text"]}' for t in transcript)
        tpath = emitter.save_transcript(sample_id, full)
    return DialogueResult(spec_text=spec_text, transcript=transcript,
                          completability=completability, transcript_path=tpath)
