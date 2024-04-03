# Advent of Code 2015, day 22, part 1
# based on random selection, may not provide the lowest value for a small number of iterations

from random import choice

class Player:
    def __init__(self, life, damage, armor, mana):
        self.life = life
        self.damage = damage
        self.armor = armor
        self.mana = mana
        self.spent_mana = 0

    def is_alive(self):
        return self.life > 0

    def attack(self, enemy):
        damage = self.damage
        if stats:
            for spell in stats:
                if spell.remaining_duration > 0:
                    damage = self.damage - spell.armor

        if damage < 1:
            damage = 1
        enemy.life -= damage

    def update_stats(self, stats):
        for spell in stats:
            if spell.remaining_duration > 0:
                spell.remaining_duration -= 1

    def update_buffs(self, buffs):
        self.update_stats(stats)
        for spell in buffs:
            if spell.remaining_duration > 0:
                spell.cast()
                spell.remaining_duration -= 1

    def cast_spell(self, stats, buffs, min_mana):
        if self.mana < min_mana:
            self.life = 0
        else:
            valid_spells = [spell for spell in spell_list if spell.cost <= self.mana]
            for spell in stats:
                if spell in valid_spells:
                    if spell.remaining_duration > 0:
                        valid_spells.remove(spell)
            for spell in buffs:
                if spell in valid_spells:
                    if spell.remaining_duration > 0:
                        valid_spells.remove(spell)
            random_spell = choice(valid_spells)

            self.mana -= random_spell.cost
            self.spent_mana += random_spell.cost

            if random_spell.name == "Magic Missile":
                boss.life -= random_spell.damage
            elif random_spell.name == "Drain":
                boss.life -= random_spell.damage
                player.life += random_spell.heal
            elif random_spell.name == "Shield":
                stats[0].remaining_duration = stats[0].duration
            elif random_spell.name == "Poison":
                buffs[0].remaining_duration = buffs[0].duration
            elif random_spell.name == "Recharge":
                buffs[1].remaining_duration = buffs[1].duration

    def check(self, player, boss, results):
        if not player.is_alive():
            return True
        if not boss.is_alive():
            results.append(player.spent_mana)
            return True

class Spell:
    def __init__(self, name, cost, duration, damage, heal, armor, mana):
        self.name = name
        self.cost = cost
        self.duration = duration
        self.remaining_duration = 0
        self.damage = damage
        self.heal = heal
        self.armor = armor
        self.mana = mana

    def cast(self):
        if self.damage > 0:
            boss.life -= self.damage
        if self.mana > 0:
            player.mana += self.mana


results = []
for i in range(100000):

    player = Player(50, 0, 0, 500)
    boss = Player(58, 9, 0, 0)

    s1 = Spell("Magic Missile", 53, 0, 4, 0, 0, 0)
    s2 = Spell("Drain", 73, 0, 2, 2, 0, 0)
    s3 = Spell("Shield", 113, 6, 0, 0, 7, 0)
    s4 = Spell("Poison", 173, 6, 3, 0, 0, 0)
    s5 = Spell("Recharge", 229, 5, 0, 0, 0, 101)

    spell_list = [s1, s2, s3, s4, s5]
    min_mana = min(spell.cost for spell in spell_list)
    buffs = [s4, s5]
    stats = [s3]
    while player.is_alive() and boss.is_alive():

        player.update_buffs(buffs)
        if player.check(player, boss, results):
            break
        player.cast_spell(stats, buffs, min_mana)
        if player.check(player, boss, results):
            break

        boss.update_buffs(buffs)
        if boss.check(player, boss, results):
            break
        boss.attack(player)
        if boss.check(player, boss, results):
            break

print(f"Mana: {min(results)}")
