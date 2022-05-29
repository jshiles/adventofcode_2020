"""
Advent of Code 2020 - Puzzel 12
https://adventofcode.com/2020/day/12
jshiles
"""

from typing import List
from adventofcode import utils, day_12


def get_input(filename: str) -> List[day_12.Direction]:
    """Returns a list of integers as our input data."""
    actions: List[day_12.Direction] = []
    with open(filename) as f:
        actions = [
            day_12.Direction(str(x[0]), int(x[1:])) for x in f.read().split()
        ]
    return actions


def follow_directions(directions: List[day_12.Direction]) -> day_12.Location:
    """
    loop through directions calling ship based direction logic.
    """
    loc = day_12.Location(0, 0)
    for d in directions:
        loc.move_ship(d)
    return loc


def follow_waypoint_based_directions(
    directions: List[day_12.Direction],
) -> day_12.Location:
    """
    loop through directions calling waypoint based direction logic.
    """
    loc = day_12.Location(0, 0)
    for d in directions:
        loc.move_waypoint(d)
    return loc


def main():
    """
    execute part 1 and part 2
    """

    # P1: after following the directions compute the taxi cab (manhatten)
    # distance.
    filename: str = utils.input_location(day="12")
    directions = get_input(filename)
    dist = follow_directions(directions).manhattan(day_12.Location(0, 0))
    print(f"P1: distance traveled is {dist}")

    # P2: after following the waypoint based directions compute the taxi cab
    # (manhatten) distance.
    filename: str = utils.input_location(day="12")
    directions = get_input(filename)
    dist = follow_waypoint_based_directions(directions).manhattan(
        day_12.Location(0, 0)
    )
    print(f"P2: distance traveled is {dist}")


if __name__ == "__main__":
    main()
