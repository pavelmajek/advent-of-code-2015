# Advent of Code 2015, day 24, part 1

import itertools
from functools import reduce

with open("../../data/24.txt") as file:
    presents = [int(line.strip()) for line in file.readlines()]

results = []
n = 5
while True:
    n_combinations = itertools.combinations(presents, n)
    for combination in n_combinations:
        if sum(combination) == sum(presents) / 3:
            difference = [item for item in presents if item not in combination]

            for i in range(n, len(difference) - n):
                second_combinations = itertools.combinations(difference, i)
                for second_comb in second_combinations:
                    if sum(second_comb) == sum(presents) / 3:
                        quant = reduce(lambda x, y: x * y, combination)
                        results.append(quant)
    if not results:
        n += 1
    else:
        break

print(f"Entanglement: {min(results)}")
