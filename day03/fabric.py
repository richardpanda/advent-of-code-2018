from collections import namedtuple

FABRIC_SIZE = 1000
Rectangle = namedtuple("Rectangle", "id col row width height")


def compute_overlap_area(claims):
    rectangles = [parse_claim(claim) for claim in claims]
    fabric = generate_fabric(rectangles)
    return sum(
        fabric[i][j] >= 2 for i in range(FABRIC_SIZE) for j in range(FABRIC_SIZE)
    )


def find_disjoint_id(claims):
    rectangles = [parse_claim(claim) for claim in claims]
    fabric = generate_fabric(rectangles)
    return next(
        rectangle.id for rectangle in rectangles if is_disjoint(fabric, rectangle)
    )


def generate_fabric(rectangles):
    fabric = [[0] * FABRIC_SIZE for _ in range(FABRIC_SIZE)]
    for _, col, row, width, height in rectangles:
        for i in range(height):
            for j in range(width):
                fabric[row + i][col + j] += 1
    return fabric


def is_disjoint(fabric, rectangle):
    _, col, row, width, height = rectangle
    return all(
        fabric[row + i][col + j] == 1 for i in range(height) for j in range(width)
    )


def parse_claim(claim):
    _id, _, start, size = claim.split()
    _id = int(_id[1:])
    start = start[:-1]
    col, row = map(int, start.split(","))
    width, height = map(int, size.split("x"))
    return Rectangle(_id, col, row, width, height)


if __name__ == "__main__":
    with open("input.txt") as f:
        claims = list(f)
    print(compute_overlap_area(claims))
    print(find_disjoint_id(claims))
