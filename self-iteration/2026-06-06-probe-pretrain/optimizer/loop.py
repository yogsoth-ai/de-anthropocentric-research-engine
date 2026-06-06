from optimizer.gate import batch_pass_ratio, converged


def pretrain(fake_batch_fn=None, run_batch_fn=None, weights=None,
             max_safety=1000, emitter=None, n=6, m=8):
    """PT6 main loop. No iteration cap (max_safety only guards runaway); stops only on the convergence gate.
    Freeze after convergence (caller persists). Each batch's samples accumulate into the dataset (pretrain-result-as-dataset).
    emitter optional: emit run_start/batch_start/batch_done/converged/run_end observability events."""
    run = fake_batch_fn or run_batch_fn
    if emitter:
        emitter.emit("run_start", n=n, m=m)
    ratios, all_samples = [], []
    i = 0
    while i < max_safety:
        batch_id = f"batch{i}"
        if emitter:
            emitter.emit("batch_start", batch_id=batch_id)
        out = run(batch_id, weights)
        all_samples.extend(out.get("samples", []))
        r = batch_pass_ratio(out["topic_pass_flags"])
        ratios.append(r)
        i += 1
        if emitter:
            emitter.emit("batch_done", batch_id=batch_id, pass_ratio=r,
                         topic_pass_flags=out["topic_pass_flags"],
                         recent_ratios=ratios[-3:],
                         any_rigor_floor=out.get("any_rigor_floor", False))
        if converged(ratios):
            if emitter:
                emitter.emit("converged", num_batches=i, ratios=ratios)
                emitter.emit("run_end", converged=True, total_samples=len(all_samples))
            return {"converged": True, "num_batches": i, "ratios": ratios,
                    "samples": all_samples}
    if emitter:
        emitter.emit("run_end", converged=False, total_samples=len(all_samples))
    return {"converged": False, "num_batches": i, "ratios": ratios,
            "samples": all_samples}
