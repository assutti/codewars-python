"""
Kata: Generate range of integers
Level: 8 kyu

Given start, stop and step, return a list of integers
from start to stop (inclusive), using the given step.
"""


def generate_range(start, stop, step):
    ls = list(range(start, stop + 1, step))
    return ls