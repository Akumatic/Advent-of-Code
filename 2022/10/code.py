# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/10

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [line.split() for line in f.readlines()]

def run_instructions(instructions: list) -> list:
    history = []
    x = 1
    for instruction in instructions:
        match instruction:
            case ["noop"]:
                history.append(x)
            case ["addx", val]:
                history.extend([x, x])
                x += int(val)
    return history

def part1(vals: list) -> int:
    history = run_instructions(vals)
    return sum((i + 1) * history[i] for i in range(19, 220, 40))

def part2(vals: list) -> str:
    history = run_instructions(vals)
    result = ["\n"]
    for y in range(6):
        for x in range(40):
            result.append("#" if x in range(history[y*40+x]-1, history[y*40+x]+2) else ".")
        result.append("\n")
    return "".join(result)

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
