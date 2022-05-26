"""
Advent of Code 2020 - Puzzel 4
https://adventofcode.com/2020/day/4
jshiles
"""

import ast
import logging
import re
from dataclasses import dataclass, field
from typing import List
from adventofcode import utils


@dataclass
class Passport:

    byr: str  # (Birth Year)
    iyr: str  # (Issue Year)
    eyr: str  # (Expiration Year)
    hgt: str  # (Height in cm)
    hcl: str  # (Hair Color)
    ecl: str  # (Eye Color)
    pid: str  # (Passport ID)
    cid: str = field(default="")  # (Country ID)

    def __post_init__(self):
        """ensure rules are adhered to or raise type error"""

        if not (1920 <= int(self.byr) <= 2002):
            raise TypeError(f"byr {self.byr} not between 1920 and 2002.")

        if not (2010 <= int(self.iyr) <= 2020):
            raise TypeError(f"iyr {self.iyr} not between 2010 and 2020.")

        if not (2020 <= int(self.eyr) <= 2030):
            raise TypeError(f"eyr {self.eyr} not between 2020 and 2030.")

        if not (
            (self.hgt.endswith("in") and 59 <= int(self.hgt[:-2]) <= 76)
            or (self.hgt.endswith("cm") and 150 <= int(self.hgt[:-2]) <= 193)
        ):
            raise TypeError(f"hgt {self.hgt} out of range.")

        if re.match(r"^\#[0-9a-fA-F]{6}", self.hcl) is None:
            raise TypeError(f"hcl {self.hcl} not 6 digit hex number.")

        if self.ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            raise TypeError(f"ecl {self.ecl} not valid.")

        if re.match(r"^[0-9]{9}$", self.pid) is None:
            raise TypeError(f"ecl {self.pid} not valid.")


def parse_input(filename: str) -> list:
    """Returns a list of Passport objects as our input data."""

    passports: List[Passport] = []
    with open(filename) as f:
        for p in re.split(r"(?:\r?\n){2,}", f.read()):
            p = "{" + re.sub("\s+", ",", p) + "}"
            p = re.sub(r"(\w+):([\#\w]+)", r"'\1':'\2'", p)
            p = ast.literal_eval(p)
            try:
                passports.append(Passport(**p))
            except (TypeError) as e:
                logging.error((p, e))

    return passports


def main():
    """
    execute part 1 and part 2
    """
    filename: str = utils.input_location(day="4")
    passports: List[Passport] = parse_input(filename)
    print(f"Valid Passports: {len(passports)}")


if __name__ == "__main__":
    main()
