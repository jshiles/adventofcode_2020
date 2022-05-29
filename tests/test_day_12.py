"""
day 11 tests
"""
import copy
from adventofcode import day_12


def test_standard_movement():
    test_directions = [
        day_12.Direction("F", 10),
        day_12.Direction("N", 3),
        day_12.Direction("F", 7),
        day_12.Direction("R", 90),
        day_12.Direction("F", 11),
    ]
    loc = day_12.Location(0, 0)
    for d in test_directions:
        loc.move_ship(d)
    assert loc.manhattan(day_12.Location(0, 0)) == 25


def test_right_rotation():
    """rotate right 4 times and should end up at the same location"""
    start = day_12.Location(170, 38, 90, 180, 42)
    loc = copy.deepcopy(start)
    for _ in range(4):
        loc.rotate_waypoint_right()
    assert (
        loc.waypoint_x == start.waypoint_x
        and loc.waypoint_y == start.waypoint_y
    )


def test_left_rotation():
    """rotate left 4 times and should end up at the same location"""
    start = day_12.Location(170, 38, 90, 180, 42)
    loc = copy.deepcopy(start)
    for _ in range(4):
        loc.rotate_waypoint_left()
    assert (
        loc.waypoint_x == start.waypoint_x
        and loc.waypoint_y == start.waypoint_y
    )


def test_waypoint_movement():
    test_directions = [
        day_12.Direction("F", 10),
        day_12.Direction("N", 3),
        day_12.Direction("F", 7),
        day_12.Direction("R", 90),
        day_12.Direction("F", 11),
    ]
    loc = day_12.Location(0, 0)
    for d in test_directions:
        loc.move_waypoint(d)
    assert loc.manhattan(day_12.Location(0, 0)) == 286
