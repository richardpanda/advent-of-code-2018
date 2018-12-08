def calculate_metadata_sum(license):
    def calculate_metadata_sum_dfs():
        num_children, num_metadata = license.pop(), license.pop()
        return sum(calculate_metadata_sum_dfs() for _ in range(num_children)) + sum(
            license.pop() for _ in range(num_metadata)
        )

    license = list(reversed(license))
    return calculate_metadata_sum_dfs()


def calculate_root_value(license):
    def calculate_root_value_dfs():
        num_children, num_metadata = license.pop(), license.pop()
        child_values = [calculate_root_value_dfs() for _ in range(num_children)]
        metadata = [license.pop() for _ in range(num_metadata)]
        return (
            sum(
                child_values[entry - 1] if 1 <= entry <= len(child_values) else 0
                for entry in metadata
            )
            if num_children
            else sum(metadata)
        )

    license = list(reversed(license))
    return calculate_root_value_dfs()


if __name__ == "__main__":
    with open("input.txt") as f:
        license = list(map(int, f.readline().split()))
        print(calculate_metadata_sum(license))
        print(calculate_root_value(license))
