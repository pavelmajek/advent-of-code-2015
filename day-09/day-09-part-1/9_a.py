# Advent of Code 2015, day 9, part 1

from collections import defaultdict

dict_cities = defaultdict(list)

with open("../../data/9.txt") as file:
    for line in file.readlines():
        command = line.strip().split()
        dict_cities[command[0]].append((command[2], command[4]))
        dict_cities[command[2]].append((command[0], command[4]))


set_cities = set(dict_cities.keys())

def find_way(start, visited, path):
    visited.append(start)
    path.append(start)

    if len(visited) == len(set_cities):
        paths.append(path[:])
    else:
        for item in dict_cities[start]:
            if item[0] not in visited:
                find_way(item[0], visited, path)

    visited.pop()
    path.pop()

paths = []
for i in set_cities:
    find_way(i, [], [])

distances = []
for path in paths:
    distance = 0
    for i in range(len(set_cities) - 1):
        for j in dict_cities[path[i]]:
            if j[0] == path[i + 1]:
                distance += int(j[1])
    distances.append(distance)

print(f"Shortest route: {min(distances)}")
