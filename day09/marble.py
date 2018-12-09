from collections import deque


def calculate_high_score(num_players, last_marble_points):
    scores = [0] * num_players
    circle = deque([0])

    for marble in range(1, last_marble_points + 1):
        player = (marble - 1) % num_players

        if marble % 23 == 0:
            circle.rotate(7)
            scores[player] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores)


if __name__ == "__main__":
    with open("input.txt") as f:
        split_str = f.readline().split(" ")
        num_players, last_marble_points = int(split_str[0]), int(split_str[-2])

        print(calculate_high_score(num_players, last_marble_points))
        print(calculate_high_score(num_players, last_marble_points * 100))

