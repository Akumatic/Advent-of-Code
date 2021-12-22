# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/22

from collections import defaultdict

def parse_line(line: str) -> str:
    state = True if line.startswith("on") else False
    coords = line[3 if state else 4:].split(",")
    return [state] + [(int(p[0]), int(p[1])) for p in (pos[2:].split("..") for pos in coords)]

def read_file(filename: str = "input.txt") -> defaultdict:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [parse_line(line) for line in f.read().strip().split("\n")]

def areas_overlapping(a: tuple, b: tuple) -> bool:
    return a[0][0] <= b[0][1] and a[0][1] >= b[0][0] \
        and a[1][0] <= b[1][1] and a[1][1] >= b[1][0] \
        and a[2][0] <= b[2][1] and a[2][1] >= b[2][0]

def calculate_overlap(a: tuple, b: tuple) -> tuple:
    return ((max(a[0][0], b[0][0]), min(a[0][1], b[0][1])),
        (max(a[1][0], b[1][0]), min(a[1][1], b[1][1])),
        (max(a[2][0], b[2][0]), min(a[2][1], b[2][1])))

def cubes_in_cuboid(cuboid: tuple) -> int:
    return (cuboid[0][1] - cuboid[0][0] + 1) * \
        (cuboid[1][1] - cuboid[1][0] + 1) * (cuboid[2][1] - cuboid[2][0] + 1)

def changes_adding_cuboid(cuboids: list, state: bool, cuboid: tuple) -> list:
    changes = []
    signum = 1 if state else -1
    for cub, sig in cuboids:
        if areas_overlapping(cub, cuboid):
            changes.append((calculate_overlap(cub, cuboid), -sig))
    if signum == 1:
        changes.append((cuboid, 1))
    return changes

def part1(instructions: list) -> int:
    reactor = defaultdict(bool)
    area = ((-50, 50), (-50, 50), (-50, 50))
    for state, x, y, z in instructions:
        cur = (x, y, z)
        if not areas_overlapping(cur, area):
            continue
        a, b, c = calculate_overlap(cur, area)
        cubes = [(u, v, w) for u in range(a[0], a[1]+1) for v in range(b[0], b[1]+1) for w in range(c[0], c[1]+1)]
        for cube in cubes:
            reactor[cube] = state
    return sum(reactor.values())

def part2(instructions: list) -> int:
    cuboids = list()
    for state, x, y, z in instructions:
        cuboids += changes_adding_cuboid(cuboids, state, (x, y, z))
    return sum(cubes_in_cuboid(cub) * sig for cub, sig in cuboids)

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
    