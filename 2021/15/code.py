# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/15

from queue import PriorityQueue

def read_file(filename: str = "input.txt") -> tuple:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        lines = [line for line in f.read().strip().split("\n")]
    data = list()
    for line in lines:
        data += [int(x) for x in line]
    return len(lines[0]), data

def get_neighbor_idx(idx: int, dim: int) -> list:
    y = idx // dim
    x = idx - y * dim
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [n[0] + n[1]*dim for n in neighbors if 0 <= n[0] < dim and 0 <= n[1] < dim]

def dijkstra(cavern: tuple) -> dict:
    dimension, graph = cavern[0], cavern[1]
    graph_size = len(graph)
    queue = PriorityQueue()
    queue.put((0, 0))
    dist = {0: 0}

    while not queue.empty():
        distance, idx = queue.get()

        for neighbor in get_neighbor_idx(idx, dimension):
            d = distance + graph[neighbor]
            if neighbor not in dist or dist[neighbor] > d:
                dist[neighbor] = d
                queue.put((d, neighbor))

    return dist

def expand(cavern: tuple) -> tuple:
    dim = cavern[0]
    # expand to the right
    tmp = list()
    for y in range(dim):
        for i in range(5):
            for x in range(dim):
                idx = x + y * dim
                val = cavern[1][idx] + i
                if val > 9:
                    val -= 9
                tmp.append(val)
    cave = tmp

    # expand to the bottom
    for _ in range(4):
        tmp = [n + 1 if n + 1 < 10 else n - 8 for n in tmp]
        cave += tmp

    return dim * 5, cave

def part1(cavern: tuple) -> int:
    return dijkstra(cavern)[cavern[0]**2 - 1]

def part2(cavern: tuple) -> int:
    cavern = expand(cavern)
    return dijkstra(cavern)[cavern[0]**2 - 1]
        
if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
