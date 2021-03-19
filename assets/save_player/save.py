import json


class save_info():
    @staticmethod
    def write(player: object, name: str) -> bool:
        """write stats into json file from player object

        Args:
            player (object): your currunt stats
            name (str): name of file in fromat '.save_player.(name).json'

        Returns:
            bool: true if successful (bug testing)
        """
        try:
            with open(f'assets/save_player/{name}.json', 'w') as f:
                json.dump(player.__dict__, f)
                return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def read(player: object, name: str) -> object:
        """read json and inject stats to object

        Args:
            player (object): your old stats
            name (str): name of file in fromat './save_player(insert).json'

        Returns:
            player (object): your new stats
        """
        with open(f'assets/save_player/{name}.json', 'r') as f:
            stats = json.load(f)
            player.name = stats['name']
            player.gender = stats['gender']
            player.defense = stats['defense']
            player.attacks = stats['attacks']
            player.health = stats['health']
        return player

    @staticmethod
    def location(name:str) -> object:
        """read location from json and creates an object

        Args:
            name (str): name of location selected

        Returns:
            object: location to travel to
        """
        new_location = lambda:None
        with open(f'assets/save_player/{name}.json', 'r') as f:
            info = json.load(f)
            new_location.name = info['name']
            new_location.enemy = info['enemy']
            new_location.fight_text = info['fight_text']
            new_location.pathone = info['pathone']
            new_location.pathtwo = info['pathtwo']
        return new_location
