from assets import objects, monster, UI
from holy import holy


class dead():

    @staticmethod
    def fight_monster(player):
        """fight a random monster

        Args:
            player (obj): the main_player

        Returns:
            tuple: player(obj), winstate(bool)
        """
        enemy_monster = monster()
        print(f'oh no a monster {enemy_monster.name} appears!')
        win, loss = player.fight(enemy_monster)
        if win.name == player.name:
            player = win
            return player, True
        else:
            print("You died!")
            return player, False

    @staticmethod
    def path_one(player):
        """path one will call holy land and travel you there"""
        print('hello traveller, my name is john, it is not safe here. I will give you a sword and i recommend you leave!')
        player.user_equip(objects.weapon())
        print("sorry sir, i shall leave for the holy land....")
        holy.spawn(player)

    @staticmethod
    def path_two(player):
        """ you have one fight, then two paths with another fight and potions
        Args:
            player (obj): the main_player

        Returns:
            bool: True # for when the player dies
        """
        # Fight starts with a monster
        player, win = dead.fight_monster(player)
        if win:
            print("you died")
            return True
        else:
            print("well done on winning!!")
        print(
            "There is two paths one leads to  1: hell another to 2: heven.\n you choose....")
        c = UI.options("(1-2)", 1, 2)
        # choice one - you get another fight
        if c == 1:
            player, score = dead.fight_monster(player)
            if score:
                print("you died")
                return True
            else:
                print("well done on winning!!")
        # choice two - you get a potion!
        if c == 2:
            print("You find a potion on the floor!")
            player.user_equip(objects.potions())
            player, win = dead.fight_monster(player)
            if win:
                print("you died")
                return True
            else:
                print("well done on winning!!")

        print("well done on going through that mess! You have passed the trial")

    @staticmethod
    def spawn(player: object):
        """will spawn player with an option of two different paths

        Args:
            player (obj): the main_player
        """
        print("You are now in dead land, in front you see two paths. Which do you take?")
        path = UI.options("(1-2)", 1, 2)
        if path == 1:
            if dead.path_one(player):
                print("you died good luck next time")
        if path == 2:
            if dead.path_two(player):
                print("you died good luck next time")
