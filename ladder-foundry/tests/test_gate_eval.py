import subprocess, sys


def gate(*args):
    return subprocess.check_output([sys.executable, "scripts/gate_eval.py", *args],
        text=True).strip()


def test_topic_three_way_and():
    assert gate("topic", "--fidelity-rate", "0.90", "--mono", "true", "--endpoint", "true") == "true"
    assert gate("topic", "--fidelity-rate", "0.83", "--mono", "true", "--endpoint", "true") == "false"
    assert gate("topic", "--fidelity-rate", "0.95", "--mono", "false", "--endpoint", "true") == "false"
    assert gate("topic", "--fidelity-rate", "0.95", "--mono", "true", "--endpoint", "false") == "false"


def test_batch_hard_integer_line():
    assert gate("batch", "--flags", "true,true,true,true,true,true,true,false") == "true"   # 7/8
    assert gate("batch", "--flags", "true,true,true,true,true,true,false,false") == "false"  # 6/8


def test_converged_last_three():
    assert gate("converged", "--recent", "0.625,0.875,0.875,0.875") == "true"   # last 3 >= 0.80
    assert gate("converged", "--recent", "0.875,0.75,0.875") == "false"          # break in middle
