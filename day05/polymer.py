def compute_shortest_length_polymer(polymer):
    polymer_letters = set(letter.lower() for letter in polymer)
    return min(
        count_units(polymer.replace(letter, "").replace(letter.upper(), ""))
        for letter in polymer_letters
    )


def count_units(polymer):
    num_units, stack = len(polymer), []
    for i in range(len(polymer)):
        if stack and is_reactive(polymer[i], polymer[stack[-1]]):
            num_units -= 2
            stack.pop()
        else:
            stack.append(i)
    return num_units


def is_reactive(c1, c2):
    return (
        (c1.islower() and c2.isupper()) or (c1.isupper() and c2.islower())
    ) and c1.lower() == c2.lower()


if __name__ == "__main__":
    with open("input.txt") as f:
        polymer = f.readline().strip()
        print(count_units(polymer))
        print(compute_shortest_length_polymer(polymer))
