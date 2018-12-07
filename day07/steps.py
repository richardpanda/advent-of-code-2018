from heapq import heapify, heappop, heappush
from collections import defaultdict


def compute_step_order(steps):
    step_to_next_steps = defaultdict(list)
    steps_to_num_requirements = defaultdict(int)
    for curr_step in steps:
        _, step, *_, next_step, _, _ = curr_step.split(" ")
        step_to_next_steps[step].append(next_step)
        steps_to_num_requirements[next_step] += 1
    available_steps = [
        step for step in step_to_next_steps if steps_to_num_requirements[step] == 0
    ]
    heapify(available_steps)
    step_order = []
    while available_steps:
        step = heappop(available_steps)
        step_order.append(step)
        for next_step in step_to_next_steps[step]:
            steps_to_num_requirements[next_step] -= 1
            if steps_to_num_requirements[next_step] == 0:
                heappush(available_steps, next_step)
    return "".join(step_order)


def calculate_completion_time(steps, step_duration, num_workers):
    step_to_next_steps = defaultdict(list)
    steps_to_num_requirements = defaultdict(int)
    for step in steps:
        _, u, *_, v, _, _ = step.split(" ")
        step_to_next_steps[u].append(v)
        steps_to_num_requirements[v] += 1
    available_steps = [
        step for step in step_to_next_steps if steps_to_num_requirements[step] == 0
    ]
    heapify(available_steps)
    processing_steps, completion_time = [], 0
    while available_steps or processing_steps:
        while available_steps and len(processing_steps) < num_workers:
            step = heappop(available_steps)
            end_time = completion_time + ord(step) - 64 + step_duration
            heappush(processing_steps, (end_time, step))
        completion_time, step = heappop(processing_steps)
        for next_step in step_to_next_steps[step]:
            steps_to_num_requirements[next_step] -= 1
            if steps_to_num_requirements[next_step] == 0:
                heappush(available_steps, next_step)
    return completion_time


if __name__ == "__main__":
    with open("input.txt") as f:
        steps = list(f)
        print(compute_step_order(steps))
        print(calculate_completion_time(steps, 60, 5))

