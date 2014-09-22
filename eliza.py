__author__ = 'Adam'
from rules import *
import time
import re
import random

# Homework assignment for my Spoken Dialogue Systems graduate class CSC591
#
# The task is to implement ELIZA, a rogerian psychologist that utilizes repetitive text to communicate with the user
# ex: User: My girlfriend made me come here
#     Eliza: YOUR GIRLFRIEND MADE YOU COME HERE
#
# Eliza also uses substitutions for certain words matched using regular expressions
# ex: User: She says I'm depressed much of the time
#     Eliza: I AM SORRY TO HEAR YOU ARE FEELING SAD
#
# My implementation takes a more amusing approach to Eliza's responses


class Eliza():
    """
        An agent that simulates an amusing interpretation of a Rogerian psychologist.
    """
    def __init__(self):
        self.intro_message()
        self.user_name = self.get_name()

    @staticmethod
    def intro_message():
        print("Eliza: Hi, my name is Eliza. I am a Rogerian psychologist.")
        time.sleep(0)
        print("Eliza: Today I will help you with your problems.")
        time.sleep(0)

    @staticmethod
    def get_name():
        return input("Eliza: What is your name?\n")

    def interact(self):
        """
            Main loop where the user interacts with Eliza
            The input is processed and a response is generated
        """
        print("Eliza: What is wrong, {0}?".format(self.user_name))
        while True:
            user_input = input("{0}: ".format(self.user_name))
            processed_input = self.process_user_input(user_input)
            self.print_response(processed_input)

    def process_user_input(self, user_input):
        """
            Capitalize all words to make our lives easier with capitlization rules.
            Also, sanatize the input using a remove_punct method that removes punctuation.
            Replace the perspective of the user with the perspective of Eliza.
            Additional tuples may be added here.
        """
        user_input = self.remove_punct(user_input)
        words = user_input.upper().split()
        replacements = [
            ('I', 'YOU'),
            ('YOU', 'I'),
            ('ME', 'YOU'),
            ('MY', 'YOUR'),
            ('AM', 'ARE'),
            ('ARE', 'AM'),
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
        """
            Create a response message and print it for the user to see.
        """
        response_message = self.create_response(words)
        print("Eliza: ", end="")
        print("".join(response_message).upper())

    @staticmethod
    def create_response(words):
        """
            Create a response message based on the user input and any patterns matched from rules.py.
            Check each pattern with the input text and accumulate all matches and replacement text in 'matched' array.
            Print only the replacement text of the first match since it is determined to be the higher ranking.
            Implemented this way to show that a ranking order does occur. I can then choose to print any replacement
            text I want from the 'matched' array.
        """
        matched = []
        for pattern, replacement in rules.items():
            p = re.compile(pattern)
            match = p.search(" ".join(words))
            if match:
                matched.append([match.group(0), random.choice(replacement)])
        if len(matched) > 0:
            return [word for word in matched[0][1]]
        else:
            return words


if __name__ == "__main__":
    eliza = Eliza()
    eliza.interact()