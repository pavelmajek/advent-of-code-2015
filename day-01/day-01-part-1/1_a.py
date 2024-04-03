# Advent of Code 2015, day 1, part 1

with open("../../data/1.txt") as file:
    content = file.read()

print(f"Floor: {content.count("(") - content.count(")")}")
