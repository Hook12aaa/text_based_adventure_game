from .core_parts import *
import random


class monster(base_creature):
    def __init__(self):
        base_creature.__init__(self)
        self.gen_identity()

    def gen_identity(self):
        names = ["Wolf", "Fang", "Stompper", "Goblin"]
        self.gender = random.choice(["male", "female"])
        self.name = random.choice(names)
        self.health = random.randint(70, 130)

    def fight(self, player: object):
        if(self.health > 0):
            self.is_defending = False
            c, a = base_ai.choose_state(), self.get_attack()
            if c == "Attack":
                d = player.get_pain(a)
                print(
                    f"The {self.name} monster  hits {player.name} with A:{a} and landed d:{d}")

            if c == "Defend":
                self.is_defending = True
                print(f"{self.name} has their body in defense")

            if c == "Failed":
                print(f"{self.name} stalks {player.name}")
            return player.fight(self)
        else:
            print(f"{player.name} wins!")
            return player, self
