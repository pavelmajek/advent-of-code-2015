# Advent of Code 2015, day 5, part 2

import re

with open("../../data/5.txt") as file:
    content = [line.rstrip() for line in file.readlines()]

count = 0
for string in content:
    if (re.search(r"([a-zA-Z]{2}).*?\1", string) and
            re.search(r"([a-zA-Z]).\1", string)):
        count += 1

print(f"Nice strings: {count}")
