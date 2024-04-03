# Advent of Code 2015, day 1, part 2

with open("../../data/1.txt") as file:
    content = file.read()

floor = 0
for index, char in enumerate(content, 1):
    floor += 1 if char == "(" else -1
    if floor == -1:
        print(f"Position: {index}")
        break
    index += 1
