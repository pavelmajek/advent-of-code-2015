# Advent of Code 2015, day 14, part 1

deers = []
with open("../../data/14.txt") as file:
    for line in file.readlines():
        deer = []
        parts = line.strip().rstrip(".").split()
        deer.extend([parts[0], int(parts[3]), int(parts[6]), int(parts[-2])])
        deers.append(deer)

results = []
def race(time, deer):
    block = time // (deer[2] + deer[3])

    if (time % (deer[2] + deer[3])) > deer[2]:
        rest = deer[1] * deer[2]
    else:
        rest = (time % (deer[2] + deer[3])) * deer[1]
    distance = block * deer[1] * deer[2] + rest
    results.append(distance)

for deer in deers:
    race(2503, deer)

print(f"Distance: {max(results)}")
