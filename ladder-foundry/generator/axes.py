"""L3 ① — pure read of the axis_prose weight. Source never moves; training
edits w["axis_prose"] (DATA), proven by test_revise_changes_data_not_source.
"""


def level_text(w, axis, level):
    return w["axis_prose"][axis][level]
