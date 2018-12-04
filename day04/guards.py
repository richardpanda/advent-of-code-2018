from collections import defaultdict

NUM_MINUTES = 60


def compute_guard_and_minute_product(logs, aggregate_func):
    guard_to_shift = generate_guard_to_shift(logs)
    _, guard = max(
        (aggregate_func(shift), guard) for guard, shift in guard_to_shift.items()
    )
    most_asleep_minute = guard_to_shift[guard].index(max(guard_to_shift[guard]))
    return guard * most_asleep_minute


def find_most_consistently_asleep_guard(logs):
    return compute_guard_and_minute_product(logs, max)


def find_most_frequently_asleep_guard(logs):
    return compute_guard_and_minute_product(logs, sum)


def generate_guard_to_shift(logs):
    logs = sorted(logs)

    begin_idxs = [idx for idx, log in enumerate(logs) if "begins" in log] + [len(logs)]
    shifts = [
        logs[begin_idxs[i] : begin_idxs[i + 1]] for i in range(len(begin_idxs) - 1)
    ]

    guard_to_shift = defaultdict(lambda: [0] * NUM_MINUTES)
    for shift in shifts:
        guard = int(shift[0].split()[3][1:])
        for i in range(1, len(shift), 2):
            start, end = map(
                lambda s: int(s.split(":")[1][:2]), [shift[i], shift[i + 1]]
            )
            for j in range(start, end):
                guard_to_shift[guard][j] += 1

    return guard_to_shift


if __name__ == "__main__":
    with open("input.txt") as f:
        logs = list(f)
        print(find_most_frequently_asleep_guard(logs))
        print(find_most_consistently_asleep_guard(logs))

