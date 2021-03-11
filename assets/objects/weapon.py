#!/usr/bin/env python3
import random


class weapon():

    """weapon object:

    ._get_rarity() = self triggered weapon luck
    .use_weapon return int of player.attack used weapon

    """
    equip = "attack"
    name = ''
    modifer = 0

    def __init__(self):
        self._get_rarity()

    def _get_rarity(self):
        self.modifer, self.name = random.randint(
            0, 20), random.choice(["dagger", "spear", "spear"])

    def use_weapon(self, player: object) -> int:
        """[use_weapon will add attack value from moodier]

        Args:
            player (object): player to get affected

        Returns:
            int: player (object).attack
        """
        player.attack += self.modifer
        print(f"{player.name}:\nAttached:{self.name}\nAttack:{self.modifer}+")
        return player.attack

    def __del__(self):
        print("you have used destroyed your sword!")
