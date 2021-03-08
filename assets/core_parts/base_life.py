#!/usr/bin/env python3
import random


class base_stats():
    # Core Stats For all life
    defense = random.randint(5, 50)
    attack = random.randint(5, 50)
    health = 100

    # Overwritable stats
    name = "OVERWRITEABLE"
    gender = "OVERWRITEABLE"

    def stats(self):

        return f"""
        Name : {self.name}
        Gender : {self.gender}
        Defense: {self.defense}
        Attacks: {self.health}
        Health : {self.health}
        """


class fight_values(base_stats):
    is_defending = False

    def get_attack(self) -> int:
        return round(self.attack * random.uniform(1, 2), 0)

    def get_pain(self, attack: int) -> int:
        if not self.is_defending:
            p = round(((self.defense / 100)+1) * attack, 1)
            self.health -= p
            return p
        else:
            return 1


class base_creature(fight_values, base_stats):
    def __init__(self):
        base_stats.__init__(self)
        fight_values.__init__(self)
