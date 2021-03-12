#!/usr/bin/env python3
import random


class armour():

    """weapon object:

    ._get_rarity() = self triggered armour luck
    .use_weapon return int of player.defense used armour

    """
    equip = "defense"
    name = ''
    modifer = 0

    def __init__(self):
        self._get_rarity()

    def _get_rarity(self):
        self.modifer, self.name = random.randint(
            0, 20), random.choice(["chest plate", "shield", "brace"])

    def use_armour(self, player: object) -> int:
        """[use_armour will add defense value from moodier]

        Args:
            player (object): player to get affected

        Returns:
            int: player (object).defense
        """
        player.defense += self.modifer
        print(f"{player.name}:\nAttached:{self.name}\Defense:{self.modifer}+")
        return player.defense

    def __del__(self):
        print("you have used up your armour!")
