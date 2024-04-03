# Advent of Code 2015, day 7, part 2

import copy

with open("../../data/7.txt") as file:
    equation_dict = {}
    for line in file.readlines():
        line_equation = line.strip().split(" -> ")
        equation_dict.update({line_equation[1]: line_equation[0].split()})

results = {}


def find_value(x, results, equation_dict):
    if x.isdigit():
        return int(x)

    if x not in results:
        eq_parts = equation_dict[x]

        if len(eq_parts) == 1:
            result = find_value(eq_parts[0], results, equation_dict)
        else:
            if eq_parts[-2] == "NOT":
                result = ~find_value(eq_parts[-1], results, equation_dict) & 0xffff
            elif eq_parts[-2] == "AND":
                result = find_value(eq_parts[0], results, equation_dict) & find_value(eq_parts[2], results, equation_dict)
            elif eq_parts[-2] == "OR":
                result = find_value(eq_parts[0], results, equation_dict) | find_value(eq_parts[2], results, equation_dict)
            elif eq_parts[-2] == "RSHIFT":
                result = find_value(eq_parts[0], results, equation_dict) >> find_value(eq_parts[2], results, equation_dict)
            elif eq_parts[-2] == "LSHIFT":
                result = find_value(eq_parts[0], results, equation_dict) << find_value(eq_parts[2], results, equation_dict)

        results[x] = result
    return results[x]


value = find_value("a", results, equation_dict)
second_dict = copy.deepcopy(equation_dict)
second_dict["b"] = [str(value)]

results2 = {}

print(find_value("a", results2, second_dict))
