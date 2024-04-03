# Advent of Code 2015, day 21, part 2

from itertools import combinations

weapons = [
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0)]

armors = [
    ("None", 0, 0, 0),
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5)]

rings = [
    ("None", 0, 0, 0),
    ("Damage +1", 25, 1, 0),
    ("Damage +2", 50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3)]

def generate_equipment(weapons, armors):
    noring_combinations = []
    for i in range(len(weapons)):
        for j in range(len(armors)):
            noring_combinations.append((weapons[i], armors[j]))
    return noring_combinations

def generate_equipment_with_rings(weapons, armors, rings):
    ring_combinations = []
    for combination in generate_equipment(weapons, armors):
        for item in list(combinations(rings, 2)):
            ring_combinations.append((*combination, *item))
    return ring_combinations


equipment_no_ring = generate_equipment(weapons, armors)
equipment_with_ring = generate_equipment_with_rings(weapons, armors, rings)

equip = equipment_no_ring + equipment_with_ring

player_input = []
for comb in equip:
    gold, damage, armor = 0, 0, 0
    for item in comb:
        gold += int(item[1])
        damage += int(item[2])
        armor += int(item[3])
    player_input.append((gold, damage, armor))

boss_stat = (8, 2)

results = []
for item in player_input:
    player_life = 100
    boss_life = 100
    while True:
        damage = item[1] - boss_stat[1]
        boss_life -= (damage if damage > 1 else 1)
        if boss_life <= 0:
            break
        damage = boss_stat[0] - item[2]
        player_life -= (damage if damage > 1 else 1)
        if player_life <= 0:
            results.append(item[0])
            break

print(f"Gold: {max(results)}")
