"""
Advent of Code 2020 - Puzzel 2
https://adventofcode.com/2020/day/2
jshiles
"""

import re
from dataclasses import dataclass, InitVar, field
from typing import List
from adventofcode import utils


@dataclass(frozen=True, slots=True)
class SledPasswordRule:
    """
    Class for password rules, which contain a charcter ch,
    a min/max occurrence count for ch.
    """

    min: int
    max: int
    ch: str

    def is_valid(self, password: str) -> bool:
        return self.min <= password.count(self.ch) <= self.max


@dataclass(frozen=True, slots=True)
class TobogganPasswordRule:
    """
    Class for password rules, which contain a charcter ch,
    a positions that character must be found.
    """

    pos1: int
    pos2: int
    ch: str

    def is_valid(self, password: str) -> bool:
        """pos1 or pos2 must contain ch (not both), index starts at 1"""
        return (
            password[self.pos1 - 1] == self.ch or
            password[self.pos2 - 1] == self.ch
        ) and not (
            password[self.pos1 - 1] == self.ch and
            password[self.pos2 - 1] == self.ch
        )


@dataclass(slots=True)
class Password:
    """
    Password class which contains a password and some corp. rules we
    can test against.
    """

    input_str: InitVar
    sled_rule: SledPasswordRule = field(default=None)
    tob_rule: TobogganPasswordRule = field(default=None)
    password: str = field(default="")

    def __post_init__(self, input_str: str):
        """parse inputs"""
        m = re.search(r"^(\d+)\-(\d+)\ (\w)\:\ (\w+)$", input_str)
        if m:
            self.sled_rule = SledPasswordRule(
                int(m.group(1)), int(m.group(2)), m.group(3)
            )
            self.tob_rule = TobogganPasswordRule(
                int(m.group(1)), int(m.group(2)), m.group(3)
            )
            self.password = m.group(4)

    def is_valid_sled(self) -> bool:
        return self.sled_rule.is_valid(self.password)

    def is_valid_toboggan(self) -> bool:
        return self.tob_rule.is_valid(self.password)


def get_input():
    """Returns a list of integers as our input data."""
    filename: str = utils.input_location(day="2")
    with open(filename) as f:
        return f.readlines()


def main():
    """
    execute part 1 and part 2
    """
    passwords: List[str] = get_input()
    valid_cnt_sled: int = 0
    valid_cnt_toboggan: int = 0
    for line in passwords:
        pw: Password = Password(line.strip())
        if pw is not None and pw.is_valid_sled():
            valid_cnt_sled += 1
        if pw is not None and pw.is_valid_toboggan():
            valid_cnt_toboggan += 1

    print(f"Part 1: {valid_cnt_sled} valid passwords.")
    print(f"Part 2: {valid_cnt_toboggan} valid passwords.")


if __name__ == "__main__":
    main()
