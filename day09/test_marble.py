from marble import calculate_high_score


def test_calculate_high_score():
    assert calculate_high_score(9, 23) == 32
    assert calculate_high_score(10, 1618) == 8317
    assert calculate_high_score(13, 7999) == 146373
    assert calculate_high_score(17, 1104) == 2764
    assert calculate_high_score(21, 6111) == 54718
    assert calculate_high_score(30, 5807) == 37305

    with open("input.txt") as f:
        split_str = f.readline().split(" ")
        num_players, last_marble_points = int(split_str[0]), int(split_str[-2])

        assert calculate_high_score(num_players, last_marble_points) == 398048
        assert calculate_high_score(num_players, last_marble_points * 100) == 3180373421
