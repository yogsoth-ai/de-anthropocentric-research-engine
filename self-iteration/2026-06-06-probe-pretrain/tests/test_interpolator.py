from generator.interpolator import ladder_levels, rung_count_default


def test_n6_maps_to_monotone_levels():
    levels = ladder_levels(n=6)  # list of dict per rung
    assert len(levels) == 6
    a1 = [r["A1"] for r in levels]
    # monotonically non-decreasing level numbers L0..L4 (pressure non-increasing)
    nums = [int(x[1]) for x in a1]
    assert nums == sorted(nums)
    assert nums[0] == 0 and nums[-1] == 4  # endpoints reach L0/L4


def test_n6_collapse_detected():
    # n=6 mapped to 5 levels must have an adjacent collapse (round(t*4))
    levels = ladder_levels(n=6)
    nums = [int(r["A1"][1]) for r in levels]
    # at least one adjacent pair is equal (to be separated by the secondary knob)
    assert any(nums[i] == nums[i + 1] for i in range(len(nums) - 1))


def test_rung_count_default_is_6():
    assert rung_count_default() == 6
