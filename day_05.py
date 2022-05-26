"""
Advent of Code 2020 - Puzzel 5
https://adventofcode.com/2020/day/5
jshiles
"""

import math
from typing import List
from adventofcode import utils


def get_input(filename: str) -> list:
    """Returns a list of strings as our input data."""
    passes: List[str] = []
    with open(filename) as f:
        passes = [x for x in f.read().split()]
    return passes


def row_determination(row: str, min: int = 0, max: int = 127) -> int:
    """recursive binary search through row."""
    if len(row) > 7:
        raise ValueError(f"{row} is too long!")
    elif len(row) == 1 and row[0] == "F":
        return min
    elif len(row) == 1 and row[0] == "B":
        return max
    else:
        return row_determination(
            row[1:],
            min=min if (row[0] == 'F') else min+math.ceil((max-min)/2),
            max=max if (row[0] == 'B') else max-math.ceil((max-min)/2)
        )


def col_determination(col: str, min: int = 0, max: int = 7) -> int:
    """recursive binary search through col."""
    if len(col) > 3:
        raise ValueError(f"{col} is too long!")
    elif len(col) == 1 and col[0] == "L":
        return min
    elif len(col) == 1 and col[0] == "R":
        return max
    else:
        return col_determination(
            col[1:],
            min=min if (col[0] == 'L') else min+math.ceil((max-min)/2),
            max=max if (col[0] == 'R') else max-math.ceil((max-min)/2)
        )

def generate_seat_id(boarding_pass: str) -> int:
    """
    Every seat also has a unique seat ID: multiply the row by 8, then 
    add the column.
    """

    if len(boarding_pass) != 10:
        raise ValueError(
            f"boarding pass, {boarding_pass}, is not the correct length."
        )
    else:
        return row_determination(boarding_pass[:7]) * 8 +\
            col_determination(boarding_pass[7:])


def main():
    """
    execute part 1 and part 2
    """
    assert row_determination("FBFBBFF") == 44
    assert col_determination("RLR") == 5
    assert generate_seat_id("FBFBBFFRLR") == 357

    filename: str = utils.input_location(day="5")
    passes: List[str] = get_input(filename)
    max = (None, 0)
    ids: List[int] = []
    for boarding_pass in passes:
        id = generate_seat_id(boarding_pass)
        ids.append(id)
        if id > max[1]:
            max = (boarding_pass, id)

    print(max)

    ids.sort()
    for prev, current in zip(ids, ids[1:]):
        if current - prev > 1:
            print(f"my seat is {current-1}")
            break


if __name__ == "__main__":
    main()
