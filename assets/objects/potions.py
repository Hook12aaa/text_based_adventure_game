#!/usr/bin/env python3
from random import randint


class potions():
    """potion object with call stats for health:

    Functions:
        ._get_rarity() = self triggered potion luck
        .use_potion return int of player.health used potion

    """

    equip = "potion"
    name = ''
    modifer = 0

    def __init__(self):
        self._get_rarity()

    def _get_rarity(self):
        type_of_potions = [[1, 1.25, "small"], [
            2, 1.50, "mid"], [1, 1.75, "large"]]
        l = randint(1, 3)
        for i in type_of_potions:
            if l == i[0]:
                self.modifer = i[1]
                self.name = f"{i[2]} potion"

    def use_potion(self, player: object) -> int:
        """This will use potion object

        Args:
            player (object): currunt player in use

        Returns:
            int: returns new health state to be be given
        """
        player.health *= self.modifer
        if player.health > player.base_health:
            player.health = player.base_health
            print(f"HP {player.health} ==> {player.base_health}")
            return round(player.health)
        else:
            print(f"HP:{player.health} ==> {player.health*self.modifer}")
            return round(player.health)

    def __del__(self):
        print("you have used a potion!")
