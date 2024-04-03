# Advent of Code 2015, day 12, part 1

import re

with open("../../data/12.txt") as file:
    content = file.read().strip()

numbers = re.findall(r"-?\d+", content)

total = 0
for number in numbers:
    total += int(number)

print(f"Sum: {total}")
