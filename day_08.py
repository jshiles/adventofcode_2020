"""
Advent of Code 2020 - Puzzel 8
https://adventofcode.com/2020/day/8
jshiles
"""

import logging
import re
from dataclasses import dataclass
from typing import List, Tuple
from adventofcode import utils


@dataclass
class Instruction:
    index: int
    operation: str
    argument: int

    def __post_init__(self):
        if self.operation not in ["acc", "jmp", "nop"]:
            raise ValueError(f"{self.operation} is not supported.")


def parse_input(filename: str) -> List[Instruction]:
    """
    Parse input file and return a list of Instructions.
    """
    instructions: List[Instruction] = []
    with open(filename) as f:
        idx: int = 0
        for instruction in f.readlines():
            operation, argument = instruction.strip().split()
            instructions.append(Instruction(idx, operation, int(argument)))
            idx += 1
    return instructions


def evaluate_code(code: List[Instruction]) -> int:
    """
    evaluate code, starting with accumulator at 0.
    If inf. loop is detected, we return accumulator prior to executing any
    line the second time.
    """

    def _eval_rec(
        code: List[Instruction], idx: int, accum: int, prev_exec: List[int]
    ) -> int:
        """recrusively execute code"""
        if idx in prev_exec:
            raise RuntimeError(f"infinite loop detected. accum {accum} prior to exit.")
        elif idx >= len(code):
            logging.debug("finished successfully")
        elif code[idx].operation == "acc":
            return _eval_rec(
                code, idx + 1, accum + code[idx].argument, prev_exec + [idx]
            )
        elif code[idx].operation == "nop":
            return _eval_rec(code, idx + 1, accum, prev_exec + [idx])
        elif code[idx].operation == "jmp":
            return _eval_rec(code, idx + code[idx].argument, accum, prev_exec + [idx])
        return accum

    return _eval_rec(code, 0, 0, [])


def change_next_operation(
    code: List[Instruction], idx: int
) -> Tuple[int, List[Instruction]]:
    """
    Loop through our code starting at idx and change the first instance of jmp
    or nop to the other operation.
    """
    found = False
    while not found:
        if code[idx].operation == "jmp":
            logging.debug(f"Changing: {code[idx]}.")
            code[idx].operation = "nop"
            found = True
        elif code[idx].operation == "nop":
            logging.debug(f"Changing: {code[idx]}.")
            code[idx].operation = "jmp"
            found = True
        else:
            idx += 1
    return idx, code


def main():
    """
    execute part 1 and part 2
    """

    test_filename: str = utils.test_input_location(day="8")
    filename: str = utils.input_location(day="8")

    # P1: What is the accumulator's value immediately before any
    # instruction is executed a second time?
    test_code = parse_input(test_filename)
    try:
        evaluate_code(test_code)
    except (RuntimeError) as e:
        assert "accum 5 prior" in str(e)

    code = parse_input(filename)
    try:
        evaluate_code(code)
    except (RuntimeError) as e:
        m = re.search(
            r"infinite loop detected. accum (\d+) prior to exit.",
            str(e)
        )
        if m:
            print(f"Part 1: {m.group(0)}")

    # Fix the program so that it terminates normally by changing exactly one
    # jmp (to nop) or nop (to jmp). What is the value of the accumulator after
    # the program terminates?
    error_not_found = True
    idx = -1
    while error_not_found:
        try:
            accum = evaluate_code(code)
            print(f"Part 2: {accum}.")
            error_not_found = False  # we can stop, we fixed it
        except (RuntimeError):
            idx, code = change_next_operation(parse_input(filename), idx+1)


if __name__ == "__main__":
    main()
