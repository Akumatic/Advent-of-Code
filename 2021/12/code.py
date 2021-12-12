# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/12

def add_to_dict(d: dict, key: str, value: str):
    if key not in d:
        d[key] = [value]
    else:
        d[key].append(value)

def parse_paths(connections: list):
    paths = dict()
    for connection in connections:
        tmp = connection.split("-")
        add_to_dict(paths, tmp[0], tmp[1])
        add_to_dict(paths, tmp[1], tmp[0])
    return paths

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [line for line in f.read().strip().split("\n")]

def part1(paths: dict) -> int:
    complete = list()
    incomplete = [["start"]]
    while incomplete:
        previous = incomplete.pop()
        for next_step in paths[previous[-1]]:
            if next_step.lower() not in previous:
                p = previous[:]
                p.append(next_step)
                complete.append(p) if next_step == "end" else incomplete.append(p)
    return len(complete)

def part2(paths: dict) -> int:
    complete = list()
    incomplete = [["start"]]
    small = [x for x in paths if x.islower() and x != "end" and x != "start"]
    while incomplete:
        previous = incomplete.pop()
        for next_step in paths[previous[-1]]:
            if next_step == "start":
                continue
            if next_step in small:
                if next_step in previous and any(previous.count(x) > 1 for x in small):
                    continue
            p = previous[:]
            p.append(next_step)
            complete.append(p) if next_step == "end" else incomplete.append(p)
    return len(complete)
    
if __name__ == "__main__":
    vals = read_file()
    paths = parse_paths(vals)
    print(f"Part 1: {part1(paths)}")
    print(f"Part 2: {part2(paths)}")
