"""
Advent of Code 2020 - Puzzel 3
https://adventofcode.com/2020/day/3
jshiles
"""

from functools import reduce
from typing import List
from adventofcode import utils


def get_input(filename: str) -> list:
    """Returns a list of strings as our input data."""
    forest: List[list] = []
    with open(filename) as f:
        forest = [x for x in f.read().split()]
    return forest


def trees_encountered(forest: List[str], r: int, d: int) -> int:
    """
    count trees encountered with the movement pattern.
    tree patterns repeat the right indefinitely.

    forest: List[str] containing '.' (no tree) and '#' (tree).
    r: amount we move in x direction
    d: amount we move in y direction
    """
    x, y, trees = 0, 0, 0
    while y < len(forest):
        adj_x = x if x < len(forest[y]) else x % len(forest[y])
        if forest[y][adj_x] == "#":
            trees += 1
        y += d
        x += r
    return trees


def main():
    """
    execute part 1 and part 2
    """
    test_filename: str = utils.test_input_location(day="3")
    test_forest: List[str] = get_input(test_filename)
    assert trees_encountered(test_forest, 3, 1) == 7

    filename: str = utils.input_location(day="3")
    forest: List[str] = get_input(filename)

    # Part 1: Sum trees when you move through the forest
    # Right 3, down 1
    print(trees_encountered(forest, 3, 1))

    # Part 2: Multiply tress encountered in the following
    # movement patterns.
    # Right 1, down 1.
    # Right 3, down 1.
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.
    p2_trees = reduce(
        (lambda x, y: x * y),
        [
            trees_encountered(forest, r, d)
            for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        ],
    )
    print(p2_trees)


if __name__ == "__main__":
    main()
