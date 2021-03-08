#!/usr/bin/env python3
import random


class base_ai():

    @staticmethod
    def __defend():
        is_lucky = random.choice([True, False])
        if is_lucky:
            return "Defend"
        if not is_lucky:
            return "Failed"

    @staticmethod
    def __attack():
        is_lucky = random.choice([True, False])
        if is_lucky:
            return "Attack"
        if not is_lucky:
            return "Failed"

    @staticmethod
    def choose_state() -> str:
        c = random.choice(["defense", "attack"])
        if c == 'attack':
            return base_ai.__attack()
        if c == 'defense':
            return base_ai.__defend()
