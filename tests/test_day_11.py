"""
day 11 tests
"""
import os
from adventofcode import utils, day_11


def test_empty_to_occupied():
    test_filename: str = utils.test_input_location(day="11")
    test_seat_plan = day_11.parse_input(test_filename)

    assert test_seat_plan.empty_to_occupied(0, 0) == True


def test_adjacent_seats():
    """test adjacent check with depth of 1"""
    test_filename_1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'day_11_1.txt')
    test_seat_plan = day_11.parse_input(test_filename_1)
    assert test_seat_plan.seats[4][3] == 'L'
    assert test_seat_plan.adj_increment_recursive(4, 3, -1, -1) == '#'
    assert test_seat_plan.adj_increment_recursive(4, 3, -1, 0) == 'L'
    assert test_seat_plan.adjacent(4, 3, max_depth=1) == (2, 0)


def test_adjacent_seats_extended():
    """test adjacent check with unlimited depth"""
    test_filename_1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'day_11_1.txt')
    test_seat_plan = day_11.parse_input(test_filename_1)
    assert test_seat_plan.seats[4][3] == 'L'
    assert test_seat_plan.adj_increment_recursive(4, 3, -1, -1) == '#'
    assert test_seat_plan.adj_increment_recursive(4, 3, -1, 0) == 'L'
    assert test_seat_plan.adjacent(4, 3) == (7, 1)

    test_filename_2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'day_11_2.txt')
    test_seat_plan_2 = day_11.parse_input(test_filename_2)
    assert test_seat_plan_2.seats[3][3] == 'L'
    assert test_seat_plan_2.adj_increment_recursive(3, 3, -1, -1) == '.'
    assert test_seat_plan_2.adj_increment_recursive(3, 3, -1, 0) == '.'
    assert test_seat_plan_2.adjacent(3, 3) == (0, 0)


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


def test_full_run_extended():
    test_filename: str = utils.test_input_location(day="11")
    test_seat_plan = day_11.parse_input(test_filename)
    changed, cnt = True, 0
    while changed:
        changed, test_seat_plan = test_seat_plan.execute_moves(5, True)
        cnt += 1
    assert test_seat_plan.count_occupied() == 26
