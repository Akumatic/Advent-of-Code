# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
#https://adventofcode.com/2020/day/13

def readFile() -> tuple:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        timestamp = int(f.readline().strip())
        values = f.readline().strip().split(",")
        bus_ids = [{"value": int(values[i]), "index": i} 
            for i in range(len(values))
            if values[i] != "x"]
        return timestamp, bus_ids 

def part1(timestamp: int, bus_ids: list) -> int:
    min = timestamp
    min_id = None
    for bus in bus_ids:
        waiting_time = bus["value"] - (timestamp % bus["value"])
        if waiting_time < min:
            min = waiting_time
            min_id = bus["value"]
    return min * min_id

def part2(bus_ids: list) -> int:
    time, step = 1, 1
    for bus in bus_ids:
        while (time + bus["index"]) % bus["value"] != 0:
            time += step
        step *= bus["value"]
    return time

if __name__ == "__main__":
    input = readFile()
    print(f"Part 1: {part1(*input)}")
    print(f"Part 2: {part2(input[1])}")