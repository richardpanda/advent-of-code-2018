from collections import defaultdict


def calculate_largest_area(coordinates):
    num_rows, num_cols = (
        max(row for _, row in coordinates) + 1,
        max(col for col, _ in coordinates) + 1,
    )
    idx_to_area, infinite_idxs = defaultdict(int), set()
    for row in range(num_rows):
        for col in range(num_cols):
            distances = [
                (abs(row - r) + abs(col - c), idx)
                for idx, (c, r) in enumerate(coordinates)
            ]
            shortest_distance, idx = min(distances)
            num_shortest_distances = sum(
                distance == shortest_distance for distance, _ in distances
            )
            if num_shortest_distances == 1:
                idx_to_area[idx] += 1
                if row in (0, num_rows - 1) or col in (0, num_cols - 1):
                    infinite_idxs.add(idx)
    return max(area for idx, area in idx_to_area.items() if idx not in infinite_idxs)


def calculate_region_size(coordinates, max_distance):
    num_rows, num_cols = (
        max(row for _, row in coordinates) + 1,
        max(col for col, _ in coordinates) + 1,
    )
    return sum(
        sum(abs(row - r) + abs(col - c) for c, r in coordinates) < max_distance
        for row in range(num_rows)
        for col in range(num_cols)
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        coordinates = [tuple(map(int, line.split(","))) for line in f]
        print(calculate_largest_area(coordinates))
        print(calculate_region_size(coordinates, 10000))

