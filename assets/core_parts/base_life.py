#!/usr/bin/env python3
import random


class base_stats():
    """store all stats for character objects"""

    def __init__(self):
        # Core Stats For all life
        self.defense = random.randint(5, 50)
        self.attack = random.randint(5, 50)
        self.health = 100

        # Overwritable stats
        self.name = "OVERWRITEABLE"
        self.gender = "OVERWRITEABLE"

    def stats(self) -> str:
        """gets stats in a string format
        Returns:
            str: all stats for object
        """
        return f"""
        Name : {self.name}
        Gender : {self.gender}
        Defense: {self.defense}
        Attacks: {self.attack}
        Health : {self.health}
        """


class fight_values(base_stats):

    is_defending = False

    def get_attack(self) -> int:
        """
        gets attack for self object's attack
        Returns:
            int: random attack value
        """
        return round(self.attack * random.uniform(1, 2), 0)

    def get_pain(self, attack: int) -> int:
        """gets pain for other object's attack and takes damage off attack

        Args:
            int: attack value from other object

        Returns:
            int: random attack value
        """
        if not self.is_defending:
            p = round(((self.defense / 100)+1) * attack, 1)
            self.health -= p
            return p
        else:
            return 1


class base_creature(fight_values, base_stats):
    """
    base_creature is parent for all character objects
    Functions:
        .get_attack()  get attack for self object's attack
        .getpaint(attack:int) return damage value; takes enemy attack
        .stats() get stats in a string format

    Returns:
        Name : self.name
        Gender : self.gender
        Defense: self.defense
        Attacks: self.attack
        Health : self.health

    """

    def __init__(self):
        base_stats.__init__(self)
        fight_values.__init__(self)
