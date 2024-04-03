# Advent of Code 2015, day 3, part 1

with open("../../data/3.txt") as file:
    content = file.read()

current_house = [0, 0]
houses = {(0, 0)}
for item in content:
    if item == "^":
        current_house[1] += 1
    elif item == "v":
        current_house[1] -= 1
    elif item == ">":
        current_house[0] += 1
    elif item == "<":
        current_house[0] -= 1
    houses.add(tuple(current_house))

print(f"Houses: {len(houses)}")
