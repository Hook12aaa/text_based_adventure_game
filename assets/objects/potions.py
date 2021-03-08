#!/usr/bin/env python3
from random import randint


class potions():
    equip = "potion"
    name = ''
    modifer = 0

    def __init__(self):
        self.get_rarity()

    def get_rarity(self):
        type_of_potions = [[1, 1.25, "small"], [
            2, 1.50, "mid"], [1, 1.75, "large"]]
        l = randint(1, 3)
        for i in type_of_potions:
            if l == i[0]:
                self.modifer = i[1]
                self.name = f"{i[2]} potion"

    def use_potion(self, player: object):
        player.health *= self.modifer
        if player.health > player.base_health:
            player.health = player.base_health
            print(f"HP {player.health} ==> {player.base_health}")
            return player.health
        else:
            print(f"HP:{player.health} ==> {player.health*self.modifer}")
            return player.health

    def __del__(self):
        print("you have used a potion!")
