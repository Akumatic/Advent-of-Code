# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/16

from re import findall

def read_file(filename: str = "input.txt") -> dict:
    pattern = "Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)"
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        values = [findall(pattern, line)[0] for line in f.readlines()]
    return {v[0]: {"flow": int(v[1]), "paths": v[2].split(", ")} for v in values}

def dijkstra(valves: dict, start: str) -> dict:
    d = {valve: float("inf") for valve in valves}
    d[start] = 0
    to_process = [valve for valve in valves]
    while to_process:
        cur = sorted([(d[valve], valve) for valve in to_process])[0][1]
        to_process.remove(cur)
        for neighbor in valves[cur]["paths"]:
            if neighbor in to_process and d[cur] + 1 < d[neighbor]:
                d[neighbor] = d[cur] + 1
    return d

def calc_flow(valves: dict, distances: dict, closed: list, cur_v: str, 
        time: int = 30, released: int = 0, flow: int = 0) -> int:
    if time < 0:
        return released
    if not closed:
        return released + flow * time
    outcomes = list()
    for valve in closed:
        time_needed = (distances[cur_v][valve] + 1)
        predicted_flow = calc_flow(valves, distances, [v for v in closed if v != valve], valve,
             time - time_needed, released + flow * time_needed, flow + valves[valve]["flow"])
        outcomes.append(released + flow * time if time_needed > time else predicted_flow)
    return max(outcomes)

def part1(vals: dict) -> int:
    dist = {valve: dijkstra(vals, valve) for valve in vals}
    closed = [valve for valve in vals if vals[valve]["flow"]]
    return calc_flow(vals, dist, closed, "AA")

def part2(vals: dict) -> int:
    pass

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
