# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/14

from collections import defaultdict

def read_file(filename: str = "input.txt") -> defaultdict:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        coords = [[(int(p.split(",")[0]), int(p.split(",")[1])) 
            for p in line.strip().split(" -> ")] for line in f.readlines()]
    d = defaultdict(lambda: ".")
    for path in coords:
        add_walls(d, path)
    return d

def add_walls(d: defaultdict, path: list) -> None:
    for i in range(1, len(path)):
        dx, dy = path[i][0] - path[i-1][0], path[i][1] - path[i-1][1]
        dx = dx + 1 if dx > 0 else dx - 1
        dy = dy + 1 if dy > 0 else dy - 1
        if dx:
            for x in range(0, dx, dx // abs(dx)):
                d[(path[i-1][0] + x, path[i][1])] = "#"
        if dy:
            for y in range(0, dy, dy // abs(dy)):
                d[(path[i][0], path[i-1][1] + y)] = "#"

def pour_sandcorn(d: defaultdict, bottomless: bool, max_depth: int) -> bool:
    cur = (500, 0)
    # stop if starting point is blocked and settled down already
    if d[cur] == "o":
        return False
    d[cur] = "o"
    while True:
        # stop if bottomless pit and first corn falls into the void
        if bottomless and cur[1] > max_depth:
            return False
        # pit is not bottomless and sandcorn reached deepest layer
        if not bottomless and cur[1] + 1 == max_depth + 2:
            return True

        possible_next = ((cur[0],cur[1]+1), (cur[0]-1,cur[1]+1), (cur[0]+1,cur[1]+1))
        # no free position, sand is resting
        if all(d[next] != "." for next in possible_next):
            return True
        # at least one free position available, move sand
        for next in possible_next:
            if d[next] == ".":
                d[next] = "o"
                d[cur] = "."
                cur = next
                break

def pour_sand(vals: defaultdict, bottomless: bool) -> int:
    d = defaultdict(lambda: ".", {k:v for k,v in vals.items()})
    lowest_point = max(point[1] for point in d.keys())
    i = 0
    while pour_sandcorn(d, bottomless=bottomless, max_depth=lowest_point):
        i += 1
    return i

def part1(vals: defaultdict) -> int:
    return pour_sand(vals, bottomless=True)

def part2(vals: defaultdict) -> int:
    return pour_sand(vals, bottomless=False)

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
