# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/10

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [line for line in f.read().strip().split("\n")]

def shorten(s: str) -> str:
    changes = True
    while changes:
        tmp = s.replace("()", "").replace("[]", "").replace("{}", "").replace("<>", "")
        changes = (tmp != s)
        s = tmp
    return s

def score_illegal(s: str) -> str:
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    return points[[x for x in shorten(s) if x in (")", "]", "}", ">")][0]]

def score_incomplete(s: str) -> str:
    points = {"(": 1, "[": 2, "{": 3, "<": 4}
    score = 0
    for c in shorten(s)[::-1]:
        score *= 5
        score += points[c]
    return score

def validate(line: str) -> bool:
    short = shorten(line)
    return sum(short.count(c) for c in (")", "]", "}", ">")) == 0

def part1(vals: list) -> int:
    return sum(score_illegal(line) for line in vals if not validate(line))

def part2(vals: list) -> int:
    scores = [score_incomplete(line) for line in vals if validate(line)]
    scores.sort()
    return scores[len(scores) // 2]
    
if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
