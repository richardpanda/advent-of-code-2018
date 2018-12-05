def compute_shortest_length_polymer(polymer):
    polymer_letters = set(letter.lower() for letter in polymer)
    return min(
        count_units(polymer.replace(letter, "").replace(letter.upper(), ""))
        for letter in polymer_letters
    )


def count_units(polymer):
    units = []
    for unit in polymer:
        if units and is_reactive(unit, units[-1]):
            units.pop()
        else:
            units.append(unit)
    return len(units)


def is_reactive(c1, c2):
    return c1.swapcase() == c2


if __name__ == "__main__":
    with open("input.txt") as f:
        polymer = f.readline().strip()
        print(count_units(polymer))
        print(compute_shortest_length_polymer(polymer))
