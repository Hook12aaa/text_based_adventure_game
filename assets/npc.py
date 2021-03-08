from .core_parts import base_ai, base_creature
from .objects import armour, potions, weapon
import random


class npc(base_creature):
    def __init__(self):
        base_creature.__init__(self)
        self.gen_identity()

    def gen_identity(self):
        names = ["Sarah", "Scott", "John", "Tom"]
        self.gender = random.choice(["male", "female"])
        self.name = random.choice(names)

    def fight(self, player: object):
        if(self.health > 0):
            self.is_defending = False
            c, a = base_ai.choose_state(), self.get_attack()
            if c == "Attack":
                d = player.get_pain(a)
                print(
                    f"{self.name} attack {player.name} with A:{a} and landed d:{d}")
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
        items = [potions(), armour(), weapon()]
        return random.choice(items)


if __name__ == '__main__':
    TravlerOne = npc()
    TravlerTwo = npc()
    TravlerTwo.fight(TravlerOne)
