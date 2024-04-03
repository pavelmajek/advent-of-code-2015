# Advent of Code 2015, day 16, part 2

template = {"children": [3],
            "cats": range(8, 100),
            "samoyeds": [2],
            "pomeranians": range(0, 3),
            "akitas": [0],
            "vizslas": [0],
            "goldfish": range(0, 5),
            "trees": range(4, 100),
            "cars": [2],
            "perfumes": [1]}

with open("../../data/16.txt") as file:
    for line in file.readlines():
        parts = line.strip().split()
        if int(parts[3].rstrip(",")) in template[parts[2].rstrip(":")] and int(parts[5].rstrip(",")) in template[parts[4].rstrip(":")] and int(parts[7]) in template[parts[6].rstrip(":")]:
            print(f"Aunt: {parts[1].rstrip(":")}")
