# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
# https://adventofcode.com/2020/day/6

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line.split() for line in f.read().strip().split("\n\n")]

def count(groups: list, everyone: bool) -> int:
    result = 0
    for group in groups:
        answers = {chr(c):0 for c in range(97, 123)}

        for answer in group:
            for letter in answer:
                answers[letter] += 1

        if everyone:
            result += sum([1 for letter in answers if answers[letter] == len(group)])
        else:
            result += sum([1 for letter in answers if answers[letter]])

    return result

def part1(groups: list) -> int:
    return count(groups, False)

def part2(seat_ids: list) -> int:
    return count(groups, True)

if __name__ == "__main__":
    groups = readFile()
    print(f"Part 1: {part1(groups)}")
    print(f"Part 2: {part2(groups)}")
    