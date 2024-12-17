#!/usr/bin/env python
import re

input_file = "input"

data = list(map(int, re.findall(r"\d+", open(input_file).read())))


def execute(a, b, c, program):
    pointer, stdout = 0, []

    while pointer < len(program):
        combo_operand = {x: x for x in range(4)} | {4: a, 5: b, 6: c}

        match program[pointer], program[pointer + 1]:
            case 0, co:
                a = a >> combo_operand[co]
            case 1, co:
                b = b ^ co
            case 2, co:
                b = 7 & combo_operand[co]
            case 3, co:
                pointer = co - 2 if a else pointer
            case 4, _:
                b = b ^ c
            case 5, co:
                stdout.append(combo_operand[co] & 7)
            case 6, co:
                b = a >> combo_operand[co]
            case 7, co:
                c = a >> combo_operand[co]
        pointer += 2
    return stdout


def backtrack_program(a, program, i):
    sub_program = execute(a, 0, 0, program)
    if sub_program == program:
        return a
    if not i or sub_program == program[-i:]:
        return min(backtrack_program(8 * a + n, program, i + 1) for n in range(8))
    return float("inf")


print(",".join(map(str, execute(data[0], data[1], data[2], data[3:]))))
print(backtrack_program(0, data[3:], 0))
