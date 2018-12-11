from fuel import (
    calculate_power_level,
    calculate_max_power_with_fixed_square,
    calculate_max_power_with_any_square,
)


def test_calculate_power_level():
    assert calculate_power_level(3, 5, 8) == 4
    assert calculate_power_level(122, 79, 57) == -5
    assert calculate_power_level(217, 196, 39) == 0
    assert calculate_power_level(101, 153, 71) == 4


def test_calculate_max_power_with_fixed_square():
    assert calculate_max_power_with_fixed_square(18) == "33,45"
    assert calculate_max_power_with_fixed_square(42) == "21,61"
    assert calculate_max_power_with_fixed_square(7400) == "34,72"


def test_calculate_max_power_with_any_square():
    assert calculate_max_power_with_any_square(18) == "90,269,16"
    assert calculate_max_power_with_any_square(42) == "232,251,12"
    assert calculate_max_power_with_any_square(7400) == "233,187,13"
