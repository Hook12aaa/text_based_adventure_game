from assets import npc, UI


class holy():

    def fight_knight(player):
        enemy_knight = npc()
        print(f'Hello {player.name}, I am  {enemy_knight.name} fight me!')
        win, __ = player.fight(enemy_knight)
        if win.name == player.name:
            player = win
            return player, True
        else:
            print("You died!")
            return player, False

    @staticmethod
    def path_one(player):
        player, win = holy.fight_knight(player)
        if not win:
            print("you died")
            return True
        else:
             print("well done on winning!!")
        print(
            "There is two paths one leads to  1: a office another to 2: a town.\n you choose....")
        c = UI.options("(1-2)", 1, 2)
        if c == 1:
            player, win = holy.fight_monster(player)
            if not win:
                print("you died")
                return True
            else:
                print("well done on winning!!")
        if c == 2:
            print("You find a potion on the floor!")
            player.user_equip(objects.potions())
            player, win = holy.fight_knight(player)
            if not win:
                print("you died")
                return True
            else:
                print("well done on winning!!")


        print("Well done on going through that mess! You have passed the trial")


    @staticmethod
    def path_two(player):
        print("you walked into a room with no floor, you died!")
        return True

    @staticmethod
    def path_three(player):
        player, win = holy.fight_monster(player)
        if not win:
            return True
        else:
            print("you won, the fight was hard and trying, you die from staveration")

    def spawn(player):
        print("You are now in holy land, in front you see three paths. Which do you take?")
        path = UI.options("(1-2)", 1, 3)
        if path == 1:
            holy.path_one(player)
        if path == 2:
            holy.path_two(player)
