# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
# https://adventofcode.com/2020/day/19

import re

def parse_rules(input: list) -> dict:
    return dict(rule.split(": ") for rule in input)

def read_file() -> tuple:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        blocks = [block.split("\n") for block in f.read().strip().split("\n\n")]
    return parse_rules(blocks[0]), blocks[1]

def regex_pattern(word, rules):
    check = word.split()
    pattern = f" {word} "
    while check:
        value = check.pop(0)
        rule = rules[value]
        if '"' not in rule:
            check += set([w for w in rule.split() if w not in ("|", "(", ")+")])
        replacement = "( " + rule + " )" if "|" in rule else rule
        pattern = pattern.replace(f" {value} ", f" {replacement} ")
    return pattern.replace('"', "").replace(" ", "")

def part1(rules, words):
    pattern = regex_pattern(rules['0'], rules)
    return sum([bool(re.fullmatch(pattern, word)) for word in words])

def part2(rules, words):
    rules["8"] = "( 42 )+"
    rules["11"] = "|".join(" 42 "*i + " 31 "*i for i in range(1, 6))
    return part1(rules, words)

if __name__ == "__main__":
    rules, words = read_file()
    print(f"Part 1: {part1(rules, words)}")
    print(f"Part 2: {part2(rules, words)}")