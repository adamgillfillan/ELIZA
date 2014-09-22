__author__ = 'Adam'
# A module to hold the dictionary of rules
# Each rule entry is a pattern that is used by eliza.py to match the input text of the user
# If a match is found, a value from the matched key is chosen
rules = {
    '(SAD|DEPRESSED|UNHAPPY)': [
        'I am sorry you feeling down'
    ],
    '(HAPPY|JOY)': [
      'I am glad you feel good'
    ]
}