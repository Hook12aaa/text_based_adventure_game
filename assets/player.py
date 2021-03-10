from .core_parts import base_creature
from .utils import UI


class main_player(base_creature):
    inventory = []

    def __init__(self, name, gender):
        base_creature.__init__(self)
        self.name = name
        self.gender = gender
        self.health = 200

    def fight(self, enemy: object):
        if self.health > 0:
            self.is_defending = False
            c, a = UI.fight_options(), self.get_attack()
            if c == 'a':  # player attacks
                d = enemy.get_paint(a)
                print(
                    f"{self.name} attack {enemy.name} with A:{a} and landed d:{d} with {enemy.health}")

            if c == "d":  # player defends
                self.is_defending = True
                print(f'{self.name} ready to protect')

            return enemy.fight(self)
        else:
            print("you died")
            return enemy, self

    def user_equip(self, item: object):
        if item.equip == 'potion':
            print('you drank a potion')
            self.health = item.use_potion(self)
        elif item.equip == 'attack':
            self.attack = item.use_weapon(self)
        elif item.equip == 'defense':
            self.defense = item.use_armour(self)
        self.inventory.append(item)
