from itertools import cycle


def find_first_duplicate_frequency(changes):
    frequency, nums_visited = 0, set([0])
    for delta in cycle(changes):
        frequency += delta
        if frequency in nums_visited:
            return frequency
        nums_visited.add(frequency)


def test_find_first_frequency():
    assert find_first_duplicate_frequency([1, -1]) == 0
    assert find_first_duplicate_frequency([3, 3, 4, -2, -4]) == 10
    assert find_first_duplicate_frequency([-6, 3, 8, 5, -6]) == 5
    assert find_first_duplicate_frequency([7, 7, -2, -7, -4]) == 14


if __name__ == "__main__":
    with open("input.txt") as f:
        changes = [int(num_str) for num_str in f]
    print(sum(changes))
    print(find_first_duplicate_frequency(changes))
