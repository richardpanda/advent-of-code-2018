from steps import compute_step_order, calculate_completion_time


def test_compute_step_order():
    with open("sample.txt") as f:
        assert compute_step_order(list(f)) == "CABDFE"

    with open("input.txt") as f:
        assert compute_step_order(list(f)) == "FHMEQGIRSXNWZBCLOTUADJPKVY"


def test_calculate_completion_time():
    with open("sample.txt") as f:
        assert calculate_completion_time(list(f), 0, 2) == 15

    with open("input.txt") as f:
        assert calculate_completion_time(list(f), 60, 5) == 917

