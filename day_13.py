"""
Advent of Code 2020 - Puzzel 13
https://adventofcode.com/2020/day/13
jshiles
"""

import math
from typing import List, Tuple
from adventofcode import utils


def get_input(filename: str) -> Tuple[int, List[int]]:
    """Our input consits of a timestamp and a list of bus route lengths"""
    busses: List[int] = []
    timestamp: int = 0
    with open(filename) as f:
        timestamp = int(f.readline())
        busses = [int(x) for x in f.readline().split(",") if x != "x"]
    return timestamp, busses


def p1_find_next_bus_wait_time(
    timestamp: int, busses: List[int]
) -> Tuple[int, int]:
    """
    Given a list of busses that depart from some time zero and take their
    value in round trip, find the bus that will come the soonest after
    timestamp. Return bus and that next timestamp as a tuple.
    """

    def closest_multiple_over_n(n: int, x: int) -> int:
        """Given the smallest multiple of x that is larger than n."""
        return math.ceil(n / x) * x

    next_departures = [
        (b, closest_multiple_over_n(timestamp, b)) for b in busses
    ]
    return min(next_departures, key=lambda t: t[1])


def main():
    """
    execute part 1 and part 2
    """
    # P1: Find the next bus. Multiply bus * wait time.
    filename: str = utils.input_location(day="13")
    timestamp, busses = get_input(filename)
    bus, departing = p1_find_next_bus_wait_time(timestamp, busses)
    print(f"P1: {bus * (departing - timestamp)}")


if __name__ == "__main__":
    main()
