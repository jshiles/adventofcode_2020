"""
Advent of Code 2020 - Puzzel 12
https://adventofcode.com/2020/day/12

classes; main is in project_root/day_12.py
"""


from __future__ import annotations
from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True)
class Direction:
    """
    Direction object action and value or magnitude of action.
    """

    action: str
    value: int


@dataclass
class Location:
    """
    A class for storing location of ship, cardinal direction, and
    waypoint location.
    """

    x: int
    y: int
    facing: int = field(default=90, repr=False)
    waypoint_x: int = field(default=10, repr=True)
    waypoint_y: int = field(default=1, repr=True)

    def manhattan(self, other: Location) -> int:
        """
        calculate manhatten distance (taxi cab)
        (x_{1},y_{1}) and (x_{2},y_{2}) is
            {\displaystyle \left|x_{1}-x_{2}\right|+\left|y_{1}-y_{2}\right|}
        """
        return abs(self.x - other.x) + abs(self.y - other.y)

    def move_ship(self, direction: Direction):
        """
        move according to the direction
        """
        if direction.action == "N":
            self.y += direction.value
        elif direction.action == "S":
            self.y -= direction.value
        elif direction.action == "E":
            self.x += direction.value
        elif direction.action == "W":
            self.x -= direction.value
        elif direction.action == "R":
            self.facing = (self.facing + direction.value) % 360
        elif direction.action == "L":
            self.facing = (360 - (direction.value % 360) + self.facing) % 360
        elif direction.action == "F":
            # translate this into NESW movement and re-call.
            cardinal_trans = ["N", "E", "S", "W"][int(self.facing / 90)]
            return self.move_ship(Direction(cardinal_trans, direction.value))

    def move_waypoint(self, direction: Direction):
        """
        everything but "F" moves the way point relative to the ship. "F" moves
        the ship toward the waypoint and the waypoint maintains distance.
        """
        if direction.action == "N":
            self.waypoint_y += direction.value
        elif direction.action == "S":
            self.waypoint_y -= direction.value
        elif direction.action == "E":
            self.waypoint_x += direction.value
        elif direction.action == "W":
            self.waypoint_x -= direction.value
        elif direction.action == "R":
            for _ in range(int((direction.value % 360) / 90)):
                self.rotate_waypoint_right()
        elif direction.action == "L":
            for _ in range(int((direction.value % 360) / 90)):
                self.rotate_waypoint_left()
        elif direction.action == "F":
            x_dist, y_dist = self.waypoint_ship_dist()
            # move ship
            self.x = self.x + x_dist * direction.value
            self.y = self.y + y_dist * direction.value
            # move waypoint relative to ship
            self.waypoint_x = self.x + x_dist
            self.waypoint_y = self.y + y_dist

    def waypoint_ship_dist(self) -> Tuple[int, int]:
        """compute x, y distances from waypoint to ship."""
        return self.waypoint_x - self.x, self.waypoint_y - self.y

    def rotate_waypoint_right(self):
        """Rotate waypoint 90 degrees right relative to ship"""
        x_dist, y_dist = self.waypoint_ship_dist()
        self.waypoint_x = self.x + y_dist
        self.waypoint_y = self.y + -1 * x_dist

    def rotate_waypoint_left(self):
        """Rotate waypoint 90 degrees left relative to ship"""
        x_dist, y_dist = self.waypoint_ship_dist()
        self.waypoint_x = self.x + -1 * y_dist
        self.waypoint_y = self.y + x_dist
