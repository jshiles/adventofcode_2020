"""
Advent of Code 2020 - Puzzel 1
https://adventofcode.com/2020/day/1
jshiles
"""

from itertools import permutations
from functools import reduce
from typing import List
from adventofcode import utils


def get_input() -> list:
    """Returns a list of integers as our input data."""
    numbers: list = []
    filename: str = utils.input_location(day="1")
    with open(filename) as f:
        numbers = [int(x) for x in f.read().split()]
    return numbers


def find_product_n_numbers_sum_to(numbers: List[int], n: int, goal: int):
    """
    Prints a tuple with the "n" from the list "numbers" that sum
    to "goal" and the product of those n numbers.
    """
    for perm in permutations(numbers, n):
        if sum(perm) == goal:
            print((perm, reduce((lambda x, y: x * y), perm)))
            break


def main():
    """
    execute part 1 and part 2
    """
    numbers: list = get_input()
    find_product_n_numbers_sum_to(numbers, 2, 2020)
    find_product_n_numbers_sum_to(numbers, 3, 2020)


if __name__ == "__main__":
    main()
