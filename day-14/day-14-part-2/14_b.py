# Advent of Code 2015, day 14, part 2

deers = []
with open("../../data/14.txt") as file:
    for line in file.readlines():
        deer = []
        parts = line.strip().rstrip(".").split()
        deer.extend([parts[0], int(parts[3]), int(parts[6]), int(parts[-2])])
        deers.append(deer)

names = [deer[0] for deer in deers]
dict_deers = dict()
for name in names:
    dict_deers[name] = 0


def race(time, deer):
    result = []
    block = time // (deer[2] + deer[3])

    if (time % (deer[2] + deer[3])) > deer[2]:
        rest = deer[1] * deer[2]
    else:
        rest = (time % (deer[2] + deer[3])) * deer[1]
    distance = block * deer[1] * deer[2] + rest
    result.extend([deer[0], distance])
    results.append(result)


for i in range(1, 2504):
    results = []
    for deer in deers:
        race(i, deer)
    distance_values = [item[1] for item in results]
    max_value = max(distance_values)

    for item in results:
        if item[1] == max_value:
            dict_deers[item[0]] += 1

print(f"Distance: {max([i for i in dict_deers.values()])}")
