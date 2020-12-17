# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
# https://adventofcode.com/2020/day/17

from itertools import product

def read_file() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [list(line.strip()) for line in f.readlines()]

def parse_input(input: list) -> set:
    active_cubes = set()
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == "#":
                active_cubes.add((x, y, 0, 0))
    return active_cubes

def simulate(active_cubes: set, size: int = 3, iterations: int = 6) -> int:
    assert 3 <= size <= 4
    # neighbor positions
    positions = product(range(-1, 2), repeat=size)
    if size == 4:
        npos = tuple(pos for pos in positions if pos != (0, 0, 0, 0))
    else: # size == 4
        npos = tuple((pos[0], pos[1], pos[2], 0) for pos in positions if pos != (0, 0, 0))

    # iterations
    for _ in range(iterations):
        next_active = set()
        neighbors = set()
        # check if active cubes stay active
        for cube in active_cubes:
            count = 0
            for n in npos:
                pos = tuple(cube[i] + n[i] for i in range(4))
                if pos in active_cubes:
                    count += 1
                else:
                    neighbors.add(pos)
            if 2 <= count <= 3:
                next_active.add(cube)
        # check neighbors of active cubes if they become active
        for cube in neighbors:
            count = 0
            for n in npos:
                pos = tuple(cube[i] + n[i] for i in range(4))
                if pos in active_cubes:
                    count += 1
            if count == 3:
                next_active.add(cube)

        active_cubes = next_active

    return len(active_cubes)

def part1(active_cubes: set) -> int:
    return simulate(active_cubes, 3)

def part2(active_cubes: set) -> int:
    return simulate(active_cubes, 4)

if __name__ == "__main__":
    input = read_file()
    data = parse_input(input)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")