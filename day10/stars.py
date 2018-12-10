import re

from collections import namedtuple

INTEGER_REGEX = re.compile("-?\d+")
Star = namedtuple("Star", "x y dx dy")


class Stars:
    def __init__(self, star_info):
        self._stars = [
            Star(*list(map(int, INTEGER_REGEX.findall(s)))) for s in star_info
        ]

    def _compute_max_x_at_secs(self, secs):
        return max(star.x + (star.dx * secs) for star in self._stars)

    def compute_message_time(self):
        secs = 0
        while self._compute_max_x_at_secs(secs) > self._compute_max_x_at_secs(secs + 1):
            secs += 1
        return secs

    def print_at_secs(self, secs):
        positions = set(
            (star.x + (star.dx * secs), star.y + (star.dy * secs))
            for star in self._stars
        )
        min_x, max_x = min(x for x, _ in positions), max(x for x, _ in positions)
        min_y, max_y = min(y for _, y in positions), max(y for _, y in positions)
        for y in range(min_y, max_y + 1):
            print(
                "".join(
                    "#" if (x, y) in positions else "." for x in range(min_x, max_x + 1)
                )
            )


if __name__ == "__main__":
    with open("input.txt") as f:
        stars = Stars(list(f))

    secs = stars.compute_message_time()
    stars.print_at_secs(secs)
    print(secs)

