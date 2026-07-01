import pytest
from generator.leak_audit import leak_audit, LeakHit


def test_clean_text_passes():
    assert leak_audit("The supervisor pushed for more operational substance.") is None


def test_denies_check_signature():
    for leak in [
        "this maps to the R7 precision check",
        "primitive P3 fires here",
        "looks like a pseudo-good sample",
        "the novel-good engine generated it",
        "detection signature matched",
    ]:
        with pytest.raises(LeakHit):
            leak_audit(leak)


def test_substring_false_positive_avoided():
    # 'P3' as a check id must deny, but 'P3' inside an unrelated word must not.
    assert leak_audit("the MP3 file format") is None


def test_out_of_range_ids_not_denied():
    # R19+/P15+ are not real check ids (R1-R18, P1-P14 only) -> must not trip the backstop
    assert leak_audit("see R25 and P40 in the appendix") is None
    # but in-range ids still deny
    with pytest.raises(LeakHit):
        leak_audit("the R7 check")
    with pytest.raises(LeakHit):
        leak_audit("primitive P14 here")
