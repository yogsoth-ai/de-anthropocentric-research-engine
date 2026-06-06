FIDELITY_BATCH_MIN = 0.90
TOPIC_PASS_RATIO_MIN = 0.80
CONVERGE_CONSECUTIVE = 3


def topic_passes(fidelity_rate, monotonicity_pass, endpoint_separation_pass):
    """A topic passes the gate = fidelity >= 90% AND monotonic AND endpoint separation (sec 4.3)."""
    return (fidelity_rate >= FIDELITY_BATCH_MIN
            and monotonicity_pass and endpoint_separation_pass)


def batch_pass_ratio(topic_pass_flags):
    """Fraction of topics in a batch that passed the gate."""
    return sum(1 for x in topic_pass_flags if x) / len(topic_pass_flags)


def converged(recent_ratios):
    """3 consecutive batches each >= 0.8 -> converged (sec 9). No iteration cap."""
    if len(recent_ratios) < CONVERGE_CONSECUTIVE:
        return False
    last = recent_ratios[-CONVERGE_CONSECUTIVE:]
    return all(r >= TOPIC_PASS_RATIO_MIN for r in last)
