# Advent of Code 2015, day 7, part 1

with open("../../data/7.txt") as file:
    equation_dict = {}
    for line in file.readlines():
        line_equation = line.strip().split(" -> ")
        equation_dict.update({line_equation[1]: line_equation[0].split()})

results = {}


def find_value(x):
    if x.isdigit():
        return int(x)

    if x not in results:
        eq_parts = equation_dict[x]

        if len(eq_parts) == 1:
            result = find_value(eq_parts[0])
        else:
            if eq_parts[-2] == "NOT":
                result = ~find_value(eq_parts[-1]) & 0xffff
            elif eq_parts[-2] == "AND":
                result = find_value(eq_parts[0]) & find_value(eq_parts[2])
            elif eq_parts[-2] == "OR":
                result = find_value(eq_parts[0]) | find_value(eq_parts[2])
            elif eq_parts[-2] == "RSHIFT":
                result = find_value(eq_parts[0]) >> find_value(eq_parts[2])
            elif eq_parts[-2] == "LSHIFT":
                result = find_value(eq_parts[0]) << find_value(eq_parts[2])

        results[x] = result
    return results[x]


print(f"Signal: {find_value("a")}")
