from assets import npc, UI


class holy():

    def fight_knight(player):
        enemy_knight = npc()
        print(f'Hello {player.name}, I am  {enemy_knight.name} fight me!')
        win, __ = player.fight(enemy_knight)
        if win.name == player.name:
            player = win
            return player, False
        else:
            print("You died!")
            return player, True

    @staticmethod
    def path_one(player):
        pass

    @staticmethod
    def path_two(player):
        pass

    @staticmethod
    def path_three(player):
        pass

    def spawn(player):
        print("You are now in holy land, in front you see three paths. Which do you take?")
        path = UI.options("(1-2)", 1, 3)
        if path == 1:
            holy.path_one(player)
        if path == 2:
            holy.path_two(player)
