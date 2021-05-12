#!/usr/bin/env python3
import random


class base_ai():
    """ base_ai logic for all fighting by npc
    .choose_state() return fight type"""

    @staticmethod
    def __defend() -> str:
        is_lucky = random.choice([True, False])
        if is_lucky:
            return "Defend"
        if not is_lucky:
            return "Failed"

    @staticmethod
    def __attack() ->str:
        is_lucky = random.choice([True, False])
        if is_lucky:
            return "Attack"
        if not is_lucky:
            return "Failed"

    @staticmethod
    def choose_state() -> str:
        """[random fighting for npc state generater]

        Returns:
            str]: Attack or Defend or Failed
        """
        c = random.choice(["defense", "attack"])
        if c == 'attack':
            return base_ai.__attack()
        if c == 'defense':
            return base_ai.__defend()
