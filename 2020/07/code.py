# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
# https://adventofcode.com/2020/day/7

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line.strip() for line in f.read().strip().split("\n")]

def parseRules(input) -> dict:
    rules = {}
    amount = {}
    for line in input:
        rule = line.strip(".").split(" contain ")
        bag = rule[0][:-(4 if rule[0][-1]=="g" else 5)]
        if rule[1] == "no other bags":
            rules[bag] = []
            amount[bag] = []
        else:
            contents = [r.split() for r in rule[1].split(", ")]
            rules[bag] = [" ".join(c[1:3]) for c in contents]
            amount[bag] = [int(c[0]) for c in contents]
    return rules, amount

def can_contain(rules: dict, rule, bag, cache):
    if rule in cache:
        return cache[rule]
    if bag in rules[rule]:
        cache[rule] = True
    else:
        cache[rule] = any(can_contain(rules, b, bag, cache) for b in rules[rule])
    return cache[rule]

def count_bags(rules: dict, amount: dict, bag, cache):
    if bag in cache:
        return cache[bag]

    if len(rules[bag]) == 0:
        cache[bag] = 0
        return 0
    else:
        sum = 0
        for i in range(len(rules[bag])):
            sum += amount[bag][i] * (count_bags(rules, amount, rules[bag][i], cache) + 1)
        cache[bag] = sum
        return cache[bag]

def part1(rules: dict) -> int:
    cache = {}
    return sum([can_contain(rules, rule, "shiny gold", cache) for rule in rules])

def part2(rules: dict, amount: dict) -> int:
    cache = {}
    return count_bags(rules, amount, "shiny gold", cache)

if __name__ == "__main__":
    rules, amount = parseRules(readFile())
    print(f"Part 1: {part1(rules)}")
    print(f"Part 2: {part2(rules, amount)}")
    