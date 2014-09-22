__author__ = 'Adam'
# A module to hold the dictionary of rules.
#
# Each rule entry is a pattern that is used by eliza.py to match the input text of the user.
# If a match is found, a value from the matched key is chosen.
#
# Ranking of rules is in descending order (highest first) - this is needed if 2 matches are found in 1 input.
# In this case, the more important pattern is used

rules = {
    "\\bSAD\\b|\\bDEPRESSED\\b|\\bUNHAPPY\\b": [
        'Suck it up kid',
        'I\'ve seen worse',
        'It\'s not like you have no food, clothes, or shelter'
    ],
    '\\bMAD\\b|\\bANGRY\\b': [
        'Do you need a wall to punch',
        'Sometimes I get mad too',
    ],
    '\\bHAPPY\\b|\\bJOY\\b': [
        'I guess my work here is done',
        'I am really good at this psychologist thing'
    ],
    '\\bDREAM\\b':[
        'I\'m not a dream interpreter',
        'Go talk to Freud',
        'That is a weird dream',
        'Do you always tell people about your dreams'
    ],
    '\\bPERSON\\b':[
        'I am too a real person',
        'Well I guess you are talking to yourself then...weirdo'
    ],
    '\\bMOM\\b|\\bMOTHER\\b':[
        'We are talking about you, not your mom'
        'My mom was a psychologist, too'
    ],
    '\\bDAD\\b|\\bFATHER\\b':[
        'Great, I\'ll tell your dad when we are done here',
        'I am your father'
    ],
    '\\bFEEL\\b|\\bFEELING\\b':[
        'Tell someone who cares how you feel',
        'I bet your mom cares'
        'I don\'t really care, #sorrynotsorry'
    ],
    '\\bCAN\'T\\b':[
        'Only the weak think they can\'t'
        'You know what I cant not do--be awesome'
    ],
    '\\bSOMEONE|SOMETHING\\b':[
        'Can you be more specific',
        'Please tell me more',
        'Go ahead and share more'
    ],
    '\\bALWAYS\\b': [
        'Can you come up with just one time this happened',
    ],
    '\\bALL\\b': [
        'In what way'
    ]
}