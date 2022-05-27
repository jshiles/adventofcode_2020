"""
Advent of Code 2020 - Puzzel 9
https://adventofcode.com/2020/day/9
jshiles
"""

import copy
from itertools import permutations
from typing import List, Tuple
from adventofcode import utils


def get_input(filename: str) -> list:
    """Returns a list of integers as our input data."""
    numbers: list = []
    with open(filename) as f:
        numbers = [int(x) for x in f.read().split()]
    return numbers


def is_valid(num: int, prev: List[int]) -> bool:
    """return true if num is the sum of any two numbers in prev"""
    for n1, n2 in permutations(prev, 2):
        if n1 + n2 == num:
            return True
    return False


def find_continguous(seq: List[int], target: int) -> Tuple[int, int]:
    """
    Find a contiguous set of number that equal our target
    """
    for length in range(2, len(seq)):
        for idx in range(0, len(seq)-length):
            if sum(seq[idx:idx+length]) == target:
                sub_seq = copy.deepcopy(sorted(seq[idx:idx+length]))
                return sub_seq[0], sub_seq[-1]


def main():
    """
    execute part 1 and part 2
    """

    test_filename: str = utils.test_input_location(day="9")
    filename: str = utils.input_location(day="9")

    # P1: The first step of attacking the weakness in the XMAS
    # data is to find the first number in the list (after the
    # preamble) which is not the sum of two of the 25 numbers
    # before it. What is the first number that does not have
    # this property?

    test_seq = get_input(test_filename)
    for idx, n in enumerate(test_seq[5:]):
        if not is_valid(n, test_seq[idx:5+idx]):
            assert n == 127
            break
    
    part_2_target = None
    seq = get_input(filename)
    for idx, n in enumerate(seq[25:]):
        if not is_valid(n, seq[idx:25+idx]):
            print(f"Part 1: {n}")
            part_2_target = n
            break

    # P2: Find a contiguous set of numbers that add to 2089807806
    # Add smallest and largest and this is the answer.
    sm, lg = find_continguous(seq, part_2_target)
    print(f"Part 2: {sm+lg}")


if __name__ == "__main__":
    main()
