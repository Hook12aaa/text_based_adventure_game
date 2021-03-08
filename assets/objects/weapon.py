#!/usr/bin/env python3
import random


class weapon():
    equip = "attack"
    name = ''
    modifer = 0

    def __init__(self):
        self.get_rarity()

    def get_rarity(self):
        self.modifer, self.name = random.randint(
            0, 20), random.choice(["dagger", "spear", "spear"])

    def use_weapon(self, player: object):
        player.attack += self.modifer
        print(f"{player.name}:\nAttached:{self.name}\nAttack:{self.modifer}+")
        return player.attack

    def __del__(self):
        print("you have used destroyed your sword!")
