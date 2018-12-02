def calculate_checksum(ids):
    twos = threes = 0
    for _id in ids:
        char_count = [0] * 26
        for char in _id:
            char_count[ord(char) - 97] += 1
        if 2 in char_count:
            twos += 1
        if 3 in char_count:
            threes += 1
    return twos * threes


def search_similar_ids(ids):
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            if sum(c1 != c2 for c1, c2 in zip(ids[i], ids[j])) == 1:
                return ids[i], ids[j]
    return "", ""


def extract_common_str_from_similar_ids(ids):
    id1, id2 = search_similar_ids(ids)
    return "".join(c1 for c1, c2 in zip(id1, id2) if c1 == c2)


def test_extract_common_str_from_similar_ids():
    ids = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
    assert extract_common_str_from_similar_ids(ids) == "fgij"


if __name__ == "__main__":
    with open("input.txt") as f:
        ids = [str.strip(_id) for _id in f]
    print(calculate_checksum(ids))
    print(extract_common_str_from_similar_ids(ids))
