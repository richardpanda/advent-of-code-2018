from guards import (
    find_most_consistently_asleep_guard,
    find_most_frequently_asleep_guard,
)


def test_find_most_frequently_asleep_guard():
    with open("sample.txt") as f:
        assert find_most_consistently_asleep_guard(list(f)) == 4455

    with open("input.txt") as f:
        assert find_most_consistently_asleep_guard(list(f)) == 96951


def test_find_sleepy_guard():
    with open("sample.txt") as f:
        assert find_most_frequently_asleep_guard(list(f)) == 240

    with open("input.txt") as f:
        assert find_most_frequently_asleep_guard(list(f)) == 131469
