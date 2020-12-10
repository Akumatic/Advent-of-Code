# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
#https://adventofcode.com/2020/day/10

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(line) for line in f.read().strip().split("\n")]

def part1(input: list) -> int:
    count = [0, 0, 1]
    cur = 0
    for num in input:
        count[num - cur - 1] += 1
        cur = num
    return count[0] * count[2]

def count_ways(input, cur, cache):
    if cur in cache:
        return cache[cur]
    cache[cur] = sum([count_ways(input, i, cache) for i in range(cur + 1, cur + 4) if i in input])
    return cache[cur]

def part2(input: list) -> int:
    cache = {input[-1]: 1}
    count_ways(input, 0, cache)
    return cache[0]

if __name__ == "__main__":
    input = readFile()
    input.sort()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")