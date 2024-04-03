# Advent of Code 2015, day 2, part 2

with open("../../data/2.txt") as file:
    content = [list(map(int, line.strip().split("x"))) for line in file.readlines()]

length = 0
for item in content:
    a, b, c = sorted(item)
    length += 2 * (a + b) + a*b*c

print(f"Length: {length}")
