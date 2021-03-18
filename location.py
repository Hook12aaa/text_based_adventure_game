from assets import monster,npc,objects,UI,main_player



class hell():
    name = 'hell'
    enemy = 'monster'
    fight_text = 'Suddenly you walk forward and see '
    pathone = ['potion','fight']
    pathtwo = ['weapon','fight']
    





class play_location():
    
    def __init__(self,player,location):
        self.player = player
        self.location = location

    def is_fight_enemy_lost(self):
        enemy = npc() if self.location.enemy == "npc" else monster()
        print(f"{self.location.fight_text}{enemy.name} is attacking you")
        win, __ = self.player.fight(enemy)
        if win.name == self.player.name:
            print("you won the fight congrats")
            return False
        else:
            print("you died!")
            return True


    def do_action(self,path):
        type_of_loot = {
            "potion": objects.potions(),
            "weapon": objects.weapon(),
            "armour": objects.armour(),
        }
        for action in path:
            for equip in type_of_loot.keys():
                if equip == action:
                    self.player.user_equip(type_of_loot[equip])

            if action == "fight":
                print("you have entered into a fight!")
                if self.is_fight_enemy_lost():
                    break
        print("you have passed, let's move on")

    def spawn(self):
        print(f"You are now in {self.location.name}\n You see two doors in front which do you choose 1 or 2?")
        c = UI.options("(1-2)",1,2)
        if c == 1:
            self.do_action(self.location.pathone)
            print('you move on to path two')
            self.do_action(self.location.pathtwo)
            print('you win!, you find a hole and escape')
        elif c == 2:
            self.do_action(self.location.pathtwo)
            print('you move on to path one')
            self.do_action(self.location.pathone)
            print('you win!, time to escape')
        
        

location = play_location(main_player("bob","male"),hell())
location.spawn()