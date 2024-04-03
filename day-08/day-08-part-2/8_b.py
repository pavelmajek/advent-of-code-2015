# Advent of Code 2015, day 8, part 2

import re
spec_char = 0

with open("../../data/8.txt") as file:
    for line in file.readlines():
        char1 = line.count('"')
        char2 = len(re.findall(r"\\", line))
        spec_char += char1 + char2 + 2

print(f"Characters: {spec_char}")
