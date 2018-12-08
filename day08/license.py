def calculate_metadata_sum(license):
    def calculate_metadata_sum_dfs():
        nonlocal idx
        num_children, num_metadata = license[idx : idx + 2]
        idx += 2

        if num_children == 0:
            metadata_sum = sum(license[idx : idx + num_metadata])
            idx += num_metadata
            return metadata_sum

        metadata_sum = sum(calculate_metadata_sum_dfs() for _ in range(num_children))
        metadata_sum += sum(license[idx : idx + num_metadata])
        idx += num_metadata

        return metadata_sum

    idx = 0
    return calculate_metadata_sum_dfs()


def calculate_root_value(license):
    def calculate_root_value_dfs():
        nonlocal idx
        num_children, num_metadata = license[idx : idx + 2]
        idx += 2

        if num_children == 0:
            metadata_sum = sum(license[idx : idx + num_metadata])
            idx += num_metadata
            return metadata_sum

        child_values = [calculate_root_value_dfs() for _ in range(num_children)]
        metadata = license[idx : idx + num_metadata]
        idx += num_metadata

        return sum(
            child_values[entry - 1] if 1 <= entry <= len(child_values) else 0
            for entry in metadata
        )

    idx = 0
    return calculate_root_value_dfs()


if __name__ == "__main__":
    with open("input.txt") as f:
        license = list(map(int, f.readline().split()))
        print(calculate_metadata_sum(license))
        print(calculate_root_value(license))
