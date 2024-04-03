# Advent of Code 2015, day 13, part 1

guests = dict()
with open("../../data/13.txt") as file:
    parts = [line.strip().rstrip(".").split() for line in file.readlines()]

names = set()
for part in parts:
    names.add(part[0])

for name in names:
    guests[name] = {}

for part in parts:
    if part[2] == "gain":
        value = int(part[3])
    else:
        value = int(part[3]) * -1
    guests[part[0]][part[-1]] = value


def seat(person, seated, order):
    seated.append(person)
    order.append(person)

    if len(seated) == len(names):
        orders.append(order[:])
    else:
        for name in names:
            if name not in seated:
                seat(name, seated, order)
    seated.pop()
    order.pop()


orders = []
for name in names:
    seat(name, [], [])

happy = []
for order in orders:
    happiness = 0
    for i in range(len(names)):
        a = guests[order[i]][order[(i + 1) % len(names)]]
        b = guests[order[i]][order[(i - 1)]]
        happiness += a + b
    happy.append(happiness)

print(f"Total happiness: {max(happy)}")
