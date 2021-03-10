import json
import random


class save():
    @staticmethod
    def write(player: object, name: str):
        """write object player to a json file"""
        try:
            with open(f'{name}.json', 'w') as f:
                json.dump(player.__dict__, f)
                True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def read(player: object, name: str):
        with open(f'{name}.json', 'r') as f:
            stats = json.load(f)
            player.name = stats['name']
            player.gender = stats['gender']
            player.defense = stats['defense']
            player.attacks = stats['attacks']
            player.health = stats['health']

        return player
