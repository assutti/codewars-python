"""
Kata: Switch it Up!
Level: 8 kyu

Given an integer from 0 to 9, return the number written in words.
"""

def switch_it_up(number):
    numbers = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    return numbers[number]