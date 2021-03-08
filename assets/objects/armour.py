#!/usr/bin/env python3
import random


class armour():
    equip = "defense"
    name = ''
    modifer = 0

    def __init__(self):
        self.get_rarity()

    def get_rarity(self):
        self.modifer, self.name = random.randint(
            0, 20), random.choice(["chest plate", "shield", "brace"])

    def use_weapon(self, player: object):
        player.defense += self.modifer
        print(f"{player.name}:\nAttached:{self.name}\Defense:{self.modifer}+")
        return player.defense

    def __del__(self):
        print("you have used destroyed your armour!")
