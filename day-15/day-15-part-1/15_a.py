# Advent of Code 2015, day 15, part 1

ingredients = {}
with (open("../../data/15.txt") as file):
    for line in file.readlines():
        parts = line.strip().split()
        dict_name = parts[0].rstrip(":")
        ingredient_names = [parts[1], parts[3], parts[5], parts[7], parts[9]]
        ingredient_quantities = [int(parts[2].rstrip(",")), int(parts[4].rstrip(",")), int(parts[6].rstrip(",")), int(parts[8].rstrip(",")), int(parts[10])]
        ingredients[dict_name] = {}
        for name, quantity in zip(ingredient_names, ingredient_quantities):
            ingredients[dict_name][name] = quantity

score = 0
for i in range(1, 98):
    for j in range(1, 98):
        for k in range(1, 98):
            for l in range(1, 98):
                if (i + j + k + l) == 100:
                    capacity = i * ingredients["Sprinkles"]["capacity"] + j * ingredients["PeanutButter"]["capacity"] + k * ingredients["Frosting"]["capacity"] + l * ingredients["Sugar"]["capacity"]
                    durability = i * ingredients["Sprinkles"]["durability"] + j * ingredients["PeanutButter"]["durability"] + k * ingredients["Frosting"]["durability"] + l * ingredients["Sugar"]["durability"]
                    flavor = i * ingredients["Sprinkles"]["flavor"] + j * ingredients["PeanutButter"]["flavor"] + k * ingredients["Frosting"]["flavor"] + l * ingredients["Sugar"]["flavor"]
                    texture = i * ingredients["Sprinkles"]["texture"] + j * ingredients["PeanutButter"]["texture"] + k * ingredients["Frosting"]["texture"] + l * ingredients["Sugar"]["texture"]

                    if capacity > 0 and durability > 0 and flavor > 0 and texture > 0:
                        temp = capacity * durability * flavor * texture
                        if temp > score:
                            score = temp

print(f"Score: {score}")
