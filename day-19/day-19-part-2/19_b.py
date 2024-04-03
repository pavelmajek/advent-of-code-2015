# Advent of Code 2015, day 19, part 2

from random import shuffle

replacements = []
with open("../../data/19.txt") as file:
    for line in file.readlines():
        line_parts = line.strip().split(" => ")
        replacements.append((line_parts[1], line_parts[0]))

molecule = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"

template = molecule
count = 0
while template != "e":
    shuffle(replacements)
    mem = template
    for a, b in replacements:
        if a in template:
            template = template.replace(a, b, 1)
            count += 1
    if mem == template:
        template = molecule
        count = 0

print(f"Steps: {count}")
