from Weapon import Weapon
from Armor import Armor
import random

class Character:
    stamina = 5
    strength = 5
    dexterity = 5
    mind = 5
    luck = 5
    speed = 5
    hp_current = 0

    name = None
    weapon = None
    helmet = None

    def __init__(self, name, stamina = 5, strength = 5, dexterity = 5, mind = 5, luck = 5, speed = 5):
        self.name = name
        self.stamina = stamina
        self.strength = strength
        self.dexterity = dexterity
        self.mind = mind
        self.luck = luck
        self.speed = speed
        self.hp_current = self.hp_max()

    def hp_max(self):
        return self.stamina * 5 + 150

    # returns whether or not a target hits a character
    def hits(self, target):
        dodge_chance = 0.05 + (target.dexterity + target.speed) / ((target.dexterity + self.dexterity) * 3)
        # to_hit_chance =  round((1 - dodge_chance) * 100, 2)
        # print(f"{self.name}'s chance to hit {target.name}: {to_hit_chance}")
        return random.random() > dodge_chance