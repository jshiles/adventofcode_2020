"""
day 11 tests
"""

import pytest
from adventofcode import utils, day_11


def test_empty_to_occupied():
    test_filename: str = utils.test_input_location(day="11")
    test_seat_plan = day_11.parse_input(test_filename)

    assert test_seat_plan.empty_to_occupied(0, 0) == True


def test_occupied_to_empty():
    test_filename: str = utils.test_input_location(day="11")
    test_seat_plan = day_11.parse_input(test_filename)
    test_seat_plan.execute_moves(4)
    test_seat_plan.execute_moves(4)

    assert test_seat_plan.occupied_to_empty(0, 0, 4) == False
    assert test_seat_plan.occupied_to_empty(9, 9, 4) == False
    assert test_seat_plan.occupied_to_empty(9, 5, 4) == False


def test_full_run():
    test_filename: str = utils.test_input_location(day="11")
    test_seat_plan = day_11.parse_input(test_filename)
    changed, cnt = True, 0
    while changed:
        changed, test_seat_plan = test_seat_plan.execute_moves(4)
        cnt += 1
    assert cnt == 6
    assert test_seat_plan.count_occupied() == 37
