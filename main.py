from assets import UI, main_player, save_info
from dead import dead
from holy import holy


class main():
    def move_to_location(Player):
        print("would you like to travel toh 1:hell or heaven?")
        location = UI.options("(1-2)", 1, 2)

        if location == 1:
            dead.spawn(Player)

        if location == 2:
            holy.spawn(Player)

    def on_boarding():
        print(f"hello and welcome to my game!\n What is your name?")
        name = UI.ask("(abc)")
        print(f"Oh your name is {name} and what is your gender?")
        gender = UI.ask("(abc)")
        Player = main_player(name, gender)
        print(f'here is your stats:\n {Player.stats()}')
        print("""Sorry for i was only interseted, it's hard to see.
        Welcome to this wonderful land.""")
        save_info.write(Player,Player.name)
        main.move_to_location(Player)

    def reload():
        print('what was your character called?')
        while True:
            try:
                player = save_info.read(main_player("name","gender"),input("(abc)>>>"))
                break
            except FileNotFoundError:
                print('that is wrong which one is it?')
                continue
        print(f'here is your stats:\n {player.stats()}\n\nWelcome to this wonderful land.')
        main.move_to_location(player)


    def run():
        print("Have you ever played before? \n 1: Yes, 2: No")
        c = UI.options("(1-2)",1,2)
        if c == 1:
            main.reload()

        if c == 2:
            main.on_boarding()


if __name__ == '__main__':
    main.run()