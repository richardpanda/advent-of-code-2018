from fabric import Rectangle, compute_overlap_area, find_disjoint_id, parse_claim


def test_compute_overlap_area():
    assert (
        compute_overlap_area(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]) == 4
    )

    with open("input.txt") as f:
        assert compute_overlap_area(list(f)) == 118539


def test_find_disjoint_id():
    assert find_disjoint_id(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]) == 3

    with open("input.txt") as f:
        assert find_disjoint_id(list(f)) == 1270


def test_parse_claim():
    assert parse_claim("#1 @ 1,3: 4x4") == Rectangle(1, 1, 3, 4, 4)
