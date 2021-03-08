from assets import objects, monster, UI


class dead():

    @staticmethod
    def fight_monster(player):
        enemy_monster = monster()
        print(f'oh no a monster {monster.name} appears!')
        win, loss = player.fight(enemy_monster)
        if win.name == player.name:
            player = win
            return player, False
        else:
            print("You died!")
            return player, True

        print("Your body gets crushed under dirt, you die..")

    @staticmethod
    def path_one(player):
        print('hello traveller, my name is john, it is not safe here. I will give you a sword and i recommend you leave!')
        player.user_equip(objects.weapon())
        print("sorry sir, i shall leave for the holy land....")

    @staticmethod
    def path_two(player):
        player, win = dead.fight_monster(player)
        return True if win else print("well done on winning!!")
        print(
            "There is two paths one leads to  1: hell another to 2: heven.\n you choose....")
        c = UI.options("(1-2)", 1, 2)
        if c == 1:
            player, score = dead.fight_monster(player)
            return True if score else print("well done on winning!!")
        if c == 2:
            "You find a potion on the floor!"
            player.user_equip(objects.potions())
            player, win = dead.fight_monster(player)
            return True if win else print("well done on winning!!")

        print("well done on going through that mess! You have passed the trial")

    @staticmethod
    def spawn(player: object):
        print("You are now in dead land, in front you see two paths. Which do you take?")
        path = UI.options("(1-2)", 1, 2)
        if path == 1:
            dead.path_one(player)
        if path == 2:
            dead.path_two(player)
