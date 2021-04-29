import json
import os

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
            with open(os.path.join(f'assets/save_player/{name}.json'), 'w') as f:
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
        with open(os.path.join(f'assets/save_player/{name}.json'), 'r') as f:
            stats = json.load(f)
            for attr in stats.keys():
                setattr(player,attr,stats[f'{attr}'])
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
        with open(os.path.join(f'assets/save_player/{name}.json'), 'r') as f:
            info = json.load(f)
            for attr in info.keys():
                setattr(new_location,attr,info[f'{attr}'])
        return new_location


    @staticmethod
    def list_players() -> list:
        """List playable charracters in the /save_player dir without .json tag

        Returns:
            list: playable charracters without .json tag ie ['test_player','test_character']
        """
        files = [f for f in os.listdir('assets/save_player/') if '.json' in f]
        return  [f.replace('.json','') for f in files if f not in ('hell.json','heven.json')]

