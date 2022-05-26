"""
Some utility functions that are useful in many of the advent of code 2020
puzzels.
"""

import os


def test_input_location(day: int, filename: str = "test_input.txt") -> str:
    """returns location of test file"""
    return os.path.join(f"data/day_{day}", filename)


def input_location(day: int, filename: str = "input.txt") -> str:
    """returns location of the production file"""
    return os.path.join(f"data/day_{day}", filename)
