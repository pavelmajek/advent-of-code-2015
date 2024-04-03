# Advent of Code 2015, day 12, part 2

import json


def sum_non_reds(s):
    if isinstance(s, int):
        return s
    elif isinstance(s, list):
        return sum(sum_non_reds(i) for i in s)
    elif isinstance(s, dict):
        if "red" in s.values():
            return 0
        else:
            return sum(sum_non_reds(i) for i in s.values())

    return 0


with open("../../data/12.txt") as file:
    print(f"Sum: {sum_non_reds(json.load(file))}")
