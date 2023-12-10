# SPDX-License-Identifier: MIT
# Copyright (c) 2023 Akumatic
#
# https://adventofcode.com/2023/day/4

import re

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [line.strip().split(": ")[1] for line in f.readlines()]

def get_matches(card: str) -> int:
    tmp = card.split(" | ")
    winning_nums = [int(x) for x in re.findall(r"\d+", tmp[0])]
    card_nums = [int(x) for x in re.findall(r"\d+", tmp[1])]
    return len([num for num in winning_nums if num in card_nums])

def part1(cards: list) -> int:
    return sum(int(2**(get_matches(card) - 1)) for card in cards)

def part2(cards: list) -> int:
    matches = [get_matches(card) for card in cards]
    count = [1 for _ in cards]
    for i in range(len(matches)):
        for j in range(i + 1, i + matches[i] + 1):
            count[j] += count[i]
    return sum(count)

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")