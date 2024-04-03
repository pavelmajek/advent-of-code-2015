# Advent of Code 2015, day 19, part 1

replacements = {}
with open("../../data/19.txt") as file:
    for line in file.readlines():
        line_parts = line.strip().split(" => ")
        replacements[line_parts[1]] = line_parts[0]

molecule = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"

list_of_molecules = []
for key, value in replacements.items():
    start_index = 0
    occurrences = []
    while start_index < len(molecule):
        index = molecule.find(value, start_index)
        if index == -1:
            break
        occurrences.append(index)
        start_index = index + len(value)

    if occurrences:
        for element in occurrences:
            temp_string = molecule[:element] + key + molecule[(element + len(value)):]
            list_of_molecules.append(temp_string)

result = set(list_of_molecules)
print(f"Molecules: {len(result)}")
