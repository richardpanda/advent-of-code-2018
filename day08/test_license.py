from license import calculate_metadata_sum, calculate_root_value


def test_calculate_metadata_sum():
    with open("sample.txt") as f:
        license = list(map(int, f.readline().split()))
        assert calculate_metadata_sum(license) == 138

    with open("input.txt") as f:
        license = list(map(int, f.readline().split()))
        assert calculate_metadata_sum(license) == 38567


def test_calculate_root_value():
    with open("sample.txt") as f:
        license = list(map(int, f.readline().split()))
        assert calculate_root_value(license) == 66

    with open("input.txt") as f:
        license = list(map(int, f.readline().split()))
        assert calculate_root_value(license) == 24453

