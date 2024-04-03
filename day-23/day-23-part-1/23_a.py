# Advent of Code 2015, day 23, part 1

with open("../../data/23.txt") as file:
    instructions = [line.strip().split() for line in file.readlines()]

reg = {"a": 0, "b": 0}
i = 0
while i < len(instructions):
    if instructions[i][0] == "hlf":
        reg[instructions[i][1]] = reg[instructions[i][1]] // 2
        i += 1

    elif instructions[i][0] == "tpl":
        reg[instructions[i][1]] = reg[instructions[i][1]] * 3
        i += 1

    elif instructions[i][0] == "inc":
        reg[instructions[i][1]] += 1
        i += 1

    elif instructions[i][0] == "jmp":
        i += int(instructions[i][1])

    elif instructions[i][0] == "jie":
        if reg[(instructions[i][1].rstrip(","))] % 2 == 0:
            i += int(instructions[i][2])
        else:
            i += 1

    elif instructions[i][0] == "jio":
        if reg[(instructions[i][1].rstrip(","))] == 1:
            i += int(instructions[i][2])
        else:
            i += 1

    else:
        break

print(f"b = {reg["b"]}")
