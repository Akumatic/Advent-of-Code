# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/11

import math 

class Monkey:
    monkeys = list()
    lcm = 1

    def __init__(self, description: str):
        self.count = 0
        self.items = [int(item) for item in description[1][15:].split(", ")]
        self.__items = self.items[:]
        self.op = description[2][17:].replace("old", "item")
        self.mod = int(description[3][19:])
        Monkey.lcm = math.lcm(Monkey.lcm, self.mod)
        self.next = {True: int(description[4][25:]), False: int(description[5][26:])}
        Monkey.monkeys.append(self)

    def throw_items(self, divide: bool):
        for item in self.items:
            level = eval(self.op)
            if divide:
                level //= 3
            Monkey.monkeys[self.next[level % self.mod == 0]].items.append(level % Monkey.lcm)
            self.count += 1
        self.items.clear()

    def reset(self):
        self.items = self.__items[:]
        self.count = 0

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [Monkey([line.strip() for line in desc.split("\n")]) 
            for desc in f.read().split("\n\n")] 

def part1(monkeys: list) -> int:
    for _ in range(20):
        for monkey in monkeys:
            monkey.throw_items(divide = True)
    inspections = sorted([monkey.count for monkey in monkeys])
    return inspections[-1] * inspections[-2]

def part2(monkeys: list) -> int:
    for monkey in monkeys:
        monkey.reset()
    for _ in range(10000):
        for monkey in monkeys:
            monkey.throw_items(divide = False)
    inspections = sorted([monkey.count for monkey in monkeys])
    return inspections[-1] * inspections[-2]

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
