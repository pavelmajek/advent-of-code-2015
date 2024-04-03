# Advent of Code 2015, day 16, part 1

template = {"children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1}
with open("../../data/16.txt") as file:
    for line in file.readlines():
        parts = line.strip().split()
        if template[parts[2].rstrip(":")] == int(parts[3].rstrip(",")) and template[parts[4].rstrip(":")] == int(parts[5].rstrip(",")) and template[parts[6].rstrip(":")] == int(parts[7]):
            print(f"Number: {parts[1].rstrip(":")}")
