# Advent of Code 2015, day 2, part 1

with open("../../data/2.txt") as file:
    content = [list(map(int, line.strip().split("x"))) for line in file.readlines()]

area = 0
for item in content:
    l, w, h = item
    area += 2 * (l*w + w*h + h*l) + min(l*w, w*h, h*l)

print(f"Area: {area}")
