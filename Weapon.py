import random
import math

class Weapon:

    damage_min = 5
    damage_max = 7
    name = 'butter knife'
    type = 'dagger'

    def __init__(self, damage_min = 5, damage_max = 7, type = 'dagger', name = 'butter knife'):
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.type = type
        self.name = name

    def __str__(self):
        return '{}: {}'.format(self.type, self.name)

    def roll_weapon_damage(self, scaling_stat, round = True):
        roll = random.random()

        low_hit = self.damage_min * (1 + scaling_stat/ 40)
        high_hit = self.damage_max * (1 + scaling_stat/ 40)

        range = high_hit - low_hit

        damage = low_hit + range * roll

        if round:
            damage = math.floor(damage)

        return damage

    def roll_ability(self, scaling_stat, potency):
        return math.floor(self.roll_weapon_damage(scaling_stat, round=False) * (potency/100))



