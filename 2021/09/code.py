# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/09

def read_file(filename: str = "input.txt") -> tuple:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        lines =  [line for line in f.read().strip().split("\n")]
    max_x = len(lines[0])
    max_y = len(lines)
    numbers = list()
    for line in lines:
        numbers += [int(x) for x in line]
    return (max_x, max_y, numbers)

def get_neighbors(idx: int, max_x: int, max_y: int) -> list:
    neighbors = list()
    if idx >= max_x:
        neighbors.append(idx - max_x)
    if idx < (max_x * max_y - max_x):
        neighbors.append(idx + max_x)
    if idx % max_x != 0:
        neighbors.append(idx - 1)
    if idx % max_x != (max_x - 1):
        neighbors.append(idx + 1)
    return neighbors

def get_low_points(max_x, max_y, grid) -> list:
    low_points = []
    for i in range(len(grid)):
        if all(grid[n] > grid[i] for n in get_neighbors(i, max_x, max_y)):
            low_points.append(i)
    return low_points

def expand(point, max_x, max_y, grid) -> set:
    result = set()
    l = {point}
    while len(l) != 0:
        p = l.pop()
        result.add(p)
        neighbors = {n for n in get_neighbors(p, max_x, max_y) if grid[n] != 9 and n not in result}
        l = l.union(neighbors)
    return result

def part1(max_x, max_y, grid) -> int:
    low_points = get_low_points(max_x, max_y, grid)
    return sum([grid[point] for point in low_points]) + len(low_points)

def part2(max_x, max_y, grid) -> int:
    low_points = get_low_points(max_x, max_y, grid)
    basin_sizes = [len(expand(point, max_x, max_y, grid)) for point in low_points]
    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
    
if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(*vals)}")
    print(f"Part 2: {part2(*vals)}")