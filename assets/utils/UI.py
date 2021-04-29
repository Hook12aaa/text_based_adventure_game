#!/usr/bin/env python3
from os import stat
from .vaildator import validator
import sys

class UI():

    @staticmethod
    def ask(String: str) -> str:
        """ prompts user and gets valid input eg 'helo','anton' and not '1sd21', '!SW"S0'

        Args:
            String (str): to display on the side for users eg abc

        Returns:
            str :  valid user input
        """
        user_input = input(f"{String}>>>").lower()
        while validator.is_not_abc(user_input):
            user_input = input(f"{String}>>>").lower()
        return str(user_input.lower())

    @staticmethod
    def options(String: str, l: int, h: int) -> int:
        """get user input via a range of options eg 1-3

        Args:
            String (str): to display on the side for users eg 1-3
            l (int): lowest number acceptable
            h (int): highest number acceptable

        Returns:
            int : user input
        """
        user_input = input(f"{String}>>>")
        while validator.is_not_accepted(user_input, l, h):
            user_input = input(f"{String}>>>")
        return int(user_input)

    @staticmethod
    def fight_options():
        """ asks for type of attack eg A - attack and D - defense

        Returns:
            str: user_input
        """
        user_input = input("(A/D) >>>").lower()
        while user_input != "a" and user_input != "d":
            user_input = input("(A/D) >>>").lower()
        return str(user_input.lower())

    @staticmethod
    def file_options(files:list)->str:
        """Will only return data when User enters a input in files

        Args:
            files (list): the list of files

        Returns:
            file (str): the name of file to be used
        """
        for f in files: print(f)
        user_input = input('(Name)>>>').lower()
        while user_input not in files:
            user_input = input('(Name)>>>').lower()

        return str(user_input)
    
    @staticmethod
    def exit_game()-> None:
        """When called the game will exit"""
        sys.exit(1)