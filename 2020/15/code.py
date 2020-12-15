# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
#https://adventofcode.com/2020/day/15

def readFile() -> tuple:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(num) for num in f.readline().split(",")]

def play(input: list, turns: int) -> int:
    mem = {val: idx + 1 for idx, val in enumerate(input)}
    prev = input[-1]
    for turn in range(len(input) + 1, turns + 1):
        next = 0 if prev not in mem else turn - 1 - mem[prev]
        mem[prev] = turn - 1
        prev = next
    return prev

def part1(input: list) -> int:
    return play(input, 2020)

def part2(input: list) -> int:
    return play(input, 30000000)

if __name__ == "__main__":
    input = readFile()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")