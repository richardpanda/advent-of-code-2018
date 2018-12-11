GRID_LENGTH, SQUARE_LENGTH = 300, 3


def calculate_power_level(x, y, serial_number):
    rack_id = x + 10
    return (((rack_id * y + serial_number) * rack_id) % 1000) // 100 - 5


def calculate_max_power_with_fixed_square(serial_number):
    grid = [
        [calculate_power_level(x, y, serial_number) for x in range(1, GRID_LENGTH + 1)]
        for y in range(1, GRID_LENGTH + 1)
    ]

    max_power_x = max_power_y = 0
    max_power_so_far = float("-inf")

    for y in range(GRID_LENGTH - SQUARE_LENGTH):
        for x in range(GRID_LENGTH - SQUARE_LENGTH):
            power = sum(
                grid[y + i][x + j]
                for i in range(SQUARE_LENGTH)
                for j in range(SQUARE_LENGTH)
            )
            if power > max_power_so_far:
                max_power_so_far = power
                max_power_x, max_power_y = x + 1, y + 1

    return f"{max_power_x},{max_power_y}"


def calculate_max_power_with_any_square(serial_number):
    grid = [
        [calculate_power_level(x, y, serial_number) for x in range(1, GRID_LENGTH + 1)]
        for y in range(1, GRID_LENGTH + 1)
    ]

    prefix_sums = [[0] * (GRID_LENGTH + 1) for _ in range(GRID_LENGTH + 1)]
    for i in range(GRID_LENGTH):
        for j in range(GRID_LENGTH):
            prefix_sums[i + 1][j + 1] = (
                prefix_sums[i + 1][j]
                + prefix_sums[i][j + 1]
                + grid[i][j]
                - prefix_sums[i][j]
            )

    max_power_x = max_power_y = 0
    max_power_square_size = 0
    max_power_so_far = float("-inf")

    for top_left_y in range(GRID_LENGTH):
        for top_left_x in range(GRID_LENGTH):
            bottom_right_x, bottom_right_y = top_left_x, top_left_y
            while bottom_right_x < GRID_LENGTH and bottom_right_y < GRID_LENGTH:
                power = (
                    prefix_sums[bottom_right_y + 1][bottom_right_x + 1]
                    - prefix_sums[top_left_y][bottom_right_x + 1]
                    - prefix_sums[bottom_right_y + 1][top_left_x]
                    + prefix_sums[top_left_y][top_left_x]
                )
                if power > max_power_so_far:
                    max_power_so_far = power
                    max_power_x, max_power_y = top_left_x + 1, top_left_y + 1
                    max_power_square_size = bottom_right_x - top_left_x + 1

                bottom_right_x, bottom_right_y = bottom_right_x + 1, bottom_right_y + 1

    return f"{max_power_x},{max_power_y},{max_power_square_size}"


if __name__ == "__main__":
    print(calculate_max_power_with_fixed_square(7400))
    print(calculate_max_power_with_any_square(7400))

