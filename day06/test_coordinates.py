from coordinates import calculate_largest_area, calculate_region_size


def test_calculate_largest_area():
    with open("sample.txt") as f:
        coordinates = [tuple(map(int, line.split(","))) for line in f]
        assert calculate_largest_area(coordinates) == 17

    with open("input.txt") as f:
        coordinates = [tuple(map(int, line.split(","))) for line in f]
        assert calculate_largest_area(coordinates) == 3907


def test_calculate_region_size():
    with open("sample.txt") as f:
        coordinates = [tuple(map(int, line.split(","))) for line in f]
        assert calculate_region_size(coordinates, 32) == 16

    with open("input.txt") as f:
        coordinates = [tuple(map(int, line.split(","))) for line in f]
        assert calculate_region_size(coordinates, 10000) == 42036
