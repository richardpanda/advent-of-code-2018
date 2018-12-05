from polymer import compute_shortest_length_polymer, count_units


def test_count_units():
    assert count_units("aA") == 0
    assert count_units("abBA") == 0
    assert count_units("abAB") == 4
    assert count_units("aabAAB") == 6
    assert count_units("dabAcCaCBAcCcaDA") == 10

    with open("input.txt") as f:
        assert count_units(f.readline().strip()) == 10598


def test_compute_shortest_length_polymer():
    assert compute_shortest_length_polymer("dabAcCaCBAcCcaDA") == 4

    with open("input.txt") as f:
        assert compute_shortest_length_polymer(f.readline().strip()) == 5312
