"""
Advent of Code 2020 - Puzzel 10
https://adventofcode.com/2020/day/10
jshiles
"""

from collections import Counter
from functools import lru_cache
from typing import List
from adventofcode import utils


def get_input(filename: str) -> List[int]:
    """Returns a list of integers as our input data."""
    numbers: List[int] = []
    with open(filename) as f:
        numbers = [int(x) for x in f.read().split()]
    return numbers


def jolt_differences(filename: str) -> List[int]:
    """Returns a list of ints with the jolt differences between sorted numbers"""
    numbers: List[int] = [0] + sorted(get_input(filename))
    numbers.append(numbers[-1] + 3)  # append our device.
    return numbers


def group_differences(numbers: List[int]) -> Counter:
    """Returns the distribution of differences in a Counter object"""
    return Counter([y - x for x, y in zip(numbers, numbers[1:])])


def p1_compute_answer(filename: str) -> int:
    """Returns number of 1 jolt differences * 3 jolt differences"""
    c: Counter = group_differences(jolt_differences(filename))
    return c[1] * c[3]


@lru_cache
def _recursive_adapter_configs(numbers: tuple) -> int:
    """
    depth first explore different combinations where next value
    is less than 3 jolts away or less. returns count of possible
    combinations.

    Note: I cast the list to a tuple of ints so that I could cache
    the function calls, otherwise I compute the same thing over
    and over.
    'time' on my machine reports:
        python day_10.py  0.03s user 0.01s system 91% cpu 0.039 total
    so speed up is very worth it and necessary!
    """
    if len(numbers) <= 1:
        return 1
    else:
        count = 0
        first_element = numbers[0]
        for idx, v in enumerate(numbers[1:]):
            if v-first_element <= 3:
                count += _recursive_adapter_configs(numbers[idx+1:])
            else:
                break
        return count


def p2_num_compute_adapter_configs(filename: str) -> int:
    """Return the number of possible adapter configurations"""
    numbers: List[int] = jolt_differences(filename)
    return _recursive_adapter_configs(tuple(numbers))


def main():
    """
    execute part 1 and part 2
    """
    test_filename1: str = utils.test_input_location(
        day="10", filename="test_input1.txt"
    )
    test_filename2: str = utils.test_input_location(
        day="10", filename="test_input2.txt"
    )
    filename: str = utils.input_location(day="10")

    # P1: What is the number of 1-jolt differences multiplied
    # by the number of 3-jolt differences?
    assert p1_compute_answer(test_filename1) == 7 * 5
    assert p1_compute_answer(test_filename2) == 220
    print(f"Part 1: {p1_compute_answer(filename)}")

    # P2: What is the total number of distinct ways you can
    # arrange the adapters to connect the charging outlet to your device?
    assert p2_num_compute_adapter_configs(test_filename1) == 8
    assert p2_num_compute_adapter_configs(test_filename2) == 19208
    print(f"Part 2: {p2_num_compute_adapter_configs(filename)}")


if __name__ == "__main__":
    main()
