from .core_parts import *
import random


class monster(base_creature):
    """
    monster object class inherits base_creature
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

    def _gen_identity(self) -> None:
        """creates identity randomly returns none"""
        names = ["Wolf", "Fang", "Stompper", "Goblin"]
        self.gender = random.choice(["male", "female"])
        self.name = random.choice(names)
        self.health = random.randint(70, 130)

    def fight(self, player: object):
        """simulate a fight turn by attack/defend/miss on the player

        Args:
            player (object): player that the monster fights

        Returns:
            self (object): monster
            self (object): player
        """
        if(self.health > 0):
            self.is_defending = False
            c, a = base_ai.choose_state(), self.get_attack()
            if not player.is_defending:
                if c == "Attack":
                    d = player.get_pain(a)
                    print(
                        f"The {self.name} monster  hits {player.name} with A:{a} and landed d:{d} with {player.health}")

                if c == "Defend":
                    self.is_defending = True
                    print(f"{self.name} has their body in defense")

                if c == "Failed":
                    print(f"{self.name} stalks {player.name}")
            return player.fight(self)
        else:
            print(f"{player.name} wins!")
            return player, self
