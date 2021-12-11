# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/11

class Octopus:
    def __init__(self, idx, energy):
        self.idx = idx
        self._get_neighbor_idx()
        self.energy = energy
        self.flashed = False
        self.neighbors = list()

    def _get_neighbor_idx(self):
        if self.idx == 0: # top left corner
            self.neighbor_idx = [self.idx + i for i in (1, 10, 11)]
        elif self.idx == 9: # top right corner
            self.neighbor_idx = [self.idx + i for i in (-1, 9, 10)]
        elif self.idx == 90: # bottom left corner
            self.neighbor_idx = [self.idx + i for i in (-10, -9, 1)]
        elif self.idx == 99: # bottom right corner
            self.neighbor_idx = [self.idx + i for i in (-11, -10, -1)]
        elif self.idx < 10: # top edge
            self.neighbor_idx = [self.idx + i for i in (-1, 1, 9, 10, 11)]
        elif self.idx > 90: # bottom edge
            self.neighbor_idx = [self.idx + i for i in (-11, -10, -9, -1, 1)]
        elif self.idx % 10 == 0: # left edge
            self.neighbor_idx = [self.idx + i for i in (-10, -9, 1, 10, 11)]
        elif self.idx % 10 == 9: # right edge
            self.neighbor_idx = [self.idx + i for i in (-11, -10, -1, 9, 10)]
        else:
            self.neighbor_idx = [self.idx + i for i in (-11, -10, -9, -1, 1, 9, 10, 11)]

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def flash(self):
        self.flashed = True
        for neighbor in self.neighbors:
            neighbor.energy += 1

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        lines = [line for line in f.read().strip().split("\n")]
    values = list()
    for line in lines:
        values += [int(x) for x in list(line)]
    return values

def create_octopuses(vals: int) -> list:
    octopuses = [Octopus(i, vals[i]) for i in range(len(vals))]
    for octopus in octopuses:
        for i in octopus.neighbor_idx:
            octopus.add_neighbor(octopuses[i])
    return octopuses

def step(octopuses: list) -> int:
    flashes = 0
    for octopus in octopuses:
        octopus.energy += 1

    repeat = True
    while repeat:
        repeat = False
        for octopus in octopuses:
            if octopus.energy > 9 and octopus.flashed == False:
                octopus.flash()
                flashes += 1
                repeat = True

    for octopus in octopuses:
        if octopus.flashed:
            octopus.flashed = False
            octopus.energy = 0

    return flashes

def part1(vals: list) -> int:
    flashes = 0
    octopuses = create_octopuses(vals)
    for _ in range(100):
        flashes += step(octopuses)
    return flashes

def part2(vals: list) -> int:
    octopuses = create_octopuses(vals)
    count = 0
    flashes = 0
    while flashes != 100:
        flashes = step(octopuses)
        count += 1
    return count
    
if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
