#!/usr/bin/env python3
from .vaildator import validator


class UI():

    @staticmethod
    def ask(String: str):
        user_input = input(f"{String}>>>")
        while validator.is_not_abc(user_input):
            user_input = input(f"{String}>>>")
        return str(user_input)

    @staticmethod
    def options(String: str, l: int, h: int):
        user_input = input(f"{String}>>>")
        while validator.is_not_accepted(user_input, l, h):
            user_input = input(f"{String}>>>")
        return int(user_input)

    @staticmethod
    def fight_options():
        user_input = input("(A/D) >>>").lower()
        while user_input != "a" and user_input != "d":
            user_input = input("(A/D) >>>").lower()
        return str(user_input.lower())


if __name__ == '__main__':
    check = UI.options(2, 1, 3)
    print(check)
