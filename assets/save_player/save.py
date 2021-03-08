
import json
import random


class save():
    @staticmethod
    def write(player: object, name: str):
        stats = {"name": player.name,
                 "gender": player.gender,
                 "defense": player.defense,
                 "attacks": player.health,
                 "health": player.health,
                 }

        with open(f'{name}.json', 'w') as f:
            json.dump(stats, f)

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
