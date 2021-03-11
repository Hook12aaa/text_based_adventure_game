from .core_parts import base_ai, base_creature
from .objects import armour, potions, weapon
import random


class npc(base_creature):
    """
    npc object class inherits base_creature
    Functions:
        .get_attack()  get attack for self object's attack
        .getpaint(attack:int) return damage value; takes enemy attack
        .stats() get stats in a string format
        ._gen_identity() self starting makes identity
        .fight() fight script that requires player
    Returns:
        Name : self.name
        Gender : self.gender
        Defense: self.defense
        Attacks: self.health
        Health : self.attack

    """

    def __init__(self):
        base_creature.__init__(self)
        self._gen_identity()

    def _gen_identity(self):
        """creates identity randomly returns none"""
        names = ["Sarah", "Scott", "John", "Tom"]
        self.gender = random.choice(["male", "female"])
        self.name = random.choice(names)

    def fight(self, player: object):
        """simulate a fight turn by attack/defend/miss on the player returns tuple in (win,loss)

        Args:
            player (object): player that the npc fights

        Returns:
            self (object): npc
            self (object): player
        """
        if(self.health > 0):
            self.is_defending = False
            c, a = base_ai.choose_state(), self.get_attack()
            if c == "Attack":
                d = player.get_pain(a)
                print(
                    f"{self.name} attack {player.name} with A:{a} and landed d:{d} with {player.health}")
            if c == "Defend":
                self.is_defending = True
                print(f"{self.name} is blocking your attacks")

            if c == "Failed":
                print(f"{self.name} Failed and missed")
            return player.fight(self)
        else:
            print(f"{player.name} wins!")
            return player, self

    def drop_item(self):
        """ gets a random drop from npc

        Returns:
            item (obj): which is ethier [potions(), armour(), weapon()]
        """
        items = [potions(), armour(), weapon()]
        return random.choice(items)
