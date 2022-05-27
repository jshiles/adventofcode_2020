"""
Advent of Code 2020 - Puzzel 6
https://adventofcode.com/2020/day/6
jshiles
"""

import re
from functools import reduce
from typing import List
from adventofcode import utils


def parse_input_p1(filename: str) -> List[set]:
    """Returns a list of sets with all positive questions."""
    positive_asnwers: List[set] = []
    with open(filename) as f:
        for ans in re.split(r"(?:\r?\n){2,}", f.read()):
            ans = set("".join(ans.replace(" ", "").splitlines()))
            positive_asnwers.append(ans)
    return positive_asnwers


def parse_input_p2(filename: str) -> List[set]:
    """Returns a list of sets where everyone answered yes."""
    positive_asnwers: List[set] = []
    with open(filename) as f:
        for ans in re.split(r"(?:\r?\n){2,}", f.read()):
            positive_asnwers.append(
                reduce(
                    (lambda x, y: x.intersection(y)),
                    [
                        set(individual)
                        for individual in ans.replace(" ", "").splitlines()
                    ],
                )
            )
    return positive_asnwers


def main():
    """
    execute part 1 and part 2
    """
    test_filename: str = utils.test_input_location(day="6")
    filename: str = utils.input_location(day="6")

    # For each group, count the number of questions to which anyone
    # answered "yes". What is the sum of those counts?
    test_positive_asnwers_uniq = parse_input_p1(test_filename)
    assert sum([len(s) for s in test_positive_asnwers_uniq]) == 11

    positive_asnwers_uniq = parse_input_p1(filename)
    part1_ans = sum([len(s) for s in positive_asnwers_uniq])
    print(f"Part 1: {part1_ans}")

    # For each group, count the number of questions to which everyone
    # answered "yes". What is the sum of those counts?
    test_positive_asnwers_common = parse_input_p2(test_filename)
    assert sum([len(s) for s in test_positive_asnwers_common]) == 6

    positive_asnwers_common = parse_input_p2(filename)
    part2_ans = sum([len(s) for s in positive_asnwers_common])
    print(f"Part 2: {part2_ans}")


if __name__ == "__main__":
    main()
