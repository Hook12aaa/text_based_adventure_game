from assets import UI, main_player, save_info
from location import play_location
class main():

    @staticmethod
    def move_to_location(Player):
        """Will call a class depending on user input

        Locations:
            dead.spawn(),
            holy.spawn()

        Args:
            player (obj): the main_player
        
        """
        print("would you like to travel toh 1:hell or heaven?")
        location = UI.options("(1-2)", 1, 2)

        if location == 1:
            hell = play_location(Player,save_info.location("hell"))
            hell.spawn()

        if location == 2:
            heven = play_location(Player,save_info.location("heven"))
            heven.spawn()
    @staticmethod
    def on_boarding():
        """ creates a player object with user input ,writes to save and starts the location"""
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

    @staticmethod
    def reload():
        """ loads a player object with user input starts the location"""
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

    @staticmethod
    def run():
        """main function to run"""
        print("Have you ever played before? \n 1: Yes, 2: No")
        c = UI.options("(1-2)",1,2)
        if c == 1:
            main.reload()

        if c == 2:
            main.on_boarding()


if __name__ == '__main__':
    main.run()