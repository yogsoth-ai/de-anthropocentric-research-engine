from generator.interpolator import ladder_levels, rung_count_default


def test_n6_maps_to_monotone_levels():
    levels = ladder_levels(n=6)  # list of dict per rung
    assert len(levels) == 6
    a1 = [r["A1"] for r in levels]
    # 单调非降的等级编号 L0..L4（压力非增）
    nums = [int(x[1]) for x in a1]
    assert nums == sorted(nums)
    assert nums[0] == 0 and nums[-1] == 4  # 端点到 L0/L4


def test_n6_collapse_detected():
    # n=6 映射到 5 级必有相邻塌档（round(t*4)）
    levels = ladder_levels(n=6)
    nums = [int(r["A1"][1]) for r in levels]
    # 至少存在一处相邻相等（待二级旋钮拉开）
    assert any(nums[i] == nums[i + 1] for i in range(len(nums) - 1))


def test_rung_count_default_is_6():
    assert rung_count_default() == 6
