"""
Advent of Code 2020 - Puzzel 11
https://adventofcode.com/2020/day/11
jshiles
"""

from typing import List, Tuple
from adventofcode import utils, day_11


def p1_run_until_stable(filename: str) -> Tuple[int, int]:
    """
    Runs until no more changes were made and returns number of
    iterations and occupied seats.
    """
    test_seat_plan = day_11.parse_input(filename)
    changed, cnt = True, 0
    while changed:
        changed, test_seat_plan = test_seat_plan.execute_moves(4)
        cnt += 1
    return cnt, test_seat_plan.count_occupied()


def p2_run_until_stable(
    filename: str, occupied_tol: int = 5
) -> Tuple[int, int]:
    """
    Runs until no more changes were made and returns number of
    iterations and occupied seats.
    """
    test_seat_plan = day_11.parse_input(filename)
    changed, cnt = True, 0
    while changed:
        changed, test_seat_plan = test_seat_plan.execute_moves(
            occupied_tol, True
        )
        cnt += 1
    return cnt, test_seat_plan.count_occupied()


def main():
    """
    execute part 1 and part 2
    """
    # Part 1: run until stable and count occupied seats
    test_filename: str = utils.test_input_location(day="11")
    cnt, occupied = p1_run_until_stable(test_filename)
    assert occupied == 37

    filename: str = utils.input_location(day="11")
    cnt, occupied = p1_run_until_stable(filename)
    print(
        f"P1: stabilized after {cnt} iterations "
        f"with {occupied} occupied seats."
    )

    # Part 2: change in the rules
    # Extend view over isle spaces.
    # Also, people seem to be more tolerant than you expected: it now takes
    # five or more visible occupied seats for an occupied seat to become empty
    # (rather than four or more from the previous rules).
    filename: str = utils.input_location(day="11")
    cnt, occupied = p2_run_until_stable(filename)
    print(
        f"P2: stabilized after {cnt} iterations "
        f"with {occupied} occupied seats."
    )


if __name__ == "__main__":
    main()
