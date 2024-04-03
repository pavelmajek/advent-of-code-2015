# Advent of Code 2015, day 5, part 1

import re

with open("../../data/5.txt") as file:
    content = [line.rstrip() for line in file.readlines()]

count = 0
for string in content:
    if (re.search(r"[aeiou].*[aeiou].*[aeiou]", string, re.IGNORECASE) and
            re.search(r"([a-zA-Z])\1", string) and
            not re.search(r"ab|cd|pq|xy", string)):
        count += 1

print(f"Nice strings: {count}")
