from assets import UI, main_player
from dead import dead


def move_to_location(Player):
    location = UI.options("(1-4)", 1, 3)

    if location == 1:
        dead.spawn(Player)

    if location == 2:
        print("bulding it!")
        # holy.spawn(Player)

    if location == 3:
        # monster.spawn(Player)
        print('bulding it')


def on_boarding():
    print(f"hello and welcome to my game!\n What is your name?")
    name = UI.ask("(abc)")
    print(f"Oh your name is {name} and what is your gender?")
    gender = UI.ask("(abc)")
    Player = main_player(name, gender)
    print(f'here is your stats:\n {Player.stats()}')
    print("""Sorry for i was only interseted, it's hard to see.
    Welcome to this wonderful land.""")
    move_to_location(Player)
