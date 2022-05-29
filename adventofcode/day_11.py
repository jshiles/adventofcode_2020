"""
Advent of Code 2020 - Puzzel 11
https://adventofcode.com/2020/day/11

Classes and helper code for day 11; main is in root dir day_11.py
"""

from __future__ import annotations
import copy
from collections import Counter
from itertools import product
from typing import List, Tuple, Optional
from dataclasses import dataclass, field


@dataclass
class SeatPlan:
    seats: List[str] = field(default_factory=list)

    def adj_increment_recursive(
        self,
        row: int,
        col: int,
        x: int = 0,
        y: int = 0,
        max_depth: Optional[int] = None,
    ) -> str:
        """
        Recurse from (row, col) in x, y increments until non-isle or end
        of seats.
        """
        if not (
            (0 <= row + x < len(self.seats))
            and (0 <= col + y < len(self.seats[row]))
        ):
            return "."
        elif self.seats[row + x][col + y] == "." and (
            max_depth is None or max_depth > 1
        ):
            new_depth = max_depth - 1 if isinstance(max_depth, int) else None
            return self.adj_increment_recursive(
                row + x, col + y, x, y, new_depth
            )
        else:
            return self.seats[row + x][col + y]

    def adjacent(
        self,
        row: int,
        col: int,
        max_depth: Optional[int] = None,
    ) -> Tuple[int, int]:
        """
        Returns a count of occupied and unoccupied from row and col.
        """
        c = Counter(
            [
                self.adj_increment_recursive(row, col, x, y, max_depth)
                for x, y in product([-1, 0, 1], [-1, 0, 1])
                if not (x == 0 and y == 0)
            ]
        )
        return c.get("#", 0), c.get("L", 0)

    def empty_to_occupied(
        self, row: int, col: int, max_depth: Optional[int] = None
    ) -> bool:
        """
        If no seats are occupied in 8 adjacent squares return True
        else False
        """
        occupied, empty = self.adjacent(row, col, max_depth)
        if occupied == 0:
            return True
        return False

    def occupied_to_empty(
        self,
        row: int,
        col: int,
        occupied_tol: int,
        max_depth: Optional[int] = None,
    ) -> bool:
        """
        If >=4 seats are occupied in 8 adjacent squares return True
        else False
        """
        occupied, empty = self.adjacent(row, col, max_depth)
        if occupied >= occupied_tol:
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

    def execute_moves(
        self, occupied_tol: int, extended_view: bool = False
    ) -> Tuple[bool, SeatPlan]:
        """
        The following rules are applied to every seat simultaneously:
        If a seat is empty (L) and there are no occupied seats adjacent to
           it, the seat becomes occupied.
        If a seat is occupied (#) and four or more seats adjacent to it are
           also occupied, the seat becomes empty.
        Otherwise, the seat's state does not change.
        """
        new_seatplan = copy.deepcopy(self)
        max_depth = None if extended_view else 1
        changed = False
        for ridx, row in enumerate(self.seats):
            for cidx, val in enumerate(row):
                if val == "#" and self.occupied_to_empty(
                    ridx, cidx, occupied_tol, max_depth
                ):
                    new_seatplan.switch_seat(ridx, cidx)
                    changed = True
                elif val == "L" and self.empty_to_occupied(
                    ridx, cidx, max_depth
                ):
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
