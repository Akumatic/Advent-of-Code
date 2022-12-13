# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/13

from json import loads
from functools import cmp_to_key

def read_file(filename: str = "input.txt") -> dict:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [loads(line.strip()) for line in f.readlines() if line != "\n"]

def cmp(a, b) -> int:
    match a, b:
        case int(), int():
            return 0 if a == b else (b - a) // abs(b - a)
        case int(), list(): 
            return cmp([a], b)
        case list(), int():
            return cmp(a, [b])
        case list(), list():
            for pair in zip(a, b):
                tmp = cmp(*pair)
                if tmp:
                    return tmp
            return 0 if len(a) == len(b) else (len(b) - len(a)) // abs(len(b) - len(a))

def part1(vals: list) -> int:
    pairs = [vals[i:i+2] for i in range(0, len(vals), 2)]
    return sum(idx for idx, pair in enumerate(pairs, 1) if cmp(*pair) == 1)

def part2(vals: list) -> int:
    ordered = sorted(vals + [[[2]], [[6]]], reverse=True, key=cmp_to_key(cmp))
    return (ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1)

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
