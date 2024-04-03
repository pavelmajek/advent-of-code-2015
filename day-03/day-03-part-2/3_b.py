# Advent of Code 2015, day 3, part 2

with open("../../data/3.txt") as file:
    content = file.read()

santa_position = [0, 0]
robot_position = [0, 0]
houses = {(0, 0)}
for index, item in enumerate(content):
    if index % 2 == 0:
        current_house = santa_position
    else:
        current_house = robot_position

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
