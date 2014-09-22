__author__ = 'Adam'
from rules import *
import time
import re


class Eliza():
    """
        An agent that simulates an amusing interpretation of a Rogerian psychologist.
    """
    def __init__(self):
        self.intro_message()
        self.user_name = self.determine_name()

    @staticmethod
    def intro_message():
        print("Eliza: Hi, my name is Eliza. I am a Rogerian psychologist.")
        time.sleep(0)
        print("Eliza: Today I will help you with your problems.")
        time.sleep(0)

    @staticmethod
    def determine_name():
        return input("Eliza: What is your name?\n")

    def interact(self):
        print("Eliza: What is wrong, {0}?".format(self.user_name))
        while True:
            user_input = input("{0}: ".format(self.user_name))
            processed_input = self.process_user_input(user_input)
            self.print_response(processed_input)

    def process_user_input(self, user_input):
        user_input = self.remove_punct(user_input)
        words = user_input.upper().split()
        replacements = [
            ('I', 'YOU'),
            ('YOU', 'I'),
            ('ME', 'YOU'),
            ('MY', 'YOUR'),
            ('AM', 'ARE'),
            ('ARE', 'AM')
        ]

        return [self.replace_words(word, replacements) for word in words]

    @staticmethod
    def replace_words(word, replacements):
        """
            Replace a word if it exists in the replacements list of tuples.
        """
        for old_word, new_word in replacements:
            if word == old_word:
                return new_word
        return word

    @staticmethod
    def remove_punct(user_input):
        punct = ',;.?!:'
        for char in user_input:
            if char in punct:
                user_input = user_input.replace(char, '')
        return user_input

    def print_response(self, words):
        response_message = self.create_response(words)
        print("Eliza: ", end="")
        print(" ".join(response_message).upper())

    @staticmethod
    def create_response(words):
        for pattern, replacement in rules.items():
            p = re.compile(pattern)
            match = p.search(" ".join(words))
            if match:
                return [word for word in replacement]
        return words


if __name__ == "__main__":
    eliza = Eliza()
    eliza.interact()