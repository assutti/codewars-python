"""
Kata: Sum of positive
Level: 8 kyu

Given a list of numbers, return the sum
of all positive numbers.
"""


def positive_sum(arr):
    return sum(x for x in arr if x > 0)