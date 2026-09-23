"""
Kata: Well of Ideas - Easy Version
Level: 8 kyu

Given a list containing "good" and "bad" ideas,
return a message based on the number of good ideas.
"""


def well(x):
    good = x.count("good")

    if good == 0:
        return "Fail!"
    elif good <= 2:
        return "Publish!"
    else:
        return "I smell a series!"