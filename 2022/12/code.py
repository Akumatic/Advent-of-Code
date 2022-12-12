# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/12

from queue import Queue

def read_file(filename: str = "input.txt") -> dict:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        map = [[ord(char) for char in line.strip()] for line in f.readlines()]
    N, M = len(map[0]), len(map)
    start = [(i, j) for i in range(N) for j in range(M) if map[j][i] == ord("S")][0]
    end = [(i, j) for i in range(N) for j in range(M) if map[j][i] == ord("E")][0]
    map[start[1]][start[0]] = ord("a")
    map[end[1]][end[0]] = ord("z")
    return {"map": map, "start": start, "end": end, "dims": {"X": N, "Y": M}}
 
def get_dist(map: list, start: tuple, end: tuple, dims: dict) -> int:
    queue = Queue()
    dist = {start: 0}
    queue.put(start)
    while not queue.empty():
        cur = queue.get()
        if cur == end:
            return dist[cur]
        neighbors = [(cur[0] + dir[0], cur[1] + dir[1])
            for dir in ((1, 0), (-1, 0), (0, 1), (0, -1))
            if 0 <= cur[0] + dir[0] < dims["X"] and 0 <= cur[1] + dir[1] < dims["Y"]]
        for nb in neighbors:
            if (nb not in dist) and (map[nb[1]][nb[0]] - map[cur[1]][cur[0]]) < 2:
                queue.put(nb)
                dist[nb] = dist[cur] + 1
    # target not reachable
    return -1

def part1(vals: dict) -> int:
    return get_dist(vals["map"], vals["start"], vals["end"], vals["dims"])

def part2(vals: dict) -> int:
    start_pos = [(i, j) for i in range(vals["dims"]["X"]) 
        for j in range(vals["dims"]["Y"]) if vals["map"][j][i] == ord("a")]
    distances = [get_dist(vals["map"], start, vals["end"], vals["dims"]) for start in start_pos]
    return min(dist for dist in distances if dist != -1)

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
