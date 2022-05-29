"""
Advent of Code 2020 - Puzzel 11
https://adventofcode.com/2020/day/11

Classes and helper code for day 11; main is in root dir day_11.py
"""

from __future__ import annotations
import copy
from typing import List, Tuple
from dataclasses import dataclass, field

@dataclass
class SeatPlan:
    seats: List[str] = field(default_factory=list)

    def empty_to_occupied(self, row: int, col: int) -> bool:
        """
        If no seats are occupied in 8 adjacent squares return True
        else False
        """
        min_row = row - 1 if row - 1 >= 0 else 0
        min_col = col - 1 if col - 1 >= 0 else 0
        max_row = row + 1 if row + 1 < len(self.seats) else len(self.seats) - 1
        max_col = (
            col + 1 if col + 1 < len(self.seats[row]) else len(self.seats[row]) - 1
        )
        for i in range(min_row, max_row + 1):
            for j in range(min_col, max_col + 1):
                if not (i == row and j == col) and self.seats[i][j] in ["#"]:
                    return False
        return True

    def occupied_to_empty(self, row: int, col: int, occupied_tol: int) -> bool:
        """
        If >=4 seats are occupied in 8 adjacent squares return True
        else False
        """
        min_row = row - 1 if row - 1 >= 0 else 0
        min_col = col - 1 if col - 1 >= 0 else 0
        max_row = row + 1 if row + 1 < len(self.seats) else len(self.seats) - 1
        max_col = (
            col + 1 if col + 1 < len(self.seats[row]) else len(self.seats[row]) - 1
        )
        occupied_adj = 0
        for i in range(min_row, max_row + 1):
            for j in range(min_col, max_col + 1):
                if not (i == row and j == col) and self.seats[i][j] == "#":
                    occupied_adj += 1
        if occupied_adj >= occupied_tol:
            return True
        return False

    def switch_seat(self, row: int, col: int):
        """
        Flips seat from occupied to unoccupied or vice versa.
        """
        new_value = "#" if self.seats[row][col] == "L" else "L"
        if col == 0:
            self.seats[row] = new_value + self.seats[row][1:]
        elif col == len(self.seats[row]) - 1:
            self.seats[row] = self.seats[row][:-1] + new_value
        else:
            self.seats[row] = (
                self.seats[row][:col] + new_value + self.seats[row][col + 1 :]
            )

    def execute_moves(self, occupied_tol: int) -> Tuple[bool, SeatPlan]:
        """
        The following rules are applied to every seat simultaneously:
        If a seat is empty (L) and there are no occupied seats adjacent to
           it, the seat becomes occupied.
        If a seat is occupied (#) and four or more seats adjacent to it are
           also occupied, the seat becomes empty.
        Otherwise, the seat's state does not change.
        """
        new_seatplan = copy.deepcopy(self)
        changed = False
        for ridx, row in enumerate(self.seats):
            for cidx, val in enumerate(row):
                if val == "#" and self.occupied_to_empty(ridx, cidx, occupied_tol):
                    new_seatplan.switch_seat(ridx, cidx)
                    changed = True
                elif val == "L" and self.empty_to_occupied(ridx, cidx):
                    new_seatplan.switch_seat(ridx, cidx)
                    changed = True
        return changed, new_seatplan

    def count_occupied(self) -> int:
        """Returns count of occupied seats"""
        return sum([r.count("#") for r in self.seats])

    def __str__(self):
        """return string representation."""
        return "\n".join([row for row in self.seats])


def parse_input(filename: str) -> SeatPlan:
    """
    Parse text input from filename into a SeatPlan object.
    """
    rows: List[str] = []
    with open(filename) as f:
        for line in f.readlines():
            rows.append(line.strip())
    return SeatPlan(rows)