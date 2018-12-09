class CircularDoublyLinkedListNode:
    def __init__(self, value, prev=None, _next=None):
        self.value = value
        self.prev = prev
        self.next = _next


def calculate_high_score(num_players, last_marble_points):
    scores = [0] * num_players

    curr_node = CircularDoublyLinkedListNode(0)
    curr_node.prev = curr_node.next = curr_node

    for marble in range(1, last_marble_points + 1):
        player = (marble - 1) % num_players

        if marble % 23 == 0:
            for _ in range(7):
                curr_node = curr_node.prev

            scores[player] += marble + curr_node.value
            curr_node.prev.next, curr_node.next.prev, curr_node = (
                curr_node.next,
                curr_node.prev,
                curr_node.next,
            )
        else:
            curr_node = curr_node.next
            curr_node.next = CircularDoublyLinkedListNode(
                marble, curr_node, curr_node.next
            )
            curr_node.next.next.prev, curr_node = curr_node.next, curr_node.next

    return max(scores)


if __name__ == "__main__":
    with open("input.txt") as f:
        split_str = f.readline().split(" ")
        num_players, last_marble_points = int(split_str[0]), int(split_str[-2])

        print(calculate_high_score(num_players, last_marble_points))
        print(calculate_high_score(num_players, last_marble_points * 100))

